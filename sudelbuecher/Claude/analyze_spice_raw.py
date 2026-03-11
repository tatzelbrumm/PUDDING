#!/usr/bin/env python3
"""
ngspice RAW analyzer — pure stdlib, keine Dependencies
Usage: python3 analyze_spice_raw.py <file.raw> [--csv] [--list-vars] [--outdir DIR]
Output: <stem>_summary.txt  and  <stem>.html  (standalone, kein Server)
"""
import argparse, math, os, re, struct, sys
from pathlib import Path


# ─── Parse ─────────────────────────────────────────────────────────────────────

def parse_raw(path):
    """Liest alle Plots aus einer ngspice binary RAW Datei.
    Gibt Liste von dicts zurück: {name, nv, np, vars:[(idx,name,type)], data:[[float]]}"""
    raw    = open(path, "rb").read()
    plots  = []
    pos    = 0

    while (binary_pos := raw.find(b"Binary:\n", pos)) != -1:
        # Header parsen
        header    = raw[pos:binary_pos].decode(errors="replace")
        plot_name = ""
        nv = np   = 0
        variables = []

        for line in header.splitlines():
            line = line.strip()
            if   line.startswith("Plotname:"):      plot_name = line[9:].strip()
            elif line.startswith("No. Variables:"): nv        = int(line[14:])
            elif line.startswith("No. Points:"):    np        = int(line[11:])
            elif re.match(r"\d+\t", line):
                idx, name, kind = line.split("\t")[:3]
                variables.append((int(idx), name.strip(), kind.strip()))

        # Binärdaten lesen
        data_start = binary_pos + 8   # len("Binary:\n") == 8
        if nv > 0 and np > 0:
            flat = struct.unpack_from(f"<{nv * np}d", raw, data_start)
            data = [list(flat[row * nv : (row + 1) * nv]) for row in range(np)]
            plots.append({"name": plot_name, "nv": nv, "np": np,
                          "vars": variables, "data": data})
            pos = data_start + nv * np * 8
        else:
            pos = data_start + 1

    return plots


# ─── Helpers ───────────────────────────────────────────────────────────────────

def find_col(plot, needle):
    """Gibt Spaltenindex für Variablenname (exakt, dann partial, case-insensitiv)."""
    needle = needle.lower()
    names  = [name.lower() for (_, name, _) in plot["vars"]]
    for i, name in enumerate(names):
        if name == needle:    return i
    for i, name in enumerate(names):
        if needle in name:    return i
    return None


def get_col(plot, needle):
    """Gibt Spalte als Liste oder None."""
    i = find_col(plot, needle)
    return [row[i] for row in plot["data"]] if i is not None else None


def detect_outer_sweep(plot):
    """
    DC-Sweeps haben eine innere (z.B. VDS) und eine äußere Achse (z.B. VlogI).
    Erkennt die Struktur anhand von Rücksprüngen in Spalte 0.
    Gibt (n_inner, n_outer, inner_axis) zurück.
    """
    axis    = [row[0] for row in plot["data"]]
    resets  = [i for i in range(1, len(axis)) if axis[i] - axis[i-1] < -0.05]
    n_inner = resets[0]          if resets else len(axis)
    n_outer = len(resets) + 1
    return n_inner, n_outer, axis[:n_inner]


def logi_to_iref(n_outer):
    """Äußerer Sweep ist VlogI von -8 bis -6 → IRef in Ampere."""
    return [10 ** (-8 + i * 2 / max(n_outer - 1, 1)) for i in range(n_outer)]


def si(value, unit=""):
    """Formatiert Zahl mit SI-Präfix, z.B. 1.5e-9 → '1.5 nA'."""
    if not math.isfinite(value): return "n/a"
    prefixes = [(1e15,"f"),(1e12,"p"),(1e9,"n"),(1e6,"µ"),(1e3,"m"),(1,"")]
    for scale, prefix in prefixes:
        if abs(value) * scale >= 0.999 and abs(value) * scale < 1000:
            return f"{value * scale:.4g} {prefix}{unit}".strip()
    return f"{value:.3e} {unit}".strip()


