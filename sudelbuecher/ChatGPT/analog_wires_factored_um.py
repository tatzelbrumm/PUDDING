import pya

layout = pya.Layout()
layout.dbu = 0.001  # 1 nm database units; geometry below is specified in um

top = layout.create_cell("analog_wires")

L_30_0 = layout.layer(30, 0)
L_30_2 = layout.layer(30, 2)
L_30_25 = layout.layer(30, 25)
L_189_4 = layout.layer(189, 4)


def add_path_um(layer, x1, y1, x2, y2, width):
    top.shapes(layer).insert(
        pya.DPath([pya.DPoint(x1, y1), pya.DPoint(x2, y2)], width)
    )


def add_rect_um(layer, x1, y1, x2, y2):
    top.shapes(layer).insert(pya.DBox(x1, y1, x2, y2))


def add_text_um(layer, text, x, y, size=0.4):
    t = pya.DText(text, x, y)
    t.size = size
    top.shapes(layer).insert(t)


def shift_path_list(items, dy):
    return [(x1, y1 + dy, x2, y2 + dy, width) for x1, y1, x2, y2, width in items]


def shift_rect_list(items, dy):
    return [(x1, y1 + dy, x2, y2 + dy) for x1, y1, x2, y2 in items]


die_area = (0.0, 0.0, 99.6, 188.0)
BANK_DY = 128.280

lower_bank_paths = [
    (0.0, 39.900, 10.910, 39.900, 0.700),  # VcascP[1]
    (0.0, 23.530, 10.910, 23.530, 0.700),  # VcascP[0]
    (0.0, 31.715, 21.910, 31.715, 0.700),  # Iout[0]
    (0.0, 25.145, 20.700, 25.145, 1.730),  # VDDA[0]
    (0.0, 38.285, 20.700, 38.285, 1.730),  # VDDA[1]
    (0.0, 33.015, 21.910, 33.015, 0.700),  # VbiasP[1]
    (0.0, 30.415, 21.910, 30.415, 0.700),  # VbiasP[0]
]

lower_bank_markers = [
    (0.0, 39.550, 0.400, 40.250),
    (0.0, 23.180, 0.400, 23.880),
    (0.0, 31.365, 0.400, 32.065),
    (0.0, 24.280, 0.400, 26.010),
    (0.0, 37.420, 0.400, 39.150),
    (0.0, 30.065, 0.400, 30.765),
    (0.0, 32.665, 0.400, 33.365),
]

lower_bank_labels = [
    ("VcascP[0]", 0.200, 23.530),
    ("VcascP[1]", 0.200, 39.900),
    ("Iout[0]", 0.200, 31.715),
    ("VDDA[0]", 0.200, 25.145),
    ("VDDA[1]", 0.200, 38.285),
    ("VbiasP[1]", 0.200, 33.015),
    ("VbiasP[0]", 0.200, 30.415),
]

upper_bank_paths = shift_path_list(lower_bank_paths, BANK_DY)
upper_bank_markers = shift_rect_list(lower_bank_markers, BANK_DY)
upper_bank_labels = [
    ("VcascP[2]", 0.200, 151.810),
    ("VcascP[3]", 0.200, 168.180),
    ("Iout[1]", 0.200, 159.995),
    ("VDDA[2]", 0.200, 153.425),
    ("VDDA[3]", 0.200, 166.565),
    ("VbiasP[3]", 0.200, 161.295),
    ("VbiasP[2]", 0.200, 158.695),
]

right_edge_io_paths = [
    (0.0, 96.095, 99.600, 96.095, 0.700),
    (0.0, 104.280, 99.600, 104.280, 0.700),
]

right_edge_markers = [
    (99.200, 95.745, 99.600, 96.445),
    (99.200, 103.930, 99.600, 104.630),
]

right_edge_io_labels = [
    ("i_out", 99.400, 96.095),
    ("i_in", 99.400, 104.280),
]


# DIE AREA
add_rect_um(L_189_4, *die_area)

# BANK PATHS
for x1, y1, x2, y2, width in lower_bank_paths:
    add_path_um(L_30_0, x1, y1, x2, y2, width)

for x1, y1, x2, y2, width in upper_bank_paths:
    add_path_um(L_30_0, x1, y1, x2, y2, width)

# RIGHT EDGE PATHS
for x1, y1, x2, y2, width in right_edge_io_paths:
    add_path_um(L_30_0, x1, y1, x2, y2, width)

# BANK MARKERS
for x1, y1, x2, y2 in lower_bank_markers:
    add_rect_um(L_30_2, x1, y1, x2, y2)

for x1, y1, x2, y2 in upper_bank_markers:
    add_rect_um(L_30_2, x1, y1, x2, y2)

# RIGHT EDGE MARKERS
for x1, y1, x2, y2 in right_edge_markers:
    add_rect_um(L_30_2, x1, y1, x2, y2)

# BANK LABELS
for text, x, y in lower_bank_labels:
    add_text_um(L_30_25, text, x, y)

for text, x, y in upper_bank_labels:
    add_text_um(L_30_25, text, x, y)

# RIGHT EDGE LABELS
for text, x, y in right_edge_io_labels:
    add_text_um(L_30_25, text, x, y)

layout.write("analog_wires_roundtrip.gds")
