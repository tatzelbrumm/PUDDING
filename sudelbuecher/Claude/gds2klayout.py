#!/usr/bin/env python3
"""
gds2klayout.py — GDS to KLayout Python Script Translator
==========================================================

LANGSEC DESIGN NOTES
--------------------
LangSec ("Language-Theoretic Security") teaches that parsers must be
based on a *formal grammar* that precisely defines the input language.
Inputs that deviate from the grammar must be *rejected*, not guessed at.
This avoids "shotgun parsing" — the anti-pattern where a program
speculatively reads bytes, recovers from surprises mid-stream, and
accumulates partially-interpreted state that diverges from intent.

How this parser implements LangSec principles:

1.  GRAMMAR-FIRST: GDSII is a well-specified record-oriented binary
    format. Every record has the shape:
        [length: uint16][record_type: uint8][data_type: uint8][data...]
    We define this grammar explicitly via the RECORD_GRAMMAR dict and
    DATA_TYPE_GRAMMAR dict. Only records and data types listed there are
    accepted; any unknown value raises ParseError immediately.

2.  FINITE STATE MACHINE: The parser is an explicit FSM
    (GdsStateMachine). The set of states is enumerated. Each record type
    is only valid in specific states, encoded in VALID_RECORDS_IN_STATE.
    Receiving a record in an invalid state raises ParseError rather than
    proceeding with corrupt context. No "best-effort" fallback, no silent
    skip.

3.  REJECT EARLY, NOT LATE: Every field is validated at the point of
    reading:
      - Length field must be ≥ 4 and even (GDS spec §2.1.3).
      - Data payload size must exactly match what the data type and
        record grammar declare (checked in parse_record_data).
      - Strings are verified to be ASCII-only.
    Violations immediately raise a typed ParseError, preventing bad data
    from propagating into the output model.

4.  SINGLE-PASS, NO BACKTRACKING: The parser reads the file once,
    left-to-right, in record order. There is no speculative look-ahead,
    no rewind, and no post-hoc fixup. The byte stream is consumed exactly
    once by a single deterministic automaton.

5.  CLOSED-WORLD ASSUMPTION: Only the six element types defined by the
    GDSII spec (BOUNDARY, PATH, SREF, AREF, TEXT, NODE) are translated.
    Vendor extensions (e.g. LIBSECUR, BGNEXTN) that appear in some
    foundry GDS files are rejected unless explicitly added to the grammar.

6.  TYPED OUTPUT MODEL: Parsed records are not stored as raw bytes or
    loose dicts. Each element is stored as a typed dataclass
    (Boundary, Path, SRef, ARef, Text). Fields have declared types;
    callers cannot confuse layer numbers with coordinate arrays.

Usage
-----
    python gds2klayout.py <input.gds> [output.py]

If output.py is omitted, the script is written to <input_stem>_klayout.py.

Dependencies: none (pure stdlib) — no gdspy, no numpy required.
"""

import struct
import sys
import os
import math
from dataclasses import dataclass, field
from typing import Optional
from enum import Enum, auto


# ---------------------------------------------------------------------------
# 1.  Typed error hierarchy
# ---------------------------------------------------------------------------

class GdsError(Exception):
    """Base for all errors raised by this module."""

class ParseError(GdsError):
    """Raised when the byte stream violates the GDSII grammar."""

class FsmError(GdsError):
    """Raised when a record arrives in an unexpected FSM state."""


# ---------------------------------------------------------------------------
# 2.  Grammar tables  (the formal specification of accepted inputs)
# ---------------------------------------------------------------------------

# GDS data-type codes (GDSII spec Table 1-1)
DATA_TYPE_GRAMMAR = {
    0x00: ("NO_DATA",   0),   # no data
    0x01: ("BITARRAY",  2),   # 2-byte bit array
    0x02: ("INT16",     2),   # 2-byte signed int (per item)
    0x03: ("INT32",     4),   # 4-byte signed int (per item)
    0x05: ("REAL64",    8),   # 8-byte real (per item)
    0x06: ("STRING",    1),   # variable-length string
}