UNIT_OF = {"voltage": "V", "current": "A", "admittance": "S", "capacitance": "F"}
INTERESTING_KEYS = ("ids", "gm", "gds", "vth", "vgs", "vds", "cgg", "cgsol", "cgdol")


# ─── Text Summary ──────────────────────────────────────────────────────────────

def make_summary(plots, path):
    lines = ["═" * 68, f"  {Path(path).name}", "═" * 68]

    for pi, plot in enumerate(plots):
        name = plot["name"]
        lines.append(f"\n[{pi}] {name}  ({plot['np']} pts, {plot['nv']} vars)")

        if "operating" in name.lower():
            for (_, var_name, var_type) in plot["vars"]:
                if any(k in var_name.lower() for k in INTERESTING_KEYS):
                    value = plot["data"][0][find_col(plot, var_name)]
                    unit  = UNIT_OF.get(var_type, "")
                    lines.append(f"  {var_name:<48} {si(value, unit):>14}")

        elif "dc" in name.lower() or "transfer" in name.lower():
            n_inner, n_outer, vds_axis = detect_outer_sweep(plot)
            i_vd     = get_col(plot, "i(vd)")        # < 0 when NMOS sinks current
            i_vprobe = get_col(plot, "i(vprobe)")    # > 0, equals IRef

            if i_vd is None:
                lines.append("  (Kein i(vd) gefunden)")
                continue

            iref_list = logi_to_iref(n_outer)
            vds_idx   = min(range(len(vds_axis)), key=lambda i: abs(vds_axis[i] - 0.6))

            lines.append(f"  {n_outer} IRef-Kurven × {n_inner} VDS-Punkte"
                         f"  (VDS {vds_axis[0]:.2f}…{vds_axis[-1]:.2f} V)")
            lines.append(f"  {'IRef':>10}  {'Iout@0.6V':>12}  {'Ratio':>8}  {'ro@0.6V':>12}")

            for k in range(n_outer):
                # Vorzeichen: Iout = -i(vd),  IRef = i(vprobe)
                Iout = [-i_vd[k * n_inner + j]     for j in range(n_inner)]
                IRef =  i_vprobe[k * n_inner + vds_idx] if i_vprobe else iref_list[k]

                ratio = Iout[vds_idx] / (IRef + 1e-30)

                # r_o = median(dVDS/dIout) im linearen Bereich
                ro_samples = [
                    abs((vds_axis[j] - vds_axis[j-1]) / (Iout[j] - Iout[j-1] + 1e-30))
                    for j in range(1, n_inner)
                    if 0.3 < (vds_axis[j] + vds_axis[j-1]) / 2 < 0.9
                ]
                ro = sorted(ro_samples)[len(ro_samples) // 2] if ro_samples else float("nan")

                lines.append(f"  {si(IRef,'A'):>10}  {si(Iout[vds_idx],'A'):>12}"
                             f"  {ratio:>8.5f}  {si(ro,'Ω'):>12}")

    lines.append("\n" + "═" * 68)
    return "\n".join(lines)


# ─── CSV Export ────────────────────────────────────────────────────────────────

def write_csv(plot, path):
    n_inner, n_outer, _ = detect_outer_sweep(plot)
    col_names = ",".join(name for (_, name, _) in plot["vars"])

    with open(path, "w") as f:
        f.write(f"sweep_idx,{col_names}\n")
        for k in range(n_outer):
            for j in range(n_inner):
                row = plot["data"][k * n_inner + j]
                f.write(f"{k}," + ",".join(f"{v:.6e}" for v in row) + "\n")


# ─── SVG Chart ─────────────────────────────────────────────────────────────────
#
# Series format: [(label, [x...], [y...], color), ...]

COLORS = ["#58a6ff","#3fb950","#ff7b72","#d2a8ff","#ffa657",
          "#79c0ff","#56d364","#ff9492","#bc8cff","#ffb86c"]

def make_svg(width, height, title, series, xlabel, ylabel,
             xlog=False, ylog=False, hline=None):

    PAD_L, PAD_R, PAD_T, PAD_B = 72, 20, 36, 48
    W = width  - PAD_L - PAD_R
    H = height - PAD_T - PAD_B

    # Data range
    all_x = [x for (_, xs, ys, _) in series for x in xs
              if math.isfinite(x) and (x > 0 if xlog else True)]
    all_y = [y for (_, xs, ys, _) in series for y in ys
              if math.isfinite(y) and (y > 0 if ylog else True)]
    if not all_x or not all_y:
        return f'<svg width="{width}" height="{height}" style="background:#161b22"></svg>'

    x_min, x_max = min(all_x), max(all_x)
    y_min, y_max = min(all_y), max(all_y)
    if x_min == x_max: x_max = x_min + 1
    if y_min == y_max: y_max = y_min * 10 if y_min > 0 else y_min + 1

    def to_px(x, lo, hi, out_size, log):
        if log:
            lx = math.log10(max(x,  1e-300))
            ll = math.log10(max(lo, 1e-300))
            lh = math.log10(max(hi, 1e-300))
            return (lx - ll) / (lh - ll + 1e-30) * out_size
        return (x - lo) / (hi - lo) * out_size

    def px(x): return PAD_L + to_px(x, x_min, x_max, W, xlog)
    def py(y): return PAD_T + H - to_px(y, y_min, y_max, H, ylog)

    def nice_ticks(lo, hi, n=6):
        if hi <= lo: return [lo]
        step = (hi - lo) / n
        mag  = 10 ** math.floor(math.log10(step))
        step = min([1, 2, 2.5, 5, 10], key=lambda s: abs(s * mag - step)) * mag
        v    = math.ceil(lo / step) * step
        ticks = []
        while v <= hi + step * 0.01:
            ticks.append(round(v, 12)); v += step
        return ticks

    def log_ticks(lo, hi):
        e0 = math.floor(math.log10(max(lo, 1e-300)))
        e1 = math.ceil( math.log10(max(hi, 1e-300)))
        return [10.0 ** e for e in range(int(e0), int(e1) + 1)]

    def fmt(v):
        a = abs(v)
        for d, p in ((1e9,"G"),(1e6,"M"),(1e3,"k"),(1,""),(1e-3,"m"),(1e-6,"µ"),(1e-9,"n"),(1e-12,"p")):
            if a / d >= 0.999 and a / d < 1000: return f"{v/d:.3g}{p}"
        return f"{v:.2e}"

    x_ticks = log_ticks(x_min, x_max) if xlog else nice_ticks(x_min, x_max, 7)
    y_ticks = log_ticks(y_min, y_max) if ylog else nice_ticks(y_min, y_max, 6)
    clip_id = f"c{abs(hash(title)) % 99999}"

    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
               f'style="background:#161b22;border-radius:6px;display:block;margin:4px">')
    svg.append(f'<defs><clipPath id="{clip_id}">'
               f'<rect x="{PAD_L}" y="{PAD_T}" width="{W}" height="{H}"/></clipPath></defs>')

    # Grid lines + tick labels
    for xv in x_ticks:
        xp = px(xv)
        if PAD_L <= xp <= PAD_L + W:
            svg.append(f'<line x1="{xp:.1f}" y1="{PAD_T}" x2="{xp:.1f}" y2="{PAD_T+H}" stroke="#21262d"/>')
            svg.append(f'<text x="{xp:.1f}" y="{PAD_T+H+14}" fill="#8b949e" font-size="10" '
                       f'text-anchor="middle" font-family="monospace">{fmt(xv)}</text>')
    for yv in y_ticks:
        yp = py(yv)
        if PAD_T <= yp <= PAD_T + H:
            svg.append(f'<line x1="{PAD_L}" y1="{yp:.1f}" x2="{PAD_L+W}" y2="{yp:.1f}" stroke="#21262d"/>')
            svg.append(f'<text x="{PAD_L-4}" y="{yp+4:.1f}" fill="#8b949e" font-size="10" '
                       f'text-anchor="end" font-family="monospace">{fmt(yv)}</text>')

    svg.append(f'<rect x="{PAD_L}" y="{PAD_T}" width="{W}" height="{H}" '
               f'fill="none" stroke="#30363d" stroke-width="1.5"/>')

    # Optional horizontal reference line
    if hline is not None and y_min <= hline <= y_max:
        yp = py(hline)
        svg.append(f'<line x1="{PAD_L}" y1="{yp:.1f}" x2="{PAD_L+W}" y2="{yp:.1f}" '
                   f'stroke="#555" stroke-dasharray="5,4"/>')

    # Data series
    for (label, xs, ys, color) in series:
        points = []
        for x, y in zip(xs, ys):
            if not (math.isfinite(x) and math.isfinite(y)): continue
            if xlog and x <= 0: continue
            if ylog and y <= 0: continue
            points.append(f"{px(x):.1f},{py(y):.1f}")
        if points:
            svg.append(f'<polyline clip-path="url(#{clip_id})" points="{" ".join(points)}" '
                       f'fill="none" stroke="{color}" stroke-width="1.8" '
                       f'stroke-linejoin="round" stroke-linecap="round"/>')

    # Legend (top-right, inside plot)
    for i, (label, _, _, color) in enumerate(series[:8]):
        lx = PAD_L + W - 8
        ly = PAD_T + 8 + i * 16
        svg.append(f'<line x1="{lx-26}" y1="{ly+4}" x2="{lx-3}" y2="{ly+4}" '
                   f'stroke="{color}" stroke-width="2"/>')
        svg.append(f'<text x="{lx-29}" y="{ly+8}" fill="#c9d1d9" font-size="9" '
                   f'text-anchor="end" font-family="monospace">{label}</text>')

    # Axis labels + title
    svg.append(f'<text x="{PAD_L+W//2}" y="{height-5}" fill="#8b949e" font-size="11" '
               f'text-anchor="middle" font-family="monospace">{xlabel}</text>')
    svg.append(f'<text x="11" y="{PAD_T+H//2}" fill="#8b949e" font-size="11" '
               f'text-anchor="middle" font-family="monospace" '
               f'transform="rotate(-90,11,{PAD_T+H//2})">{ylabel}</text>')
    svg.append(f'<text x="{PAD_L+W//2}" y="{PAD_T-10}" fill="#e6edf3" font-size="12" '
               f'font-weight="bold" text-anchor="middle" font-family="monospace">{title}</text>')
    svg.append("</svg>")
    return "\n".join(svg)


