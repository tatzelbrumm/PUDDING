# make_dac_pads.py
try:
    from klayout import db as pya
except:
    import pya

# Create layout
layout = pya.Layout()
layout.dbu = 0.001  # 1 nm units
top = layout.create_cell("DAC_PADS")

# Parameters
coordinates = ((-275,-4765),(275,-4765))
suffixes=("","B")
size = 290
columns = (64,2)
origins = ((2000, 0),(0, 0))
offsets = ((2000, 0),(65*2000,0))
labels = ("ON","EN")

# Layers
l_m2pin = layout.layer(pya.LayerInfo(10, 2))
l_m2text= layout.layer(pya.LayerInfo(10,25))

# Draw shapes
half = size // 2
for n, origin, offset, label in zip(columns, origins, offsets, labels):
    for source in range(n):
        for coordinate, suffix in zip(coordinates, suffixes):
            # element-wise addition: coordinate + source*offset
            x, y = (c + source * m + o for c, m, o in zip(coordinate, offset, origin))
            top.shapes(l_m2pin).insert(pya.Box(x - half, y - half, x + half, y + half))

            text = pya.Text(label + suffix + f"[{source}]", x, y)
            text.halign = pya.Text.HAlignCenter
            text.valign = pya.Text.VAlignCenter
            top.shapes(l_m2text).insert(text)

# Draw shapes of upside down row
toprow=(130000, 16370)
for n, origin, offset, label, in zip(columns, origins, offsets, labels):
    for source in range(n):
        for coordinate, suffix in zip(coordinates, suffixes):
            # element-wise addition: coordinate + source*offset
            x, y = (t - (c + source * m + o) for t, c, m, o in zip(toprow, coordinate, offset, origin))
            top.shapes(l_m2pin).insert(pya.Box(x - half, y - half, x + half, y + half))

            index= source + n
            text = pya.Text(label + suffix + f"[{index}]", x, y)
            text.halign = pya.Text.HAlignCenter
            text.valign = pya.Text.VAlignCenter
            top.shapes(l_m2text).insert(text)

# Save GDS
layout.write("dac_pads.gds")
print("Wrote dac_pads.gds")