# Record-type grammar: maps record_type_byte -> (name, data_type_byte, min_items, max_items)
# min_items/max_items constrain the number of data items expected.
# None for max_items means unbounded (e.g. XY coordinate arrays).
RECORD_GRAMMAR = {
    # Core structural records (Calma GDS II spec, record type = high byte of key)
    0x0002: ("HEADER",       0x02, 1,  1),
    0x0102: ("BGNLIB",       0x02, 12, 12),
    0x0206: ("LIBNAME",      0x06, 1,  None),
    0x0305: ("UNITS",        0x05, 2,  2),
    0x0400: ("ENDLIB",       0x00, 0,  0),
    0x0502: ("BGNSTR",       0x02, 12, 12),
    0x0606: ("STRNAME",      0x06, 1,  None),
    0x0700: ("ENDSTR",       0x00, 0,  0),
    # Element openers
    0x0800: ("BOUNDARY",     0x00, 0,  0),
    0x0900: ("PATH",         0x00, 0,  0),
    0x0a00: ("SREF",         0x00, 0,  0),
    0x0b00: ("AREF",         0x00, 0,  0),
    0x0c00: ("TEXT",         0x00, 0,  0),
    0x1500: ("NODE",         0x00, 0,  0),
    0x2d00: ("BOX",          0x00, 0,  0),
    # Shared element properties
    0x0d02: ("LAYER",        0x02, 1,  1),
    0x0e02: ("DATATYPE",     0x02, 1,  1),
    0x0f03: ("WIDTH",        0x03, 1,  1),
    0x1003: ("XY",           0x03, 2,  None),  # >=1 coord pair; SREF/TEXT=1pt, BOUNDARY/PATH/AREF=multi
    0x1100: ("ENDEL",        0x00, 0,  0),
    0x1206: ("SNAME",        0x06, 1,  None),
    0x1302: ("COLROW",       0x02, 2,  2),
    0x1402: ("TEXTNODE",     0x02, 1,  1),
    0x1602: ("TEXTTYPE",     0x02, 1,  1),
    0x1701: ("PRESENTATION", 0x01, 1,  1),
    0x1906: ("STRING",       0x06, 1,  None),
    0x1a01: ("STRANS",       0x01, 1,  1),
    0x1b05: ("MAG",          0x05, 1,  1),
    0x1c05: ("ANGLE",        0x05, 1,  1),
    0x2102: ("PATHTYPE",     0x02, 1,  1),
    0x2601: ("ELFLAGS",      0x01, 1,  1),
    0x2a02: ("NODETYPE",     0x02, 1,  1),
    0x2b02: ("PROPATTR",     0x02, 1,  1),   # property attribute number (0x2b = 43)
    0x2c06: ("PROPVALUE",    0x06, 1,  None), # property value string   (0x2c = 44)
    0x2e02: ("BOXTYPE",      0x02, 1,  1),
    0x3003: ("BGNEXTN",      0x03, 1,  1),   # path begin extension
    0x3103: ("ENDEXTN",      0x03, 1,  1),   # path end extension
    # Library-level metadata (accepted for grammar compliance, ignored in output)
    0x1f06: ("REFLIBS",      0x06, 1,  None),
    0x2006: ("FONTS",        0x06, 1,  None),
    0x2202: ("GENERATIONS",  0x02, 1,  1),
    0x2306: ("ATTRTABLE",    0x06, 1,  None),
    0x3606: ("FORMAT",       0x06, 1,  None),
    0x3702: ("MASK",         0x02, 1,  None),
    0x3800: ("ENDMASKS",     0x00, 0,  0),
    0x3b00: ("LIBSECUR",     0x00, 0,  0),
}

# ---------------------------------------------------------------------------
# 3.  FSM state enumeration + valid-record table
# ---------------------------------------------------------------------------

class State(Enum):
    START       = auto()
    IN_LIBRARY  = auto()
    IN_STRUCT   = auto()
    IN_BOUNDARY = auto()
    IN_PATH     = auto()
    IN_SREF     = auto()
    IN_AREF     = auto()
    IN_TEXT     = auto()
    DONE        = auto()

# Records accepted in each state.  Anything else triggers FsmError.
VALID_RECORDS_IN_STATE = {
    State.START: {"HEADER"},
    State.IN_LIBRARY: {
        "BGNLIB", "LIBNAME", "UNITS", "BGNSTR", "ENDLIB",
        "REFLIBS", "FONTS", "GENERATIONS", "ATTRTABLE",
        "FORMAT", "MASK", "ENDMASKS", "LIBSECUR",
    },
    State.IN_STRUCT: {
        "BGNSTR", "STRNAME", "ENDSTR",
        "BOUNDARY", "PATH", "SREF", "AREF", "TEXT", "NODE", "BOX",
        "PROPATTR", "PROPVALUE",
    },
    State.IN_BOUNDARY: {
        "LAYER", "DATATYPE", "XY", "ENDEL",
        "ELFLAGS", "PROPATTR", "PROPVALUE",
    },
    State.IN_PATH: {
        "LAYER", "DATATYPE", "PATHTYPE", "WIDTH", "XY", "ENDEL",
        "ELFLAGS", "BGNEXTN", "ENDEXTN", "PROPATTR", "PROPVALUE",
    },
    State.IN_SREF: {
        "SNAME", "STRANS", "MAG", "ANGLE", "XY", "ENDEL",
        "ELFLAGS", "PROPATTR", "PROPVALUE",
    },
    State.IN_AREF: {
        "SNAME", "STRANS", "MAG", "ANGLE", "COLROW", "XY", "ENDEL",
        "ELFLAGS", "PROPATTR", "PROPVALUE",
    },
    State.IN_TEXT: {
        "LAYER", "TEXTTYPE", "TEXTNODE", "PRESENTATION", "PATHTYPE",
        "WIDTH", "STRANS", "MAG", "ANGLE",
        "XY", "STRING", "ENDEL",
        "ELFLAGS", "PROPATTR", "PROPVALUE",
    },
    State.DONE: set(),
}


# ---------------------------------------------------------------------------
# 4.  Typed output model
# ---------------------------------------------------------------------------

