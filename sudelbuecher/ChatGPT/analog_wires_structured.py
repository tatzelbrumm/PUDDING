import pya

layout = pya.Layout()
layout.dbu = 0.001

top = layout.create_cell("analog_wires")

L_30_0 = layout.layer(30, 0)
L_30_2 = layout.layer(30, 2)
L_30_25 = layout.layer(30, 25)
L_189_4 = layout.layer(189, 4)


def add_path(layer, x1, y1, x2, y2, width):
    top.shapes(layer).insert(pya.Path([pya.Point(x1, y1), pya.Point(x2, y2)], width))


def add_rect(layer, x1, y1, x2, y2):
    top.shapes(layer).insert(
        pya.Polygon([
            pya.Point(x1, y1),
            pya.Point(x1, y2),
            pya.Point(x2, y2),
            pya.Point(x2, y1),
            pya.Point(x1, y1),
        ])
    )


def add_text(layer, text, x, y, size=400):
    t = pya.Text(text, x, y)
    t.size = size
    top.shapes(layer).insert(t)


# PATHS
for x1, y1, x2, y2, width in [
    (0, 39900, 10910, 39900, 700),
    (0, 23530, 10910, 23530, 700),
    (0, 31715, 21910, 31715, 700),
    (0, 25145, 20700, 25145, 1730),
    (0, 38285, 20700, 38285, 1730),
    (0, 33015, 21910, 33015, 700),
    (0, 30415, 21910, 30415, 700),
    (0, 153425, 20700, 153425, 1730),
    (0, 166565, 20700, 166565, 1730),
    (0, 161295, 21910, 161295, 700),
    (0, 158695, 21910, 158695, 700),
    (0, 159995, 21910, 159995, 700),
    (0, 168180, 10910, 168180, 700),
    (0, 151810, 10910, 151810, 700),
    (0, 96095, 99600, 96095, 700),
    (0, 104280, 99600, 104280, 700),
]:
    add_path(L_30_0, x1, y1, x2, y2, width)


# BOUNDARY / DIE AREA
add_rect(L_189_4, 0, 0, 99600, 188000)


# PIN / MARKER RECTANGLES
for x1, y1, x2, y2 in [
    (99200, 103930, 99600, 104630),
    (99200, 95745, 99600, 96445),
    (0, 167830, 400, 168530),
    (0, 151460, 400, 152160),
    (0, 159645, 400, 160345),
    (0, 152560, 400, 154290),
    (0, 165700, 400, 167430),
    (0, 158345, 400, 159045),
    (0, 160945, 400, 161645),
    (0, 39550, 400, 40250),
    (0, 23180, 400, 23880),
    (0, 31365, 400, 32065),
    (0, 24280, 400, 26010),
    (0, 37420, 400, 39150),
    (0, 30065, 400, 30765),
    (0, 32665, 400, 33365),
]:
    add_rect(L_30_2, x1, y1, x2, y2)


# TEXTS
for text, x, y in [
    ("VcascP[0]", 200, 23530),
    ("VcascP[1]", 200, 39900),
    ("Iout[0]", 200, 31715),
    ("VDDA[0]", 200, 25145),
    ("VDDA[1]", 200, 38285),
    ("VbiasP[1]", 200, 33015),
    ("VbiasP[0]", 200, 30415),
    ("VcascP[2]", 200, 151810),
    ("VcascP[3]", 200, 168180),
    ("Iout[1]", 200, 159995),
    ("VDDA[2]", 200, 153425),
    ("VDDA[3]", 200, 166565),
    ("VbiasP[3]", 200, 161295),
    ("VbiasP[2]", 200, 158695),
    ("i_in", 99400, 104280),
    ("i_out", 99400, 96095),
]:
    add_text(L_30_25, text, x, y)

layout.write("analog_wires_roundtrip.gds")
