# make_dac_m2_pins.py
# Generates Metal2 EN/ENB/ON/ONB input pin boxes + labels for dac4x32module top level.
#
# Reads pin positions directly from dac2u32out4in sub-cell geometry, so positions
# are always correct. Applies global index mapping across 4 instances.
#
# Global numbering (physical left → right):
#   TOP:    EN8  ENB8  ON64..79  ONB64..79  EN9  ENB9  |  EN10..11  ON80..95 ...
#   BOTTOM: EN7  ENB7  ONB63..48 ON63..48   EN6  ENB6  |  EN5..4    ONB47..32 ...
#
# Sub-cell local → global mapping for instance k (0=leftmost):
#   sub EN[0] (bot-left)  → EN[7-2k]
#   sub EN[1] (bot-right) → EN[6-2k]
#   sub EN[3] (top-left)  → EN[8+2k]
#   sub EN[2] (top-right) → EN[9+2k]
#   sub ON[i]  bottom     → ON[63-16k-i]   (i=0..15)
#   sub ON[i]  top        → ON[95+16k-i]   (i=16..31, reverses to 64+16k..79+16k)
#   ONB follows same mapping as ON

try:
    from klayout import db as pya
except ImportError:
    import pya

import re, sys

# ── open the existing dac4x32module GDS ──────────────────────────────────────
GDS_IN  = "dac4x32module.gds"
GDS_OUT = "dac4x32module.gds"   # overwrite in place (change to _out.gds to be safe)

layout = pya.Layout()
layout.read(GDS_IN)

top = layout.cell("dac4x32module")
sub = layout.cell("dac2u32out4in")

if top is None or sub is None:
    sys.exit("Could not find dac4x32module or dac2u32out4in in GDS")

l_pin   = layout.layer(pya.LayerInfo(10, 2))
l_label = layout.layer(pya.LayerInfo(10, 25))

HALF_X = 100   # 200 nm wide
HALF_Y = 145   # 290 nm tall

# ── collect sub-cell pin positions by name ───────────────────────────────────
sub_pins = {}   # name → (local_x, local_y)  center coords in sub-cell frame
for shape in sub.shapes(l_label):
    if shape.is_text():
        t = shape.text
        name = t.string
        if re.match(r'(EN|ENB|ON|ONB)\[', name):
            sub_pins[name] = (t.x * layout.dbu, t.y * layout.dbu)

# ── find dac2u32out4in instance origins (may be a single array instance) ────
# KLayout CellInstArray: iterate with each_inst(), expand columns/rows manually
inst_origins = []
for inst in top.each_inst():
    if layout.cell(inst.cell_index).name == "dac2u32out4in":
        na = inst.size_a if inst.is_regular_array() else 1
        nb = inst.size_b if inst.is_regular_array() else 1
        for ia in range(na):
            for ib in range(nb):
                disp = inst.dtrans.disp
                if inst.is_regular_array():
                    disp = disp + inst.a * ia + inst.b * ib
                inst_origins.append(disp.x * layout.dbu)
inst_origins = sorted(inst_origins)

if len(inst_origins) != 4:
    print(f"Warning: found {len(inst_origins)} dac2u32out4in origins, expected 4")
print("Instance origins (um):", inst_origins)

# ── global name mapping ───────────────────────────────────────────────────────
def global_name(sub_name, k):
    m = re.match(r'(EN|ENB|ON|ONB)\[(\d+)\]', sub_name)
    if not m:
        return sub_name
    sig, idx = m.group(1), int(m.group(2))
    if sig in ('EN', 'ENB'):
        # sub EN[0]=bot-left, EN[1]=bot-right, EN[2]=top-right, EN[3]=top-left
        en_map = {0: 7-2*k, 1: 6-2*k, 2: 9+2*k, 3: 8+2*k}
        return f"{sig}[{en_map[idx]}]"
    else:  # ON or ONB
        if idx <= 15:   # bottom row: sub 0..15 → global 63-16k .. 48-16k
            g = 63 - 16*k - idx
        else:           # top row:    sub 16..31 → global 64+16k .. 79+16k
            g = 95 + 16*k - idx
        return f"{sig}[{g}]"

# ── remove any existing generated pins/labels ────────────────────────────────
# (delete all M2 pin/label shapes directly on the top cell)
top.shapes(l_pin).clear()
top.shapes(l_label).clear()

# ── place pins ───────────────────────────────────────────────────────────────
dbu = layout.dbu

def place(name, cx_um, cy_um):
    cx = round(cx_um / dbu)
    cy = round(cy_um / dbu)
    top.shapes(l_pin).insert(pya.Box(cx-HALF_X, cy-HALF_Y, cx+HALF_X, cy+HALF_Y))
    t = pya.Text(name, pya.Trans(pya.Vector(cx, cy)))
    t.halign = pya.HAlign.HAlignCenter
    t.valign = pya.VAlign.VAlignCenter
    top.shapes(l_label).insert(t)

for k, ox in enumerate(inst_origins):
    for sub_name, (lx, ly) in sub_pins.items():
        gname = global_name(sub_name, k)
        place(gname, ox + lx, ly)

layout.write(GDS_OUT)
n = top.shapes(l_pin).size()
print(f"Wrote {GDS_OUT}  ({n} pins)")