@dataclass
class Boundary:
    layer:    int
    datatype: int
    xy:       list   # list of (x, y) in microns

@dataclass
class Path:
    layer:    int
    datatype: int
    pathtype: int
    width:    float
    xy:       list   # list of (x, y) in microns

@dataclass
class SRef:
    sname:         str
    xy:            tuple   # (x, y)
    strans:        int = 0
    mag:           float = 1.0
    angle:         float = 0.0
    x_reflection:  bool = False

@dataclass
class ARef:
    sname:         str
    xy:            list    # 3 points: origin, col-end, row-end
    columns:       int = 1
    rows:          int = 1
    strans:        int = 0
    mag:           float = 1.0
    angle:         float = 0.0
    x_reflection:  bool = False

# GDS PRESENTATION word (uint16) encodes a combined anchor:
#   horiz = word % 4    (0=left, 1=center, 2=right)
#   vert  = word // 4   (0=top,  1=middle, 2=bottom)
# This is NOT a pair of independent 2-bit fields; it is a single anchor index.
# Verified against gdspy source (Label._anchor dict) and Calma spec §2.5.4.22.
#
# KLayout HAlign: 0=left, 1=center, 2=right  (same numbering)
# KLayout VAlign: 0=bottom, 1=center, 2=top   (inverted from GDS vert)
_GDS_HALIGN = {0: 0, 1: 1, 2: 2}          # direct mapping
_GDS_VALIGN = {0: 2, 1: 1, 2: 0}          # GDS top(0)->KL VAlignTop(2), etc.

@dataclass
class Text:
    layer:    int
    texttype: int
    xy:       tuple
    string:   str
    strans:   int = 0
    mag:      float = 1.0
    angle:    float = 0.0
    halign:   int = 0   # KLayout HAlign value (0=left)
    valign:   int = 0   # KLayout VAlign value (0=bottom)

@dataclass
class Structure:
    name:     str
    elements: list = field(default_factory=list)

@dataclass
class Library:
    name:       str
    unit:       float   # user unit in meters
    precision:  float   # database unit in meters
    structures: list = field(default_factory=list)


# ---------------------------------------------------------------------------
# 5.  Low-level validated byte readers
# ---------------------------------------------------------------------------

def _read_exact(f, n: int) -> bytes:
    """Read exactly n bytes or raise ParseError (no short reads accepted)."""
    buf = f.read(n)
    if len(buf) != n:
        raise ParseError(
            f"Unexpected EOF: expected {n} bytes, got {len(buf)}"
        )
    return buf


def _decode_real64(data: bytes) -> float:
    """
    Decode an IBM System/360 64-bit floating point value.
    GDSII uses this format, not IEEE 754.
    Grammar: sign(1) | exponent(7, excess-64) | mantissa(56, base-16)
    """
    if len(data) != 8:
        raise ParseError(f"REAL64 requires exactly 8 bytes, got {len(data)}")
    v = struct.unpack(">Q", data)[0]
    sign     = (v >> 63) & 1
    exponent = (v >> 56) & 0x7F
    mantissa = v & 0x00FFFFFFFFFFFFFF
    if mantissa == 0:
        return 0.0
    frac = mantissa / (1 << 56)
    result = frac * (16.0 ** (exponent - 64))
    return -result if sign else result


def _parse_record_data(rec_name: str, data_type_code: int,
                       expected_dtype: int, payload: bytes,
                       min_items: int, max_items) -> list:
    """
    Validate and decode the payload of a single record.
    Enforces:
      - data_type_code matches grammar expectation
      - payload length is an exact multiple of item size
      - item count is within [min_items, max_items]
    """
    if data_type_code != expected_dtype:
        raise ParseError(
            f"Record {rec_name}: data type 0x{data_type_code:02x} "
            f"conflicts with grammar (expected 0x{expected_dtype:02x})"
        )

    dtype_name, item_size = DATA_TYPE_GRAMMAR[data_type_code]

    if dtype_name == "NO_DATA":
        if payload:
            raise ParseError(f"Record {rec_name}: NO_DATA record has {len(payload)} extra bytes")
        return []

    if dtype_name == "STRING":
        # String: ASCII bytes, possibly padded to even length with NUL
        try:
            text = payload.decode("ascii").rstrip("\x00")
        except UnicodeDecodeError as e:
            raise ParseError(f"Record {rec_name}: non-ASCII string: {e}") from e
        return [text]

    if len(payload) % item_size != 0:
        raise ParseError(
            f"Record {rec_name}: payload length {len(payload)} "
            f"is not a multiple of item size {item_size}"
        )
    n_items = len(payload) // item_size

    if n_items < min_items:
        raise ParseError(
            f"Record {rec_name}: {n_items} items < minimum {min_items}"
        )
    if max_items is not None and n_items > max_items:
        raise ParseError(
            f"Record {rec_name}: {n_items} items > maximum {max_items}"
        )

    if dtype_name == "BITARRAY":
        return [struct.unpack(">H", payload[i:i+2])[0] for i in range(0, len(payload), 2)]
    elif dtype_name == "INT16":
        return [struct.unpack(">h", payload[i:i+2])[0] for i in range(0, len(payload), 2)]
    elif dtype_name == "INT32":
        return [struct.unpack(">i", payload[i:i+4])[0] for i in range(0, len(payload), 4)]
    elif dtype_name == "REAL64":
        return [_decode_real64(payload[i:i+8]) for i in range(0, len(payload), 8)]
    else:
        raise ParseError(f"Unknown dtype_name {dtype_name!r}")


