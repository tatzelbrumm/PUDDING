import pya

layout = pya.Layout()
layout.dbu = 0.001  # 1 nm per DBU; all coordinates below are in µm

cell = layout.create_cell("analog_wires")


# ── helpers ──────────────────────────────────────────────────────────────────

def dbu(um):
    """Convert microns to database units."""
    return round(um / layout.dbu)

def poly(layer, datatype, pts_um):
    idx = layout.layer(layer, datatype)
    pts = [pya.Point(dbu(x), dbu(y)) for x, y in pts_um]
    cell.shapes(idx).insert(pya.Polygon(pts))

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


# ── Polygons ─────────────────────────────────────────────────────────────────

# layer 189/4 – PR boundary / bounding box
poly(189, 4, [
    (  0.0,   0.0),
    (  0.0, 188.0),
    ( 99.6, 188.0),
    ( 99.6,   0.0),
])

# layer 30/2 – pin marker rectangles (right side)
poly(30, 2, [(99.2, 103.930), (99.2, 104.630), (99.6, 104.630), (99.6, 103.930)])
poly(30, 2, [(99.2,  95.745), (99.2,  96.445), (99.6,  96.445), (99.6,  95.745)])

# layer 30/2 – pin marker rectangles (left side, top group ~152–168 µm)
poly(30, 2, [( 0.0, 167.830), ( 0.0, 168.530), ( 0.4, 168.530), ( 0.4, 167.830)])
poly(30, 2, [( 0.0, 151.460), ( 0.0, 152.160), ( 0.4, 152.160), ( 0.4, 151.460)])
poly(30, 2, [( 0.0, 159.645), ( 0.0, 160.345), ( 0.4, 160.345), ( 0.4, 159.645)])
poly(30, 2, [( 0.0, 152.560), ( 0.0, 154.290), ( 0.4, 154.290), ( 0.4, 152.560)])
poly(30, 2, [( 0.0, 165.700), ( 0.0, 167.430), ( 0.4, 167.430), ( 0.4, 165.700)])
poly(30, 2, [( 0.0, 158.345), ( 0.0, 159.045), ( 0.4, 159.045), ( 0.4, 158.345)])
poly(30, 2, [( 0.0, 160.945), ( 0.0, 161.645), ( 0.4, 161.645), ( 0.4, 160.945)])

# layer 30/2 – pin marker rectangles (left side, bottom group ~19–36 µm)
poly(30, 2, [( 0.0,  35.770), ( 0.0,  36.470), ( 0.4,  36.470), ( 0.4,  35.770)])
poly(30, 2, [( 0.0,  19.400), ( 0.0,  20.100), ( 0.4,  20.100), ( 0.4,  19.400)])
poly(30, 2, [( 0.0,  27.585), ( 0.0,  28.285), ( 0.4,  28.285), ( 0.4,  27.585)])
poly(30, 2, [( 0.0,  20.500), ( 0.0,  22.230), ( 0.4,  22.230), ( 0.4,  20.500)])
poly(30, 2, [( 0.0,  33.640), ( 0.0,  35.370), ( 0.4,  35.370), ( 0.4,  33.640)])
poly(30, 2, [( 0.0,  26.285), ( 0.0,  26.985), ( 0.4,  26.985), ( 0.4,  26.285)])
poly(30, 2, [( 0.0,  28.885), ( 0.0,  29.585), ( 0.4,  29.585), ( 0.4,  28.885)])


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