# ─── HTML Report ───────────────────────────────────────────────────────────────

HTML_CSS = """
* { box-sizing: border-box; margin: 0; padding: 0 }
body { background: #0d1117; color: #e6edf3; font-family: 'Courier New', monospace;
       padding: 28px; line-height: 1.5 }
h1   { color: #58a6ff; font-size: 1.3em; margin-bottom: 4px }
h2   { color: #79c0ff; font-size: 1.0em; margin: 28px 0 10px;
       padding-bottom: 5px; border-bottom: 1px solid #30363d }
.sub { color: #8b949e; font-size: .82em; font-weight: normal }
.row { display: flex; flex-wrap: wrap; gap: 6px }
pre  { background: #161b22; border: 1px solid #30363d; border-radius: 6px;
       padding: 14px; font-size: .79em; overflow-x: auto; color: #c9d1d9; margin: 14px 0 }
table { border-collapse: collapse; font-size: .83em }
th, td { padding: 5px 14px; border-bottom: 1px solid #21262d }
th { background: #21262d; color: #58a6ff }
tr:hover td { background: #161b22 }
"""

def make_html(plots, summary_text, path):
    stem     = Path(path).stem
    sections = []

    for pi, plot in enumerate(plots):
        name = plot["name"]

        # ── Operating Point: einfache Tabelle ──────────────────────────
        if "operating" in name.lower():
            rows = ""
            for (idx, var_name, var_type) in plot["vars"]:
                if any(k in var_name.lower() for k in INTERESTING_KEYS):
                    value = plot["data"][0][idx]
                    unit  = UNIT_OF.get(var_type, "")
                    rows += f"<tr><td>{var_name}</td><td>{si(value, unit)}</td></tr>"
            if rows:
                sections.append(
                    f"<h2>Operating Point &mdash; Run {pi+1}</h2>"
                    f"<table><tr><th>Variable</th><th>Wert</th></tr>{rows}</table>")
            continue

        if not ("dc" in name.lower() or "transfer" in name.lower()):
            continue

        # ── DC Sweep: drei Charts ───────────────────────────────────────
        n_inner, n_outer, vds_axis = detect_outer_sweep(plot)
        i_vd     = get_col(plot, "i(vd)")
        i_vprobe = get_col(plot, "i(vprobe)")

        if i_vd is None:
            continue

        iref_list = logi_to_iref(n_outer)
        labels    = [si(iref, "A") for iref in iref_list]

        def curve_slice(col, k):
            return [col[k * n_inner + j] for j in range(n_inner)]

        # Chart 1: Iout vs VDS
        series_ids = []
        for k in range(n_outer):
            Iout = [-v for v in curve_slice(i_vd, k)]   # Iout = -i(vd)
            series_ids.append((labels[k], vds_axis, Iout, COLORS[k % len(COLORS)]))

        # Chart 2: Mirror Ratio = -i(vd) / i(vprobe) = Iout / IRef
        series_ratio = []
        if i_vprobe:
            for k in range(n_outer):
                Iout = [-v for v in curve_slice(i_vd, k)]
                IRef =        curve_slice(i_vprobe, k)      # IRef = +i(vprobe)
                xs   = [vds_axis[j] for j in range(n_inner) if vds_axis[j] > 0.05]
                ys   = [Iout[j] / (IRef[j] + 1e-30) for j in range(n_inner) if vds_axis[j] > 0.05]
                series_ratio.append((labels[k], xs, ys, COLORS[k % len(COLORS)]))

        # Chart 3: r_o vs VDS (log Y)
        series_ro = []
        for k in range(n_outer):
            Iout = [-v for v in curve_slice(i_vd, k)]
            xs, ys = [], []
            for j in range(1, n_inner):
                vds_mid = (vds_axis[j] + vds_axis[j-1]) / 2
                dVDS    =  vds_axis[j] - vds_axis[j-1]
                dIout   =  Iout[j]    - Iout[j-1]
                if vds_mid > 0.05 and abs(dIout) > 1e-30:
                    xs.append(vds_mid)
                    ys.append(abs(dVDS / dIout))
            series_ro.append((labels[k], xs, ys, COLORS[k % len(COLORS)]))

        sub = f"{n_outer} I_ref &times; {n_inner} V_DS"
        sections.append(
            f"<h2>DC Sweep &mdash; Run {pi+1} <span class=sub>({sub})</span></h2>"
            f"<div class=row>"
            f"{make_svg(640, 310, 'I_out vs V_DS', series_ids, 'V_DS [V]', 'I_out [A]')}"
            + (f"{make_svg(640, 270, 'Mirror Ratio I_out/I_ref', series_ratio, 'V_DS [V]', 'I_out / I_ref', hline=1.0)}" if series_ratio else "")
            + f"{make_svg(640, 270, 'r_o vs V_DS', series_ro, 'V_DS [V]', 'r_o [Ω]', ylog=True)}"
            f"</div>")

    # ── Parametric Comparison: alle DC-Runs zusammen ───────────────────
    dc_plots = [p for p in plots
                if "dc" in p["name"].lower() or "transfer" in p["name"].lower()]

    if len(dc_plots) >= 2:
        series_iout  = []
        series_ratio = []

        for pi, plot in enumerate(dc_plots):
            n_inner, n_outer, vds_axis = detect_outer_sweep(plot)
            i_vd     = get_col(plot, "i(vd)")
            i_vprobe = get_col(plot, "i(vprobe)")
            if i_vd is None: continue

            vds_idx = min(range(len(vds_axis)), key=lambda i: abs(vds_axis[i] - 0.6))
            xs = logi_to_iref(n_outer)

            Iout_at_vds = [-i_vd    [k * n_inner + vds_idx] for k in range(n_outer)]
            IRef_at_vds = [ i_vprobe[k * n_inner + vds_idx] for k in range(n_outer)] if i_vprobe else xs
            ratio_at_vds = [Iout_at_vds[k] / (IRef_at_vds[k] + 1e-30) for k in range(n_outer)]

            color = COLORS[pi % len(COLORS)]
            series_iout .append((f"Run {pi+1}", xs, Iout_at_vds,  color))
            series_ratio.append((f"Run {pi+1}", xs, ratio_at_vds, color))

        # Ideallinie
        all_x = sorted({x for (_, xs, _, _) in series_iout for x in xs})
        series_iout.append(("ideal", all_x, all_x, "#555"))

        sections.append(
            "<h2>Parametric Comparison &mdash; alle Runs</h2>"
            "<div class=row>"
            + make_svg(640, 300, "I_out @ V_DS=0.6V vs I_ref", series_iout,
                       "I_ref [A]", "I_out [A]", xlog=True, ylog=True)
            + make_svg(640, 280, "Mirror Ratio vs I_ref", series_ratio,
                       "I_ref [A]", "I_out / I_ref", xlog=True, hline=1.0)
            + "</div>")

    return (f"<!DOCTYPE html><html lang=de><head><meta charset=UTF-8>"
            f"<title>{stem}</title><style>{HTML_CSS}</style></head><body>"
            f"<h1>ngspice RAW &mdash; {stem}</h1>"
            f"<pre>{summary_text}</pre>"
            + "".join(sections)
            + "</body></html>")


