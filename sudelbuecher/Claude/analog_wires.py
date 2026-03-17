import pya

layout = pya.Layout()
layout.dbu = 0.001  # 1 nm per DBU; all coordinates below are in µm

cell = layout.create_cell("analog_wires")


# ── helpers ──────────────────────────────────────────────────────────────────

def dbu(um):
    """Convert microns to database units."""
    return round(um / layout.dbu)

def box(layer, datatype, x1_um, y1_um, x2_um, y2_um):
    idx = layout.layer(layer, datatype)
    cell.shapes(idx).insert(pya.Box(dbu(x1_um), dbu(y1_um), dbu(x2_um), dbu(y2_um)))

def path(layer, datatype, pts_um, width_um):
    idx = layout.layer(layer, datatype)
    pts = [pya.Point(dbu(x), dbu(y)) for x, y in pts_um]
    p = pya.Path(pts, dbu(width_um))
    # GDS pathtype 2 = flush ends (no extension beyond endpoint)
    p.bgn_ext = 0
    p.end_ext = 0
    cell.shapes(idx).insert(p)

def label(layer, texttype, text, x_um, y_um):
    idx = layout.layer(layer, texttype)
    # anchor=5 in gdspy = W (west / left-center)
    t = pya.Text(text, pya.Trans(pya.Point(dbu(x_um), dbu(y_um))))
    t.halign = pya.HAlign.HAlignLeft
    t.valign = pya.VAlign.VAlignCenter
    cell.shapes(idx).insert(t)


# ── Boxes ─────────────────────────────────────────────────────────────────────

# layer 189/4 – PR boundary / bounding box
box(189, 4,   0.0,   0.0,  99.6, 188.0)

# layer 30/2 – pin marker rectangles (right side)
box(30, 2,  99.2, 103.930,  99.6, 104.630)
box(30, 2,  99.2,  95.745,  99.6,  96.445)

# layer 30/2 – pin marker rectangles (left side, top group ~152–168 µm)
box(30, 2,   0.0, 167.830,   0.4, 168.530)
box(30, 2,   0.0, 151.460,   0.4, 152.160)
box(30, 2,   0.0, 159.645,   0.4, 160.345)
box(30, 2,   0.0, 152.560,   0.4, 154.290)
box(30, 2,   0.0, 165.700,   0.4, 167.430)
box(30, 2,   0.0, 158.345,   0.4, 159.045)
box(30, 2,   0.0, 160.945,   0.4, 161.645)

# layer 30/2 – pin marker rectangles (left side, bottom group ~19–36 µm)
box(30, 2,   0.0,  35.770,   0.4,  36.470)
box(30, 2,   0.0,  19.400,   0.4,  20.100)
box(30, 2,   0.0,  27.585,   0.4,  28.285)
box(30, 2,   0.0,  20.500,   0.4,  22.230)
box(30, 2,   0.0,  33.640,   0.4,  35.370)
box(30, 2,   0.0,  26.285,   0.4,  26.985)
box(30, 2,   0.0,  28.885,   0.4,  29.585)


# ── Paths (layer 30/0, flush ends) ───────────────────────────────────────────

# bottom group
path(30, 0, [( 0.0,  36.120), (10.91,  36.120)],  0.7)
path(30, 0, [( 0.0,  19.750), (10.91,  19.750)],  0.7)
path(30, 0, [( 0.0,  27.935), (21.91,  27.935)],  0.7)
path(30, 0, [( 0.0,  21.365), (20.70,  21.365)],  1.73)
path(30, 0, [( 0.0,  34.505), (20.70,  34.505)],  1.73)
path(30, 0, [( 0.0,  29.235), (21.91,  29.235)],  0.7)
path(30, 0, [( 0.0,  26.635), (21.91,  26.635)],  0.7)

# top group
path(30, 0, [( 0.0, 153.425), (20.70, 153.425)],  1.73)
path(30, 0, [( 0.0, 166.565), (20.70, 166.565)],  1.73)
path(30, 0, [( 0.0, 161.295), (21.91, 161.295)],  0.7)
path(30, 0, [( 0.0, 158.695), (21.91, 158.695)],  0.7)
path(30, 0, [( 0.0, 159.995), (21.91, 159.995)],  0.7)
path(30, 0, [( 0.0, 168.180), (10.91, 168.180)],  0.7)
path(30, 0, [( 0.0, 151.810), (10.91, 151.810)],  0.7)

# full-width horizontal bus wires
path(30, 0, [( 0.0,  96.095), (99.60,  96.095)],  0.7)
path(30, 0, [( 0.0, 104.280), (99.60, 104.280)],  0.7)


# ── Labels (layer 30/25) ─────────────────────────────────────────────────────

# bottom group
label(30, 25, "VcascP[0]",  0.2,  19.750)
label(30, 25, "VcascP[1]",  0.2,  36.120)
label(30, 25, "Iout[0]",    0.2,  27.935)
label(30, 25, "VDDA[0]",    0.2,  21.365)
label(30, 25, "VDDA[1]",    0.2,  34.505)
label(30, 25, "VbiasP[1]",  0.2,  29.235)
label(30, 25, "VbiasP[0]",  0.2,  26.635)

# top group
label(30, 25, "VcascP[2]",  0.2, 151.810)
label(30, 25, "VcascP[3]",  0.2, 168.180)
label(30, 25, "Iout[1]",    0.2, 159.995)
label(30, 25, "VDDA[2]",    0.2, 153.425)
label(30, 25, "VDDA[3]",    0.2, 166.565)
label(30, 25, "VbiasP[3]",  0.2, 161.295)
label(30, 25, "VbiasP[2]",  0.2, 158.695)

# right-side pins
label(30, 25, "i_in",       99.4, 104.280)
label(30, 25, "i_out",      99.4,  96.095)


# ── Write ─────────────────────────────────────────────────────────────────────

layout.write("analog_wires_rebuilt.gds")
print("Written: analog_wires_rebuilt.gds")