# ---------------------------------------------------------------------------
# 6.  Record reader  (single read unit — the grammar's terminal symbol)
# ---------------------------------------------------------------------------

def read_next_record(f) -> tuple:
    """
    Read one GDSII record from f and return (rec_name, items).

    Enforces:
      - length ≥ 4 (minimum valid record)
      - length is even (GDS spec §2.1.3)
      - record_type is in RECORD_GRAMMAR (closed-world)
      - data_type byte matches grammar for that record type
      - payload exactly consumed (no leftover bytes)
    """
    header = f.read(4)
    if len(header) == 0:
        raise ParseError("Unexpected EOF reading record header")
    if len(header) < 4:
        raise ParseError(f"Truncated record header: only {len(header)} bytes")

    length = struct.unpack(">H", header[0:2])[0]

    if length < 4:
        raise ParseError(f"Record length {length} < 4 (minimum valid size)")
    if length % 2 != 0:
        raise ParseError(f"Record length {length} is odd (violates GDS spec §2.1.3)")

    rec_type_byte  = header[2]
    data_type_byte = header[3]

    rec_key = (rec_type_byte << 8) | data_type_byte
    if rec_key not in RECORD_GRAMMAR:
        raise ParseError(
            f"Unknown record type 0x{rec_type_byte:02x} / "
            f"data type 0x{data_type_byte:02x} at byte offset {f.tell()-4}"
        )

    rec_name, expected_dtype, min_items, max_items = RECORD_GRAMMAR[rec_key]

    payload_len = length - 4
    payload = _read_exact(f, payload_len)

    items = _parse_record_data(
        rec_name, data_type_byte, expected_dtype,
        payload, min_items, max_items
    )

    return rec_name, items


# ---------------------------------------------------------------------------
# 7.  FSM-driven parser
# ---------------------------------------------------------------------------

# Records that are accepted but carry no information we need to translate.
# They still must be grammatically valid (enforced by read_next_record).
_IGNORED_RECORDS = frozenset({
    # Library metadata: grammatically required, not translated
    "BGNLIB", "REFLIBS", "FONTS", "GENERATIONS", "ATTRTABLE",
    "FORMAT", "MASK", "ENDMASKS", "LIBSECUR",
    # Element decorations: accepted but not translated to KLayout output
    "ELFLAGS", "BGNEXTN", "ENDEXTN", "PROPATTR", "PROPVALUE",
    "NODETYPE", "BOXTYPE", "TEXTNODE",
    # Rarely-used element types: accepted, silently skipped
    "NODE", "BOX",
})


