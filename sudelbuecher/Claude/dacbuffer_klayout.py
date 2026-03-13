import pya

layout = pya.Layout()

layout.dbu = 0.001

# --- layer index variables ---
L_8_0 = layout.layer(8, 0)
L_8_2 = layout.layer(8, 2)
L_8_25 = layout.layer(8, 25)
L_30_0 = layout.layer(30, 0)
L_30_2 = layout.layer(30, 2)
L_30_25 = layout.layer(30, 25)
L_189_4 = layout.layer(189, 4)

# --- cell declarations ---
cell_dacbuffer = layout.create_cell("dacbuffer")

# === dacbuffer ===
_path = pya.DPath([pya.DPoint(0, 0.25), pya.DPoint(37.8, 0.25)], 0.5)
cell_dacbuffer.shapes(L_8_0).insert(_path)
_path = pya.DPath([pya.DPoint(0, 13.095), pya.DPoint(37.8, 13.095)], 0.7)
cell_dacbuffer.shapes(L_8_0).insert(_path)
_path = pya.DPath([pya.DPoint(0, 25.94), pya.DPoint(37.8, 25.94)], 0.5)
cell_dacbuffer.shapes(L_8_0).insert(_path)
_path = pya.DPath([pya.DPoint(0, 0.865), pya.DPoint(37.8, 0.865)], 1.73)
cell_dacbuffer.shapes(L_30_0).insert(_path)
_path = pya.DPath([pya.DPoint(0, 3.295), pya.DPoint(37.8, 3.295)], 1.73)
cell_dacbuffer.shapes(L_30_0).insert(_path)
_path = pya.DPath([pya.DPoint(0, 6.525), pya.DPoint(37.8, 6.525)], 1.73)
cell_dacbuffer.shapes(L_30_0).insert(_path)
_path = pya.DPath([pya.DPoint(0, 19.665), pya.DPoint(37.8, 19.665)], 1.73)
cell_dacbuffer.shapes(L_30_0).insert(_path)
_path = pya.DPath([pya.DPoint(0, 22.895), pya.DPoint(37.8, 22.895)], 1.73)
cell_dacbuffer.shapes(L_30_0).insert(_path)
_path = pya.DPath([pya.DPoint(0, 25.325), pya.DPoint(37.8, 25.325)], 1.73)
cell_dacbuffer.shapes(L_30_0).insert(_path)
cell_dacbuffer.shapes(L_189_4).insert(
    pya.DPolygon([pya.DPoint(0, -0.07), pya.DPoint(0, 26.26), pya.DPoint(37.8, 26.26), pya.DPoint(37.8, -0.07), pya.DPoint(0, -0.07)]))
cell_dacbuffer.shapes(L_8_2).insert(
    pya.DPolygon([pya.DPoint(0, 12.745), pya.DPoint(0, 13.445), pya.DPoint(37.8, 13.445), pya.DPoint(37.8, 12.745), pya.DPoint(0, 12.745)]))
_txt = pya.Text("Iout",
               pya.Trans(0, False, pya.Vector(18900, 13095)))
_txt.halign = 1
_txt.valign = 1
cell_dacbuffer.shapes(L_8_25).insert(_txt)
cell_dacbuffer.shapes(L_30_2).insert(
    pya.DPolygon([pya.DPoint(0, 0), pya.DPoint(0, 1.73), pya.DPoint(37.8, 1.73), pya.DPoint(37.8, 0), pya.DPoint(0, 0)]))
cell_dacbuffer.shapes(L_30_2).insert(
    pya.DPolygon([pya.DPoint(0, 2.43), pya.DPoint(0, 4.16), pya.DPoint(37.8, 4.16), pya.DPoint(37.8, 2.43), pya.DPoint(0, 2.43)]))
cell_dacbuffer.shapes(L_30_2).insert(
    pya.DPolygon([pya.DPoint(0, 5.66), pya.DPoint(0, 7.39), pya.DPoint(37.8, 7.39), pya.DPoint(37.8, 5.66), pya.DPoint(0, 5.66)]))
cell_dacbuffer.shapes(L_30_2).insert(
    pya.DPolygon([pya.DPoint(0, 18.8), pya.DPoint(0, 20.53), pya.DPoint(37.8, 20.53), pya.DPoint(37.8, 18.8), pya.DPoint(0, 18.8)]))
cell_dacbuffer.shapes(L_30_2).insert(
    pya.DPolygon([pya.DPoint(0, 22.03), pya.DPoint(0, 23.76), pya.DPoint(37.8, 23.76), pya.DPoint(37.8, 22.03), pya.DPoint(0, 22.03)]))
cell_dacbuffer.shapes(L_30_2).insert(
    pya.DPolygon([pya.DPoint(0, 24.46), pya.DPoint(0, 26.19), pya.DPoint(37.8, 26.19), pya.DPoint(37.8, 24.46), pya.DPoint(0, 24.46)]))
_txt = pya.Text("VSS",
               pya.Trans(0, False, pya.Vector(18900, 250)))
_txt.halign = 1
_txt.valign = 1
cell_dacbuffer.shapes(L_8_25).insert(_txt)
_txt = pya.Text("VSS",
               pya.Trans(0, False, pya.Vector(18900, 865)))
_txt.halign = 1
_txt.valign = 1
cell_dacbuffer.shapes(L_30_25).insert(_txt)
_txt = pya.Text("VDD",
               pya.Trans(0, False, pya.Vector(18900, 3295)))
_txt.halign = 1
_txt.valign = 1
cell_dacbuffer.shapes(L_30_25).insert(_txt)
_txt = pya.Text("VDD",
               pya.Trans(0, False, pya.Vector(18900, 6525)))
_txt.halign = 1
_txt.valign = 1
cell_dacbuffer.shapes(L_30_25).insert(_txt)
_txt = pya.Text("VDD",
               pya.Trans(0, False, pya.Vector(18900, 19665)))
_txt.halign = 1
_txt.valign = 1
cell_dacbuffer.shapes(L_30_25).insert(_txt)
_txt = pya.Text("VDD",
               pya.Trans(0, False, pya.Vector(18900, 22895)))
_txt.halign = 1
_txt.valign = 1
cell_dacbuffer.shapes(L_30_25).insert(_txt)
_txt = pya.Text("VSS",
               pya.Trans(0, False, pya.Vector(18900, 25325)))
_txt.halign = 1
_txt.valign = 1
cell_dacbuffer.shapes(L_30_25).insert(_txt)
_txt = pya.Text("VSS",
               pya.Trans(0, False, pya.Vector(18900, 25940)))
_txt.halign = 1
_txt.valign = 1
cell_dacbuffer.shapes(L_8_25).insert(_txt)

# Save
layout.write("output.gds")