# ─── Main ──────────────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("raw")
    ap.add_argument("--outdir",    default=".")
    ap.add_argument("--csv",       action="store_true", help="CSV-Dateien exportieren")
    ap.add_argument("--list-vars", action="store_true", help="Variablen auflisten")
    args = ap.parse_args()

    if not os.path.exists(args.raw):
        sys.exit(f"Fehler: '{args.raw}' nicht gefunden.")

    os.makedirs(args.outdir, exist_ok=True)
    stem = os.path.join(args.outdir, Path(args.raw).stem)

    plots = parse_raw(args.raw)
    print(f"{len(plots)} plot(s) in {args.raw}\n")

    if args.list_vars:
        for pi, plot in enumerate(plots):
            print(f"[{pi}] {plot['name']}  ({plot['np']} pts, {plot['nv']} vars)")
            for (idx, name, kind) in plot["vars"]:
                print(f"  {idx:3d}  {name:<50}  {kind}")
        return

    summary = make_summary(plots, args.raw)
    print(summary)

    open(f"{stem}_summary.txt", "w").write(summary)
    print(f"\n→ {stem}_summary.txt")

    if args.csv:
        for pi, plot in enumerate(plots):
            slug = re.sub(r"\W", "_", plot["name"]).lower()
            out  = f"{stem}_{slug}.csv"
            write_csv(plot, out)
            print(f"→ {out}")

    html = make_html(plots, summary, args.raw)
    open(f"{stem}.html", "w").write(html)
    print(f"→ {stem}.html")


if __name__ == "__main__":
    main()