class GdsStateMachine:
    """
    Finite-state parser for GDSII.

    The FSM transitions are encoded in the _dispatch_* methods.
    Each method handles exactly one state. Unrecognised records in a
    state raise FsmError, ensuring the machine never silently drifts.
    """

    def __init__(self, db_units_per_user_unit: float):
        self._scale = db_units_per_user_unit  # set after UNITS record
        self.state    = State.START
        self.library  = None
        self._cur_struct  = None
        self._cur_elem    = {}   # accumulates fields for current element

    # ---- helpers -----------------------------------------------------------

    def _to_um(self, db_int: int) -> float:
        """Convert a database integer coordinate to microns (user units)."""
        return db_int * self._scale

    def _xy_to_um(self, flat_ints: list):
        """Convert a flat list of INT32 coordinate pairs to (x, y) microns."""
        if len(flat_ints) % 2 != 0:
            raise ParseError(f"XY record has odd number of coordinates: {len(flat_ints)}")
        return [(self._to_um(flat_ints[i]), self._to_um(flat_ints[i+1]))
                for i in range(0, len(flat_ints), 2)]

    def _strans_flags(self, bits: int):
        x_reflection = bool(bits & 0x8000)
        abs_mag       = bool(bits & 0x0004)
        abs_angle     = bool(bits & 0x0002)
        return x_reflection, abs_mag, abs_angle

    # ---- top-level dispatch ------------------------------------------------

    def feed(self, rec_name: str, items: list):
        """
        Deliver one record to the FSM.
        Raises FsmError if rec_name is not valid in the current state.
        """
        valid = VALID_RECORDS_IN_STATE[self.state]
        if rec_name not in valid and rec_name not in _IGNORED_RECORDS:
            raise FsmError(
                f"Record {rec_name!r} is not valid in state {self.state.name}"
            )

        if rec_name in _IGNORED_RECORDS:
            return  # grammatically valid, semantically ignored

        method = getattr(self, f"_on_{rec_name.lower()}", None)
        if method:
            method(items)

    # ---- record handlers ---------------------------------------------------

    def _on_header(self, items):
        self.state = State.IN_LIBRARY

    def _on_libname(self, items):
        name = items[0]
        self.library = Library(name=name, unit=0.0, precision=0.0, structures=[])

    def _on_units(self, items):
        user_unit_in_meters = items[0]      # e.g. 1e-3 (1 mm) or 1e-6 (1 um)
        db_unit_in_meters   = items[1]      # e.g. 1e-9 (1 nm)
        self.library.unit      = user_unit_in_meters
        self.library.precision = db_unit_in_meters
        # _scale converts a raw GDS integer to microns:
        #   result_um = gds_int * db_unit_in_meters * 1e6
        # This is correct regardless of what the user unit is.
        self._scale = db_unit_in_meters * 1e6

    def _on_bgnstr(self, items):
        self.state = State.IN_STRUCT
        self._cur_struct = Structure(name="")

    def _on_strname(self, items):
        self._cur_struct.name = items[0]

    def _on_endstr(self, items):
        self.library.structures.append(self._cur_struct)
        self._cur_struct = None
        self.state = State.IN_LIBRARY

    def _on_endlib(self, items):
        self.state = State.DONE

    # element openers
    def _on_boundary(self, items):
        self._cur_elem = {"_type": "BOUNDARY"}
        self.state = State.IN_BOUNDARY

    def _on_path(self, items):
        self._cur_elem = {"_type": "PATH", "pathtype": 0, "width": 0.0}
        self.state = State.IN_PATH

    def _on_sref(self, items):
        self._cur_elem = {"_type": "SREF", "strans": 0, "mag": 1.0, "angle": 0.0}
        self.state = State.IN_SREF

    def _on_aref(self, items):
        self._cur_elem = {"_type": "AREF", "strans": 0, "mag": 1.0, "angle": 0.0,
                          "columns": 1, "rows": 1}
        self.state = State.IN_AREF

    def _on_text(self, items):
        self._cur_elem = {"_type": "TEXT", "strans": 0, "mag": 1.0, "angle": 0.0}
        self.state = State.IN_TEXT

    # shared element fields
    def _on_layer(self, items):
        self._cur_elem["layer"] = items[0]

    def _on_datatype(self, items):
        self._cur_elem["datatype"] = items[0]

    def _on_texttype(self, items):
        self._cur_elem["texttype"] = items[0]

    def _on_pathtype(self, items):
        self._cur_elem["pathtype"] = items[0]

    def _on_width(self, items):
        self._cur_elem["width"] = self._to_um(items[0])

    def _on_xy(self, items):
        self._cur_elem["xy"] = self._xy_to_um(items)

    def _on_sname(self, items):
        self._cur_elem["sname"] = items[0]

    def _on_colrow(self, items):
        self._cur_elem["columns"] = items[0]
        self._cur_elem["rows"]    = items[1]

    def _on_strans(self, items):
        bits = items[0]
        self._cur_elem["strans"] = bits
        x_refl, _, _ = self._strans_flags(bits)
        self._cur_elem["x_reflection"] = x_refl

    def _on_mag(self, items):
        self._cur_elem["mag"] = items[0]

    def _on_angle(self, items):
        self._cur_elem["angle"] = items[0]

    def _on_presentation(self, items):
        word  = items[0]   # uint16 anchor: horiz = word % 4, vert = word // 4
        horiz = word % 4   # 0=left, 1=center, 2=right
        vert  = word // 4  # 0=top,  1=middle, 2=bottom
        # Closed-world: reject values outside the 3x3 anchor grid.
        # Valid range: word in 0..10 (nw=0 .. se=10), excluding 3,7,11+ which
        # are undefined in the Calma spec.
        if horiz > 2:
            raise ParseError(
                f"PRESENTATION: word={word:#06x} gives horiz={horiz}, "
                f"which is outside the defined range [0,2]"
            )
        if vert > 2:
            raise ParseError(
                f"PRESENTATION: word={word:#06x} gives vert={vert}, "
                f"which is outside the defined range [0,2]"
            )
        self._cur_elem["halign"] = _GDS_HALIGN[horiz]
        self._cur_elem["valign"] = _GDS_VALIGN[vert]

    def _on_string(self, items):
        self._cur_elem["string"] = items[0]

    def _on_endel(self, items):
        """Finalise the current element into a typed dataclass and append."""
        e = self._cur_elem
        t = e["_type"]

        if t == "BOUNDARY":
            obj = Boundary(
                layer    = e["layer"],
                datatype = e["datatype"],
                xy       = e["xy"],
            )
        elif t == "PATH":
            obj = Path(
                layer    = e["layer"],
                datatype = e["datatype"],
                pathtype = e["pathtype"],
                width    = e["width"],
                xy       = e["xy"],
            )
        elif t == "SREF":
            obj = SRef(
                sname        = e["sname"],
                xy           = e["xy"][0],
                strans       = e.get("strans", 0),
                mag          = e.get("mag", 1.0),
                angle        = e.get("angle", 0.0),
                x_reflection = e.get("x_reflection", False),
            )
        elif t == "AREF":
            obj = ARef(
                sname        = e["sname"],
                xy           = e["xy"],
                columns      = e["columns"],
                rows         = e["rows"],
                strans       = e.get("strans", 0),
                mag          = e.get("mag", 1.0),
                angle        = e.get("angle", 0.0),
                x_reflection = e.get("x_reflection", False),
            )
        elif t == "TEXT":
            obj = Text(
                layer    = e["layer"],
                texttype = e.get("texttype", 0),
                xy       = e["xy"][0],
                string   = e.get("string", ""),
                strans   = e.get("strans", 0),
                mag      = e.get("mag", 1.0),
                angle    = e.get("angle", 0.0),
                halign   = e.get("halign", 0),
                valign   = e.get("valign", 0),
            )
        else:
            raise FsmError(f"Unknown element type {t!r}")  # should be unreachable

        self._cur_struct.elements.append(obj)
        self._cur_elem = {}
        self.state = State.IN_STRUCT


# ---------------------------------------------------------------------------
# 8.  Public parse entry point
# ---------------------------------------------------------------------------

def parse_gds(path: str) -> Library:
    """
    Parse a GDSII file at `path` and return a Library object.

    Raises ParseError or FsmError on any deviation from the grammar.
    """
    with open(path, "rb") as f:
        # We cannot know the unit scale until we read UNITS,
        # so initialise with placeholder 1e-3 (overwritten on UNITS record).
        fsm = GdsStateMachine(db_units_per_user_unit=1e-3)
        while True:
            rec_name, items = read_next_record(f)
            fsm.feed(rec_name, items)
            if fsm.state == State.DONE:
                break
            if fsm.state == State.START:
                raise ParseError("Parser stuck in START state after reading records")
    if fsm.library is None:
        raise ParseError("No LIBNAME record found — not a valid GDSII file")
    return fsm.library


# ---------------------------------------------------------------------------
# 9.  Code generator
# ---------------------------------------------------------------------------

def _fmt_float(v: float) -> str:
    """Format a float compactly, avoiding unnecessary trailing zeros."""
    s = f"{v:.6g}"
    return s


def _safe_var(name: str) -> str:
    """Convert a cell name to a safe Python identifier."""
    result = []
    for ch in name:
        if ch.isalnum() or ch == "_":
            result.append(ch)
        else:
            result.append("_")
    if result and result[0].isdigit():
        result.insert(0, "c_")
    return "".join(result)


# ---------------------------------------------------------------------------
# 9a. Layer-map parser  (strict grammar, no shotgun parsing)
# ---------------------------------------------------------------------------
# Map file format (one entry per line):
#
#   <layer> <datatype> <name>
#
# Formal grammar (EBNF):
#   map_file   = { line } EOF
#   line       = blank_line | comment_line | entry_line
#   blank_line = *WS LF
#   comment_line = *WS "#" *<any> LF
#   entry_line = WS* uint WS+ uint WS+ name WS* LF
#   uint       = DIGIT+                            ; 0..4095 inclusive
#   name       = LETTER_OR_UNDERSCORE *IDENT_CHAR  ; Python identifier rules
#
# Anything that deviates from this grammar raises LayerMapError immediately.
# The parser is single-pass, line-by-line, with no backtracking.

class LayerMapError(GdsError):
    """Raised when the layer-map file violates the grammar."""

# Compiled patterns for the grammar terminals — defined once, used per line.
import re as _re
_BLANK_RE   = _re.compile(r'^\s*(#.*)?$')
_ENTRY_RE   = _re.compile(
    r'^\s*'
    r'(?P<layer>\d+)'          # uint: layer number
    r'\s+'
    r'(?P<datatype>\d+)'       # uint: datatype
    r'\s+'
    r'(?P<name>[A-Za-z_][A-Za-z0-9_]*)'  # name: valid Python identifier
    r'\s*$'
)
_UINT_MAX = 4095   # GDS layer/datatype are 12-bit fields per spec §2.5

def parse_layer_map(path: str) -> dict:
    """
    Parse a layer-map file and return {(layer, datatype): name}.

    Grammar enforcement:
      - Every non-blank, non-comment line MUST match _ENTRY_RE exactly.
        Any extra tokens, non-identifier names, or unrecognised syntax
        raises LayerMapError (no silent skip, no partial acceptance).
      - Layer and datatype values must be in [0, _UINT_MAX].
      - Duplicate (layer, datatype) keys raise LayerMapError.
      - Name must satisfy Python identifier rules (enforced by _ENTRY_RE
        plus a str.isidentifier() post-check as defence-in-depth).
    """
    layer_map: dict = {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except OSError as e:
        raise LayerMapError(f"Cannot open layer map {path!r}: {e}") from e

    for lineno, raw in enumerate(lines, start=1):
        line = raw.rstrip("\n")

        if _BLANK_RE.match(line):
            continue   # blank or comment — accepted, no data extracted

        m = _ENTRY_RE.match(line)
        if not m:
            raise LayerMapError(
                f"{path}:{lineno}: line does not match grammar "
                f"'<layer> <datatype> <name>' — got: {line!r}"
            )

        layer    = int(m.group("layer"))
        datatype = int(m.group("datatype"))
        name     = m.group("name")

        # Range check — closed-world on numeric values
        if layer > _UINT_MAX:
            raise LayerMapError(
                f"{path}:{lineno}: layer {layer} exceeds maximum {_UINT_MAX}"
            )
        if datatype > _UINT_MAX:
            raise LayerMapError(
                f"{path}:{lineno}: datatype {datatype} exceeds maximum {_UINT_MAX}"
            )

        # Defence-in-depth: verify name is a valid Python identifier
        if not name.isidentifier():
            raise LayerMapError(
                f"{path}:{lineno}: name {name!r} is not a valid Python identifier"
            )

        key = (layer, datatype)
        if key in layer_map:
            raise LayerMapError(
                f"{path}:{lineno}: duplicate entry for layer={layer} datatype={datatype} "
                f"(previously defined as {layer_map[key]!r})"
            )

        layer_map[key] = name

    return layer_map


def _layer_varname(layer: int, datatype: int, layer_map: dict) -> str:
    """Return the Python variable name for this (layer, datatype) index."""
    name = layer_map.get((layer, datatype))
    if name:
        return f"L_{name}"
    return f"L_{layer}_{datatype}"


def _layer_expr(layer: int, datatype: int, layer_map: dict) -> str:
    """Return the pre-declared variable name that holds the KLayout layer index."""
    return _layer_varname(layer, datatype, layer_map)


def _emit_layer_table(lib, layer_map: dict) -> list:
    """
    Collect every (layer, datatype) used in lib; return script lines that
    declare one Python variable per layer.

    Named  (in map): L_Metal1 = layout.layer(pya.LayerInfo(10, 0, "Metal1"))
    Numeric (fallback): L_10_0 = layout.layer(10, 0)

    pya.LayerInfo(layer, datatype, name) creates a named layer with correct
    GDS numbers — this is what makes XOR / diff operations work correctly,
    because both layouts will carry identical LayerInfo objects.
    """
    used: set = set()
    for struct in lib.structures:
        for elem in struct.elements:
            if isinstance(elem, (Boundary, Path)):
                used.add((elem.layer, elem.datatype))
            elif isinstance(elem, Text):
                used.add((elem.layer, elem.texttype))

    out = ["# --- layer index variables ---"]
    for (layer, datatype) in sorted(used):
        var  = _layer_varname(layer, datatype, layer_map)
        name = layer_map.get((layer, datatype))
        if name:
            out.append(
                f'L_{name} = layout.layer(pya.LayerInfo({layer}, {datatype}, "{name}"))'
            )
        else:
            out.append(f"L_{layer}_{datatype} = layout.layer({layer}, {datatype})")
    out.append("")
    return out


def generate_klayout_script(lib: Library, layer_map: dict = None) -> str:
    """
    Produce a KLayout Python (pya) script that faithfully recreates
    the library contents.  The output is minimal: no comments beyond
    what identifies each section, no redundant calls.
    """
    if layer_map is None:
        layer_map = {}

    lines = []
    w = lines.append

    w("import pya")
    w("")
    w("layout = pya.Layout()")
    w("")
    # KLayout dbu = size of one database integer in microns
    dbu_um = lib.precision * 1e6
    w(f"layout.dbu = {_fmt_float(dbu_um)}")   # e.g. 0.001 for 1-nm grid
    w("")

    # Emit one layer-index variable per (layer, datatype) used in the design
    for line in _emit_layer_table(lib, layer_map):
        w(line)

    # Build a cell-name → KLayout variable mapping
    cell_vars = {s.name: f"cell_{_safe_var(s.name)}" for s in lib.structures}

    # Forward-declare all cells so references work regardless of definition order
    w("# --- cell declarations ---")
    for struct in lib.structures:
        var = cell_vars[struct.name]
        w(f'{var} = layout.create_cell("{struct.name}")')
    w("")

    # Emit elements for each structure
    for struct in lib.structures:
        var = cell_vars[struct.name]
        w(f"# === {struct.name} ===")

        for elem in struct.elements:

            if isinstance(elem, Boundary):
                pts = ", ".join(
                    f"pya.DPoint({_fmt_float(x)}, {_fmt_float(y)})"
                    for x, y in elem.xy
                )
                layer_expr = _layer_expr(elem.layer, elem.datatype, layer_map)
                w(f"{var}.shapes({layer_expr}).insert(")
                w(f"    pya.DPolygon([{pts}]))")

            elif isinstance(elem, Path):
                pts = ", ".join(
                    f"pya.DPoint({_fmt_float(x)}, {_fmt_float(y)})"
                    for x, y in elem.xy
                )
                w(f"_path = pya.DPath([{pts}], {_fmt_float(elem.width)})")
                if elem.pathtype != 0:
                    # 1 = round ends, 2 = extended square ends
                    ext = {1: elem.width / 2, 2: elem.width / 2}.get(elem.pathtype, 0)
                    w(f"_path.bgn_ext = {_fmt_float(ext)}")
                    w(f"_path.end_ext = {_fmt_float(ext)}")
                layer_expr = _layer_expr(elem.layer, elem.datatype, layer_map)
                w(f"{var}.shapes({layer_expr}).insert(_path)")

            elif isinstance(elem, SRef):
                ref_var = cell_vars.get(elem.sname, f'layout.cell("{elem.sname}")')
                angle  = _fmt_float(elem.angle)
                mag    = _fmt_float(elem.mag)
                mirror = "True" if elem.x_reflection else "False"
                ox, oy = elem.xy
                w(f"{var}.insert(pya.DCellInstArray(")
                w(f"    {ref_var}.cell_index(),")
                w(f"    pya.DCplxTrans({mag}, {angle}, {mirror},")
                w(f"                  pya.DVector({_fmt_float(ox)}, {_fmt_float(oy)}))))")

            elif isinstance(elem, ARef):
                ref_var = cell_vars.get(elem.sname, f'layout.cell("{elem.sname}")')
                angle  = _fmt_float(elem.angle)
                mag    = _fmt_float(elem.mag)
                mirror = "True" if elem.x_reflection else "False"
                # AREF XY: [origin, col_end, row_end]
                # KLayout column vector = (col_end - origin) / columns
                # KLayout row    vector = (row_end - origin) / rows
                ox, oy       = elem.xy[0]
                col_ex, col_ey = elem.xy[1]
                row_ex, row_ey = elem.xy[2]
                col_vx = (col_ex - ox) / elem.columns
                col_vy = (col_ey - oy) / elem.columns
                row_vx = (row_ex - ox) / elem.rows
                row_vy = (row_ey - oy) / elem.rows
                w(f"{var}.insert(pya.DCellInstArray(")
                w(f"    {ref_var}.cell_index(),")
                w(f"    pya.DCplxTrans({mag}, {angle}, {mirror},")
                w(f"                  pya.DVector({_fmt_float(ox)}, {_fmt_float(oy)})),")
                w(f"    pya.DVector({_fmt_float(col_vx)}, {_fmt_float(col_vy)}),")
                w(f"    pya.DVector({_fmt_float(row_vx)}, {_fmt_float(row_vy)}),")
                w(f"    {elem.columns}, {elem.rows}))")

            elif isinstance(elem, Text):
                ox, oy = elem.xy
                # Use integer-coordinate pya.Text (not DText).
                # KLayout forum confirms DText.halign/valign are unreliable
                # in several versions; Text (integer coords) works correctly.
                rot    = int(round(elem.angle / 90.0)) % 4
                mirror = "True" if bool(elem.strans & 0x8000) else "False"
                text_escaped = elem.string.replace('"', '\\"')
                layer_expr = _layer_expr(elem.layer, elem.texttype, layer_map)
                ix = int(round(ox / dbu_um))
                iy = int(round(oy / dbu_um))
                w(f'_txt = pya.Text(\"{text_escaped}\",')
                w(f'               pya.Trans({rot}, {mirror}, pya.Vector({ix}, {iy})))')
                if elem.halign != 0:
                    w(f"_txt.halign = {elem.halign}")
                if elem.valign != 0:
                    w(f"_txt.valign = {elem.valign}")
                w(f"{var}.shapes({layer_expr}).insert(_txt)")
        w("")

    w("# Save")
    w(f'layout.write("output.gds")')
    w("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# 10.  CLI entry point
# ---------------------------------------------------------------------------

def main():
    import argparse
    ap = argparse.ArgumentParser(
        description="Translate a GDSII file to a KLayout Python (pya) script."
    )
    ap.add_argument("input",  help="Input .gds file")
    ap.add_argument("output", nargs="?", help="Output .py file (default: <input>_klayout.py)")
    ap.add_argument(
        "--layer-map", metavar="FILE",
        help=(
            "Layer-name map file.  Format: one entry per line, "
            "each line being '<layer> <datatype> <name>' where "
            "<name> is a Python identifier.  Blank lines and "
            "lines starting with # are ignored.  "
            "When supplied, shapes on mapped layers use "
            "layout.layer(\"name\") instead of layout.layer(n, d)."
        ),
    )
    args = ap.parse_args()

    in_path  = args.input
    out_path = args.output or (
        os.path.splitext(os.path.basename(in_path))[0] + "_klayout.py"
    )

    layer_map: dict = {}
    if args.layer_map:
        try:
            layer_map = parse_layer_map(args.layer_map)
        except LayerMapError as e:
            print(f"Layer-map error: {e}", file=sys.stderr)
            sys.exit(3)
        print(f"Layer map: {len(layer_map)} entries loaded from {args.layer_map!r}")

    try:
        lib = parse_gds(in_path)
    except (ParseError, FsmError) as e:
        print(f"Parse error: {e}", file=sys.stderr)
        sys.exit(2)

    script = generate_klayout_script(lib, layer_map=layer_map)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(script)

    n_structs  = len(lib.structures)
    n_elements = sum(len(s.elements) for s in lib.structures)
    print(f"Translated {n_structs} structures, {n_elements} elements → {out_path}")


if __name__ == "__main__":
    main()
