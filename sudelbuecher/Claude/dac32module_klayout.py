import pya

layout = pya.Layout()
layout.dbu = 0.001

# --- cell declarations ---
cell____CONTEXT_INFO___ = layout.create_cell("$$$CONTEXT_INFO$$$")
cell_FEOL_contacts_1_1_1_1_1 = layout.create_cell("FEOL$contacts$1$1$1$1$1")
cell_FEOL_contacts_3_2_1 = layout.create_cell("FEOL$contacts$3$2$1")
cell_via_stack_1_1_1_1_1 = layout.create_cell("via_stack$1$1$1$1$1")
cell_FEOL_contacts_9_1 = layout.create_cell("FEOL$contacts$9$1")
cell_via_stack_3_1_1 = layout.create_cell("via_stack$3$1$1")
cell_via_stack_2_1_1_1 = layout.create_cell("via_stack$2$1$1$1")
cell_NONOVERLAP = layout.create_cell("NONOVERLAP")
cell_DAC_SW = layout.create_cell("DAC_SW")
cell_FEOL_contacts_6_1_1_1 = layout.create_cell("FEOL$contacts$6$1$1$1")
cell_FEOL_contacts_7_1_1_1 = layout.create_cell("FEOL$contacts$7$1$1$1")
cell_FEOL_contacts_5_1_1_1 = layout.create_cell("FEOL$contacts$5$1$1$1")
cell_FEOL_contacts_4_1_1_1 = layout.create_cell("FEOL$contacts$4$1$1$1")
cell_FEOL_contacts_1_2_1_1 = layout.create_cell("FEOL$contacts$1$2$1$1")
cell_via_stack_9_1 = layout.create_cell("via_stack$9$1")
cell_CASCODEDRIVE = layout.create_cell("CASCODEDRIVE")
cell_PCSOURCE2U = layout.create_cell("PCSOURCE2U")
cell_via_stack_4_1 = layout.create_cell("via_stack$4$1")
cell_via_stack_7_2 = layout.create_cell("via_stack$7$2")
cell_via_stack_6_2_1 = layout.create_cell("via_stack$6$2$1")
cell_via_stack_6 = layout.create_cell("via_stack$6")
cell_via_stack_5 = layout.create_cell("via_stack$5")
cell_FEOL_contacts_8 = layout.create_cell("FEOL$contacts$8")
cell_FEOL_contacts_3_1 = layout.create_cell("FEOL$contacts$3$1")
cell_unitsource2u = layout.create_cell("unitsource2u")
cell_CASCODEBIAS = layout.create_cell("CASCODEBIAS")
cell_dac2u16out2in = layout.create_cell("dac2u16out2in")
cell_via_stack = layout.create_cell("via_stack")
cell_via_stack_4 = layout.create_cell("via_stack$4")
cell_via_stack_7 = layout.create_cell("via_stack$7")
cell_dac2u32out4in = layout.create_cell("dac2u32out4in")
cell_dac128module_vdd_strap = layout.create_cell("dac128module_vdd_strap")
cell_dac128module_vss_strap = layout.create_cell("dac128module_vss_strap")
cell_dac128module_analog_straps = layout.create_cell("dac128module_analog_straps")
cell_dac32module = layout.create_cell("dac32module")

# === $$$CONTEXT_INFO$$$ ===
cell____CONTEXT_INFO___.insert(pya.DCellInstArray(
    cell_via_stack_7.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(0, 0))))

# === FEOL$contacts$1$1$1$1$1 ===
cell_FEOL_contacts_1_1_1_1_1.shapes(layout.layer(8, 0)).insert(
    pya.DPolygon([pya.DPoint(0, 0), pya.DPoint(0, 0.16), pya.DPoint(0.26, 0.16), pya.DPoint(0.26, 0), pya.DPoint(0, 0)]))
cell_FEOL_contacts_1_1_1_1_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(0.05, 0), pya.DPoint(0.05, 0.16), pya.DPoint(0.21, 0.16), pya.DPoint(0.21, 0), pya.DPoint(0.05, 0)]))

# === FEOL$contacts$3$2$1 ===
cell_FEOL_contacts_3_2_1.shapes(layout.layer(8, 0)).insert(
    pya.DPolygon([pya.DPoint(0, 0), pya.DPoint(0, 0.5), pya.DPoint(1.92, 0.5), pya.DPoint(1.92, 0), pya.DPoint(0, 0)]))
cell_FEOL_contacts_3_2_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(0.2, 0), pya.DPoint(0.2, 0.16), pya.DPoint(0.36, 0.16), pya.DPoint(0.36, 0), pya.DPoint(0.2, 0)]))
cell_FEOL_contacts_3_2_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(0.54, 0), pya.DPoint(0.54, 0.16), pya.DPoint(0.7, 0.16), pya.DPoint(0.7, 0), pya.DPoint(0.54, 0)]))
cell_FEOL_contacts_3_2_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(0.88, 0), pya.DPoint(0.88, 0.16), pya.DPoint(1.04, 0.16), pya.DPoint(1.04, 0), pya.DPoint(0.88, 0)]))
cell_FEOL_contacts_3_2_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(1.22, 0), pya.DPoint(1.22, 0.16), pya.DPoint(1.38, 0.16), pya.DPoint(1.38, 0), pya.DPoint(1.22, 0)]))
cell_FEOL_contacts_3_2_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(1.56, 0), pya.DPoint(1.56, 0.16), pya.DPoint(1.72, 0.16), pya.DPoint(1.72, 0), pya.DPoint(1.56, 0)]))
cell_FEOL_contacts_3_2_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(0.2, 0.34), pya.DPoint(0.2, 0.5), pya.DPoint(0.36, 0.5), pya.DPoint(0.36, 0.34), pya.DPoint(0.2, 0.34)]))
cell_FEOL_contacts_3_2_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(0.54, 0.34), pya.DPoint(0.54, 0.5), pya.DPoint(0.7, 0.5), pya.DPoint(0.7, 0.34), pya.DPoint(0.54, 0.34)]))
cell_FEOL_contacts_3_2_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(0.88, 0.34), pya.DPoint(0.88, 0.5), pya.DPoint(1.04, 0.5), pya.DPoint(1.04, 0.34), pya.DPoint(0.88, 0.34)]))
cell_FEOL_contacts_3_2_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(1.22, 0.34), pya.DPoint(1.22, 0.5), pya.DPoint(1.38, 0.5), pya.DPoint(1.38, 0.34), pya.DPoint(1.22, 0.34)]))
cell_FEOL_contacts_3_2_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(1.56, 0.34), pya.DPoint(1.56, 0.5), pya.DPoint(1.72, 0.5), pya.DPoint(1.72, 0.34), pya.DPoint(1.56, 0.34)]))

# === via_stack$1$1$1$1$1 ===
cell_via_stack_1_1_1_1_1.shapes(layout.layer(8, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.145, -0.145), pya.DPoint(-0.145, 0.145), pya.DPoint(0.145, 0.145), pya.DPoint(0.145, -0.145), pya.DPoint(-0.145, -0.145)]))
cell_via_stack_1_1_1_1_1.shapes(layout.layer(10, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.145, -0.145), pya.DPoint(-0.145, 0.145), pya.DPoint(0.145, 0.145), pya.DPoint(0.145, -0.145), pya.DPoint(-0.145, -0.145)]))
cell_via_stack_1_1_1_1_1.shapes(layout.layer(19, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.095, -0.095), pya.DPoint(-0.095, 0.095), pya.DPoint(0.095, 0.095), pya.DPoint(0.095, -0.095), pya.DPoint(-0.095, -0.095)]))

# === FEOL$contacts$9$1 ===
cell_FEOL_contacts_9_1.shapes(layout.layer(8, 0)).insert(
    pya.DPolygon([pya.DPoint(0, 0), pya.DPoint(0, 0.16), pya.DPoint(0.26, 0.16), pya.DPoint(0.26, 0), pya.DPoint(0, 0)]))
cell_FEOL_contacts_9_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(0.05, 0), pya.DPoint(0.05, 0.16), pya.DPoint(0.21, 0.16), pya.DPoint(0.21, 0), pya.DPoint(0.05, 0)]))

# === via_stack$3$1$1 ===
cell_via_stack_3_1_1.shapes(layout.layer(8, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.145, -0.145), pya.DPoint(-0.145, 0.145), pya.DPoint(0.145, 0.145), pya.DPoint(0.145, -0.145), pya.DPoint(-0.145, -0.145)]))
cell_via_stack_3_1_1.shapes(layout.layer(10, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.145, -0.145), pya.DPoint(-0.145, 0.145), pya.DPoint(0.145, 0.145), pya.DPoint(0.145, -0.145), pya.DPoint(-0.145, -0.145)]))
cell_via_stack_3_1_1.shapes(layout.layer(19, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.095, -0.095), pya.DPoint(-0.095, 0.095), pya.DPoint(0.095, 0.095), pya.DPoint(0.095, -0.095), pya.DPoint(-0.095, -0.095)]))
cell_via_stack_3_1_1.shapes(layout.layer(30, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.145, -0.145), pya.DPoint(-0.145, 0.145), pya.DPoint(0.145, 0.145), pya.DPoint(0.145, -0.145), pya.DPoint(-0.145, -0.145)]))
cell_via_stack_3_1_1.shapes(layout.layer(29, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.095, -0.095), pya.DPoint(-0.095, 0.095), pya.DPoint(0.095, 0.095), pya.DPoint(0.095, -0.095), pya.DPoint(-0.095, -0.095)]))

# === via_stack$2$1$1$1 ===
cell_via_stack_2_1_1_1.shapes(layout.layer(8, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.145, -0.145), pya.DPoint(-0.145, 0.145), pya.DPoint(0.145, 0.145), pya.DPoint(0.145, -0.145), pya.DPoint(-0.145, -0.145)]))
cell_via_stack_2_1_1_1.shapes(layout.layer(10, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.145, -0.145), pya.DPoint(-0.145, 0.145), pya.DPoint(0.145, 0.145), pya.DPoint(0.145, -0.145), pya.DPoint(-0.145, -0.145)]))
cell_via_stack_2_1_1_1.shapes(layout.layer(19, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.095, -0.095), pya.DPoint(-0.095, 0.095), pya.DPoint(0.095, 0.095), pya.DPoint(0.095, -0.095), pya.DPoint(-0.095, -0.095)]))

# === NONOVERLAP ===
cell_NONOVERLAP.insert(pya.DCellInstArray(
    cell_FEOL_contacts_3_2_1.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(-0.96, 0.55))))
cell_NONOVERLAP.insert(pya.DCellInstArray(
    cell_FEOL_contacts_1_1_1_1_1.cell_index(),
    pya.DCplxTrans(1, 90, False,
                  pya.DVector(0.825, -0.13))))
cell_NONOVERLAP.insert(pya.DCellInstArray(
    cell_FEOL_contacts_1_1_1_1_1.cell_index(),
    pya.DCplxTrans(1, 90, False,
                  pya.DVector(0.08, -0.13))))
cell_NONOVERLAP.insert(pya.DCellInstArray(
    cell_FEOL_contacts_1_1_1_1_1.cell_index(),
    pya.DCplxTrans(1, 90, False,
                  pya.DVector(-0.665, -0.13))))
cell_NONOVERLAP.insert(pya.DCellInstArray(
    cell_FEOL_contacts_1_1_1_1_1.cell_index(),
    pya.DCplxTrans(1, 90, False,
                  pya.DVector(-0.26, -0.5))))
cell_NONOVERLAP.insert(pya.DCellInstArray(
    cell_FEOL_contacts_1_1_1_1_1.cell_index(),
    pya.DCplxTrans(1, 90, False,
                  pya.DVector(0.42, -0.5))))
cell_NONOVERLAP.insert(pya.DCellInstArray(
    cell_FEOL_contacts_1_1_1_1_1.cell_index(),
    pya.DCplxTrans(1, 90, False,
                  pya.DVector(-0.665, -2.23))))
cell_NONOVERLAP.insert(pya.DCellInstArray(
    cell_FEOL_contacts_1_1_1_1_1.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(0.165, -1.41))))
cell_NONOVERLAP.insert(pya.DCellInstArray(
    cell_FEOL_contacts_1_1_1_1_1.cell_index(),
    pya.DCplxTrans(1, 90, False,
                  pya.DVector(0.825, -2.23))))
cell_NONOVERLAP.insert(pya.DCellInstArray(
    cell_FEOL_contacts_1_1_1_1_1.cell_index(),
    pya.DCplxTrans(1, 90, False,
                  pya.DVector(0.08, -2.23))))
cell_NONOVERLAP.insert(pya.DCellInstArray(
    cell_FEOL_contacts_3_2_1.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(-0.96, -3.03))))
cell_NONOVERLAP.insert(pya.DCellInstArray(
    cell_via_stack_1_1_1_1_1.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(0.275, -0.455))))
cell_NONOVERLAP.insert(pya.DCellInstArray(
    cell_via_stack_1_1_1_1_1.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(-0.275, -0.455))))
cell_NONOVERLAP.insert(pya.DCellInstArray(
    cell_via_stack_1_1_1_1_1.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(0.745, 0.025))))
cell_NONOVERLAP.insert(pya.DCellInstArray(
    cell_via_stack_1_1_1_1_1.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(-0.745, 0.025))))
cell_NONOVERLAP.insert(pya.DCellInstArray(
    cell_FEOL_contacts_1_1_1_1_1.cell_index(),
    pya.DCplxTrans(1, 90, False,
                  pya.DVector(0.825, -0.98))))
_path = pya.DPath([pya.DPoint(0.38, -1.33), pya.DPoint(-0.745, -1.33)], 0.16)
cell_NONOVERLAP.shapes(layout.layer(8, 0)).insert(_path)
_path = pya.DPath([pya.DPoint(-0.745, -2.02), pya.DPoint(-0.745, -0.08)], 0.16)
cell_NONOVERLAP.shapes(layout.layer(8, 0)).insert(_path)
_path = pya.DPath([pya.DPoint(0.745, -2.02), pya.DPoint(0.745, -0.08)], 0.16)
cell_NONOVERLAP.shapes(layout.layer(8, 0)).insert(_path)
_path = pya.DPath([pya.DPoint(0, -2.02), pya.DPoint(0, -2.69)], 0.16)
cell_NONOVERLAP.shapes(layout.layer(8, 0)).insert(_path)
_path = pya.DPath([pya.DPoint(0, 0.71), pya.DPoint(0, -0.08)], 0.16)
cell_NONOVERLAP.shapes(layout.layer(8, 0)).insert(_path)
cell_NONOVERLAP.shapes(layout.layer(8, 0)).insert(
    pya.DPolygon([pya.DPoint(-1, 0.55), pya.DPoint(-1, 1.05), pya.DPoint(1, 1.05), pya.DPoint(1, 0.55), pya.DPoint(-1, 0.55)]))
cell_NONOVERLAP.shapes(layout.layer(8, 0)).insert(
    pya.DPolygon([pya.DPoint(-1, -3.03), pya.DPoint(-1, -2.53), pya.DPoint(1, -2.53), pya.DPoint(1, -3.03), pya.DPoint(-1, -3.03)]))
cell_NONOVERLAP.shapes(layout.layer(8, 0)).insert(
    pya.DPolygon([pya.DPoint(-1, 0.55), pya.DPoint(-1, 1.05), pya.DPoint(1, 1.05), pya.DPoint(1, 0.55), pya.DPoint(-1, 0.55)]))
_path = pya.DPath([pya.DPoint(0, -1.63), pya.DPoint(0, -2.18)], 0.15)
cell_NONOVERLAP.shapes(layout.layer(1, 0)).insert(_path)
_path = pya.DPath([pya.DPoint(0.82, -1.635), pya.DPoint(0.82, -2.18)], 0.15)
cell_NONOVERLAP.shapes(layout.layer(1, 0)).insert(_path)
_path = pya.DPath([pya.DPoint(-0.82, -1.63), pya.DPoint(-0.82, -2.18)], 0.15)
cell_NONOVERLAP.shapes(layout.layer(1, 0)).insert(_path)
cell_NONOVERLAP.shapes(layout.layer(1, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.895, -0.15), pya.DPoint(-0.895, 0.15), pya.DPoint(0.895, 0.15), pya.DPoint(0.895, -0.15), pya.DPoint(-0.895, -0.15)]))
cell_NONOVERLAP.shapes(layout.layer(1, 0)).insert(
    pya.DPolygon([pya.DPoint(-1, 0.48), pya.DPoint(-1, 1.12), pya.DPoint(1, 1.12), pya.DPoint(1, 0.48), pya.DPoint(-1, 0.48)]))
cell_NONOVERLAP.shapes(layout.layer(1, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.895, -1.7), pya.DPoint(-0.895, -1.55), pya.DPoint(0.895, -1.55), pya.DPoint(0.895, -1.7), pya.DPoint(-0.895, -1.7)]))
cell_NONOVERLAP.shapes(layout.layer(1, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.895, -2.25), pya.DPoint(-0.895, -1.95), pya.DPoint(-0.595, -1.95), pya.DPoint(-0.595, -2.25), pya.DPoint(-0.895, -2.25)]))
cell_NONOVERLAP.shapes(layout.layer(1, 0)).insert(
    pya.DPolygon([pya.DPoint(0.595, -2.25), pya.DPoint(0.595, -1.95), pya.DPoint(0.895, -1.95), pya.DPoint(0.895, -2.25), pya.DPoint(0.595, -2.25)]))
cell_NONOVERLAP.shapes(layout.layer(1, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.15, -2.25), pya.DPoint(-0.15, -1.95), pya.DPoint(0.15, -1.95), pya.DPoint(0.15, -2.25), pya.DPoint(-0.15, -2.25)]))
cell_NONOVERLAP.shapes(layout.layer(1, 0)).insert(
    pya.DPolygon([pya.DPoint(-1, -3.1), pya.DPoint(-1, -2.46), pya.DPoint(1, -2.46), pya.DPoint(1, -3.1), pya.DPoint(-1, -3.1)]))
_path = pya.DPath([pya.DPoint(-0.295, -1.475), pya.DPoint(-0.295, -0.85), pya.DPoint(0.745, -0.85)], 0.3)
cell_NONOVERLAP.shapes(layout.layer(5, 0)).insert(_path)
cell_NONOVERLAP.shapes(layout.layer(5, 0)).insert(
    pya.DPolygon([pya.DPoint(0.19, -0.33), pya.DPoint(0.19, 0.33), pya.DPoint(0.32, 0.33), pya.DPoint(0.32, -0.33), pya.DPoint(0.19, -0.33)]))
cell_NONOVERLAP.shapes(layout.layer(5, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.32, -0.33), pya.DPoint(-0.32, 0.33), pya.DPoint(-0.19, 0.33), pya.DPoint(-0.19, -0.33), pya.DPoint(-0.32, -0.33)]))
cell_NONOVERLAP.shapes(layout.layer(5, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.49, -0.52), pya.DPoint(-0.49, -0.22), pya.DPoint(-0.19, -0.22), pya.DPoint(-0.19, -0.52), pya.DPoint(-0.49, -0.52)]))
cell_NONOVERLAP.shapes(layout.layer(5, 0)).insert(
    pya.DPolygon([pya.DPoint(0.19, -0.52), pya.DPoint(0.19, -0.22), pya.DPoint(0.49, -0.22), pya.DPoint(0.49, -0.52), pya.DPoint(0.19, -0.52)]))
cell_NONOVERLAP.shapes(layout.layer(5, 0)).insert(
    pya.DPolygon([pya.DPoint(0.145, -1.88), pya.DPoint(0.145, -1.37), pya.DPoint(0.665, -1.37), pya.DPoint(0.665, -1.88), pya.DPoint(0.145, -1.88)]))
cell_NONOVERLAP.shapes(layout.layer(5, 0)).insert(
    pya.DPolygon([pya.DPoint(0.145, -1.48), pya.DPoint(0.145, -1.18), pya.DPoint(0.445, -1.18), pya.DPoint(0.445, -1.48), pya.DPoint(0.145, -1.48)]))
cell_NONOVERLAP.shapes(layout.layer(5, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.665, -1.88), pya.DPoint(-0.665, -1.37), pya.DPoint(-0.145, -1.37), pya.DPoint(-0.145, -1.88), pya.DPoint(-0.665, -1.88)]))
cell_NONOVERLAP.shapes(layout.layer(5, 0)).insert(
    pya.DPolygon([pya.DPoint(0.595, -1), pya.DPoint(0.595, -0.7), pya.DPoint(0.895, -0.7), pya.DPoint(0.895, -1), pya.DPoint(0.595, -1)]))
cell_NONOVERLAP.shapes(layout.layer(14, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.195, -0.45), pya.DPoint(-1.195, 0.45), pya.DPoint(1.195, 0.45), pya.DPoint(1.195, -0.45), pya.DPoint(-1.195, -0.45)]))
cell_NONOVERLAP.shapes(layout.layer(14, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.195, -3.13), pya.DPoint(-1.195, -2.43), pya.DPoint(1.195, -2.43), pya.DPoint(1.195, -3.13), pya.DPoint(-1.195, -3.13)]))
cell_NONOVERLAP.shapes(layout.layer(31, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.24, -0.505), pya.DPoint(-1.24, 1.44), pya.DPoint(1.24, 1.44), pya.DPoint(1.24, -0.505), pya.DPoint(-1.24, -0.505)]))
cell_NONOVERLAP.shapes(layout.layer(189, 4)).insert(
    pya.DPolygon([pya.DPoint(-1, -3.1), pya.DPoint(-1, 1.12), pya.DPoint(1, 1.12), pya.DPoint(1, -3.1), pya.DPoint(-1, -3.1)]))
cell_NONOVERLAP.shapes(layout.layer(8, 2)).insert(
    pya.DPolygon([pya.DPoint(-1, -3.03), pya.DPoint(-1, -2.53), pya.DPoint(1, -2.53), pya.DPoint(1, -3.03), pya.DPoint(-1, -3.03)]))
cell_NONOVERLAP.shapes(layout.layer(8, 2)).insert(
    pya.DPolygon([pya.DPoint(-1, 0.55), pya.DPoint(-1, 1.05), pya.DPoint(1, 1.05), pya.DPoint(1, 0.55), pya.DPoint(-1, 0.55)]))
cell_NONOVERLAP.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(-0.89, -0.12), pya.DPoint(-0.89, 0.17), pya.DPoint(-0.6, 0.17), pya.DPoint(-0.6, -0.12), pya.DPoint(-0.89, -0.12)]))
cell_NONOVERLAP.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(-0.42, -0.6), pya.DPoint(-0.42, -0.31), pya.DPoint(-0.13, -0.31), pya.DPoint(-0.13, -0.6), pya.DPoint(-0.42, -0.6)]))
cell_NONOVERLAP.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(0.13, -0.6), pya.DPoint(0.13, -0.31), pya.DPoint(0.42, -0.31), pya.DPoint(0.42, -0.6), pya.DPoint(0.13, -0.6)]))
cell_NONOVERLAP.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(0.6, -0.12), pya.DPoint(0.6, 0.17), pya.DPoint(0.89, 0.17), pya.DPoint(0.89, -0.12), pya.DPoint(0.6, -0.12)]))
cell_NONOVERLAP.shapes(layout.layer(8, 25)).insert(
    pya.DText("VSS",
              pya.DTrans(0, False, pya.DVector(0, -2.78))))
cell_NONOVERLAP.shapes(layout.layer(8, 25)).insert(
    pya.DText("VDD",
              pya.DTrans(0, False, pya.DVector(0, 0.8))))
cell_NONOVERLAP.shapes(layout.layer(10, 25)).insert(
    pya.DText("OUTN",
              pya.DTrans(0, False, pya.DVector(-0.745, 0.025))))
cell_NONOVERLAP.shapes(layout.layer(10, 25)).insert(
    pya.DText("INP",
              pya.DTrans(0, False, pya.DVector(-0.275, -0.455))))
cell_NONOVERLAP.shapes(layout.layer(10, 25)).insert(
    pya.DText("OUTP",
              pya.DTrans(0, False, pya.DVector(0.745, 0.025))))
cell_NONOVERLAP.shapes(layout.layer(10, 25)).insert(
    pya.DText("INN",
              pya.DTrans(0, False, pya.DVector(0.275, -0.455))))

# === DAC_SW ===
cell_DAC_SW.insert(pya.DCellInstArray(
    cell_FEOL_contacts_9_1.cell_index(),
    pya.DCplxTrans(1, 90, False,
                  pya.DVector(-0.26, -0.63))))
cell_DAC_SW.insert(pya.DCellInstArray(
    cell_FEOL_contacts_9_1.cell_index(),
    pya.DCplxTrans(1, 90, False,
                  pya.DVector(0.42, -0.63))))
cell_DAC_SW.insert(pya.DCellInstArray(
    cell_via_stack_2_1_1_1.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(-0.34, -0.5))))
cell_DAC_SW.insert(pya.DCellInstArray(
    cell_via_stack_3_1_1.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(-0.51, 0))))
cell_DAC_SW.insert(pya.DCellInstArray(
    cell_via_stack_2_1_1_1.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(0.34, -0.5))))
cell_DAC_SW.insert(pya.DCellInstArray(
    cell_via_stack_2_1_1_1.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(0, 0))))
_path = pya.DPath([pya.DPoint(0.43, 0), pya.DPoint(0.8, 0), pya.DPoint(0.8, -0.985)], 0.26)
cell_DAC_SW.shapes(layout.layer(8, 0)).insert(_path)
cell_DAC_SW.shapes(layout.layer(8, 0)).insert(
    pya.DPolygon([pya.DPoint(0.43, -0.13), pya.DPoint(0.43, 0.13), pya.DPoint(0.59, 0.13), pya.DPoint(0.59, -0.13), pya.DPoint(0.43, -0.13)]))
cell_DAC_SW.shapes(layout.layer(8, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.59, -0.13), pya.DPoint(-0.59, 0.13), pya.DPoint(-0.43, 0.13), pya.DPoint(-0.43, -0.13), pya.DPoint(-0.59, -0.13)]))
cell_DAC_SW.shapes(layout.layer(8, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.08, -0.13), pya.DPoint(-0.08, 0.13), pya.DPoint(0.08, 0.13), pya.DPoint(0.08, -0.13), pya.DPoint(-0.08, -0.13)]))
cell_DAC_SW.shapes(layout.layer(8, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.49, -0.65), pya.DPoint(-0.49, -0.35), pya.DPoint(-0.19, -0.35), pya.DPoint(-0.19, -0.65), pya.DPoint(-0.49, -0.65)]))
cell_DAC_SW.shapes(layout.layer(8, 0)).insert(
    pya.DPolygon([pya.DPoint(0.19, -0.65), pya.DPoint(0.19, -0.35), pya.DPoint(0.49, -0.35), pya.DPoint(0.49, -0.65), pya.DPoint(0.19, -0.65)]))
cell_DAC_SW.shapes(layout.layer(8, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.66, -0.15), pya.DPoint(-0.66, 0.15), pya.DPoint(-0.36, 0.15), pya.DPoint(-0.36, -0.15), pya.DPoint(-0.66, -0.15)]))
cell_DAC_SW.shapes(layout.layer(8, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.15, -0.15), pya.DPoint(-0.15, 0.15), pya.DPoint(0.15, 0.15), pya.DPoint(0.15, -0.15), pya.DPoint(-0.15, -0.15)]))
cell_DAC_SW.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(0.43, -0.08), pya.DPoint(0.43, 0.08), pya.DPoint(0.59, 0.08), pya.DPoint(0.59, -0.08), pya.DPoint(0.43, -0.08)]))
cell_DAC_SW.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.59, -0.08), pya.DPoint(-0.59, 0.08), pya.DPoint(-0.43, 0.08), pya.DPoint(-0.43, -0.08), pya.DPoint(-0.59, -0.08)]))
cell_DAC_SW.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.08, -0.08), pya.DPoint(-0.08, 0.08), pya.DPoint(0.08, 0.08), pya.DPoint(0.08, -0.08), pya.DPoint(-0.08, -0.08)]))
_path = pya.DPath([pya.DPoint(-0.745, -1.95), pya.DPoint(-0.745, -0.545), pya.DPoint(-0.24, -0.545)], 0.2)
cell_DAC_SW.shapes(layout.layer(10, 0)).insert(_path)
_path = pya.DPath([pya.DPoint(0.74, -1.95), pya.DPoint(0.74, -0.545), pya.DPoint(0.24, -0.545)], 0.2)
cell_DAC_SW.shapes(layout.layer(10, 0)).insert(_path)
cell_DAC_SW.shapes(layout.layer(10, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.845, -0.145), pya.DPoint(-0.845, 0.205), pya.DPoint(-0.365, 0.205), pya.DPoint(-0.365, -0.145), pya.DPoint(-0.845, -0.145)]))
cell_DAC_SW.shapes(layout.layer(1, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.66, -0.15), pya.DPoint(-0.66, 0.15), pya.DPoint(0.66, 0.15), pya.DPoint(0.66, -0.15), pya.DPoint(-0.66, -0.15)]))
cell_DAC_SW.shapes(layout.layer(5, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.32, -0.375), pya.DPoint(-0.32, 0.33), pya.DPoint(-0.19, 0.33), pya.DPoint(-0.19, -0.375), pya.DPoint(-0.32, -0.375)]))
cell_DAC_SW.shapes(layout.layer(5, 0)).insert(
    pya.DPolygon([pya.DPoint(0.19, -0.375), pya.DPoint(0.19, 0.33), pya.DPoint(0.32, 0.33), pya.DPoint(0.32, -0.375), pya.DPoint(0.19, -0.375)]))
cell_DAC_SW.shapes(layout.layer(5, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.49, -0.65), pya.DPoint(-0.49, -0.35), pya.DPoint(-0.19, -0.35), pya.DPoint(-0.19, -0.65), pya.DPoint(-0.49, -0.65)]))
cell_DAC_SW.shapes(layout.layer(5, 0)).insert(
    pya.DPolygon([pya.DPoint(0.19, -0.65), pya.DPoint(0.19, -0.35), pya.DPoint(0.49, -0.35), pya.DPoint(0.49, -0.65), pya.DPoint(0.19, -0.65)]))
cell_DAC_SW.shapes(layout.layer(14, 0)).insert(
    pya.DPolygon([pya.DPoint(-1, -0.45), pya.DPoint(-1, 0.45), pya.DPoint(1, 0.45), pya.DPoint(1, -0.45), pya.DPoint(-1, -0.45)]))
cell_DAC_SW.shapes(layout.layer(31, 0)).insert(
    pya.DPolygon([pya.DPoint(-1, -0.5), pya.DPoint(-1, 0.5), pya.DPoint(1, 0.5), pya.DPoint(1, -0.5), pya.DPoint(-1, -0.5)]))
cell_DAC_SW.shapes(layout.layer(189, 4)).insert(
    pya.DPolygon([pya.DPoint(-1, -0.36), pya.DPoint(-1, 0.36), pya.DPoint(1, 0.36), pya.DPoint(1, -0.36), pya.DPoint(-1, -0.36)]))

# === FEOL$contacts$6$1$1$1 ===
cell_FEOL_contacts_6_1_1_1.shapes(layout.layer(8, 0)).insert(
    pya.DPolygon([pya.DPoint(0, 0), pya.DPoint(0, 0.16), pya.DPoint(1.16, 0.16), pya.DPoint(1.16, 0), pya.DPoint(0, 0)]))
cell_FEOL_contacts_6_1_1_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(0.16, 0), pya.DPoint(0.16, 0.16), pya.DPoint(0.32, 0.16), pya.DPoint(0.32, 0), pya.DPoint(0.16, 0)]))
cell_FEOL_contacts_6_1_1_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(0.5, 0), pya.DPoint(0.5, 0.16), pya.DPoint(0.66, 0.16), pya.DPoint(0.66, 0), pya.DPoint(0.5, 0)]))
cell_FEOL_contacts_6_1_1_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(0.84, 0), pya.DPoint(0.84, 0.16), pya.DPoint(1, 0.16), pya.DPoint(1, 0), pya.DPoint(0.84, 0)]))

# === FEOL$contacts$7$1$1$1 ===
cell_FEOL_contacts_7_1_1_1.shapes(layout.layer(8, 0)).insert(
    pya.DPolygon([pya.DPoint(0, 0), pya.DPoint(0, 0.16), pya.DPoint(1.45, 0.16), pya.DPoint(1.45, 0), pya.DPoint(0, 0)]))
cell_FEOL_contacts_7_1_1_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(0.135, 0), pya.DPoint(0.135, 0.16), pya.DPoint(0.295, 0.16), pya.DPoint(0.295, 0), pya.DPoint(0.135, 0)]))
cell_FEOL_contacts_7_1_1_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(0.475, 0), pya.DPoint(0.475, 0.16), pya.DPoint(0.635, 0.16), pya.DPoint(0.635, 0), pya.DPoint(0.475, 0)]))
cell_FEOL_contacts_7_1_1_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(0.815, 0), pya.DPoint(0.815, 0.16), pya.DPoint(0.975, 0.16), pya.DPoint(0.975, 0), pya.DPoint(0.815, 0)]))
cell_FEOL_contacts_7_1_1_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(1.155, 0), pya.DPoint(1.155, 0.16), pya.DPoint(1.315, 0.16), pya.DPoint(1.315, 0), pya.DPoint(1.155, 0)]))

# === FEOL$contacts$5$1$1$1 ===
cell_FEOL_contacts_5_1_1_1.shapes(layout.layer(8, 0)).insert(
    pya.DPolygon([pya.DPoint(0, 0), pya.DPoint(0, 0.16), pya.DPoint(1.92, 0.16), pya.DPoint(1.92, 0), pya.DPoint(0, 0)]))
cell_FEOL_contacts_5_1_1_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(0.2, 0), pya.DPoint(0.2, 0.16), pya.DPoint(0.36, 0.16), pya.DPoint(0.36, 0), pya.DPoint(0.2, 0)]))
cell_FEOL_contacts_5_1_1_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(0.54, 0), pya.DPoint(0.54, 0.16), pya.DPoint(0.7, 0.16), pya.DPoint(0.7, 0), pya.DPoint(0.54, 0)]))
cell_FEOL_contacts_5_1_1_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(0.88, 0), pya.DPoint(0.88, 0.16), pya.DPoint(1.04, 0.16), pya.DPoint(1.04, 0), pya.DPoint(0.88, 0)]))
cell_FEOL_contacts_5_1_1_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(1.22, 0), pya.DPoint(1.22, 0.16), pya.DPoint(1.38, 0.16), pya.DPoint(1.38, 0), pya.DPoint(1.22, 0)]))
cell_FEOL_contacts_5_1_1_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(1.56, 0), pya.DPoint(1.56, 0.16), pya.DPoint(1.72, 0.16), pya.DPoint(1.72, 0), pya.DPoint(1.56, 0)]))

# === FEOL$contacts$4$1$1$1 ===
cell_FEOL_contacts_4_1_1_1.shapes(layout.layer(8, 0)).insert(
    pya.DPolygon([pya.DPoint(0, 0), pya.DPoint(0, 0.16), pya.DPoint(4.93, 0.16), pya.DPoint(4.93, 0), pya.DPoint(0, 0)]))
cell_FEOL_contacts_4_1_1_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(0.175, 0), pya.DPoint(0.175, 0.16), pya.DPoint(0.335, 0.16), pya.DPoint(0.335, 0), pya.DPoint(0.175, 0)]))
cell_FEOL_contacts_4_1_1_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(0.515, 0), pya.DPoint(0.515, 0.16), pya.DPoint(0.675, 0.16), pya.DPoint(0.675, 0), pya.DPoint(0.515, 0)]))
cell_FEOL_contacts_4_1_1_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(0.855, 0), pya.DPoint(0.855, 0.16), pya.DPoint(1.015, 0.16), pya.DPoint(1.015, 0), pya.DPoint(0.855, 0)]))
cell_FEOL_contacts_4_1_1_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(1.195, 0), pya.DPoint(1.195, 0.16), pya.DPoint(1.355, 0.16), pya.DPoint(1.355, 0), pya.DPoint(1.195, 0)]))
cell_FEOL_contacts_4_1_1_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(1.535, 0), pya.DPoint(1.535, 0.16), pya.DPoint(1.695, 0.16), pya.DPoint(1.695, 0), pya.DPoint(1.535, 0)]))
cell_FEOL_contacts_4_1_1_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(1.875, 0), pya.DPoint(1.875, 0.16), pya.DPoint(2.035, 0.16), pya.DPoint(2.035, 0), pya.DPoint(1.875, 0)]))
cell_FEOL_contacts_4_1_1_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(2.215, 0), pya.DPoint(2.215, 0.16), pya.DPoint(2.375, 0.16), pya.DPoint(2.375, 0), pya.DPoint(2.215, 0)]))
cell_FEOL_contacts_4_1_1_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(2.555, 0), pya.DPoint(2.555, 0.16), pya.DPoint(2.715, 0.16), pya.DPoint(2.715, 0), pya.DPoint(2.555, 0)]))
cell_FEOL_contacts_4_1_1_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(2.895, 0), pya.DPoint(2.895, 0.16), pya.DPoint(3.055, 0.16), pya.DPoint(3.055, 0), pya.DPoint(2.895, 0)]))
cell_FEOL_contacts_4_1_1_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(3.235, 0), pya.DPoint(3.235, 0.16), pya.DPoint(3.395, 0.16), pya.DPoint(3.395, 0), pya.DPoint(3.235, 0)]))
cell_FEOL_contacts_4_1_1_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(3.575, 0), pya.DPoint(3.575, 0.16), pya.DPoint(3.735, 0.16), pya.DPoint(3.735, 0), pya.DPoint(3.575, 0)]))
cell_FEOL_contacts_4_1_1_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(3.915, 0), pya.DPoint(3.915, 0.16), pya.DPoint(4.075, 0.16), pya.DPoint(4.075, 0), pya.DPoint(3.915, 0)]))
cell_FEOL_contacts_4_1_1_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(4.255, 0), pya.DPoint(4.255, 0.16), pya.DPoint(4.415, 0.16), pya.DPoint(4.415, 0), pya.DPoint(4.255, 0)]))
cell_FEOL_contacts_4_1_1_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(4.595, 0), pya.DPoint(4.595, 0.16), pya.DPoint(4.755, 0.16), pya.DPoint(4.755, 0), pya.DPoint(4.595, 0)]))

# === FEOL$contacts$1$2$1$1 ===
cell_FEOL_contacts_1_2_1_1.shapes(layout.layer(8, 0)).insert(
    pya.DPolygon([pya.DPoint(0, 0), pya.DPoint(0, 0.16), pya.DPoint(0.52, 0.16), pya.DPoint(0.52, 0), pya.DPoint(0, 0)]))
cell_FEOL_contacts_1_2_1_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(0.18, 0), pya.DPoint(0.18, 0.16), pya.DPoint(0.34, 0.16), pya.DPoint(0.34, 0), pya.DPoint(0.18, 0)]))

# === via_stack$9$1 ===
cell_via_stack_9_1.shapes(layout.layer(8, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.145, -0.145), pya.DPoint(-0.145, 0.145), pya.DPoint(0.145, 0.145), pya.DPoint(0.145, -0.145), pya.DPoint(-0.145, -0.145)]))
cell_via_stack_9_1.shapes(layout.layer(10, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.145, -0.145), pya.DPoint(-0.145, 0.145), pya.DPoint(0.145, 0.145), pya.DPoint(0.145, -0.145), pya.DPoint(-0.145, -0.145)]))
cell_via_stack_9_1.shapes(layout.layer(19, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.095, -0.095), pya.DPoint(-0.095, 0.095), pya.DPoint(0.095, 0.095), pya.DPoint(0.095, -0.095), pya.DPoint(-0.095, -0.095)]))
cell_via_stack_9_1.shapes(layout.layer(30, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.145, -0.145), pya.DPoint(-0.145, 0.145), pya.DPoint(0.145, 0.145), pya.DPoint(0.145, -0.145), pya.DPoint(-0.145, -0.145)]))
cell_via_stack_9_1.shapes(layout.layer(29, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.095, -0.095), pya.DPoint(-0.095, 0.095), pya.DPoint(0.095, 0.095), pya.DPoint(0.095, -0.095), pya.DPoint(-0.095, -0.095)]))

# === CASCODEDRIVE ===
cell_CASCODEDRIVE.insert(pya.DCellInstArray(
    cell_DAC_SW.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(0, 0))))
cell_CASCODEDRIVE.insert(pya.DCellInstArray(
    cell_NONOVERLAP.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(0, -1.88))))

# === PCSOURCE2U ===
cell_PCSOURCE2U.insert(pya.DCellInstArray(
    cell_FEOL_contacts_4_1_1_1.cell_index(),
    pya.DCplxTrans(1, 90, False,
                  pya.DVector(-0.77, -5.38))))
cell_PCSOURCE2U.insert(pya.DCellInstArray(
    cell_FEOL_contacts_7_1_1_1.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(-0.63, -5.72))))
cell_PCSOURCE2U.insert(pya.DCellInstArray(
    cell_FEOL_contacts_5_1_1_1.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(-0.96, -6.23))))
cell_PCSOURCE2U.insert(pya.DCellInstArray(
    cell_FEOL_contacts_6_1_1_1.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(-0.36, 0.65))))
cell_PCSOURCE2U.insert(pya.DCellInstArray(
    cell_FEOL_contacts_1_2_1_1.cell_index(),
    pya.DCplxTrans(1, 90, False,
                  pya.DVector(-0.59, -0.11))))
cell_PCSOURCE2U.shapes(layout.layer(8, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.375, 0.625), pya.DPoint(-0.375, 0.835), pya.DPoint(0.815, 0.835), pya.DPoint(0.815, 0.625), pya.DPoint(-0.375, 0.625)]))
cell_PCSOURCE2U.shapes(layout.layer(8, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.78, -0.265), pya.DPoint(-0.78, 0.445), pya.DPoint(-0.56, 0.445), pya.DPoint(-0.56, -0.265), pya.DPoint(-0.78, -0.265)]))
cell_PCSOURCE2U.shapes(layout.layer(8, 0)).insert(
    pya.DPolygon([pya.DPoint(-1, -5.38), pya.DPoint(-1, -0.45), pya.DPoint(1, -0.45), pya.DPoint(1, -5.38), pya.DPoint(-1, -5.38)]))
cell_PCSOURCE2U.shapes(layout.layer(8, 0)).insert(
    pya.DPolygon([pya.DPoint(-1, -6.23), pya.DPoint(-1, -5.56), pya.DPoint(1, -5.56), pya.DPoint(1, -6.23), pya.DPoint(-1, -6.23)]))
cell_PCSOURCE2U.shapes(layout.layer(10, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.78, -0.145), pya.DPoint(-0.78, 0.445), pya.DPoint(-0.56, 0.445), pya.DPoint(-0.56, -0.145), pya.DPoint(-0.78, -0.145)]))
cell_PCSOURCE2U.shapes(layout.layer(19, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.765, -0.095), pya.DPoint(-0.765, 0.095), pya.DPoint(-0.575, 0.095), pya.DPoint(-0.575, -0.095), pya.DPoint(-0.765, -0.095)]))
cell_PCSOURCE2U.shapes(layout.layer(1, 0)).insert(
    pya.DPolygon([pya.DPoint(-1, -6.3), pya.DPoint(-1, -6), pya.DPoint(1, -6), pya.DPoint(1, -6.3), pya.DPoint(-1, -6.3)]))
cell_PCSOURCE2U.shapes(layout.layer(1, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.63, -5.79), pya.DPoint(-0.63, -0.22), pya.DPoint(0.82, -0.22), pya.DPoint(0.82, -5.79), pya.DPoint(-0.63, -5.79)]))
cell_PCSOURCE2U.shapes(layout.layer(1, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.38, -0.38), pya.DPoint(-0.38, 0.88), pya.DPoint(0.82, 0.88), pya.DPoint(0.82, -0.38), pya.DPoint(-0.38, -0.38)]))
cell_PCSOURCE2U.shapes(layout.layer(5, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.82, -0.15), pya.DPoint(-0.82, 0.45), pya.DPoint(1, 0.45), pya.DPoint(1, -0.15), pya.DPoint(-0.82, -0.15)]))
cell_PCSOURCE2U.shapes(layout.layer(5, 0)).insert(
    pya.DPolygon([pya.DPoint(-1, -5.45), pya.DPoint(-1, -0.45), pya.DPoint(1, -0.45), pya.DPoint(1, -5.45), pya.DPoint(-1, -5.45)]))
cell_PCSOURCE2U.shapes(layout.layer(14, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.12, -5.97), pya.DPoint(-1.12, 1.06), pya.DPoint(1.12, 1.06), pya.DPoint(1.12, -5.97), pya.DPoint(-1.12, -5.97)]))
cell_PCSOURCE2U.shapes(layout.layer(31, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.24, -6.54), pya.DPoint(-1.24, 1.19), pya.DPoint(1.24, 1.19), pya.DPoint(1.24, -6.54), pya.DPoint(-1.24, -6.54)]))
cell_PCSOURCE2U.shapes(layout.layer(189, 4)).insert(
    pya.DPolygon([pya.DPoint(-1, -6.3), pya.DPoint(-1, 0.88), pya.DPoint(1, 0.88), pya.DPoint(1, -6.3), pya.DPoint(-1, -6.3)]))
cell_PCSOURCE2U.shapes(layout.layer(8, 2)).insert(
    pya.DPolygon([pya.DPoint(-1, -5.38), pya.DPoint(-1, -0.45), pya.DPoint(1, -0.45), pya.DPoint(1, -5.38), pya.DPoint(-1, -5.38)]))
cell_PCSOURCE2U.shapes(layout.layer(8, 2)).insert(
    pya.DPolygon([pya.DPoint(-1, -6.23), pya.DPoint(-1, -5.56), pya.DPoint(1, -5.56), pya.DPoint(1, -6.23), pya.DPoint(-1, -6.23)]))
cell_PCSOURCE2U.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(-0.775, -0.145), pya.DPoint(-0.775, 0.445), pya.DPoint(-0.565, 0.445), pya.DPoint(-0.565, -0.145), pya.DPoint(-0.775, -0.145)]))
cell_PCSOURCE2U.shapes(layout.layer(63, 0)).insert(
    pya.DPolygon([pya.DPoint(0.14, 0.585), pya.DPoint(0.14, 0.875), pya.DPoint(0.3, 0.875), pya.DPoint(0.3, 0.585), pya.DPoint(0.14, 0.585)]))
cell_PCSOURCE2U.shapes(layout.layer(63, 0)).insert(
    pya.DPolygon([pya.DPoint(0.125, 0.635), pya.DPoint(0.125, 0.825), pya.DPoint(0.315, 0.825), pya.DPoint(0.315, 0.635), pya.DPoint(0.125, 0.635)]))
cell_PCSOURCE2U.shapes(layout.layer(8, 25)).insert(
    pya.DPolygon([pya.DPoint(-0.375, 0.625), pya.DPoint(-0.375, 0.835), pya.DPoint(0.815, 0.835), pya.DPoint(0.815, 0.625), pya.DPoint(-0.375, 0.625)]))
cell_PCSOURCE2U.shapes(layout.layer(8, 25)).insert(
    pya.DText("VbiasP",
              pya.DTrans(0, False, pya.DVector(0, -2.915))))
cell_PCSOURCE2U.shapes(layout.layer(8, 25)).insert(
    pya.DText("VDD",
              pya.DTrans(0, False, pya.DVector(0, -5.895))))
cell_PCSOURCE2U.shapes(layout.layer(8, 25)).insert(
    pya.DText("Iout",
              pya.DTrans(0, False, pya.DVector(0.22, 0.73))))
cell_PCSOURCE2U.shapes(layout.layer(10, 25)).insert(
    pya.DText("VcascodeP",
              pya.DTrans(0, False, pya.DVector(-0.67, 0))))

# === via_stack$4$1 ===
cell_via_stack_4_1.shapes(layout.layer(8, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.35, -0.145), pya.DPoint(-0.35, 0.145), pya.DPoint(0.35, 0.145), pya.DPoint(0.35, -0.145), pya.DPoint(-0.35, -0.145)]))
cell_via_stack_4_1.shapes(layout.layer(10, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.35, -0.145), pya.DPoint(-0.35, 0.145), pya.DPoint(0.35, 0.145), pya.DPoint(0.35, -0.145), pya.DPoint(-0.35, -0.145)]))
cell_via_stack_4_1.shapes(layout.layer(19, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.3, -0.095), pya.DPoint(-0.3, 0.095), pya.DPoint(-0.11, 0.095), pya.DPoint(-0.11, -0.095), pya.DPoint(-0.3, -0.095)]))
cell_via_stack_4_1.shapes(layout.layer(19, 0)).insert(
    pya.DPolygon([pya.DPoint(0.11, -0.095), pya.DPoint(0.11, 0.095), pya.DPoint(0.3, 0.095), pya.DPoint(0.3, -0.095), pya.DPoint(0.11, -0.095)]))
cell_via_stack_4_1.shapes(layout.layer(30, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.35, -0.145), pya.DPoint(-0.35, 0.145), pya.DPoint(0.35, 0.145), pya.DPoint(0.35, -0.145), pya.DPoint(-0.35, -0.145)]))
cell_via_stack_4_1.shapes(layout.layer(29, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.3, -0.095), pya.DPoint(-0.3, 0.095), pya.DPoint(-0.11, 0.095), pya.DPoint(-0.11, -0.095), pya.DPoint(-0.3, -0.095)]))
cell_via_stack_4_1.shapes(layout.layer(29, 0)).insert(
    pya.DPolygon([pya.DPoint(0.11, -0.095), pya.DPoint(0.11, 0.095), pya.DPoint(0.3, 0.095), pya.DPoint(0.3, -0.095), pya.DPoint(0.11, -0.095)]))

# === via_stack$7$2 ===
cell_via_stack_7_2.shapes(layout.layer(8, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.145, -0.35), pya.DPoint(-0.145, 0.35), pya.DPoint(0.145, 0.35), pya.DPoint(0.145, -0.35), pya.DPoint(-0.145, -0.35)]))
cell_via_stack_7_2.shapes(layout.layer(10, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.145, -0.35), pya.DPoint(-0.145, 0.35), pya.DPoint(0.145, 0.35), pya.DPoint(0.145, -0.35), pya.DPoint(-0.145, -0.35)]))
cell_via_stack_7_2.shapes(layout.layer(19, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.095, -0.3), pya.DPoint(-0.095, -0.11), pya.DPoint(0.095, -0.11), pya.DPoint(0.095, -0.3), pya.DPoint(-0.095, -0.3)]))
cell_via_stack_7_2.shapes(layout.layer(19, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.095, 0.11), pya.DPoint(-0.095, 0.3), pya.DPoint(0.095, 0.3), pya.DPoint(0.095, 0.11), pya.DPoint(-0.095, 0.11)]))

# === via_stack$6$2$1 ===
cell_via_stack_6_2_1.shapes(layout.layer(10, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.145, -0.145), pya.DPoint(-0.145, 0.145), pya.DPoint(0.145, 0.145), pya.DPoint(0.145, -0.145), pya.DPoint(-0.145, -0.145)]))
cell_via_stack_6_2_1.shapes(layout.layer(30, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.145, -0.145), pya.DPoint(-0.145, 0.145), pya.DPoint(0.145, 0.145), pya.DPoint(0.145, -0.145), pya.DPoint(-0.145, -0.145)]))
cell_via_stack_6_2_1.shapes(layout.layer(29, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.095, -0.095), pya.DPoint(-0.095, 0.095), pya.DPoint(0.095, 0.095), pya.DPoint(0.095, -0.095), pya.DPoint(-0.095, -0.095)]))

# === via_stack$6 ===
cell_via_stack_6.shapes(layout.layer(8, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.145, -3.025), pya.DPoint(-0.145, 3.025), pya.DPoint(0.145, 3.025), pya.DPoint(0.145, -3.025), pya.DPoint(-0.145, -3.025)]))
cell_via_stack_6.shapes(layout.layer(10, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.145, -3.025), pya.DPoint(-0.145, 3.025), pya.DPoint(0.145, 3.025), pya.DPoint(0.145, -3.025), pya.DPoint(-0.145, -3.025)]))
cell_via_stack_6.shapes(layout.layer(19, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.095, -2.975), pya.DPoint(-0.095, -2.785), pya.DPoint(0.095, -2.785), pya.DPoint(0.095, -2.975), pya.DPoint(-0.095, -2.975)]))
cell_via_stack_6.shapes(layout.layer(19, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.095, -2.495), pya.DPoint(-0.095, -2.305), pya.DPoint(0.095, -2.305), pya.DPoint(0.095, -2.495), pya.DPoint(-0.095, -2.495)]))
cell_via_stack_6.shapes(layout.layer(19, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.095, -2.015), pya.DPoint(-0.095, -1.825), pya.DPoint(0.095, -1.825), pya.DPoint(0.095, -2.015), pya.DPoint(-0.095, -2.015)]))
cell_via_stack_6.shapes(layout.layer(19, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.095, -1.535), pya.DPoint(-0.095, -1.345), pya.DPoint(0.095, -1.345), pya.DPoint(0.095, -1.535), pya.DPoint(-0.095, -1.535)]))
cell_via_stack_6.shapes(layout.layer(19, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.095, -1.055), pya.DPoint(-0.095, -0.865), pya.DPoint(0.095, -0.865), pya.DPoint(0.095, -1.055), pya.DPoint(-0.095, -1.055)]))
cell_via_stack_6.shapes(layout.layer(19, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.095, -0.575), pya.DPoint(-0.095, -0.385), pya.DPoint(0.095, -0.385), pya.DPoint(0.095, -0.575), pya.DPoint(-0.095, -0.575)]))
cell_via_stack_6.shapes(layout.layer(19, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.095, -0.095), pya.DPoint(-0.095, 0.095), pya.DPoint(0.095, 0.095), pya.DPoint(0.095, -0.095), pya.DPoint(-0.095, -0.095)]))
cell_via_stack_6.shapes(layout.layer(19, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.095, 0.385), pya.DPoint(-0.095, 0.575), pya.DPoint(0.095, 0.575), pya.DPoint(0.095, 0.385), pya.DPoint(-0.095, 0.385)]))
cell_via_stack_6.shapes(layout.layer(19, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.095, 0.865), pya.DPoint(-0.095, 1.055), pya.DPoint(0.095, 1.055), pya.DPoint(0.095, 0.865), pya.DPoint(-0.095, 0.865)]))
cell_via_stack_6.shapes(layout.layer(19, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.095, 1.345), pya.DPoint(-0.095, 1.535), pya.DPoint(0.095, 1.535), pya.DPoint(0.095, 1.345), pya.DPoint(-0.095, 1.345)]))
cell_via_stack_6.shapes(layout.layer(19, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.095, 1.825), pya.DPoint(-0.095, 2.015), pya.DPoint(0.095, 2.015), pya.DPoint(0.095, 1.825), pya.DPoint(-0.095, 1.825)]))
cell_via_stack_6.shapes(layout.layer(19, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.095, 2.305), pya.DPoint(-0.095, 2.495), pya.DPoint(0.095, 2.495), pya.DPoint(0.095, 2.305), pya.DPoint(-0.095, 2.305)]))
cell_via_stack_6.shapes(layout.layer(19, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.095, 2.785), pya.DPoint(-0.095, 2.975), pya.DPoint(0.095, 2.975), pya.DPoint(0.095, 2.785), pya.DPoint(-0.095, 2.785)]))

# === via_stack$5 ===
cell_via_stack_5.shapes(layout.layer(10, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.145, -0.35), pya.DPoint(-0.145, 0.35), pya.DPoint(0.145, 0.35), pya.DPoint(0.145, -0.35), pya.DPoint(-0.145, -0.35)]))
cell_via_stack_5.shapes(layout.layer(30, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.145, -0.35), pya.DPoint(-0.145, 0.35), pya.DPoint(0.145, 0.35), pya.DPoint(0.145, -0.35), pya.DPoint(-0.145, -0.35)]))
cell_via_stack_5.shapes(layout.layer(29, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.095, -0.3), pya.DPoint(-0.095, -0.11), pya.DPoint(0.095, -0.11), pya.DPoint(0.095, -0.3), pya.DPoint(-0.095, -0.3)]))
cell_via_stack_5.shapes(layout.layer(29, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.095, 0.11), pya.DPoint(-0.095, 0.3), pya.DPoint(0.095, 0.3), pya.DPoint(0.095, 0.11), pya.DPoint(-0.095, 0.11)]))

# === FEOL$contacts$8 ===
cell_FEOL_contacts_8.shapes(layout.layer(8, 0)).insert(
    pya.DPolygon([pya.DPoint(0, 0), pya.DPoint(0, 0.16), pya.DPoint(0.26, 0.16), pya.DPoint(0.26, 0), pya.DPoint(0, 0)]))
cell_FEOL_contacts_8.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(0.05, 0), pya.DPoint(0.05, 0.16), pya.DPoint(0.21, 0.16), pya.DPoint(0.21, 0), pya.DPoint(0.05, 0)]))

# === FEOL$contacts$3$1 ===
cell_FEOL_contacts_3_1.shapes(layout.layer(8, 0)).insert(
    pya.DPolygon([pya.DPoint(0, 0), pya.DPoint(0, 0.16), pya.DPoint(5.85, 0.16), pya.DPoint(5.85, 0), pya.DPoint(0, 0)]))
cell_FEOL_contacts_3_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(0.125, 0), pya.DPoint(0.125, 0.16), pya.DPoint(0.285, 0.16), pya.DPoint(0.285, 0), pya.DPoint(0.125, 0)]))
cell_FEOL_contacts_3_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(0.465, 0), pya.DPoint(0.465, 0.16), pya.DPoint(0.625, 0.16), pya.DPoint(0.625, 0), pya.DPoint(0.465, 0)]))
cell_FEOL_contacts_3_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(0.805, 0), pya.DPoint(0.805, 0.16), pya.DPoint(0.965, 0.16), pya.DPoint(0.965, 0), pya.DPoint(0.805, 0)]))
cell_FEOL_contacts_3_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(1.145, 0), pya.DPoint(1.145, 0.16), pya.DPoint(1.305, 0.16), pya.DPoint(1.305, 0), pya.DPoint(1.145, 0)]))
cell_FEOL_contacts_3_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(1.485, 0), pya.DPoint(1.485, 0.16), pya.DPoint(1.645, 0.16), pya.DPoint(1.645, 0), pya.DPoint(1.485, 0)]))
cell_FEOL_contacts_3_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(1.825, 0), pya.DPoint(1.825, 0.16), pya.DPoint(1.985, 0.16), pya.DPoint(1.985, 0), pya.DPoint(1.825, 0)]))
cell_FEOL_contacts_3_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(2.165, 0), pya.DPoint(2.165, 0.16), pya.DPoint(2.325, 0.16), pya.DPoint(2.325, 0), pya.DPoint(2.165, 0)]))
cell_FEOL_contacts_3_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(2.505, 0), pya.DPoint(2.505, 0.16), pya.DPoint(2.665, 0.16), pya.DPoint(2.665, 0), pya.DPoint(2.505, 0)]))
cell_FEOL_contacts_3_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(2.845, 0), pya.DPoint(2.845, 0.16), pya.DPoint(3.005, 0.16), pya.DPoint(3.005, 0), pya.DPoint(2.845, 0)]))
cell_FEOL_contacts_3_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(3.185, 0), pya.DPoint(3.185, 0.16), pya.DPoint(3.345, 0.16), pya.DPoint(3.345, 0), pya.DPoint(3.185, 0)]))
cell_FEOL_contacts_3_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(3.525, 0), pya.DPoint(3.525, 0.16), pya.DPoint(3.685, 0.16), pya.DPoint(3.685, 0), pya.DPoint(3.525, 0)]))
cell_FEOL_contacts_3_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(3.865, 0), pya.DPoint(3.865, 0.16), pya.DPoint(4.025, 0.16), pya.DPoint(4.025, 0), pya.DPoint(3.865, 0)]))
cell_FEOL_contacts_3_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(4.205, 0), pya.DPoint(4.205, 0.16), pya.DPoint(4.365, 0.16), pya.DPoint(4.365, 0), pya.DPoint(4.205, 0)]))
cell_FEOL_contacts_3_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(4.545, 0), pya.DPoint(4.545, 0.16), pya.DPoint(4.705, 0.16), pya.DPoint(4.705, 0), pya.DPoint(4.545, 0)]))
cell_FEOL_contacts_3_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(4.885, 0), pya.DPoint(4.885, 0.16), pya.DPoint(5.045, 0.16), pya.DPoint(5.045, 0), pya.DPoint(4.885, 0)]))
cell_FEOL_contacts_3_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(5.225, 0), pya.DPoint(5.225, 0.16), pya.DPoint(5.385, 0.16), pya.DPoint(5.385, 0), pya.DPoint(5.225, 0)]))
cell_FEOL_contacts_3_1.shapes(layout.layer(6, 0)).insert(
    pya.DPolygon([pya.DPoint(5.565, 0), pya.DPoint(5.565, 0.16), pya.DPoint(5.725, 0.16), pya.DPoint(5.725, 0), pya.DPoint(5.565, 0)]))

# === unitsource2u ===
cell_unitsource2u.insert(pya.DCellInstArray(
    cell_PCSOURCE2U.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(0, 6.78))))
cell_unitsource2u.insert(pya.DCellInstArray(
    cell_CASCODEDRIVE.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(0, 0))))
cell_unitsource2u.insert(pya.DCellInstArray(
    cell_via_stack_7_2.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(0.65, 0.87))))
cell_unitsource2u.insert(pya.DCellInstArray(
    cell_via_stack_4_1.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(0, -1.08))))
cell_unitsource2u.insert(pya.DCellInstArray(
    cell_via_stack_6_2_1.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(0.65, 0.985))))
cell_unitsource2u.insert(pya.DCellInstArray(
    cell_via_stack_9_1.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(-0.775, -4.66))))
cell_unitsource2u.shapes(layout.layer(8, 0)).insert(
    pya.DPolygon([pya.DPoint(0.43, -0.13), pya.DPoint(0.43, 0.71), pya.DPoint(0.93, 0.71), pya.DPoint(0.93, -0.13), pya.DPoint(0.43, -0.13)]))
_path = pya.DPath([pya.DPoint(-0.275, -4.91), pya.DPoint(-0.275, -2.19)], 0.2)
cell_unitsource2u.shapes(layout.layer(10, 0)).insert(_path)
_path = pya.DPath([pya.DPoint(0.275, -4.91), pya.DPoint(0.275, -2.19)], 0.2)
cell_unitsource2u.shapes(layout.layer(10, 0)).insert(_path)
_path = pya.DPath([pya.DPoint(-0.67, 6.685), pya.DPoint(-0.67, 0.885), pya.DPoint(0, 0.885), pya.DPoint(0, 0.095)], 0.2)
cell_unitsource2u.shapes(layout.layer(10, 0)).insert(_path)
cell_unitsource2u.shapes(layout.layer(10, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.92, -4.91), pya.DPoint(-0.92, -4.41), pya.DPoint(-0.63, -4.41), pya.DPoint(-0.63, -4.91), pya.DPoint(-0.92, -4.91)]))
_path = pya.DPath([pya.DPoint(-1, 0), pya.DPoint(1, 0)], 0.7)
cell_unitsource2u.shapes(layout.layer(30, 0)).insert(_path)
cell_unitsource2u.shapes(layout.layer(30, 0)).insert(
    pya.DPolygon([pya.DPoint(-1, 0.75), pya.DPoint(-1, 2.48), pya.DPoint(1, 2.48), pya.DPoint(1, 0.75), pya.DPoint(-1, 0.75)]))
cell_unitsource2u.shapes(layout.layer(30, 0)).insert(
    pya.DPolygon([pya.DPoint(-1, -2.48), pya.DPoint(-1, -0.75), pya.DPoint(1, -0.75), pya.DPoint(1, -2.48), pya.DPoint(-1, -2.48)]))
cell_unitsource2u.shapes(layout.layer(30, 0)).insert(
    pya.DPolygon([pya.DPoint(-1, -4.91), pya.DPoint(-1, -3.18), pya.DPoint(1, -3.18), pya.DPoint(1, -4.91), pya.DPoint(-1, -4.91)]))
cell_unitsource2u.shapes(layout.layer(30, 0)).insert(
    pya.DText("VDD",
              pya.DTrans(0, False, pya.DVector(0, 1.615))))
cell_unitsource2u.shapes(layout.layer(31, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.24, -2.385), pya.DPoint(-1.24, 7.97), pya.DPoint(1.24, 7.97), pya.DPoint(1.24, -2.385), pya.DPoint(-1.24, -2.385)]))
cell_unitsource2u.shapes(layout.layer(8, 2)).insert(
    pya.DPolygon([pya.DPoint(-1, 0.55), pya.DPoint(-1, 1.22), pya.DPoint(1, 1.22), pya.DPoint(1, 0.55), pya.DPoint(-1, 0.55)]))
cell_unitsource2u.shapes(layout.layer(8, 2)).insert(
    pya.DPolygon([pya.DPoint(-1, 1.4), pya.DPoint(-1, 6.33), pya.DPoint(1, 6.33), pya.DPoint(1, 1.4), pya.DPoint(-1, 1.4)]))
cell_unitsource2u.shapes(layout.layer(8, 2)).insert(
    pya.DPolygon([pya.DPoint(-0.375, 7.405), pya.DPoint(-0.375, 7.615), pya.DPoint(0.815, 7.615), pya.DPoint(0.815, 7.405), pya.DPoint(-0.375, 7.405)]))
cell_unitsource2u.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(0.175, -4.91), pya.DPoint(0.175, -4.62), pya.DPoint(0.375, -4.62), pya.DPoint(0.375, -4.91), pya.DPoint(0.175, -4.91)]))
cell_unitsource2u.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(-0.375, -4.91), pya.DPoint(-0.375, -4.62), pya.DPoint(-0.175, -4.62), pya.DPoint(-0.175, -4.91), pya.DPoint(-0.375, -4.91)]))
cell_unitsource2u.shapes(layout.layer(30, 2)).insert(
    pya.DPolygon([pya.DPoint(-1, -0.35), pya.DPoint(-1, 0.35), pya.DPoint(1, 0.35), pya.DPoint(1, -0.35), pya.DPoint(-1, -0.35)]))
cell_unitsource2u.shapes(layout.layer(30, 2)).insert(
    pya.DPolygon([pya.DPoint(-1, 0.75), pya.DPoint(-1, 2.48), pya.DPoint(1, 2.48), pya.DPoint(1, 0.75), pya.DPoint(-1, 0.75)]))
cell_unitsource2u.shapes(layout.layer(30, 2)).insert(
    pya.DPolygon([pya.DPoint(-1, -2.48), pya.DPoint(-1, -0.75), pya.DPoint(1, -0.75), pya.DPoint(1, -2.48), pya.DPoint(-1, -2.48)]))
cell_unitsource2u.shapes(layout.layer(30, 2)).insert(
    pya.DPolygon([pya.DPoint(-1, -4.91), pya.DPoint(-1, -3.18), pya.DPoint(1, -3.18), pya.DPoint(1, -4.91), pya.DPoint(-1, -4.91)]))
cell_unitsource2u.shapes(layout.layer(8, 25)).insert(
    pya.DText("VbiasP",
              pya.DTrans(0, False, pya.DVector(0, 3.865))))
cell_unitsource2u.shapes(layout.layer(8, 25)).insert(
    pya.DText("Iout",
              pya.DTrans(0, False, pya.DVector(0.22, 7.51))))
cell_unitsource2u.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON",
              pya.DTrans(0, False, pya.DVector(-0.275, -4.765))))
cell_unitsource2u.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB",
              pya.DTrans(0, False, pya.DVector(0.275, -4.765))))
cell_unitsource2u.shapes(layout.layer(30, 25)).insert(
    pya.DText("VSS",
              pya.DTrans(0, False, pya.DVector(0, -4.045))))
cell_unitsource2u.shapes(layout.layer(30, 25)).insert(
    pya.DText("VDD",
              pya.DTrans(0, False, pya.DVector(0, -1.615))))
cell_unitsource2u.shapes(layout.layer(30, 25)).insert(
    pya.DText("VcascP",
              pya.DTrans(0, False, pya.DVector(0, 0))))

# === CASCODEBIAS ===
cell_CASCODEBIAS.insert(pya.DCellInstArray(
    cell_FEOL_contacts_3_1.cell_index(),
    pya.DCplxTrans(1, 90, False,
                  pya.DVector(-1.67, 1.76))))
cell_CASCODEBIAS.insert(pya.DCellInstArray(
    cell_FEOL_contacts_3_1.cell_index(),
    pya.DCplxTrans(1, 90, False,
                  pya.DVector(-1.14, 1.76))))
cell_CASCODEBIAS.insert(pya.DCellInstArray(
    cell_FEOL_contacts_8.cell_index(),
    pya.DCplxTrans(1, 90, False,
                  pya.DVector(-1.67, 1.4))))
cell_CASCODEBIAS.insert(pya.DCellInstArray(
    cell_via_stack_5.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(-1.75, 0))))
cell_CASCODEBIAS.insert(pya.DCellInstArray(
    cell_via_stack_6.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(-1.75, 4.425))))
_path = pya.DPath([pya.DPoint(-1.75, 7.61), pya.DPoint(-1.75, 1.4)], 0.29)
cell_CASCODEBIAS.shapes(layout.layer(8, 0)).insert(_path)
_path = pya.DPath([pya.DPoint(-1.75, 1.61), pya.DPoint(-1.75, 1.96)], 0.16)
cell_CASCODEBIAS.shapes(layout.layer(8, 0)).insert(_path)
cell_CASCODEBIAS.shapes(layout.layer(8, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.3, 1.76), pya.DPoint(-1.3, 6.33), pya.DPoint(-0.77, 6.33), pya.DPoint(-0.77, 1.76), pya.DPoint(-1.3, 1.76)]))
_path = pya.DPath([pya.DPoint(-1.75, 1.93), pya.DPoint(-1.75, 0)], 0.29)
cell_CASCODEBIAS.shapes(layout.layer(10, 0)).insert(_path)
cell_CASCODEBIAS.shapes(layout.layer(1, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.9, 1.76), pya.DPoint(-1.9, 7.61), pya.DPoint(-1.07, 7.61), pya.DPoint(-1.07, 1.76), pya.DPoint(-1.9, 1.76)]))
cell_CASCODEBIAS.shapes(layout.layer(5, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.56, 1.68), pya.DPoint(-1.56, 7.79), pya.DPoint(-1.41, 7.79), pya.DPoint(-1.41, 1.68), pya.DPoint(-1.56, 1.68)]))
cell_CASCODEBIAS.shapes(layout.layer(5, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.9, 1.38), pya.DPoint(-1.9, 1.68), pya.DPoint(-1.41, 1.68), pya.DPoint(-1.41, 1.38), pya.DPoint(-1.9, 1.38)]))
cell_CASCODEBIAS.shapes(layout.layer(14, 0)).insert(
    pya.DPolygon([pya.DPoint(-2.08, 1.46), pya.DPoint(-2.08, 7.91), pya.DPoint(-0.89, 7.91), pya.DPoint(-0.89, 1.46), pya.DPoint(-2.08, 1.46)]))
cell_CASCODEBIAS.shapes(layout.layer(31, 0)).insert(
    pya.DPolygon([pya.DPoint(-2.21, 1.45), pya.DPoint(-2.21, 7.92), pya.DPoint(-0.76, 7.92), pya.DPoint(-0.76, 1.45), pya.DPoint(-2.21, 1.45)]))

# === dac2u16out2in ===
cell_dac2u16out2in.insert(pya.DCellInstArray(
    cell_CASCODEBIAS.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(0, 0))))
cell_dac2u16out2in.insert(pya.DCellInstArray(
    cell_unitsource2u.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(0, 0)),
    pya.DVector(2, 0),
    pya.DVector(0, 0),
    18, 1))
cell_dac2u16out2in.insert(pya.DCellInstArray(
    cell_CASCODEBIAS.cell_index(),
    pya.DCplxTrans(1, 180, True,
                  pya.DVector(34, 0))))
_path = pya.DPath([pya.DPoint(-1.9, 8.185), pya.DPoint(35.9, 8.185)], 0.7)
cell_dac2u16out2in.shapes(layout.layer(8, 0)).insert(_path)
_path = pya.DPath([pya.DPoint(-1.9, -4.66), pya.DPoint(35.9, -4.66)], 0.5)
cell_dac2u16out2in.shapes(layout.layer(8, 0)).insert(_path)
cell_dac2u16out2in.shapes(layout.layer(8, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.375, 6.2), pya.DPoint(-0.375, 7.615), pya.DPoint(0.815, 7.615), pya.DPoint(0.815, 6.2), pya.DPoint(-0.375, 6.2)]))
cell_dac2u16out2in.shapes(layout.layer(8, 0)).insert(
    pya.DPolygon([pya.DPoint(33.625, 6.2), pya.DPoint(33.625, 7.615), pya.DPoint(34.815, 7.615), pya.DPoint(34.815, 6.2), pya.DPoint(33.625, 6.2)]))
cell_dac2u16out2in.shapes(layout.layer(8, 0)).insert(
    pya.DPolygon([pya.DPoint(1.625, 7.405), pya.DPoint(1.625, 8.535), pya.DPoint(32.815, 8.535), pya.DPoint(32.815, 7.405), pya.DPoint(1.625, 7.405)]))
_path = pya.DPath([pya.DPoint(-1.9, 1.615), pya.DPoint(35.9, 1.615)], 1.73)
cell_dac2u16out2in.shapes(layout.layer(30, 0)).insert(_path)
_path = pya.DPath([pya.DPoint(-1.9, 0), pya.DPoint(35.9, 0)], 0.7)
cell_dac2u16out2in.shapes(layout.layer(30, 0)).insert(_path)
_path = pya.DPath([pya.DPoint(-1.9, -1.615), pya.DPoint(35.9, -1.615)], 1.73)
cell_dac2u16out2in.shapes(layout.layer(30, 0)).insert(_path)
_path = pya.DPath([pya.DPoint(-1.9, -4.045), pya.DPoint(35.9, -4.045)], 1.73)
cell_dac2u16out2in.shapes(layout.layer(30, 0)).insert(_path)
cell_dac2u16out2in.shapes(layout.layer(8, 2)).insert(
    pya.DPolygon([pya.DPoint(-1, 1.4), pya.DPoint(-1, 6.33), pya.DPoint(35, 6.33), pya.DPoint(35, 1.4), pya.DPoint(-1, 1.4)]))
cell_dac2u16out2in.shapes(layout.layer(8, 2)).insert(
    pya.DPolygon([pya.DPoint(-1.9, 7.835), pya.DPoint(-1.9, 8.535), pya.DPoint(35.9, 8.535), pya.DPoint(35.9, 7.835), pya.DPoint(-1.9, 7.835)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(32.175, -4.91), pya.DPoint(32.175, -4.62), pya.DPoint(32.375, -4.62), pya.DPoint(32.375, -4.91), pya.DPoint(32.175, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(32.175, -4.91), pya.DPoint(32.175, -4.62), pya.DPoint(32.375, -4.62), pya.DPoint(32.375, -4.91), pya.DPoint(32.175, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(34.175, -4.91), pya.DPoint(34.175, -4.62), pya.DPoint(34.375, -4.62), pya.DPoint(34.375, -4.91), pya.DPoint(34.175, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(33.625, -4.91), pya.DPoint(33.625, -4.62), pya.DPoint(33.825, -4.62), pya.DPoint(33.825, -4.91), pya.DPoint(33.625, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(33.625, -4.91), pya.DPoint(33.625, -4.62), pya.DPoint(33.825, -4.62), pya.DPoint(33.825, -4.91), pya.DPoint(33.625, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(34.175, -4.91), pya.DPoint(34.175, -4.62), pya.DPoint(34.375, -4.62), pya.DPoint(34.375, -4.91), pya.DPoint(34.175, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(3.625, -4.91), pya.DPoint(3.625, -4.62), pya.DPoint(3.825, -4.62), pya.DPoint(3.825, -4.91), pya.DPoint(3.625, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(4.175, -4.91), pya.DPoint(4.175, -4.62), pya.DPoint(4.375, -4.62), pya.DPoint(4.375, -4.91), pya.DPoint(4.175, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(5.625, -4.91), pya.DPoint(5.625, -4.62), pya.DPoint(5.825, -4.62), pya.DPoint(5.825, -4.91), pya.DPoint(5.625, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(6.175, -4.91), pya.DPoint(6.175, -4.62), pya.DPoint(6.375, -4.62), pya.DPoint(6.375, -4.91), pya.DPoint(6.175, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(7.625, -4.91), pya.DPoint(7.625, -4.62), pya.DPoint(7.825, -4.62), pya.DPoint(7.825, -4.91), pya.DPoint(7.625, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(8.175, -4.91), pya.DPoint(8.175, -4.62), pya.DPoint(8.375, -4.62), pya.DPoint(8.375, -4.91), pya.DPoint(8.175, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(9.625, -4.91), pya.DPoint(9.625, -4.62), pya.DPoint(9.825, -4.62), pya.DPoint(9.825, -4.91), pya.DPoint(9.625, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(10.175, -4.91), pya.DPoint(10.175, -4.62), pya.DPoint(10.375, -4.62), pya.DPoint(10.375, -4.91), pya.DPoint(10.175, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(11.625, -4.91), pya.DPoint(11.625, -4.62), pya.DPoint(11.825, -4.62), pya.DPoint(11.825, -4.91), pya.DPoint(11.625, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(12.175, -4.91), pya.DPoint(12.175, -4.62), pya.DPoint(12.375, -4.62), pya.DPoint(12.375, -4.91), pya.DPoint(12.175, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(13.625, -4.91), pya.DPoint(13.625, -4.62), pya.DPoint(13.825, -4.62), pya.DPoint(13.825, -4.91), pya.DPoint(13.625, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(14.175, -4.91), pya.DPoint(14.175, -4.62), pya.DPoint(14.375, -4.62), pya.DPoint(14.375, -4.91), pya.DPoint(14.175, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(15.625, -4.91), pya.DPoint(15.625, -4.62), pya.DPoint(15.825, -4.62), pya.DPoint(15.825, -4.91), pya.DPoint(15.625, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(16.175, -4.91), pya.DPoint(16.175, -4.62), pya.DPoint(16.375, -4.62), pya.DPoint(16.375, -4.91), pya.DPoint(16.175, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(17.625, -4.91), pya.DPoint(17.625, -4.62), pya.DPoint(17.825, -4.62), pya.DPoint(17.825, -4.91), pya.DPoint(17.625, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(18.175, -4.91), pya.DPoint(18.175, -4.62), pya.DPoint(18.375, -4.62), pya.DPoint(18.375, -4.91), pya.DPoint(18.175, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(19.625, -4.91), pya.DPoint(19.625, -4.62), pya.DPoint(19.825, -4.62), pya.DPoint(19.825, -4.91), pya.DPoint(19.625, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(20.175, -4.91), pya.DPoint(20.175, -4.62), pya.DPoint(20.375, -4.62), pya.DPoint(20.375, -4.91), pya.DPoint(20.175, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(21.625, -4.91), pya.DPoint(21.625, -4.62), pya.DPoint(21.825, -4.62), pya.DPoint(21.825, -4.91), pya.DPoint(21.625, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(22.175, -4.91), pya.DPoint(22.175, -4.62), pya.DPoint(22.375, -4.62), pya.DPoint(22.375, -4.91), pya.DPoint(22.175, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(23.625, -4.91), pya.DPoint(23.625, -4.62), pya.DPoint(23.825, -4.62), pya.DPoint(23.825, -4.91), pya.DPoint(23.625, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(24.175, -4.91), pya.DPoint(24.175, -4.62), pya.DPoint(24.375, -4.62), pya.DPoint(24.375, -4.91), pya.DPoint(24.175, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(25.625, -4.91), pya.DPoint(25.625, -4.62), pya.DPoint(25.825, -4.62), pya.DPoint(25.825, -4.91), pya.DPoint(25.625, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(26.175, -4.91), pya.DPoint(26.175, -4.62), pya.DPoint(26.375, -4.62), pya.DPoint(26.375, -4.91), pya.DPoint(26.175, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(27.625, -4.91), pya.DPoint(27.625, -4.62), pya.DPoint(27.825, -4.62), pya.DPoint(27.825, -4.91), pya.DPoint(27.625, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(28.175, -4.91), pya.DPoint(28.175, -4.62), pya.DPoint(28.375, -4.62), pya.DPoint(28.375, -4.91), pya.DPoint(28.175, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(29.625, -4.91), pya.DPoint(29.625, -4.62), pya.DPoint(29.825, -4.62), pya.DPoint(29.825, -4.91), pya.DPoint(29.625, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(30.175, -4.91), pya.DPoint(30.175, -4.62), pya.DPoint(30.375, -4.62), pya.DPoint(30.375, -4.91), pya.DPoint(30.175, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(31.625, -4.91), pya.DPoint(31.625, -4.62), pya.DPoint(31.825, -4.62), pya.DPoint(31.825, -4.91), pya.DPoint(31.625, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(-0.375, -4.91), pya.DPoint(-0.375, -4.62), pya.DPoint(-0.175, -4.62), pya.DPoint(-0.175, -4.91), pya.DPoint(-0.375, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(0.175, -4.91), pya.DPoint(0.175, -4.62), pya.DPoint(0.375, -4.62), pya.DPoint(0.375, -4.91), pya.DPoint(0.175, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(1.625, -4.91), pya.DPoint(1.625, -4.62), pya.DPoint(1.825, -4.62), pya.DPoint(1.825, -4.91), pya.DPoint(1.625, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(2.175, -4.91), pya.DPoint(2.175, -4.62), pya.DPoint(2.375, -4.62), pya.DPoint(2.375, -4.91), pya.DPoint(2.175, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(3.625, -4.91), pya.DPoint(3.625, -4.62), pya.DPoint(3.825, -4.62), pya.DPoint(3.825, -4.91), pya.DPoint(3.625, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(4.175, -4.91), pya.DPoint(4.175, -4.62), pya.DPoint(4.375, -4.62), pya.DPoint(4.375, -4.91), pya.DPoint(4.175, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(5.625, -4.91), pya.DPoint(5.625, -4.62), pya.DPoint(5.825, -4.62), pya.DPoint(5.825, -4.91), pya.DPoint(5.625, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(6.175, -4.91), pya.DPoint(6.175, -4.62), pya.DPoint(6.375, -4.62), pya.DPoint(6.375, -4.91), pya.DPoint(6.175, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(7.625, -4.91), pya.DPoint(7.625, -4.62), pya.DPoint(7.825, -4.62), pya.DPoint(7.825, -4.91), pya.DPoint(7.625, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(8.175, -4.91), pya.DPoint(8.175, -4.62), pya.DPoint(8.375, -4.62), pya.DPoint(8.375, -4.91), pya.DPoint(8.175, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(9.625, -4.91), pya.DPoint(9.625, -4.62), pya.DPoint(9.825, -4.62), pya.DPoint(9.825, -4.91), pya.DPoint(9.625, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(10.175, -4.91), pya.DPoint(10.175, -4.62), pya.DPoint(10.375, -4.62), pya.DPoint(10.375, -4.91), pya.DPoint(10.175, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(11.625, -4.91), pya.DPoint(11.625, -4.62), pya.DPoint(11.825, -4.62), pya.DPoint(11.825, -4.91), pya.DPoint(11.625, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(12.175, -4.91), pya.DPoint(12.175, -4.62), pya.DPoint(12.375, -4.62), pya.DPoint(12.375, -4.91), pya.DPoint(12.175, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(13.625, -4.91), pya.DPoint(13.625, -4.62), pya.DPoint(13.825, -4.62), pya.DPoint(13.825, -4.91), pya.DPoint(13.625, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(14.175, -4.91), pya.DPoint(14.175, -4.62), pya.DPoint(14.375, -4.62), pya.DPoint(14.375, -4.91), pya.DPoint(14.175, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(15.625, -4.91), pya.DPoint(15.625, -4.62), pya.DPoint(15.825, -4.62), pya.DPoint(15.825, -4.91), pya.DPoint(15.625, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(16.175, -4.91), pya.DPoint(16.175, -4.62), pya.DPoint(16.375, -4.62), pya.DPoint(16.375, -4.91), pya.DPoint(16.175, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(17.625, -4.91), pya.DPoint(17.625, -4.62), pya.DPoint(17.825, -4.62), pya.DPoint(17.825, -4.91), pya.DPoint(17.625, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(18.175, -4.91), pya.DPoint(18.175, -4.62), pya.DPoint(18.375, -4.62), pya.DPoint(18.375, -4.91), pya.DPoint(18.175, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(19.625, -4.91), pya.DPoint(19.625, -4.62), pya.DPoint(19.825, -4.62), pya.DPoint(19.825, -4.91), pya.DPoint(19.625, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(20.175, -4.91), pya.DPoint(20.175, -4.62), pya.DPoint(20.375, -4.62), pya.DPoint(20.375, -4.91), pya.DPoint(20.175, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(21.625, -4.91), pya.DPoint(21.625, -4.62), pya.DPoint(21.825, -4.62), pya.DPoint(21.825, -4.91), pya.DPoint(21.625, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(22.175, -4.91), pya.DPoint(22.175, -4.62), pya.DPoint(22.375, -4.62), pya.DPoint(22.375, -4.91), pya.DPoint(22.175, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(23.625, -4.91), pya.DPoint(23.625, -4.62), pya.DPoint(23.825, -4.62), pya.DPoint(23.825, -4.91), pya.DPoint(23.625, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(24.175, -4.91), pya.DPoint(24.175, -4.62), pya.DPoint(24.375, -4.62), pya.DPoint(24.375, -4.91), pya.DPoint(24.175, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(25.625, -4.91), pya.DPoint(25.625, -4.62), pya.DPoint(25.825, -4.62), pya.DPoint(25.825, -4.91), pya.DPoint(25.625, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(26.175, -4.91), pya.DPoint(26.175, -4.62), pya.DPoint(26.375, -4.62), pya.DPoint(26.375, -4.91), pya.DPoint(26.175, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(27.625, -4.91), pya.DPoint(27.625, -4.62), pya.DPoint(27.825, -4.62), pya.DPoint(27.825, -4.91), pya.DPoint(27.625, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(28.175, -4.91), pya.DPoint(28.175, -4.62), pya.DPoint(28.375, -4.62), pya.DPoint(28.375, -4.91), pya.DPoint(28.175, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(29.625, -4.91), pya.DPoint(29.625, -4.62), pya.DPoint(29.825, -4.62), pya.DPoint(29.825, -4.91), pya.DPoint(29.625, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(30.175, -4.91), pya.DPoint(30.175, -4.62), pya.DPoint(30.375, -4.62), pya.DPoint(30.375, -4.91), pya.DPoint(30.175, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(31.625, -4.91), pya.DPoint(31.625, -4.62), pya.DPoint(31.825, -4.62), pya.DPoint(31.825, -4.91), pya.DPoint(31.625, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(-0.375, -4.91), pya.DPoint(-0.375, -4.62), pya.DPoint(-0.175, -4.62), pya.DPoint(-0.175, -4.91), pya.DPoint(-0.375, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(0.175, -4.91), pya.DPoint(0.175, -4.62), pya.DPoint(0.375, -4.62), pya.DPoint(0.375, -4.91), pya.DPoint(0.175, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(1.625, -4.91), pya.DPoint(1.625, -4.62), pya.DPoint(1.825, -4.62), pya.DPoint(1.825, -4.91), pya.DPoint(1.625, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(2.175, -4.91), pya.DPoint(2.175, -4.62), pya.DPoint(2.375, -4.62), pya.DPoint(2.375, -4.91), pya.DPoint(2.175, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(30, 2)).insert(
    pya.DPolygon([pya.DPoint(-1.9, -0.35), pya.DPoint(-1.9, 0.35), pya.DPoint(35.9, 0.35), pya.DPoint(35.9, -0.35), pya.DPoint(-1.9, -0.35)]))
cell_dac2u16out2in.shapes(layout.layer(30, 2)).insert(
    pya.DPolygon([pya.DPoint(-1.9, 0.75), pya.DPoint(-1.9, 2.48), pya.DPoint(35.9, 2.48), pya.DPoint(35.9, 0.75), pya.DPoint(-1.9, 0.75)]))
cell_dac2u16out2in.shapes(layout.layer(30, 2)).insert(
    pya.DPolygon([pya.DPoint(-1.9, -2.48), pya.DPoint(-1.9, -0.75), pya.DPoint(35.9, -0.75), pya.DPoint(35.9, -2.48), pya.DPoint(-1.9, -2.48)]))
cell_dac2u16out2in.shapes(layout.layer(30, 2)).insert(
    pya.DPolygon([pya.DPoint(-1.9, -4.91), pya.DPoint(-1.9, -3.18), pya.DPoint(35.9, -3.18), pya.DPoint(35.9, -4.91), pya.DPoint(-1.9, -4.91)]))
cell_dac2u16out2in.shapes(layout.layer(8, 25)).insert(
    pya.DText("VbiasP",
              pya.DTrans(0, False, pya.DVector(17, 3.865))))
cell_dac2u16out2in.shapes(layout.layer(8, 25)).insert(
    pya.DText("Iout",
              pya.DTrans(0, False, pya.DVector(17, 8.185))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("EN[1]",
              pya.DTrans(0, False, pya.DVector(33.725, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ENB[1]",
              pya.DTrans(0, False, pya.DVector(34.275, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[0]",
              pya.DTrans(0, False, pya.DVector(1.725, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[0]",
              pya.DTrans(0, False, pya.DVector(2.275, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[1]",
              pya.DTrans(0, False, pya.DVector(3.725, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[1]",
              pya.DTrans(0, False, pya.DVector(4.275, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[2]",
              pya.DTrans(0, False, pya.DVector(5.725, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[2]",
              pya.DTrans(0, False, pya.DVector(6.275, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[3]",
              pya.DTrans(0, False, pya.DVector(7.725, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[3]",
              pya.DTrans(0, False, pya.DVector(8.275, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[4]",
              pya.DTrans(0, False, pya.DVector(9.725, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[4]",
              pya.DTrans(0, False, pya.DVector(10.275, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("EN[0]",
              pya.DTrans(0, False, pya.DVector(-0.275, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ENB[0]",
              pya.DTrans(0, False, pya.DVector(0.275, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON",
              pya.DTrans(0, False, pya.DVector(-0.275, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB",
              pya.DTrans(0, False, pya.DVector(0.275, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON",
              pya.DTrans(0, False, pya.DVector(1.725, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB",
              pya.DTrans(0, False, pya.DVector(2.275, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON",
              pya.DTrans(0, False, pya.DVector(3.725, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB",
              pya.DTrans(0, False, pya.DVector(4.275, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON",
              pya.DTrans(0, False, pya.DVector(5.725, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB",
              pya.DTrans(0, False, pya.DVector(6.275, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON",
              pya.DTrans(0, False, pya.DVector(7.725, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB",
              pya.DTrans(0, False, pya.DVector(8.275, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON",
              pya.DTrans(0, False, pya.DVector(9.725, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB",
              pya.DTrans(0, False, pya.DVector(10.275, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[5]",
              pya.DTrans(0, False, pya.DVector(11.725, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[5]",
              pya.DTrans(0, False, pya.DVector(12.275, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[6]",
              pya.DTrans(0, False, pya.DVector(13.725, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[6]",
              pya.DTrans(0, False, pya.DVector(14.275, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[7]",
              pya.DTrans(0, False, pya.DVector(15.725, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[7]",
              pya.DTrans(0, False, pya.DVector(16.275, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[8]",
              pya.DTrans(0, False, pya.DVector(17.725, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[8]",
              pya.DTrans(0, False, pya.DVector(18.275, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[9]",
              pya.DTrans(0, False, pya.DVector(19.725, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[9]",
              pya.DTrans(0, False, pya.DVector(20.275, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[10]",
              pya.DTrans(0, False, pya.DVector(21.725, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[10]",
              pya.DTrans(0, False, pya.DVector(22.275, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON",
              pya.DTrans(0, False, pya.DVector(11.725, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB",
              pya.DTrans(0, False, pya.DVector(12.275, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON",
              pya.DTrans(0, False, pya.DVector(13.725, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB",
              pya.DTrans(0, False, pya.DVector(14.275, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON",
              pya.DTrans(0, False, pya.DVector(15.725, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB",
              pya.DTrans(0, False, pya.DVector(16.275, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON",
              pya.DTrans(0, False, pya.DVector(17.725, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB",
              pya.DTrans(0, False, pya.DVector(18.275, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON",
              pya.DTrans(0, False, pya.DVector(19.725, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB",
              pya.DTrans(0, False, pya.DVector(20.275, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON",
              pya.DTrans(0, False, pya.DVector(21.725, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB",
              pya.DTrans(0, False, pya.DVector(22.275, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[11]",
              pya.DTrans(0, False, pya.DVector(23.725, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[11]",
              pya.DTrans(0, False, pya.DVector(24.275, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[12]",
              pya.DTrans(0, False, pya.DVector(25.725, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[12]",
              pya.DTrans(0, False, pya.DVector(26.275, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[13]",
              pya.DTrans(0, False, pya.DVector(27.725, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[13]",
              pya.DTrans(0, False, pya.DVector(28.275, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[14]",
              pya.DTrans(0, False, pya.DVector(29.725, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[14]",
              pya.DTrans(0, False, pya.DVector(30.275, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[15]",
              pya.DTrans(0, False, pya.DVector(31.725, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[15]",
              pya.DTrans(0, False, pya.DVector(32.275, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON",
              pya.DTrans(0, False, pya.DVector(23.725, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB",
              pya.DTrans(0, False, pya.DVector(24.275, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON",
              pya.DTrans(0, False, pya.DVector(25.725, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB",
              pya.DTrans(0, False, pya.DVector(26.275, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON",
              pya.DTrans(0, False, pya.DVector(27.725, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB",
              pya.DTrans(0, False, pya.DVector(28.275, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON",
              pya.DTrans(0, False, pya.DVector(29.725, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB",
              pya.DTrans(0, False, pya.DVector(30.275, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON",
              pya.DTrans(0, False, pya.DVector(31.725, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB",
              pya.DTrans(0, False, pya.DVector(32.275, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON",
              pya.DTrans(0, False, pya.DVector(33.725, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB",
              pya.DTrans(0, False, pya.DVector(34.275, -4.765))))
cell_dac2u16out2in.shapes(layout.layer(30, 25)).insert(
    pya.DText("VDD",
              pya.DTrans(0, False, pya.DVector(17, 1.615))))
cell_dac2u16out2in.shapes(layout.layer(30, 25)).insert(
    pya.DText("VcascP",
              pya.DTrans(0, False, pya.DVector(17, 0))))
cell_dac2u16out2in.shapes(layout.layer(30, 25)).insert(
    pya.DText("VDD",
              pya.DTrans(0, False, pya.DVector(17, -1.615))))
cell_dac2u16out2in.shapes(layout.layer(30, 25)).insert(
    pya.DText("VSS",
              pya.DTrans(0, False, pya.DVector(17, -4.045))))

# === via_stack ===
cell_via_stack.shapes(layout.layer(30, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.825, -0.865), pya.DPoint(-1.825, 0.865), pya.DPoint(1.825, 0.865), pya.DPoint(1.825, -0.865), pya.DPoint(-1.825, -0.865)]))
cell_via_stack.shapes(layout.layer(50, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.825, -0.865), pya.DPoint(-1.825, 0.865), pya.DPoint(1.825, 0.865), pya.DPoint(1.825, -0.865), pya.DPoint(-1.825, -0.865)]))
cell_via_stack.shapes(layout.layer(49, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.775, -0.815), pya.DPoint(-1.775, -0.625), pya.DPoint(-1.585, -0.625), pya.DPoint(-1.585, -0.815), pya.DPoint(-1.775, -0.815)]))
cell_via_stack.shapes(layout.layer(49, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.775, -0.335), pya.DPoint(-1.775, -0.145), pya.DPoint(-1.585, -0.145), pya.DPoint(-1.585, -0.335), pya.DPoint(-1.775, -0.335)]))
cell_via_stack.shapes(layout.layer(49, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.775, 0.145), pya.DPoint(-1.775, 0.335), pya.DPoint(-1.585, 0.335), pya.DPoint(-1.585, 0.145), pya.DPoint(-1.775, 0.145)]))
cell_via_stack.shapes(layout.layer(49, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.775, 0.625), pya.DPoint(-1.775, 0.815), pya.DPoint(-1.585, 0.815), pya.DPoint(-1.585, 0.625), pya.DPoint(-1.775, 0.625)]))
cell_via_stack.shapes(layout.layer(49, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.295, -0.815), pya.DPoint(-1.295, -0.625), pya.DPoint(-1.105, -0.625), pya.DPoint(-1.105, -0.815), pya.DPoint(-1.295, -0.815)]))
cell_via_stack.shapes(layout.layer(49, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.295, -0.335), pya.DPoint(-1.295, -0.145), pya.DPoint(-1.105, -0.145), pya.DPoint(-1.105, -0.335), pya.DPoint(-1.295, -0.335)]))
cell_via_stack.shapes(layout.layer(49, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.295, 0.145), pya.DPoint(-1.295, 0.335), pya.DPoint(-1.105, 0.335), pya.DPoint(-1.105, 0.145), pya.DPoint(-1.295, 0.145)]))
cell_via_stack.shapes(layout.layer(49, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.295, 0.625), pya.DPoint(-1.295, 0.815), pya.DPoint(-1.105, 0.815), pya.DPoint(-1.105, 0.625), pya.DPoint(-1.295, 0.625)]))
cell_via_stack.shapes(layout.layer(49, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.815, -0.815), pya.DPoint(-0.815, -0.625), pya.DPoint(-0.625, -0.625), pya.DPoint(-0.625, -0.815), pya.DPoint(-0.815, -0.815)]))
cell_via_stack.shapes(layout.layer(49, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.815, -0.335), pya.DPoint(-0.815, -0.145), pya.DPoint(-0.625, -0.145), pya.DPoint(-0.625, -0.335), pya.DPoint(-0.815, -0.335)]))
cell_via_stack.shapes(layout.layer(49, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.815, 0.145), pya.DPoint(-0.815, 0.335), pya.DPoint(-0.625, 0.335), pya.DPoint(-0.625, 0.145), pya.DPoint(-0.815, 0.145)]))
cell_via_stack.shapes(layout.layer(49, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.815, 0.625), pya.DPoint(-0.815, 0.815), pya.DPoint(-0.625, 0.815), pya.DPoint(-0.625, 0.625), pya.DPoint(-0.815, 0.625)]))
cell_via_stack.shapes(layout.layer(49, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.335, -0.815), pya.DPoint(-0.335, -0.625), pya.DPoint(-0.145, -0.625), pya.DPoint(-0.145, -0.815), pya.DPoint(-0.335, -0.815)]))
cell_via_stack.shapes(layout.layer(49, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.335, -0.335), pya.DPoint(-0.335, -0.145), pya.DPoint(-0.145, -0.145), pya.DPoint(-0.145, -0.335), pya.DPoint(-0.335, -0.335)]))
cell_via_stack.shapes(layout.layer(49, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.335, 0.145), pya.DPoint(-0.335, 0.335), pya.DPoint(-0.145, 0.335), pya.DPoint(-0.145, 0.145), pya.DPoint(-0.335, 0.145)]))
cell_via_stack.shapes(layout.layer(49, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.335, 0.625), pya.DPoint(-0.335, 0.815), pya.DPoint(-0.145, 0.815), pya.DPoint(-0.145, 0.625), pya.DPoint(-0.335, 0.625)]))
cell_via_stack.shapes(layout.layer(49, 0)).insert(
    pya.DPolygon([pya.DPoint(0.145, -0.815), pya.DPoint(0.145, -0.625), pya.DPoint(0.335, -0.625), pya.DPoint(0.335, -0.815), pya.DPoint(0.145, -0.815)]))
cell_via_stack.shapes(layout.layer(49, 0)).insert(
    pya.DPolygon([pya.DPoint(0.145, -0.335), pya.DPoint(0.145, -0.145), pya.DPoint(0.335, -0.145), pya.DPoint(0.335, -0.335), pya.DPoint(0.145, -0.335)]))
cell_via_stack.shapes(layout.layer(49, 0)).insert(
    pya.DPolygon([pya.DPoint(0.145, 0.145), pya.DPoint(0.145, 0.335), pya.DPoint(0.335, 0.335), pya.DPoint(0.335, 0.145), pya.DPoint(0.145, 0.145)]))
cell_via_stack.shapes(layout.layer(49, 0)).insert(
    pya.DPolygon([pya.DPoint(0.145, 0.625), pya.DPoint(0.145, 0.815), pya.DPoint(0.335, 0.815), pya.DPoint(0.335, 0.625), pya.DPoint(0.145, 0.625)]))
cell_via_stack.shapes(layout.layer(49, 0)).insert(
    pya.DPolygon([pya.DPoint(0.625, -0.815), pya.DPoint(0.625, -0.625), pya.DPoint(0.815, -0.625), pya.DPoint(0.815, -0.815), pya.DPoint(0.625, -0.815)]))
cell_via_stack.shapes(layout.layer(49, 0)).insert(
    pya.DPolygon([pya.DPoint(0.625, -0.335), pya.DPoint(0.625, -0.145), pya.DPoint(0.815, -0.145), pya.DPoint(0.815, -0.335), pya.DPoint(0.625, -0.335)]))
cell_via_stack.shapes(layout.layer(49, 0)).insert(
    pya.DPolygon([pya.DPoint(0.625, 0.145), pya.DPoint(0.625, 0.335), pya.DPoint(0.815, 0.335), pya.DPoint(0.815, 0.145), pya.DPoint(0.625, 0.145)]))
cell_via_stack.shapes(layout.layer(49, 0)).insert(
    pya.DPolygon([pya.DPoint(0.625, 0.625), pya.DPoint(0.625, 0.815), pya.DPoint(0.815, 0.815), pya.DPoint(0.815, 0.625), pya.DPoint(0.625, 0.625)]))
cell_via_stack.shapes(layout.layer(49, 0)).insert(
    pya.DPolygon([pya.DPoint(1.105, -0.815), pya.DPoint(1.105, -0.625), pya.DPoint(1.295, -0.625), pya.DPoint(1.295, -0.815), pya.DPoint(1.105, -0.815)]))
cell_via_stack.shapes(layout.layer(49, 0)).insert(
    pya.DPolygon([pya.DPoint(1.105, -0.335), pya.DPoint(1.105, -0.145), pya.DPoint(1.295, -0.145), pya.DPoint(1.295, -0.335), pya.DPoint(1.105, -0.335)]))
cell_via_stack.shapes(layout.layer(49, 0)).insert(
    pya.DPolygon([pya.DPoint(1.105, 0.145), pya.DPoint(1.105, 0.335), pya.DPoint(1.295, 0.335), pya.DPoint(1.295, 0.145), pya.DPoint(1.105, 0.145)]))
cell_via_stack.shapes(layout.layer(49, 0)).insert(
    pya.DPolygon([pya.DPoint(1.105, 0.625), pya.DPoint(1.105, 0.815), pya.DPoint(1.295, 0.815), pya.DPoint(1.295, 0.625), pya.DPoint(1.105, 0.625)]))
cell_via_stack.shapes(layout.layer(49, 0)).insert(
    pya.DPolygon([pya.DPoint(1.585, -0.815), pya.DPoint(1.585, -0.625), pya.DPoint(1.775, -0.625), pya.DPoint(1.775, -0.815), pya.DPoint(1.585, -0.815)]))
cell_via_stack.shapes(layout.layer(49, 0)).insert(
    pya.DPolygon([pya.DPoint(1.585, -0.335), pya.DPoint(1.585, -0.145), pya.DPoint(1.775, -0.145), pya.DPoint(1.775, -0.335), pya.DPoint(1.585, -0.335)]))
cell_via_stack.shapes(layout.layer(49, 0)).insert(
    pya.DPolygon([pya.DPoint(1.585, 0.145), pya.DPoint(1.585, 0.335), pya.DPoint(1.775, 0.335), pya.DPoint(1.775, 0.145), pya.DPoint(1.585, 0.145)]))
cell_via_stack.shapes(layout.layer(49, 0)).insert(
    pya.DPolygon([pya.DPoint(1.585, 0.625), pya.DPoint(1.585, 0.815), pya.DPoint(1.775, 0.815), pya.DPoint(1.775, 0.625), pya.DPoint(1.585, 0.625)]))

# === via_stack$4 ===
cell_via_stack_4.shapes(layout.layer(50, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.825, -5.905), pya.DPoint(-1.825, 5.905), pya.DPoint(1.825, 5.905), pya.DPoint(1.825, -5.905), pya.DPoint(-1.825, -5.905)]))
cell_via_stack_4.shapes(layout.layer(67, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.825, -5.905), pya.DPoint(-1.825, 5.905), pya.DPoint(1.825, 5.905), pya.DPoint(1.825, -5.905), pya.DPoint(-1.825, -5.905)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.775, -0.095), pya.DPoint(-1.775, 0.095), pya.DPoint(-1.585, 0.095), pya.DPoint(-1.585, -0.095), pya.DPoint(-1.775, -0.095)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.295, -0.095), pya.DPoint(-1.295, 0.095), pya.DPoint(-1.105, 0.095), pya.DPoint(-1.105, -0.095), pya.DPoint(-1.295, -0.095)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.815, -0.095), pya.DPoint(-0.815, 0.095), pya.DPoint(-0.625, 0.095), pya.DPoint(-0.625, -0.095), pya.DPoint(-0.815, -0.095)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.335, -0.095), pya.DPoint(-0.335, 0.095), pya.DPoint(-0.145, 0.095), pya.DPoint(-0.145, -0.095), pya.DPoint(-0.335, -0.095)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.145, -0.095), pya.DPoint(0.145, 0.095), pya.DPoint(0.335, 0.095), pya.DPoint(0.335, -0.095), pya.DPoint(0.145, -0.095)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.625, -0.095), pya.DPoint(0.625, 0.095), pya.DPoint(0.815, 0.095), pya.DPoint(0.815, -0.095), pya.DPoint(0.625, -0.095)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.105, -0.095), pya.DPoint(1.105, 0.095), pya.DPoint(1.295, 0.095), pya.DPoint(1.295, -0.095), pya.DPoint(1.105, -0.095)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.585, -0.095), pya.DPoint(1.585, 0.095), pya.DPoint(1.775, 0.095), pya.DPoint(1.775, -0.095), pya.DPoint(1.585, -0.095)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.145, 1.825), pya.DPoint(0.145, 2.015), pya.DPoint(0.335, 2.015), pya.DPoint(0.335, 1.825), pya.DPoint(0.145, 1.825)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.145, 2.305), pya.DPoint(0.145, 2.495), pya.DPoint(0.335, 2.495), pya.DPoint(0.335, 2.305), pya.DPoint(0.145, 2.305)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.145, 2.785), pya.DPoint(0.145, 2.975), pya.DPoint(0.335, 2.975), pya.DPoint(0.335, 2.785), pya.DPoint(0.145, 2.785)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.145, 3.265), pya.DPoint(0.145, 3.455), pya.DPoint(0.335, 3.455), pya.DPoint(0.335, 3.265), pya.DPoint(0.145, 3.265)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.145, 3.745), pya.DPoint(0.145, 3.935), pya.DPoint(0.335, 3.935), pya.DPoint(0.335, 3.745), pya.DPoint(0.145, 3.745)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.145, 4.225), pya.DPoint(0.145, 4.415), pya.DPoint(0.335, 4.415), pya.DPoint(0.335, 4.225), pya.DPoint(0.145, 4.225)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.145, 4.705), pya.DPoint(0.145, 4.895), pya.DPoint(0.335, 4.895), pya.DPoint(0.335, 4.705), pya.DPoint(0.145, 4.705)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.145, 5.185), pya.DPoint(0.145, 5.375), pya.DPoint(0.335, 5.375), pya.DPoint(0.335, 5.185), pya.DPoint(0.145, 5.185)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.145, 5.665), pya.DPoint(0.145, 5.855), pya.DPoint(0.335, 5.855), pya.DPoint(0.335, 5.665), pya.DPoint(0.145, 5.665)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.145, 0.385), pya.DPoint(0.145, 0.575), pya.DPoint(0.335, 0.575), pya.DPoint(0.335, 0.385), pya.DPoint(0.145, 0.385)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.625, 0.385), pya.DPoint(0.625, 0.575), pya.DPoint(0.815, 0.575), pya.DPoint(0.815, 0.385), pya.DPoint(0.625, 0.385)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.625, 0.865), pya.DPoint(0.625, 1.055), pya.DPoint(0.815, 1.055), pya.DPoint(0.815, 0.865), pya.DPoint(0.625, 0.865)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.625, 1.345), pya.DPoint(0.625, 1.535), pya.DPoint(0.815, 1.535), pya.DPoint(0.815, 1.345), pya.DPoint(0.625, 1.345)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.625, 1.825), pya.DPoint(0.625, 2.015), pya.DPoint(0.815, 2.015), pya.DPoint(0.815, 1.825), pya.DPoint(0.625, 1.825)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.625, 2.305), pya.DPoint(0.625, 2.495), pya.DPoint(0.815, 2.495), pya.DPoint(0.815, 2.305), pya.DPoint(0.625, 2.305)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.625, 2.785), pya.DPoint(0.625, 2.975), pya.DPoint(0.815, 2.975), pya.DPoint(0.815, 2.785), pya.DPoint(0.625, 2.785)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.625, 3.265), pya.DPoint(0.625, 3.455), pya.DPoint(0.815, 3.455), pya.DPoint(0.815, 3.265), pya.DPoint(0.625, 3.265)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.625, 3.745), pya.DPoint(0.625, 3.935), pya.DPoint(0.815, 3.935), pya.DPoint(0.815, 3.745), pya.DPoint(0.625, 3.745)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.625, 4.225), pya.DPoint(0.625, 4.415), pya.DPoint(0.815, 4.415), pya.DPoint(0.815, 4.225), pya.DPoint(0.625, 4.225)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.625, 4.705), pya.DPoint(0.625, 4.895), pya.DPoint(0.815, 4.895), pya.DPoint(0.815, 4.705), pya.DPoint(0.625, 4.705)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.625, 5.185), pya.DPoint(0.625, 5.375), pya.DPoint(0.815, 5.375), pya.DPoint(0.815, 5.185), pya.DPoint(0.625, 5.185)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.625, 5.665), pya.DPoint(0.625, 5.855), pya.DPoint(0.815, 5.855), pya.DPoint(0.815, 5.665), pya.DPoint(0.625, 5.665)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.145, 0.865), pya.DPoint(0.145, 1.055), pya.DPoint(0.335, 1.055), pya.DPoint(0.335, 0.865), pya.DPoint(0.145, 0.865)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.105, 0.385), pya.DPoint(1.105, 0.575), pya.DPoint(1.295, 0.575), pya.DPoint(1.295, 0.385), pya.DPoint(1.105, 0.385)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.105, 0.865), pya.DPoint(1.105, 1.055), pya.DPoint(1.295, 1.055), pya.DPoint(1.295, 0.865), pya.DPoint(1.105, 0.865)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.105, 1.345), pya.DPoint(1.105, 1.535), pya.DPoint(1.295, 1.535), pya.DPoint(1.295, 1.345), pya.DPoint(1.105, 1.345)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.105, 1.825), pya.DPoint(1.105, 2.015), pya.DPoint(1.295, 2.015), pya.DPoint(1.295, 1.825), pya.DPoint(1.105, 1.825)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.105, 2.305), pya.DPoint(1.105, 2.495), pya.DPoint(1.295, 2.495), pya.DPoint(1.295, 2.305), pya.DPoint(1.105, 2.305)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.105, 2.785), pya.DPoint(1.105, 2.975), pya.DPoint(1.295, 2.975), pya.DPoint(1.295, 2.785), pya.DPoint(1.105, 2.785)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.105, 3.265), pya.DPoint(1.105, 3.455), pya.DPoint(1.295, 3.455), pya.DPoint(1.295, 3.265), pya.DPoint(1.105, 3.265)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.105, 3.745), pya.DPoint(1.105, 3.935), pya.DPoint(1.295, 3.935), pya.DPoint(1.295, 3.745), pya.DPoint(1.105, 3.745)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.105, 4.225), pya.DPoint(1.105, 4.415), pya.DPoint(1.295, 4.415), pya.DPoint(1.295, 4.225), pya.DPoint(1.105, 4.225)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.105, 4.705), pya.DPoint(1.105, 4.895), pya.DPoint(1.295, 4.895), pya.DPoint(1.295, 4.705), pya.DPoint(1.105, 4.705)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.105, 5.185), pya.DPoint(1.105, 5.375), pya.DPoint(1.295, 5.375), pya.DPoint(1.295, 5.185), pya.DPoint(1.105, 5.185)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.105, 5.665), pya.DPoint(1.105, 5.855), pya.DPoint(1.295, 5.855), pya.DPoint(1.295, 5.665), pya.DPoint(1.105, 5.665)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.145, 1.345), pya.DPoint(0.145, 1.535), pya.DPoint(0.335, 1.535), pya.DPoint(0.335, 1.345), pya.DPoint(0.145, 1.345)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.585, 0.385), pya.DPoint(1.585, 0.575), pya.DPoint(1.775, 0.575), pya.DPoint(1.775, 0.385), pya.DPoint(1.585, 0.385)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.585, 0.865), pya.DPoint(1.585, 1.055), pya.DPoint(1.775, 1.055), pya.DPoint(1.775, 0.865), pya.DPoint(1.585, 0.865)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.585, 1.345), pya.DPoint(1.585, 1.535), pya.DPoint(1.775, 1.535), pya.DPoint(1.775, 1.345), pya.DPoint(1.585, 1.345)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.585, 1.825), pya.DPoint(1.585, 2.015), pya.DPoint(1.775, 2.015), pya.DPoint(1.775, 1.825), pya.DPoint(1.585, 1.825)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.585, 2.305), pya.DPoint(1.585, 2.495), pya.DPoint(1.775, 2.495), pya.DPoint(1.775, 2.305), pya.DPoint(1.585, 2.305)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.585, 2.785), pya.DPoint(1.585, 2.975), pya.DPoint(1.775, 2.975), pya.DPoint(1.775, 2.785), pya.DPoint(1.585, 2.785)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.585, 3.265), pya.DPoint(1.585, 3.455), pya.DPoint(1.775, 3.455), pya.DPoint(1.775, 3.265), pya.DPoint(1.585, 3.265)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.585, 3.745), pya.DPoint(1.585, 3.935), pya.DPoint(1.775, 3.935), pya.DPoint(1.775, 3.745), pya.DPoint(1.585, 3.745)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.585, 4.225), pya.DPoint(1.585, 4.415), pya.DPoint(1.775, 4.415), pya.DPoint(1.775, 4.225), pya.DPoint(1.585, 4.225)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.585, 4.705), pya.DPoint(1.585, 4.895), pya.DPoint(1.775, 4.895), pya.DPoint(1.775, 4.705), pya.DPoint(1.585, 4.705)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.585, 5.185), pya.DPoint(1.585, 5.375), pya.DPoint(1.775, 5.375), pya.DPoint(1.775, 5.185), pya.DPoint(1.585, 5.185)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.585, 5.665), pya.DPoint(1.585, 5.855), pya.DPoint(1.775, 5.855), pya.DPoint(1.775, 5.665), pya.DPoint(1.585, 5.665)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.775, 3.745), pya.DPoint(-1.775, 3.935), pya.DPoint(-1.585, 3.935), pya.DPoint(-1.585, 3.745), pya.DPoint(-1.775, 3.745)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.775, 4.225), pya.DPoint(-1.775, 4.415), pya.DPoint(-1.585, 4.415), pya.DPoint(-1.585, 4.225), pya.DPoint(-1.775, 4.225)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.775, 4.705), pya.DPoint(-1.775, 4.895), pya.DPoint(-1.585, 4.895), pya.DPoint(-1.585, 4.705), pya.DPoint(-1.775, 4.705)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.775, 5.185), pya.DPoint(-1.775, 5.375), pya.DPoint(-1.585, 5.375), pya.DPoint(-1.585, 5.185), pya.DPoint(-1.775, 5.185)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.775, 5.665), pya.DPoint(-1.775, 5.855), pya.DPoint(-1.585, 5.855), pya.DPoint(-1.585, 5.665), pya.DPoint(-1.775, 5.665)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.775, 0.385), pya.DPoint(-1.775, 0.575), pya.DPoint(-1.585, 0.575), pya.DPoint(-1.585, 0.385), pya.DPoint(-1.775, 0.385)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.295, 0.385), pya.DPoint(-1.295, 0.575), pya.DPoint(-1.105, 0.575), pya.DPoint(-1.105, 0.385), pya.DPoint(-1.295, 0.385)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.295, 0.865), pya.DPoint(-1.295, 1.055), pya.DPoint(-1.105, 1.055), pya.DPoint(-1.105, 0.865), pya.DPoint(-1.295, 0.865)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.295, 1.345), pya.DPoint(-1.295, 1.535), pya.DPoint(-1.105, 1.535), pya.DPoint(-1.105, 1.345), pya.DPoint(-1.295, 1.345)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.295, 1.825), pya.DPoint(-1.295, 2.015), pya.DPoint(-1.105, 2.015), pya.DPoint(-1.105, 1.825), pya.DPoint(-1.295, 1.825)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.295, 2.305), pya.DPoint(-1.295, 2.495), pya.DPoint(-1.105, 2.495), pya.DPoint(-1.105, 2.305), pya.DPoint(-1.295, 2.305)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.295, 2.785), pya.DPoint(-1.295, 2.975), pya.DPoint(-1.105, 2.975), pya.DPoint(-1.105, 2.785), pya.DPoint(-1.295, 2.785)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.295, 3.265), pya.DPoint(-1.295, 3.455), pya.DPoint(-1.105, 3.455), pya.DPoint(-1.105, 3.265), pya.DPoint(-1.295, 3.265)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.295, 3.745), pya.DPoint(-1.295, 3.935), pya.DPoint(-1.105, 3.935), pya.DPoint(-1.105, 3.745), pya.DPoint(-1.295, 3.745)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.295, 4.225), pya.DPoint(-1.295, 4.415), pya.DPoint(-1.105, 4.415), pya.DPoint(-1.105, 4.225), pya.DPoint(-1.295, 4.225)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.295, 4.705), pya.DPoint(-1.295, 4.895), pya.DPoint(-1.105, 4.895), pya.DPoint(-1.105, 4.705), pya.DPoint(-1.295, 4.705)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.295, 5.185), pya.DPoint(-1.295, 5.375), pya.DPoint(-1.105, 5.375), pya.DPoint(-1.105, 5.185), pya.DPoint(-1.295, 5.185)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.295, 5.665), pya.DPoint(-1.295, 5.855), pya.DPoint(-1.105, 5.855), pya.DPoint(-1.105, 5.665), pya.DPoint(-1.295, 5.665)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.775, 0.865), pya.DPoint(-1.775, 1.055), pya.DPoint(-1.585, 1.055), pya.DPoint(-1.585, 0.865), pya.DPoint(-1.775, 0.865)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.815, 0.385), pya.DPoint(-0.815, 0.575), pya.DPoint(-0.625, 0.575), pya.DPoint(-0.625, 0.385), pya.DPoint(-0.815, 0.385)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.815, 0.865), pya.DPoint(-0.815, 1.055), pya.DPoint(-0.625, 1.055), pya.DPoint(-0.625, 0.865), pya.DPoint(-0.815, 0.865)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.815, 1.345), pya.DPoint(-0.815, 1.535), pya.DPoint(-0.625, 1.535), pya.DPoint(-0.625, 1.345), pya.DPoint(-0.815, 1.345)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.815, 1.825), pya.DPoint(-0.815, 2.015), pya.DPoint(-0.625, 2.015), pya.DPoint(-0.625, 1.825), pya.DPoint(-0.815, 1.825)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.815, 2.305), pya.DPoint(-0.815, 2.495), pya.DPoint(-0.625, 2.495), pya.DPoint(-0.625, 2.305), pya.DPoint(-0.815, 2.305)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.815, 2.785), pya.DPoint(-0.815, 2.975), pya.DPoint(-0.625, 2.975), pya.DPoint(-0.625, 2.785), pya.DPoint(-0.815, 2.785)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.815, 3.265), pya.DPoint(-0.815, 3.455), pya.DPoint(-0.625, 3.455), pya.DPoint(-0.625, 3.265), pya.DPoint(-0.815, 3.265)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.815, 3.745), pya.DPoint(-0.815, 3.935), pya.DPoint(-0.625, 3.935), pya.DPoint(-0.625, 3.745), pya.DPoint(-0.815, 3.745)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.815, 4.225), pya.DPoint(-0.815, 4.415), pya.DPoint(-0.625, 4.415), pya.DPoint(-0.625, 4.225), pya.DPoint(-0.815, 4.225)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.815, 4.705), pya.DPoint(-0.815, 4.895), pya.DPoint(-0.625, 4.895), pya.DPoint(-0.625, 4.705), pya.DPoint(-0.815, 4.705)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.815, 5.185), pya.DPoint(-0.815, 5.375), pya.DPoint(-0.625, 5.375), pya.DPoint(-0.625, 5.185), pya.DPoint(-0.815, 5.185)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.815, 5.665), pya.DPoint(-0.815, 5.855), pya.DPoint(-0.625, 5.855), pya.DPoint(-0.625, 5.665), pya.DPoint(-0.815, 5.665)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.775, 1.345), pya.DPoint(-1.775, 1.535), pya.DPoint(-1.585, 1.535), pya.DPoint(-1.585, 1.345), pya.DPoint(-1.775, 1.345)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.335, 0.385), pya.DPoint(-0.335, 0.575), pya.DPoint(-0.145, 0.575), pya.DPoint(-0.145, 0.385), pya.DPoint(-0.335, 0.385)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.335, 0.865), pya.DPoint(-0.335, 1.055), pya.DPoint(-0.145, 1.055), pya.DPoint(-0.145, 0.865), pya.DPoint(-0.335, 0.865)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.335, 1.345), pya.DPoint(-0.335, 1.535), pya.DPoint(-0.145, 1.535), pya.DPoint(-0.145, 1.345), pya.DPoint(-0.335, 1.345)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.335, 1.825), pya.DPoint(-0.335, 2.015), pya.DPoint(-0.145, 2.015), pya.DPoint(-0.145, 1.825), pya.DPoint(-0.335, 1.825)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.335, 2.305), pya.DPoint(-0.335, 2.495), pya.DPoint(-0.145, 2.495), pya.DPoint(-0.145, 2.305), pya.DPoint(-0.335, 2.305)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.335, 2.785), pya.DPoint(-0.335, 2.975), pya.DPoint(-0.145, 2.975), pya.DPoint(-0.145, 2.785), pya.DPoint(-0.335, 2.785)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.335, 3.265), pya.DPoint(-0.335, 3.455), pya.DPoint(-0.145, 3.455), pya.DPoint(-0.145, 3.265), pya.DPoint(-0.335, 3.265)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.335, 3.745), pya.DPoint(-0.335, 3.935), pya.DPoint(-0.145, 3.935), pya.DPoint(-0.145, 3.745), pya.DPoint(-0.335, 3.745)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.335, 4.225), pya.DPoint(-0.335, 4.415), pya.DPoint(-0.145, 4.415), pya.DPoint(-0.145, 4.225), pya.DPoint(-0.335, 4.225)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.335, 4.705), pya.DPoint(-0.335, 4.895), pya.DPoint(-0.145, 4.895), pya.DPoint(-0.145, 4.705), pya.DPoint(-0.335, 4.705)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.335, 5.185), pya.DPoint(-0.335, 5.375), pya.DPoint(-0.145, 5.375), pya.DPoint(-0.145, 5.185), pya.DPoint(-0.335, 5.185)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.335, 5.665), pya.DPoint(-0.335, 5.855), pya.DPoint(-0.145, 5.855), pya.DPoint(-0.145, 5.665), pya.DPoint(-0.335, 5.665)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.775, 1.825), pya.DPoint(-1.775, 2.015), pya.DPoint(-1.585, 2.015), pya.DPoint(-1.585, 1.825), pya.DPoint(-1.775, 1.825)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.775, 2.305), pya.DPoint(-1.775, 2.495), pya.DPoint(-1.585, 2.495), pya.DPoint(-1.585, 2.305), pya.DPoint(-1.775, 2.305)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.775, 2.785), pya.DPoint(-1.775, 2.975), pya.DPoint(-1.585, 2.975), pya.DPoint(-1.585, 2.785), pya.DPoint(-1.775, 2.785)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.775, 3.265), pya.DPoint(-1.775, 3.455), pya.DPoint(-1.585, 3.455), pya.DPoint(-1.585, 3.265), pya.DPoint(-1.775, 3.265)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.815, -2.975), pya.DPoint(-0.815, -2.785), pya.DPoint(-0.625, -2.785), pya.DPoint(-0.625, -2.975), pya.DPoint(-0.815, -2.975)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.815, -2.495), pya.DPoint(-0.815, -2.305), pya.DPoint(-0.625, -2.305), pya.DPoint(-0.625, -2.495), pya.DPoint(-0.815, -2.495)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.815, -2.015), pya.DPoint(-0.815, -1.825), pya.DPoint(-0.625, -1.825), pya.DPoint(-0.625, -2.015), pya.DPoint(-0.815, -2.015)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.815, -1.535), pya.DPoint(-0.815, -1.345), pya.DPoint(-0.625, -1.345), pya.DPoint(-0.625, -1.535), pya.DPoint(-0.815, -1.535)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.815, -1.055), pya.DPoint(-0.815, -0.865), pya.DPoint(-0.625, -0.865), pya.DPoint(-0.625, -1.055), pya.DPoint(-0.815, -1.055)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.815, -0.575), pya.DPoint(-0.815, -0.385), pya.DPoint(-0.625, -0.385), pya.DPoint(-0.625, -0.575), pya.DPoint(-0.815, -0.575)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.295, -5.375), pya.DPoint(-1.295, -5.185), pya.DPoint(-1.105, -5.185), pya.DPoint(-1.105, -5.375), pya.DPoint(-1.295, -5.375)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.295, -4.895), pya.DPoint(-1.295, -4.705), pya.DPoint(-1.105, -4.705), pya.DPoint(-1.105, -4.895), pya.DPoint(-1.295, -4.895)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.295, -4.415), pya.DPoint(-1.295, -4.225), pya.DPoint(-1.105, -4.225), pya.DPoint(-1.105, -4.415), pya.DPoint(-1.295, -4.415)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.295, -3.935), pya.DPoint(-1.295, -3.745), pya.DPoint(-1.105, -3.745), pya.DPoint(-1.105, -3.935), pya.DPoint(-1.295, -3.935)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.295, -3.455), pya.DPoint(-1.295, -3.265), pya.DPoint(-1.105, -3.265), pya.DPoint(-1.105, -3.455), pya.DPoint(-1.295, -3.455)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.295, -2.975), pya.DPoint(-1.295, -2.785), pya.DPoint(-1.105, -2.785), pya.DPoint(-1.105, -2.975), pya.DPoint(-1.295, -2.975)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.295, -2.495), pya.DPoint(-1.295, -2.305), pya.DPoint(-1.105, -2.305), pya.DPoint(-1.105, -2.495), pya.DPoint(-1.295, -2.495)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.295, -2.015), pya.DPoint(-1.295, -1.825), pya.DPoint(-1.105, -1.825), pya.DPoint(-1.105, -2.015), pya.DPoint(-1.295, -2.015)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.295, -1.535), pya.DPoint(-1.295, -1.345), pya.DPoint(-1.105, -1.345), pya.DPoint(-1.105, -1.535), pya.DPoint(-1.295, -1.535)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.295, -1.055), pya.DPoint(-1.295, -0.865), pya.DPoint(-1.105, -0.865), pya.DPoint(-1.105, -1.055), pya.DPoint(-1.295, -1.055)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.295, -0.575), pya.DPoint(-1.295, -0.385), pya.DPoint(-1.105, -0.385), pya.DPoint(-1.105, -0.575), pya.DPoint(-1.295, -0.575)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.775, -5.375), pya.DPoint(-1.775, -5.185), pya.DPoint(-1.585, -5.185), pya.DPoint(-1.585, -5.375), pya.DPoint(-1.775, -5.375)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.775, -4.895), pya.DPoint(-1.775, -4.705), pya.DPoint(-1.585, -4.705), pya.DPoint(-1.585, -4.895), pya.DPoint(-1.775, -4.895)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.335, -5.855), pya.DPoint(-0.335, -5.665), pya.DPoint(-0.145, -5.665), pya.DPoint(-0.145, -5.855), pya.DPoint(-0.335, -5.855)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.335, -5.375), pya.DPoint(-0.335, -5.185), pya.DPoint(-0.145, -5.185), pya.DPoint(-0.145, -5.375), pya.DPoint(-0.335, -5.375)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.335, -4.895), pya.DPoint(-0.335, -4.705), pya.DPoint(-0.145, -4.705), pya.DPoint(-0.145, -4.895), pya.DPoint(-0.335, -4.895)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.335, -4.415), pya.DPoint(-0.335, -4.225), pya.DPoint(-0.145, -4.225), pya.DPoint(-0.145, -4.415), pya.DPoint(-0.335, -4.415)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.335, -3.935), pya.DPoint(-0.335, -3.745), pya.DPoint(-0.145, -3.745), pya.DPoint(-0.145, -3.935), pya.DPoint(-0.335, -3.935)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.335, -3.455), pya.DPoint(-0.335, -3.265), pya.DPoint(-0.145, -3.265), pya.DPoint(-0.145, -3.455), pya.DPoint(-0.335, -3.455)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.335, -2.975), pya.DPoint(-0.335, -2.785), pya.DPoint(-0.145, -2.785), pya.DPoint(-0.145, -2.975), pya.DPoint(-0.335, -2.975)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.335, -2.495), pya.DPoint(-0.335, -2.305), pya.DPoint(-0.145, -2.305), pya.DPoint(-0.145, -2.495), pya.DPoint(-0.335, -2.495)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.335, -2.015), pya.DPoint(-0.335, -1.825), pya.DPoint(-0.145, -1.825), pya.DPoint(-0.145, -2.015), pya.DPoint(-0.335, -2.015)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.335, -1.535), pya.DPoint(-0.335, -1.345), pya.DPoint(-0.145, -1.345), pya.DPoint(-0.145, -1.535), pya.DPoint(-0.335, -1.535)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.335, -1.055), pya.DPoint(-0.335, -0.865), pya.DPoint(-0.145, -0.865), pya.DPoint(-0.145, -1.055), pya.DPoint(-0.335, -1.055)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.335, -0.575), pya.DPoint(-0.335, -0.385), pya.DPoint(-0.145, -0.385), pya.DPoint(-0.145, -0.575), pya.DPoint(-0.335, -0.575)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.775, -4.415), pya.DPoint(-1.775, -4.225), pya.DPoint(-1.585, -4.225), pya.DPoint(-1.585, -4.415), pya.DPoint(-1.775, -4.415)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.775, -3.935), pya.DPoint(-1.775, -3.745), pya.DPoint(-1.585, -3.745), pya.DPoint(-1.585, -3.935), pya.DPoint(-1.775, -3.935)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.775, -3.455), pya.DPoint(-1.775, -3.265), pya.DPoint(-1.585, -3.265), pya.DPoint(-1.585, -3.455), pya.DPoint(-1.775, -3.455)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.775, -2.975), pya.DPoint(-1.775, -2.785), pya.DPoint(-1.585, -2.785), pya.DPoint(-1.585, -2.975), pya.DPoint(-1.775, -2.975)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.775, -2.495), pya.DPoint(-1.775, -2.305), pya.DPoint(-1.585, -2.305), pya.DPoint(-1.585, -2.495), pya.DPoint(-1.775, -2.495)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.775, -2.015), pya.DPoint(-1.775, -1.825), pya.DPoint(-1.585, -1.825), pya.DPoint(-1.585, -2.015), pya.DPoint(-1.775, -2.015)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.775, -1.535), pya.DPoint(-1.775, -1.345), pya.DPoint(-1.585, -1.345), pya.DPoint(-1.585, -1.535), pya.DPoint(-1.775, -1.535)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.775, -1.055), pya.DPoint(-1.775, -0.865), pya.DPoint(-1.585, -0.865), pya.DPoint(-1.585, -1.055), pya.DPoint(-1.775, -1.055)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.775, -0.575), pya.DPoint(-1.775, -0.385), pya.DPoint(-1.585, -0.385), pya.DPoint(-1.585, -0.575), pya.DPoint(-1.775, -0.575)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.775, -5.855), pya.DPoint(-1.775, -5.665), pya.DPoint(-1.585, -5.665), pya.DPoint(-1.585, -5.855), pya.DPoint(-1.775, -5.855)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-1.295, -5.855), pya.DPoint(-1.295, -5.665), pya.DPoint(-1.105, -5.665), pya.DPoint(-1.105, -5.855), pya.DPoint(-1.295, -5.855)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.815, -5.855), pya.DPoint(-0.815, -5.665), pya.DPoint(-0.625, -5.665), pya.DPoint(-0.625, -5.855), pya.DPoint(-0.815, -5.855)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.815, -5.375), pya.DPoint(-0.815, -5.185), pya.DPoint(-0.625, -5.185), pya.DPoint(-0.625, -5.375), pya.DPoint(-0.815, -5.375)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.815, -4.895), pya.DPoint(-0.815, -4.705), pya.DPoint(-0.625, -4.705), pya.DPoint(-0.625, -4.895), pya.DPoint(-0.815, -4.895)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.815, -4.415), pya.DPoint(-0.815, -4.225), pya.DPoint(-0.625, -4.225), pya.DPoint(-0.625, -4.415), pya.DPoint(-0.815, -4.415)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.815, -3.935), pya.DPoint(-0.815, -3.745), pya.DPoint(-0.625, -3.745), pya.DPoint(-0.625, -3.935), pya.DPoint(-0.815, -3.935)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.815, -3.455), pya.DPoint(-0.815, -3.265), pya.DPoint(-0.625, -3.265), pya.DPoint(-0.625, -3.455), pya.DPoint(-0.815, -3.455)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.105, -4.895), pya.DPoint(1.105, -4.705), pya.DPoint(1.295, -4.705), pya.DPoint(1.295, -4.895), pya.DPoint(1.105, -4.895)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.105, -4.415), pya.DPoint(1.105, -4.225), pya.DPoint(1.295, -4.225), pya.DPoint(1.295, -4.415), pya.DPoint(1.105, -4.415)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.105, -3.935), pya.DPoint(1.105, -3.745), pya.DPoint(1.295, -3.745), pya.DPoint(1.295, -3.935), pya.DPoint(1.105, -3.935)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.105, -3.455), pya.DPoint(1.105, -3.265), pya.DPoint(1.295, -3.265), pya.DPoint(1.295, -3.455), pya.DPoint(1.105, -3.455)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.105, -2.975), pya.DPoint(1.105, -2.785), pya.DPoint(1.295, -2.785), pya.DPoint(1.295, -2.975), pya.DPoint(1.105, -2.975)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.105, -2.495), pya.DPoint(1.105, -2.305), pya.DPoint(1.295, -2.305), pya.DPoint(1.295, -2.495), pya.DPoint(1.105, -2.495)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.105, -2.015), pya.DPoint(1.105, -1.825), pya.DPoint(1.295, -1.825), pya.DPoint(1.295, -2.015), pya.DPoint(1.105, -2.015)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.105, -1.535), pya.DPoint(1.105, -1.345), pya.DPoint(1.295, -1.345), pya.DPoint(1.295, -1.535), pya.DPoint(1.105, -1.535)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.105, -1.055), pya.DPoint(1.105, -0.865), pya.DPoint(1.295, -0.865), pya.DPoint(1.295, -1.055), pya.DPoint(1.105, -1.055)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.105, -0.575), pya.DPoint(1.105, -0.385), pya.DPoint(1.295, -0.385), pya.DPoint(1.295, -0.575), pya.DPoint(1.105, -0.575)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.625, -5.375), pya.DPoint(0.625, -5.185), pya.DPoint(0.815, -5.185), pya.DPoint(0.815, -5.375), pya.DPoint(0.625, -5.375)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.625, -4.895), pya.DPoint(0.625, -4.705), pya.DPoint(0.815, -4.705), pya.DPoint(0.815, -4.895), pya.DPoint(0.625, -4.895)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.625, -4.415), pya.DPoint(0.625, -4.225), pya.DPoint(0.815, -4.225), pya.DPoint(0.815, -4.415), pya.DPoint(0.625, -4.415)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.625, -3.935), pya.DPoint(0.625, -3.745), pya.DPoint(0.815, -3.745), pya.DPoint(0.815, -3.935), pya.DPoint(0.625, -3.935)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.625, -3.455), pya.DPoint(0.625, -3.265), pya.DPoint(0.815, -3.265), pya.DPoint(0.815, -3.455), pya.DPoint(0.625, -3.455)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.625, -2.975), pya.DPoint(0.625, -2.785), pya.DPoint(0.815, -2.785), pya.DPoint(0.815, -2.975), pya.DPoint(0.625, -2.975)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.625, -2.495), pya.DPoint(0.625, -2.305), pya.DPoint(0.815, -2.305), pya.DPoint(0.815, -2.495), pya.DPoint(0.625, -2.495)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.625, -2.015), pya.DPoint(0.625, -1.825), pya.DPoint(0.815, -1.825), pya.DPoint(0.815, -2.015), pya.DPoint(0.625, -2.015)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.625, -1.535), pya.DPoint(0.625, -1.345), pya.DPoint(0.815, -1.345), pya.DPoint(0.815, -1.535), pya.DPoint(0.625, -1.535)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.625, -1.055), pya.DPoint(0.625, -0.865), pya.DPoint(0.815, -0.865), pya.DPoint(0.815, -1.055), pya.DPoint(0.625, -1.055)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.625, -0.575), pya.DPoint(0.625, -0.385), pya.DPoint(0.815, -0.385), pya.DPoint(0.815, -0.575), pya.DPoint(0.625, -0.575)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.145, -5.375), pya.DPoint(0.145, -5.185), pya.DPoint(0.335, -5.185), pya.DPoint(0.335, -5.375), pya.DPoint(0.145, -5.375)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.145, -4.895), pya.DPoint(0.145, -4.705), pya.DPoint(0.335, -4.705), pya.DPoint(0.335, -4.895), pya.DPoint(0.145, -4.895)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.585, -5.855), pya.DPoint(1.585, -5.665), pya.DPoint(1.775, -5.665), pya.DPoint(1.775, -5.855), pya.DPoint(1.585, -5.855)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.585, -5.375), pya.DPoint(1.585, -5.185), pya.DPoint(1.775, -5.185), pya.DPoint(1.775, -5.375), pya.DPoint(1.585, -5.375)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.585, -4.895), pya.DPoint(1.585, -4.705), pya.DPoint(1.775, -4.705), pya.DPoint(1.775, -4.895), pya.DPoint(1.585, -4.895)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.585, -4.415), pya.DPoint(1.585, -4.225), pya.DPoint(1.775, -4.225), pya.DPoint(1.775, -4.415), pya.DPoint(1.585, -4.415)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.585, -3.935), pya.DPoint(1.585, -3.745), pya.DPoint(1.775, -3.745), pya.DPoint(1.775, -3.935), pya.DPoint(1.585, -3.935)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.585, -3.455), pya.DPoint(1.585, -3.265), pya.DPoint(1.775, -3.265), pya.DPoint(1.775, -3.455), pya.DPoint(1.585, -3.455)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.585, -2.975), pya.DPoint(1.585, -2.785), pya.DPoint(1.775, -2.785), pya.DPoint(1.775, -2.975), pya.DPoint(1.585, -2.975)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.585, -2.495), pya.DPoint(1.585, -2.305), pya.DPoint(1.775, -2.305), pya.DPoint(1.775, -2.495), pya.DPoint(1.585, -2.495)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.585, -2.015), pya.DPoint(1.585, -1.825), pya.DPoint(1.775, -1.825), pya.DPoint(1.775, -2.015), pya.DPoint(1.585, -2.015)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.585, -1.535), pya.DPoint(1.585, -1.345), pya.DPoint(1.775, -1.345), pya.DPoint(1.775, -1.535), pya.DPoint(1.585, -1.535)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.585, -1.055), pya.DPoint(1.585, -0.865), pya.DPoint(1.775, -0.865), pya.DPoint(1.775, -1.055), pya.DPoint(1.585, -1.055)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.585, -0.575), pya.DPoint(1.585, -0.385), pya.DPoint(1.775, -0.385), pya.DPoint(1.775, -0.575), pya.DPoint(1.585, -0.575)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.145, -4.415), pya.DPoint(0.145, -4.225), pya.DPoint(0.335, -4.225), pya.DPoint(0.335, -4.415), pya.DPoint(0.145, -4.415)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.145, -3.935), pya.DPoint(0.145, -3.745), pya.DPoint(0.335, -3.745), pya.DPoint(0.335, -3.935), pya.DPoint(0.145, -3.935)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.145, -3.455), pya.DPoint(0.145, -3.265), pya.DPoint(0.335, -3.265), pya.DPoint(0.335, -3.455), pya.DPoint(0.145, -3.455)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.145, -2.975), pya.DPoint(0.145, -2.785), pya.DPoint(0.335, -2.785), pya.DPoint(0.335, -2.975), pya.DPoint(0.145, -2.975)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.145, -2.495), pya.DPoint(0.145, -2.305), pya.DPoint(0.335, -2.305), pya.DPoint(0.335, -2.495), pya.DPoint(0.145, -2.495)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.145, -2.015), pya.DPoint(0.145, -1.825), pya.DPoint(0.335, -1.825), pya.DPoint(0.335, -2.015), pya.DPoint(0.145, -2.015)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.145, -1.535), pya.DPoint(0.145, -1.345), pya.DPoint(0.335, -1.345), pya.DPoint(0.335, -1.535), pya.DPoint(0.145, -1.535)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.145, -1.055), pya.DPoint(0.145, -0.865), pya.DPoint(0.335, -0.865), pya.DPoint(0.335, -1.055), pya.DPoint(0.145, -1.055)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.145, -0.575), pya.DPoint(0.145, -0.385), pya.DPoint(0.335, -0.385), pya.DPoint(0.335, -0.575), pya.DPoint(0.145, -0.575)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.145, -5.855), pya.DPoint(0.145, -5.665), pya.DPoint(0.335, -5.665), pya.DPoint(0.335, -5.855), pya.DPoint(0.145, -5.855)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(0.625, -5.855), pya.DPoint(0.625, -5.665), pya.DPoint(0.815, -5.665), pya.DPoint(0.815, -5.855), pya.DPoint(0.625, -5.855)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.105, -5.855), pya.DPoint(1.105, -5.665), pya.DPoint(1.295, -5.665), pya.DPoint(1.295, -5.855), pya.DPoint(1.105, -5.855)]))
cell_via_stack_4.shapes(layout.layer(66, 0)).insert(
    pya.DPolygon([pya.DPoint(1.105, -5.375), pya.DPoint(1.105, -5.185), pya.DPoint(1.295, -5.185), pya.DPoint(1.295, -5.375), pya.DPoint(1.105, -5.375)]))

# === via_stack$7 ===
cell_via_stack_7.shapes(layout.layer(8, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.35, -0.35), pya.DPoint(-0.35, 0.35), pya.DPoint(0.35, 0.35), pya.DPoint(0.35, -0.35), pya.DPoint(-0.35, -0.35)]))
cell_via_stack_7.shapes(layout.layer(10, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.35, -0.35), pya.DPoint(-0.35, 0.35), pya.DPoint(0.35, 0.35), pya.DPoint(0.35, -0.35), pya.DPoint(-0.35, -0.35)]))
cell_via_stack_7.shapes(layout.layer(19, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.3, -0.3), pya.DPoint(-0.3, -0.11), pya.DPoint(-0.11, -0.11), pya.DPoint(-0.11, -0.3), pya.DPoint(-0.3, -0.3)]))
cell_via_stack_7.shapes(layout.layer(19, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.3, 0.11), pya.DPoint(-0.3, 0.3), pya.DPoint(-0.11, 0.3), pya.DPoint(-0.11, 0.11), pya.DPoint(-0.3, 0.11)]))
cell_via_stack_7.shapes(layout.layer(19, 0)).insert(
    pya.DPolygon([pya.DPoint(0.11, -0.3), pya.DPoint(0.11, -0.11), pya.DPoint(0.3, -0.11), pya.DPoint(0.3, -0.3), pya.DPoint(0.11, -0.3)]))
cell_via_stack_7.shapes(layout.layer(19, 0)).insert(
    pya.DPolygon([pya.DPoint(0.11, 0.11), pya.DPoint(0.11, 0.3), pya.DPoint(0.3, 0.3), pya.DPoint(0.3, 0.11), pya.DPoint(0.11, 0.11)]))
cell_via_stack_7.shapes(layout.layer(30, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.35, -0.35), pya.DPoint(-0.35, 0.35), pya.DPoint(0.35, 0.35), pya.DPoint(0.35, -0.35), pya.DPoint(-0.35, -0.35)]))
cell_via_stack_7.shapes(layout.layer(29, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.3, -0.3), pya.DPoint(-0.3, -0.11), pya.DPoint(-0.11, -0.11), pya.DPoint(-0.11, -0.3), pya.DPoint(-0.3, -0.3)]))
cell_via_stack_7.shapes(layout.layer(29, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.3, 0.11), pya.DPoint(-0.3, 0.3), pya.DPoint(-0.11, 0.3), pya.DPoint(-0.11, 0.11), pya.DPoint(-0.3, 0.11)]))
cell_via_stack_7.shapes(layout.layer(29, 0)).insert(
    pya.DPolygon([pya.DPoint(0.11, -0.3), pya.DPoint(0.11, -0.11), pya.DPoint(0.3, -0.11), pya.DPoint(0.3, -0.3), pya.DPoint(0.11, -0.3)]))
cell_via_stack_7.shapes(layout.layer(29, 0)).insert(
    pya.DPolygon([pya.DPoint(0.11, 0.11), pya.DPoint(0.11, 0.3), pya.DPoint(0.3, 0.3), pya.DPoint(0.3, 0.11), pya.DPoint(0.11, 0.11)]))

# === dac2u32out4in ===
cell_dac2u32out4in.insert(pya.DCellInstArray(
    cell_dac2u16out2in.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(1.9, 4.91))))
cell_dac2u32out4in.insert(pya.DCellInstArray(
    cell_dac2u16out2in.cell_index(),
    pya.DCplxTrans(1, 180, False,
                  pya.DVector(35.9, 21.28))))
cell_dac2u32out4in.shapes(layout.layer(14, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.18, 5.72), pya.DPoint(-0.18, 20.47), pya.DPoint(37.98, 20.47), pya.DPoint(37.98, 5.72), pya.DPoint(-0.18, 5.72)]))
cell_dac2u32out4in.shapes(layout.layer(31, 0)).insert(
    pya.DPolygon([pya.DPoint(-0.31, 2.525), pya.DPoint(-0.31, 23.665), pya.DPoint(38.11, 23.665), pya.DPoint(38.11, 2.525), pya.DPoint(-0.31, 2.525)]))
cell_dac2u32out4in.shapes(layout.layer(189, 4)).insert(
    pya.DPolygon([pya.DPoint(0, -0.07), pya.DPoint(0, 26.26), pya.DPoint(37.8, 26.26), pya.DPoint(37.8, -0.07), pya.DPoint(0, -0.07)]))
cell_dac2u32out4in.shapes(layout.layer(8, 2)).insert(
    pya.DPolygon([pya.DPoint(0.9, 14.95), pya.DPoint(0.9, 19.88), pya.DPoint(36.9, 19.88), pya.DPoint(36.9, 14.95), pya.DPoint(0.9, 14.95)]))
cell_dac2u32out4in.shapes(layout.layer(8, 2)).insert(
    pya.DPolygon([pya.DPoint(0, 12.745), pya.DPoint(0, 13.445), pya.DPoint(37.8, 13.445), pya.DPoint(37.8, 12.745), pya.DPoint(0, 12.745)]))
cell_dac2u32out4in.shapes(layout.layer(8, 2)).insert(
    pya.DPolygon([pya.DPoint(0.9, 6.31), pya.DPoint(0.9, 11.24), pya.DPoint(36.9, 11.24), pya.DPoint(36.9, 6.31), pya.DPoint(0.9, 6.31)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(34.075, 25.9), pya.DPoint(34.075, 26.19), pya.DPoint(34.275, 26.19), pya.DPoint(34.275, 25.9), pya.DPoint(34.075, 25.9)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(34.075, 0), pya.DPoint(34.075, 0.29), pya.DPoint(34.275, 0.29), pya.DPoint(34.275, 0), pya.DPoint(34.075, 0)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(36.075, 25.9), pya.DPoint(36.075, 26.19), pya.DPoint(36.275, 26.19), pya.DPoint(36.275, 25.9), pya.DPoint(36.075, 25.9)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(35.525, 25.9), pya.DPoint(35.525, 26.19), pya.DPoint(35.725, 26.19), pya.DPoint(35.725, 25.9), pya.DPoint(35.525, 25.9)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(2.075, 25.9), pya.DPoint(2.075, 26.19), pya.DPoint(2.275, 26.19), pya.DPoint(2.275, 25.9), pya.DPoint(2.075, 25.9)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(3.525, 25.9), pya.DPoint(3.525, 26.19), pya.DPoint(3.725, 26.19), pya.DPoint(3.725, 25.9), pya.DPoint(3.525, 25.9)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(4.075, 25.9), pya.DPoint(4.075, 26.19), pya.DPoint(4.275, 26.19), pya.DPoint(4.275, 25.9), pya.DPoint(4.075, 25.9)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(5.525, 25.9), pya.DPoint(5.525, 26.19), pya.DPoint(5.725, 26.19), pya.DPoint(5.725, 25.9), pya.DPoint(5.525, 25.9)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(6.075, 25.9), pya.DPoint(6.075, 26.19), pya.DPoint(6.275, 26.19), pya.DPoint(6.275, 25.9), pya.DPoint(6.075, 25.9)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(7.525, 25.9), pya.DPoint(7.525, 26.19), pya.DPoint(7.725, 26.19), pya.DPoint(7.725, 25.9), pya.DPoint(7.525, 25.9)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(8.075, 25.9), pya.DPoint(8.075, 26.19), pya.DPoint(8.275, 26.19), pya.DPoint(8.275, 25.9), pya.DPoint(8.075, 25.9)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(9.525, 25.9), pya.DPoint(9.525, 26.19), pya.DPoint(9.725, 26.19), pya.DPoint(9.725, 25.9), pya.DPoint(9.525, 25.9)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(10.075, 25.9), pya.DPoint(10.075, 26.19), pya.DPoint(10.275, 26.19), pya.DPoint(10.275, 25.9), pya.DPoint(10.075, 25.9)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(11.525, 25.9), pya.DPoint(11.525, 26.19), pya.DPoint(11.725, 26.19), pya.DPoint(11.725, 25.9), pya.DPoint(11.525, 25.9)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(12.075, 25.9), pya.DPoint(12.075, 26.19), pya.DPoint(12.275, 26.19), pya.DPoint(12.275, 25.9), pya.DPoint(12.075, 25.9)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(13.525, 25.9), pya.DPoint(13.525, 26.19), pya.DPoint(13.725, 26.19), pya.DPoint(13.725, 25.9), pya.DPoint(13.525, 25.9)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(14.075, 25.9), pya.DPoint(14.075, 26.19), pya.DPoint(14.275, 26.19), pya.DPoint(14.275, 25.9), pya.DPoint(14.075, 25.9)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(15.525, 25.9), pya.DPoint(15.525, 26.19), pya.DPoint(15.725, 26.19), pya.DPoint(15.725, 25.9), pya.DPoint(15.525, 25.9)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(16.075, 25.9), pya.DPoint(16.075, 26.19), pya.DPoint(16.275, 26.19), pya.DPoint(16.275, 25.9), pya.DPoint(16.075, 25.9)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(17.525, 25.9), pya.DPoint(17.525, 26.19), pya.DPoint(17.725, 26.19), pya.DPoint(17.725, 25.9), pya.DPoint(17.525, 25.9)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(18.075, 25.9), pya.DPoint(18.075, 26.19), pya.DPoint(18.275, 26.19), pya.DPoint(18.275, 25.9), pya.DPoint(18.075, 25.9)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(19.525, 25.9), pya.DPoint(19.525, 26.19), pya.DPoint(19.725, 26.19), pya.DPoint(19.725, 25.9), pya.DPoint(19.525, 25.9)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(20.075, 25.9), pya.DPoint(20.075, 26.19), pya.DPoint(20.275, 26.19), pya.DPoint(20.275, 25.9), pya.DPoint(20.075, 25.9)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(21.525, 25.9), pya.DPoint(21.525, 26.19), pya.DPoint(21.725, 26.19), pya.DPoint(21.725, 25.9), pya.DPoint(21.525, 25.9)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(22.075, 25.9), pya.DPoint(22.075, 26.19), pya.DPoint(22.275, 26.19), pya.DPoint(22.275, 25.9), pya.DPoint(22.075, 25.9)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(23.525, 25.9), pya.DPoint(23.525, 26.19), pya.DPoint(23.725, 26.19), pya.DPoint(23.725, 25.9), pya.DPoint(23.525, 25.9)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(24.075, 25.9), pya.DPoint(24.075, 26.19), pya.DPoint(24.275, 26.19), pya.DPoint(24.275, 25.9), pya.DPoint(24.075, 25.9)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(25.525, 25.9), pya.DPoint(25.525, 26.19), pya.DPoint(25.725, 26.19), pya.DPoint(25.725, 25.9), pya.DPoint(25.525, 25.9)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(26.075, 25.9), pya.DPoint(26.075, 26.19), pya.DPoint(26.275, 26.19), pya.DPoint(26.275, 25.9), pya.DPoint(26.075, 25.9)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(27.525, 25.9), pya.DPoint(27.525, 26.19), pya.DPoint(27.725, 26.19), pya.DPoint(27.725, 25.9), pya.DPoint(27.525, 25.9)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(28.075, 25.9), pya.DPoint(28.075, 26.19), pya.DPoint(28.275, 26.19), pya.DPoint(28.275, 25.9), pya.DPoint(28.075, 25.9)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(29.525, 25.9), pya.DPoint(29.525, 26.19), pya.DPoint(29.725, 26.19), pya.DPoint(29.725, 25.9), pya.DPoint(29.525, 25.9)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(30.075, 25.9), pya.DPoint(30.075, 26.19), pya.DPoint(30.275, 26.19), pya.DPoint(30.275, 25.9), pya.DPoint(30.075, 25.9)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(31.525, 25.9), pya.DPoint(31.525, 26.19), pya.DPoint(31.725, 26.19), pya.DPoint(31.725, 25.9), pya.DPoint(31.525, 25.9)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(32.075, 25.9), pya.DPoint(32.075, 26.19), pya.DPoint(32.275, 26.19), pya.DPoint(32.275, 25.9), pya.DPoint(32.075, 25.9)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(33.525, 25.9), pya.DPoint(33.525, 26.19), pya.DPoint(33.725, 26.19), pya.DPoint(33.725, 25.9), pya.DPoint(33.525, 25.9)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(1.525, 25.9), pya.DPoint(1.525, 26.19), pya.DPoint(1.725, 26.19), pya.DPoint(1.725, 25.9), pya.DPoint(1.525, 25.9)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(8.075, 0), pya.DPoint(8.075, 0.29), pya.DPoint(8.275, 0.29), pya.DPoint(8.275, 0), pya.DPoint(8.075, 0)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(4.075, 0), pya.DPoint(4.075, 0.29), pya.DPoint(4.275, 0.29), pya.DPoint(4.275, 0), pya.DPoint(4.075, 0)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(3.525, 0), pya.DPoint(3.525, 0.29), pya.DPoint(3.725, 0.29), pya.DPoint(3.725, 0), pya.DPoint(3.525, 0)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(7.525, 0), pya.DPoint(7.525, 0.29), pya.DPoint(7.725, 0.29), pya.DPoint(7.725, 0), pya.DPoint(7.525, 0)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(6.075, 0), pya.DPoint(6.075, 0.29), pya.DPoint(6.275, 0.29), pya.DPoint(6.275, 0), pya.DPoint(6.075, 0)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(2.075, 0), pya.DPoint(2.075, 0.29), pya.DPoint(2.275, 0.29), pya.DPoint(2.275, 0), pya.DPoint(2.075, 0)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(1.525, 0), pya.DPoint(1.525, 0.29), pya.DPoint(1.725, 0.29), pya.DPoint(1.725, 0), pya.DPoint(1.525, 0)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(5.525, 0), pya.DPoint(5.525, 0.29), pya.DPoint(5.725, 0.29), pya.DPoint(5.725, 0), pya.DPoint(5.525, 0)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(33.525, 0), pya.DPoint(33.525, 0.29), pya.DPoint(33.725, 0.29), pya.DPoint(33.725, 0), pya.DPoint(33.525, 0)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(32.075, 0), pya.DPoint(32.075, 0.29), pya.DPoint(32.275, 0.29), pya.DPoint(32.275, 0), pya.DPoint(32.075, 0)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(31.525, 0), pya.DPoint(31.525, 0.29), pya.DPoint(31.725, 0.29), pya.DPoint(31.725, 0), pya.DPoint(31.525, 0)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(30.075, 0), pya.DPoint(30.075, 0.29), pya.DPoint(30.275, 0.29), pya.DPoint(30.275, 0), pya.DPoint(30.075, 0)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(29.525, 0), pya.DPoint(29.525, 0.29), pya.DPoint(29.725, 0.29), pya.DPoint(29.725, 0), pya.DPoint(29.525, 0)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(28.075, 0), pya.DPoint(28.075, 0.29), pya.DPoint(28.275, 0.29), pya.DPoint(28.275, 0), pya.DPoint(28.075, 0)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(27.525, 0), pya.DPoint(27.525, 0.29), pya.DPoint(27.725, 0.29), pya.DPoint(27.725, 0), pya.DPoint(27.525, 0)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(26.075, 0), pya.DPoint(26.075, 0.29), pya.DPoint(26.275, 0.29), pya.DPoint(26.275, 0), pya.DPoint(26.075, 0)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(25.525, 0), pya.DPoint(25.525, 0.29), pya.DPoint(25.725, 0.29), pya.DPoint(25.725, 0), pya.DPoint(25.525, 0)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(24.075, 0), pya.DPoint(24.075, 0.29), pya.DPoint(24.275, 0.29), pya.DPoint(24.275, 0), pya.DPoint(24.075, 0)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(23.525, 0), pya.DPoint(23.525, 0.29), pya.DPoint(23.725, 0.29), pya.DPoint(23.725, 0), pya.DPoint(23.525, 0)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(22.075, 0), pya.DPoint(22.075, 0.29), pya.DPoint(22.275, 0.29), pya.DPoint(22.275, 0), pya.DPoint(22.075, 0)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(21.525, 0), pya.DPoint(21.525, 0.29), pya.DPoint(21.725, 0.29), pya.DPoint(21.725, 0), pya.DPoint(21.525, 0)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(20.075, 0), pya.DPoint(20.075, 0.29), pya.DPoint(20.275, 0.29), pya.DPoint(20.275, 0), pya.DPoint(20.075, 0)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(19.525, 0), pya.DPoint(19.525, 0.29), pya.DPoint(19.725, 0.29), pya.DPoint(19.725, 0), pya.DPoint(19.525, 0)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(18.075, 0), pya.DPoint(18.075, 0.29), pya.DPoint(18.275, 0.29), pya.DPoint(18.275, 0), pya.DPoint(18.075, 0)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(17.525, 0), pya.DPoint(17.525, 0.29), pya.DPoint(17.725, 0.29), pya.DPoint(17.725, 0), pya.DPoint(17.525, 0)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(16.075, 0), pya.DPoint(16.075, 0.29), pya.DPoint(16.275, 0.29), pya.DPoint(16.275, 0), pya.DPoint(16.075, 0)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(15.525, 0), pya.DPoint(15.525, 0.29), pya.DPoint(15.725, 0.29), pya.DPoint(15.725, 0), pya.DPoint(15.525, 0)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(14.075, 0), pya.DPoint(14.075, 0.29), pya.DPoint(14.275, 0.29), pya.DPoint(14.275, 0), pya.DPoint(14.075, 0)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(13.525, 0), pya.DPoint(13.525, 0.29), pya.DPoint(13.725, 0.29), pya.DPoint(13.725, 0), pya.DPoint(13.525, 0)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(12.075, 0), pya.DPoint(12.075, 0.29), pya.DPoint(12.275, 0.29), pya.DPoint(12.275, 0), pya.DPoint(12.075, 0)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(11.525, 0), pya.DPoint(11.525, 0.29), pya.DPoint(11.725, 0.29), pya.DPoint(11.725, 0), pya.DPoint(11.525, 0)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(10.075, 0), pya.DPoint(10.075, 0.29), pya.DPoint(10.275, 0.29), pya.DPoint(10.275, 0), pya.DPoint(10.075, 0)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(9.525, 0), pya.DPoint(9.525, 0.29), pya.DPoint(9.725, 0.29), pya.DPoint(9.725, 0), pya.DPoint(9.525, 0)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(36.075, 0), pya.DPoint(36.075, 0.29), pya.DPoint(36.275, 0.29), pya.DPoint(36.275, 0), pya.DPoint(36.075, 0)]))
cell_dac2u32out4in.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(35.525, 0), pya.DPoint(35.525, 0.29), pya.DPoint(35.725, 0.29), pya.DPoint(35.725, 0), pya.DPoint(35.525, 0)]))
cell_dac2u32out4in.shapes(layout.layer(30, 2)).insert(
    pya.DPolygon([pya.DPoint(0, 20.93), pya.DPoint(0, 21.63), pya.DPoint(37.8, 21.63), pya.DPoint(37.8, 20.93), pya.DPoint(0, 20.93)]))
cell_dac2u32out4in.shapes(layout.layer(30, 2)).insert(
    pya.DPolygon([pya.DPoint(0, 4.56), pya.DPoint(0, 5.26), pya.DPoint(37.8, 5.26), pya.DPoint(37.8, 4.56), pya.DPoint(0, 4.56)]))
cell_dac2u32out4in.shapes(layout.layer(30, 2)).insert(
    pya.DPolygon([pya.DPoint(0, 22.03), pya.DPoint(0, 23.76), pya.DPoint(37.8, 23.76), pya.DPoint(37.8, 22.03), pya.DPoint(0, 22.03)]))
cell_dac2u32out4in.shapes(layout.layer(30, 2)).insert(
    pya.DPolygon([pya.DPoint(0, 5.66), pya.DPoint(0, 7.39), pya.DPoint(37.8, 7.39), pya.DPoint(37.8, 5.66), pya.DPoint(0, 5.66)]))
cell_dac2u32out4in.shapes(layout.layer(30, 2)).insert(
    pya.DPolygon([pya.DPoint(0, 2.43), pya.DPoint(0, 4.16), pya.DPoint(37.8, 4.16), pya.DPoint(37.8, 2.43), pya.DPoint(0, 2.43)]))
cell_dac2u32out4in.shapes(layout.layer(30, 2)).insert(
    pya.DPolygon([pya.DPoint(0, 18.8), pya.DPoint(0, 20.53), pya.DPoint(37.8, 20.53), pya.DPoint(37.8, 18.8), pya.DPoint(0, 18.8)]))
cell_dac2u32out4in.shapes(layout.layer(30, 2)).insert(
    pya.DPolygon([pya.DPoint(0, 0), pya.DPoint(0, 1.73), pya.DPoint(37.8, 1.73), pya.DPoint(37.8, 0), pya.DPoint(0, 0)]))
cell_dac2u32out4in.shapes(layout.layer(30, 2)).insert(
    pya.DPolygon([pya.DPoint(0, 24.46), pya.DPoint(0, 26.19), pya.DPoint(37.8, 26.19), pya.DPoint(37.8, 24.46), pya.DPoint(0, 24.46)]))
cell_dac2u32out4in.shapes(layout.layer(8, 25)).insert(
    pya.DText("VbiasP[1]",
              pya.DTrans(2, False, pya.DVector(18.9, 17.415))))
cell_dac2u32out4in.shapes(layout.layer(8, 25)).insert(
    pya.DText("Iout",
              pya.DTrans(2, False, pya.DVector(18.9, 13.095))))
cell_dac2u32out4in.shapes(layout.layer(8, 25)).insert(
    pya.DText("VbiasP[0]",
              pya.DTrans(0, False, pya.DVector(18.9, 8.775))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("EN[1]",
              pya.DTrans(0, False, pya.DVector(35.625, 0.145))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ENB[1]",
              pya.DTrans(0, False, pya.DVector(36.175, 0.145))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("EN[2]",
              pya.DTrans(0, False, pya.DVector(36.175, 26.045))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ENB[2]",
              pya.DTrans(0, False, pya.DVector(35.625, 26.045))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[16]",
              pya.DTrans(0, False, pya.DVector(34.175, 26.045))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[16]",
              pya.DTrans(0, False, pya.DVector(33.625, 26.045))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[17]",
              pya.DTrans(0, False, pya.DVector(32.175, 26.045))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[17]",
              pya.DTrans(0, False, pya.DVector(31.625, 26.045))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[18]",
              pya.DTrans(0, False, pya.DVector(30.175, 26.045))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[18]",
              pya.DTrans(0, False, pya.DVector(29.625, 26.045))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[19]",
              pya.DTrans(0, False, pya.DVector(28.175, 26.045))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[19]",
              pya.DTrans(0, False, pya.DVector(27.625, 26.045))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[20]",
              pya.DTrans(0, False, pya.DVector(26.175, 26.045))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[20]",
              pya.DTrans(0, False, pya.DVector(25.625, 26.045))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[21]",
              pya.DTrans(0, False, pya.DVector(24.175, 26.045))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[21]",
              pya.DTrans(0, False, pya.DVector(23.625, 26.045))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[22]",
              pya.DTrans(0, False, pya.DVector(22.175, 26.045))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[22]",
              pya.DTrans(0, False, pya.DVector(21.625, 26.045))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[23]",
              pya.DTrans(0, False, pya.DVector(20.175, 26.045))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[23]",
              pya.DTrans(0, False, pya.DVector(19.625, 26.045))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[24]",
              pya.DTrans(0, False, pya.DVector(18.175, 26.045))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[24]",
              pya.DTrans(0, False, pya.DVector(17.625, 26.045))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[25]",
              pya.DTrans(0, False, pya.DVector(16.175, 26.045))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[25]",
              pya.DTrans(0, False, pya.DVector(15.625, 26.045))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[26]",
              pya.DTrans(0, False, pya.DVector(14.175, 26.045))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[26]",
              pya.DTrans(0, False, pya.DVector(13.625, 26.045))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[27]",
              pya.DTrans(0, False, pya.DVector(12.175, 26.045))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[27]",
              pya.DTrans(0, False, pya.DVector(11.625, 26.045))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[28]",
              pya.DTrans(0, False, pya.DVector(10.175, 26.045))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[28]",
              pya.DTrans(0, False, pya.DVector(9.625, 26.045))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[29]",
              pya.DTrans(0, False, pya.DVector(8.175, 26.045))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[29]",
              pya.DTrans(0, False, pya.DVector(7.625, 26.045))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[30]",
              pya.DTrans(0, False, pya.DVector(6.175, 26.045))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[30]",
              pya.DTrans(0, False, pya.DVector(5.625, 26.045))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[31]",
              pya.DTrans(0, False, pya.DVector(4.175, 26.045))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[31]",
              pya.DTrans(0, False, pya.DVector(3.625, 26.045))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("EN[3]",
              pya.DTrans(0, False, pya.DVector(2.175, 26.045))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ENB[3]",
              pya.DTrans(0, False, pya.DVector(1.625, 26.045))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[0]",
              pya.DTrans(0, False, pya.DVector(3.625, 0.145))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[0]",
              pya.DTrans(0, False, pya.DVector(4.175, 0.145))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[1]",
              pya.DTrans(0, False, pya.DVector(5.625, 0.145))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[1]",
              pya.DTrans(0, False, pya.DVector(6.175, 0.145))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[2]",
              pya.DTrans(0, False, pya.DVector(7.625, 0.145))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[2]",
              pya.DTrans(0, False, pya.DVector(8.175, 0.145))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[3]",
              pya.DTrans(0, False, pya.DVector(9.625, 0.145))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[3]",
              pya.DTrans(0, False, pya.DVector(10.175, 0.145))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[4]",
              pya.DTrans(0, False, pya.DVector(11.625, 0.145))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[4]",
              pya.DTrans(0, False, pya.DVector(12.175, 0.145))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[5]",
              pya.DTrans(0, False, pya.DVector(13.625, 0.145))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[5]",
              pya.DTrans(0, False, pya.DVector(14.175, 0.145))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[6]",
              pya.DTrans(0, False, pya.DVector(15.625, 0.145))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("EN[0]",
              pya.DTrans(0, False, pya.DVector(1.625, 0.145))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ENB[0]",
              pya.DTrans(0, False, pya.DVector(2.175, 0.145))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[6]",
              pya.DTrans(0, False, pya.DVector(16.175, 0.145))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[7]",
              pya.DTrans(0, False, pya.DVector(17.625, 0.145))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[7]",
              pya.DTrans(0, False, pya.DVector(18.175, 0.145))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[8]",
              pya.DTrans(0, False, pya.DVector(19.625, 0.145))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[8]",
              pya.DTrans(0, False, pya.DVector(20.175, 0.145))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[9]",
              pya.DTrans(0, False, pya.DVector(21.625, 0.145))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[9]",
              pya.DTrans(0, False, pya.DVector(22.175, 0.145))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[10]",
              pya.DTrans(0, False, pya.DVector(23.625, 0.145))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[10]",
              pya.DTrans(0, False, pya.DVector(24.175, 0.145))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[11]",
              pya.DTrans(0, False, pya.DVector(25.625, 0.145))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[11]",
              pya.DTrans(0, False, pya.DVector(26.175, 0.145))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[12]",
              pya.DTrans(0, False, pya.DVector(27.625, 0.145))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[12]",
              pya.DTrans(0, False, pya.DVector(28.175, 0.145))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[13]",
              pya.DTrans(0, False, pya.DVector(29.625, 0.145))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[13]",
              pya.DTrans(0, False, pya.DVector(30.175, 0.145))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[14]",
              pya.DTrans(0, False, pya.DVector(31.625, 0.145))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[14]",
              pya.DTrans(0, False, pya.DVector(32.175, 0.145))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[15]",
              pya.DTrans(0, False, pya.DVector(33.625, 0.145))))
cell_dac2u32out4in.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[15]",
              pya.DTrans(0, False, pya.DVector(34.175, 0.145))))
cell_dac2u32out4in.shapes(layout.layer(30, 25)).insert(
    pya.DText("VcascP[0]",
              pya.DTrans(0, False, pya.DVector(18.9, 4.91))))
cell_dac2u32out4in.shapes(layout.layer(30, 25)).insert(
    pya.DText("VSS",
              pya.DTrans(0, False, pya.DVector(18.9, 0.865))))
cell_dac2u32out4in.shapes(layout.layer(30, 25)).insert(
    pya.DText("VSS",
              pya.DTrans(2, False, pya.DVector(18.9, 25.325))))
cell_dac2u32out4in.shapes(layout.layer(30, 25)).insert(
    pya.DText("VDD",
              pya.DTrans(0, False, pya.DVector(18.9, 3.295))))
cell_dac2u32out4in.shapes(layout.layer(30, 25)).insert(
    pya.DText("VDD",
              pya.DTrans(0, False, pya.DVector(18.9, 6.525))))
cell_dac2u32out4in.shapes(layout.layer(30, 25)).insert(
    pya.DText("VDD",
              pya.DTrans(2, False, pya.DVector(18.9, 22.895))))
cell_dac2u32out4in.shapes(layout.layer(30, 25)).insert(
    pya.DText("VDD",
              pya.DTrans(2, False, pya.DVector(18.9, 19.665))))
cell_dac2u32out4in.shapes(layout.layer(30, 25)).insert(
    pya.DText("VcascP[1]",
              pya.DTrans(2, False, pya.DVector(18.9, 21.28))))

# === dac128module_vdd_strap ===
cell_dac128module_vdd_strap.insert(pya.DCellInstArray(
    cell_via_stack.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(1.825, 22.895))))
cell_dac128module_vdd_strap.insert(pya.DCellInstArray(
    cell_via_stack.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(1.825, 3.295))))
cell_dac128module_vdd_strap.insert(pya.DCellInstArray(
    cell_via_stack.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(1.825, 6.525))))
cell_dac128module_vdd_strap.insert(pya.DCellInstArray(
    cell_via_stack.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(1.825, 19.665))))
cell_dac128module_vdd_strap.insert(pya.DCellInstArray(
    cell_via_stack_4.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(1.825, 5.905))))
_path = pya.DPath([pya.DPoint(1.825, 26.19), pya.DPoint(1.825, 0)], 3.65)
cell_dac128module_vdd_strap.shapes(layout.layer(50, 0)).insert(_path)

# === dac128module_vss_strap ===
cell_dac128module_vss_strap.insert(pya.DCellInstArray(
    cell_via_stack.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(1.825, 25.325))))
cell_dac128module_vss_strap.insert(pya.DCellInstArray(
    cell_via_stack.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(1.825, 0.865))))
cell_dac128module_vss_strap.insert(pya.DCellInstArray(
    cell_via_stack_4.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(1.825, 20.285))))
_path = pya.DPath([pya.DPoint(1.825, 26.19), pya.DPoint(1.825, 0)], 3.65)
cell_dac128module_vss_strap.shapes(layout.layer(50, 0)).insert(_path)

# === dac128module_analog_straps ===
cell_dac128module_analog_straps.insert(pya.DCellInstArray(
    cell_via_stack_7.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(0, 0))))
cell_dac128module_analog_straps.insert(pya.DCellInstArray(
    cell_via_stack_7.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(-1.775, 1.3))))
cell_dac128module_analog_straps.insert(pya.DCellInstArray(
    cell_via_stack_7.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(-1.33, -1.3))))
_path = pya.DPath([pya.DPoint(-2.125, 1.3), pya.DPoint(0.35, 1.3)], 0.7)
cell_dac128module_analog_straps.shapes(layout.layer(30, 0)).insert(_path)
_path = pya.DPath([pya.DPoint(-1.68, -1.3), pya.DPoint(0.35, -1.3)], 0.7)
cell_dac128module_analog_straps.shapes(layout.layer(30, 0)).insert(_path)

# === dac32module ===
cell_dac32module.insert(pya.DCellInstArray(
    cell_dac2u32out4in.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(0, 0))))
cell_dac32module.insert(pya.DCellInstArray(
    cell_dac128module_vss_strap.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(0, 0)),
    pya.DVector(24, 0),
    pya.DVector(0, 0),
    2, 1))
cell_dac32module.insert(pya.DCellInstArray(
    cell_dac128module_vdd_strap.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(10.15, 0)),
    pya.DVector(24, 0),
    pya.DVector(0, 0),
    2, 1))
cell_dac32module.insert(pya.DCellInstArray(
    cell_dac128module_analog_straps.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(37.45, 13.095))))
cell_dac32module.shapes(layout.layer(189, 4)).insert(
    pya.DPolygon([pya.DPoint(0, -0.07), pya.DPoint(0, 26.26), pya.DPoint(37.8, 26.26), pya.DPoint(37.8, -0.07), pya.DPoint(0, -0.07)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(34.075, 0), pya.DPoint(34.075, 0.29), pya.DPoint(34.275, 0.29), pya.DPoint(34.275, 0), pya.DPoint(34.075, 0)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(34.075, 25.9), pya.DPoint(34.075, 26.19), pya.DPoint(34.275, 26.19), pya.DPoint(34.275, 25.9), pya.DPoint(34.075, 25.9)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(36.075, 25.9), pya.DPoint(36.075, 26.19), pya.DPoint(36.275, 26.19), pya.DPoint(36.275, 25.9), pya.DPoint(36.075, 25.9)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(35.525, 25.9), pya.DPoint(35.525, 26.19), pya.DPoint(35.725, 26.19), pya.DPoint(35.725, 25.9), pya.DPoint(35.525, 25.9)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(31.525, 25.9), pya.DPoint(31.525, 26.19), pya.DPoint(31.725, 26.19), pya.DPoint(31.725, 25.9), pya.DPoint(31.525, 25.9)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(30.075, 25.9), pya.DPoint(30.075, 26.19), pya.DPoint(30.275, 26.19), pya.DPoint(30.275, 25.9), pya.DPoint(30.075, 25.9)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(29.525, 25.9), pya.DPoint(29.525, 26.19), pya.DPoint(29.725, 26.19), pya.DPoint(29.725, 25.9), pya.DPoint(29.525, 25.9)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(28.075, 25.9), pya.DPoint(28.075, 26.19), pya.DPoint(28.275, 26.19), pya.DPoint(28.275, 25.9), pya.DPoint(28.075, 25.9)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(27.525, 25.9), pya.DPoint(27.525, 26.19), pya.DPoint(27.725, 26.19), pya.DPoint(27.725, 25.9), pya.DPoint(27.525, 25.9)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(26.075, 25.9), pya.DPoint(26.075, 26.19), pya.DPoint(26.275, 26.19), pya.DPoint(26.275, 25.9), pya.DPoint(26.075, 25.9)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(25.525, 25.9), pya.DPoint(25.525, 26.19), pya.DPoint(25.725, 26.19), pya.DPoint(25.725, 25.9), pya.DPoint(25.525, 25.9)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(24.075, 25.9), pya.DPoint(24.075, 26.19), pya.DPoint(24.275, 26.19), pya.DPoint(24.275, 25.9), pya.DPoint(24.075, 25.9)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(23.525, 25.9), pya.DPoint(23.525, 26.19), pya.DPoint(23.725, 26.19), pya.DPoint(23.725, 25.9), pya.DPoint(23.525, 25.9)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(22.075, 25.9), pya.DPoint(22.075, 26.19), pya.DPoint(22.275, 26.19), pya.DPoint(22.275, 25.9), pya.DPoint(22.075, 25.9)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(21.525, 25.9), pya.DPoint(21.525, 26.19), pya.DPoint(21.725, 26.19), pya.DPoint(21.725, 25.9), pya.DPoint(21.525, 25.9)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(20.075, 25.9), pya.DPoint(20.075, 26.19), pya.DPoint(20.275, 26.19), pya.DPoint(20.275, 25.9), pya.DPoint(20.075, 25.9)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(19.525, 25.9), pya.DPoint(19.525, 26.19), pya.DPoint(19.725, 26.19), pya.DPoint(19.725, 25.9), pya.DPoint(19.525, 25.9)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(18.075, 25.9), pya.DPoint(18.075, 26.19), pya.DPoint(18.275, 26.19), pya.DPoint(18.275, 25.9), pya.DPoint(18.075, 25.9)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(17.525, 25.9), pya.DPoint(17.525, 26.19), pya.DPoint(17.725, 26.19), pya.DPoint(17.725, 25.9), pya.DPoint(17.525, 25.9)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(16.075, 25.9), pya.DPoint(16.075, 26.19), pya.DPoint(16.275, 26.19), pya.DPoint(16.275, 25.9), pya.DPoint(16.075, 25.9)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(15.525, 25.9), pya.DPoint(15.525, 26.19), pya.DPoint(15.725, 26.19), pya.DPoint(15.725, 25.9), pya.DPoint(15.525, 25.9)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(14.075, 25.9), pya.DPoint(14.075, 26.19), pya.DPoint(14.275, 26.19), pya.DPoint(14.275, 25.9), pya.DPoint(14.075, 25.9)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(13.525, 25.9), pya.DPoint(13.525, 26.19), pya.DPoint(13.725, 26.19), pya.DPoint(13.725, 25.9), pya.DPoint(13.525, 25.9)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(12.075, 25.9), pya.DPoint(12.075, 26.19), pya.DPoint(12.275, 26.19), pya.DPoint(12.275, 25.9), pya.DPoint(12.075, 25.9)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(11.525, 25.9), pya.DPoint(11.525, 26.19), pya.DPoint(11.725, 26.19), pya.DPoint(11.725, 25.9), pya.DPoint(11.525, 25.9)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(10.075, 25.9), pya.DPoint(10.075, 26.19), pya.DPoint(10.275, 26.19), pya.DPoint(10.275, 25.9), pya.DPoint(10.075, 25.9)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(9.525, 25.9), pya.DPoint(9.525, 26.19), pya.DPoint(9.725, 26.19), pya.DPoint(9.725, 25.9), pya.DPoint(9.525, 25.9)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(8.075, 25.9), pya.DPoint(8.075, 26.19), pya.DPoint(8.275, 26.19), pya.DPoint(8.275, 25.9), pya.DPoint(8.075, 25.9)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(7.525, 25.9), pya.DPoint(7.525, 26.19), pya.DPoint(7.725, 26.19), pya.DPoint(7.725, 25.9), pya.DPoint(7.525, 25.9)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(6.075, 25.9), pya.DPoint(6.075, 26.19), pya.DPoint(6.275, 26.19), pya.DPoint(6.275, 25.9), pya.DPoint(6.075, 25.9)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(5.525, 25.9), pya.DPoint(5.525, 26.19), pya.DPoint(5.725, 26.19), pya.DPoint(5.725, 25.9), pya.DPoint(5.525, 25.9)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(4.075, 25.9), pya.DPoint(4.075, 26.19), pya.DPoint(4.275, 26.19), pya.DPoint(4.275, 25.9), pya.DPoint(4.075, 25.9)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(3.525, 25.9), pya.DPoint(3.525, 26.19), pya.DPoint(3.725, 26.19), pya.DPoint(3.725, 25.9), pya.DPoint(3.525, 25.9)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(2.075, 25.9), pya.DPoint(2.075, 26.19), pya.DPoint(2.275, 26.19), pya.DPoint(2.275, 25.9), pya.DPoint(2.075, 25.9)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(1.525, 25.9), pya.DPoint(1.525, 26.19), pya.DPoint(1.725, 26.19), pya.DPoint(1.725, 25.9), pya.DPoint(1.525, 25.9)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(33.525, 25.9), pya.DPoint(33.525, 26.19), pya.DPoint(33.725, 26.19), pya.DPoint(33.725, 25.9), pya.DPoint(33.525, 25.9)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(32.075, 25.9), pya.DPoint(32.075, 26.19), pya.DPoint(32.275, 26.19), pya.DPoint(32.275, 25.9), pya.DPoint(32.075, 25.9)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(12.075, 0), pya.DPoint(12.075, 0.29), pya.DPoint(12.275, 0.29), pya.DPoint(12.275, 0), pya.DPoint(12.075, 0)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(13.525, 0), pya.DPoint(13.525, 0.29), pya.DPoint(13.725, 0.29), pya.DPoint(13.725, 0), pya.DPoint(13.525, 0)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(14.075, 0), pya.DPoint(14.075, 0.29), pya.DPoint(14.275, 0.29), pya.DPoint(14.275, 0), pya.DPoint(14.075, 0)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(15.525, 0), pya.DPoint(15.525, 0.29), pya.DPoint(15.725, 0.29), pya.DPoint(15.725, 0), pya.DPoint(15.525, 0)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(16.075, 0), pya.DPoint(16.075, 0.29), pya.DPoint(16.275, 0.29), pya.DPoint(16.275, 0), pya.DPoint(16.075, 0)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(17.525, 0), pya.DPoint(17.525, 0.29), pya.DPoint(17.725, 0.29), pya.DPoint(17.725, 0), pya.DPoint(17.525, 0)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(18.075, 0), pya.DPoint(18.075, 0.29), pya.DPoint(18.275, 0.29), pya.DPoint(18.275, 0), pya.DPoint(18.075, 0)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(19.525, 0), pya.DPoint(19.525, 0.29), pya.DPoint(19.725, 0.29), pya.DPoint(19.725, 0), pya.DPoint(19.525, 0)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(20.075, 0), pya.DPoint(20.075, 0.29), pya.DPoint(20.275, 0.29), pya.DPoint(20.275, 0), pya.DPoint(20.075, 0)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(21.525, 0), pya.DPoint(21.525, 0.29), pya.DPoint(21.725, 0.29), pya.DPoint(21.725, 0), pya.DPoint(21.525, 0)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(22.075, 0), pya.DPoint(22.075, 0.29), pya.DPoint(22.275, 0.29), pya.DPoint(22.275, 0), pya.DPoint(22.075, 0)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(23.525, 0), pya.DPoint(23.525, 0.29), pya.DPoint(23.725, 0.29), pya.DPoint(23.725, 0), pya.DPoint(23.525, 0)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(24.075, 0), pya.DPoint(24.075, 0.29), pya.DPoint(24.275, 0.29), pya.DPoint(24.275, 0), pya.DPoint(24.075, 0)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(25.525, 0), pya.DPoint(25.525, 0.29), pya.DPoint(25.725, 0.29), pya.DPoint(25.725, 0), pya.DPoint(25.525, 0)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(26.075, 0), pya.DPoint(26.075, 0.29), pya.DPoint(26.275, 0.29), pya.DPoint(26.275, 0), pya.DPoint(26.075, 0)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(27.525, 0), pya.DPoint(27.525, 0.29), pya.DPoint(27.725, 0.29), pya.DPoint(27.725, 0), pya.DPoint(27.525, 0)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(28.075, 0), pya.DPoint(28.075, 0.29), pya.DPoint(28.275, 0.29), pya.DPoint(28.275, 0), pya.DPoint(28.075, 0)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(29.525, 0), pya.DPoint(29.525, 0.29), pya.DPoint(29.725, 0.29), pya.DPoint(29.725, 0), pya.DPoint(29.525, 0)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(30.075, 0), pya.DPoint(30.075, 0.29), pya.DPoint(30.275, 0.29), pya.DPoint(30.275, 0), pya.DPoint(30.075, 0)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(31.525, 0), pya.DPoint(31.525, 0.29), pya.DPoint(31.725, 0.29), pya.DPoint(31.725, 0), pya.DPoint(31.525, 0)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(32.075, 0), pya.DPoint(32.075, 0.29), pya.DPoint(32.275, 0.29), pya.DPoint(32.275, 0), pya.DPoint(32.075, 0)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(33.525, 0), pya.DPoint(33.525, 0.29), pya.DPoint(33.725, 0.29), pya.DPoint(33.725, 0), pya.DPoint(33.525, 0)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(5.525, 0), pya.DPoint(5.525, 0.29), pya.DPoint(5.725, 0.29), pya.DPoint(5.725, 0), pya.DPoint(5.525, 0)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(1.525, 0), pya.DPoint(1.525, 0.29), pya.DPoint(1.725, 0.29), pya.DPoint(1.725, 0), pya.DPoint(1.525, 0)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(2.075, 0), pya.DPoint(2.075, 0.29), pya.DPoint(2.275, 0.29), pya.DPoint(2.275, 0), pya.DPoint(2.075, 0)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(6.075, 0), pya.DPoint(6.075, 0.29), pya.DPoint(6.275, 0.29), pya.DPoint(6.275, 0), pya.DPoint(6.075, 0)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(7.525, 0), pya.DPoint(7.525, 0.29), pya.DPoint(7.725, 0.29), pya.DPoint(7.725, 0), pya.DPoint(7.525, 0)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(3.525, 0), pya.DPoint(3.525, 0.29), pya.DPoint(3.725, 0.29), pya.DPoint(3.725, 0), pya.DPoint(3.525, 0)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(4.075, 0), pya.DPoint(4.075, 0.29), pya.DPoint(4.275, 0.29), pya.DPoint(4.275, 0), pya.DPoint(4.075, 0)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(8.075, 0), pya.DPoint(8.075, 0.29), pya.DPoint(8.275, 0.29), pya.DPoint(8.275, 0), pya.DPoint(8.075, 0)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(9.525, 0), pya.DPoint(9.525, 0.29), pya.DPoint(9.725, 0.29), pya.DPoint(9.725, 0), pya.DPoint(9.525, 0)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(10.075, 0), pya.DPoint(10.075, 0.29), pya.DPoint(10.275, 0.29), pya.DPoint(10.275, 0), pya.DPoint(10.075, 0)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(11.525, 0), pya.DPoint(11.525, 0.29), pya.DPoint(11.725, 0.29), pya.DPoint(11.725, 0), pya.DPoint(11.525, 0)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(36.075, 0), pya.DPoint(36.075, 0.29), pya.DPoint(36.275, 0.29), pya.DPoint(36.275, 0), pya.DPoint(36.075, 0)]))
cell_dac32module.shapes(layout.layer(10, 2)).insert(
    pya.DPolygon([pya.DPoint(35.525, 0), pya.DPoint(35.525, 0.29), pya.DPoint(35.725, 0.29), pya.DPoint(35.725, 0), pya.DPoint(35.525, 0)]))
cell_dac32module.shapes(layout.layer(30, 2)).insert(
    pya.DPolygon([pya.DPoint(37.1, 12.745), pya.DPoint(37.1, 13.445), pya.DPoint(37.8, 13.445), pya.DPoint(37.8, 12.745), pya.DPoint(37.1, 12.745)]))
cell_dac32module.shapes(layout.layer(30, 2)).insert(
    pya.DPolygon([pya.DPoint(37.1, 11.445), pya.DPoint(37.1, 12.145), pya.DPoint(37.8, 12.145), pya.DPoint(37.8, 11.445), pya.DPoint(37.1, 11.445)]))
cell_dac32module.shapes(layout.layer(30, 2)).insert(
    pya.DPolygon([pya.DPoint(37.1, 14.045), pya.DPoint(37.1, 14.745), pya.DPoint(37.8, 14.745), pya.DPoint(37.8, 14.045), pya.DPoint(37.1, 14.045)]))
cell_dac32module.shapes(layout.layer(30, 2)).insert(
    pya.DPolygon([pya.DPoint(0, 4.56), pya.DPoint(0, 5.26), pya.DPoint(37.8, 5.26), pya.DPoint(37.8, 4.56), pya.DPoint(0, 4.56)]))
cell_dac32module.shapes(layout.layer(30, 2)).insert(
    pya.DPolygon([pya.DPoint(0, 20.93), pya.DPoint(0, 21.63), pya.DPoint(37.8, 21.63), pya.DPoint(37.8, 20.93), pya.DPoint(0, 20.93)]))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("EN[1]",
              pya.DTrans(0, False, pya.DVector(35.625, 0.145))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ENB[1]",
              pya.DTrans(0, False, pya.DVector(36.175, 0.145))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("EN[2]",
              pya.DTrans(0, False, pya.DVector(36.175, 26.045))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ENB[2]",
              pya.DTrans(0, False, pya.DVector(35.625, 26.045))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[16]",
              pya.DTrans(0, False, pya.DVector(34.175, 26.045))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[16]",
              pya.DTrans(0, False, pya.DVector(33.625, 26.045))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[17]",
              pya.DTrans(0, False, pya.DVector(32.175, 26.045))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[17]",
              pya.DTrans(0, False, pya.DVector(31.625, 26.045))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[18]",
              pya.DTrans(0, False, pya.DVector(30.175, 26.045))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[18]",
              pya.DTrans(0, False, pya.DVector(29.625, 26.045))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[19]",
              pya.DTrans(0, False, pya.DVector(28.175, 26.045))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[19]",
              pya.DTrans(0, False, pya.DVector(27.625, 26.045))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[20]",
              pya.DTrans(0, False, pya.DVector(26.175, 26.045))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[20]",
              pya.DTrans(0, False, pya.DVector(25.625, 26.045))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[21]",
              pya.DTrans(0, False, pya.DVector(24.175, 26.045))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[21]",
              pya.DTrans(0, False, pya.DVector(23.625, 26.045))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[22]",
              pya.DTrans(0, False, pya.DVector(22.175, 26.045))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[22]",
              pya.DTrans(0, False, pya.DVector(21.625, 26.045))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[23]",
              pya.DTrans(0, False, pya.DVector(20.175, 26.045))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[23]",
              pya.DTrans(0, False, pya.DVector(19.625, 26.045))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[24]",
              pya.DTrans(0, False, pya.DVector(18.175, 26.045))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[24]",
              pya.DTrans(0, False, pya.DVector(17.625, 26.045))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[25]",
              pya.DTrans(0, False, pya.DVector(16.175, 26.045))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[25]",
              pya.DTrans(0, False, pya.DVector(15.625, 26.045))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[26]",
              pya.DTrans(0, False, pya.DVector(14.175, 26.045))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[26]",
              pya.DTrans(0, False, pya.DVector(13.625, 26.045))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[27]",
              pya.DTrans(0, False, pya.DVector(12.175, 26.045))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[27]",
              pya.DTrans(0, False, pya.DVector(11.625, 26.045))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[28]",
              pya.DTrans(0, False, pya.DVector(10.175, 26.045))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[28]",
              pya.DTrans(0, False, pya.DVector(9.625, 26.045))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[29]",
              pya.DTrans(0, False, pya.DVector(8.175, 26.045))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[29]",
              pya.DTrans(0, False, pya.DVector(7.625, 26.045))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[30]",
              pya.DTrans(0, False, pya.DVector(6.175, 26.045))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[30]",
              pya.DTrans(0, False, pya.DVector(5.625, 26.045))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[31]",
              pya.DTrans(0, False, pya.DVector(4.175, 26.045))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[31]",
              pya.DTrans(0, False, pya.DVector(3.625, 26.045))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("EN[3]",
              pya.DTrans(0, False, pya.DVector(2.175, 26.045))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ENB[3]",
              pya.DTrans(0, False, pya.DVector(1.625, 26.045))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[0]",
              pya.DTrans(0, False, pya.DVector(3.625, 0.145))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[0]",
              pya.DTrans(0, False, pya.DVector(4.175, 0.145))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[1]",
              pya.DTrans(0, False, pya.DVector(5.625, 0.145))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[1]",
              pya.DTrans(0, False, pya.DVector(6.175, 0.145))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[2]",
              pya.DTrans(0, False, pya.DVector(7.625, 0.145))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[2]",
              pya.DTrans(0, False, pya.DVector(8.175, 0.145))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[3]",
              pya.DTrans(0, False, pya.DVector(9.625, 0.145))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[3]",
              pya.DTrans(0, False, pya.DVector(10.175, 0.145))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[4]",
              pya.DTrans(0, False, pya.DVector(11.625, 0.145))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[4]",
              pya.DTrans(0, False, pya.DVector(12.175, 0.145))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[5]",
              pya.DTrans(0, False, pya.DVector(13.625, 0.145))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[5]",
              pya.DTrans(0, False, pya.DVector(14.175, 0.145))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[6]",
              pya.DTrans(0, False, pya.DVector(15.625, 0.145))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("EN[0]",
              pya.DTrans(0, False, pya.DVector(1.625, 0.145))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ENB[0]",
              pya.DTrans(0, False, pya.DVector(2.175, 0.145))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[6]",
              pya.DTrans(0, False, pya.DVector(16.175, 0.145))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[7]",
              pya.DTrans(0, False, pya.DVector(17.625, 0.145))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[7]",
              pya.DTrans(0, False, pya.DVector(18.175, 0.145))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[8]",
              pya.DTrans(0, False, pya.DVector(19.625, 0.145))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[8]",
              pya.DTrans(0, False, pya.DVector(20.175, 0.145))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[9]",
              pya.DTrans(0, False, pya.DVector(21.625, 0.145))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[9]",
              pya.DTrans(0, False, pya.DVector(22.175, 0.145))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[10]",
              pya.DTrans(0, False, pya.DVector(23.625, 0.145))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[10]",
              pya.DTrans(0, False, pya.DVector(24.175, 0.145))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[11]",
              pya.DTrans(0, False, pya.DVector(25.625, 0.145))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[11]",
              pya.DTrans(0, False, pya.DVector(26.175, 0.145))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[12]",
              pya.DTrans(0, False, pya.DVector(27.625, 0.145))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[12]",
              pya.DTrans(0, False, pya.DVector(28.175, 0.145))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[13]",
              pya.DTrans(0, False, pya.DVector(29.625, 0.145))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[13]",
              pya.DTrans(0, False, pya.DVector(30.175, 0.145))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[14]",
              pya.DTrans(0, False, pya.DVector(31.625, 0.145))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[14]",
              pya.DTrans(0, False, pya.DVector(32.175, 0.145))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ON[15]",
              pya.DTrans(0, False, pya.DVector(33.625, 0.145))))
cell_dac32module.shapes(layout.layer(10, 25)).insert(
    pya.DText("ONB[15]",
              pya.DTrans(0, False, pya.DVector(34.175, 0.145))))
cell_dac32module.shapes(layout.layer(30, 25)).insert(
    pya.DText("Iout",
              pya.DTrans(2, False, pya.DVector(37.45, 13.095))))
cell_dac32module.shapes(layout.layer(30, 25)).insert(
    pya.DText("VbiasP[0]",
              pya.DTrans(2, False, pya.DVector(37.45, 11.795))))
cell_dac32module.shapes(layout.layer(30, 25)).insert(
    pya.DText("VbiasP[1]",
              pya.DTrans(2, False, pya.DVector(37.45, 14.395))))
cell_dac32module.shapes(layout.layer(30, 25)).insert(
    pya.DText("VcascP[1]",
              pya.DTrans(2, False, pya.DVector(18.9, 21.28))))
cell_dac32module.shapes(layout.layer(30, 25)).insert(
    pya.DText("VcascP[0]",
              pya.DTrans(0, False, pya.DVector(18.9, 4.91))))
cell_dac32module.shapes(layout.layer(67, 0)).insert(
    pya.DPolygon([pya.DPoint(0, 14.38), pya.DPoint(0, 26.19), pya.DPoint(37.8, 26.19), pya.DPoint(37.8, 14.38), pya.DPoint(0, 14.38)]))
cell_dac32module.shapes(layout.layer(67, 0)).insert(
    pya.DPolygon([pya.DPoint(0, 0), pya.DPoint(0, 11.81), pya.DPoint(37.8, 11.81), pya.DPoint(37.8, 0), pya.DPoint(0, 0)]))
cell_dac32module.shapes(layout.layer(67, 2)).insert(
    pya.DPolygon([pya.DPoint(0, 0), pya.DPoint(0, 11.81), pya.DPoint(37.8, 11.81), pya.DPoint(37.8, 0), pya.DPoint(0, 0)]))
cell_dac32module.shapes(layout.layer(67, 2)).insert(
    pya.DPolygon([pya.DPoint(0, 14.38), pya.DPoint(0, 26.19), pya.DPoint(37.8, 26.19), pya.DPoint(37.8, 14.38), pya.DPoint(0, 14.38)]))
cell_dac32module.shapes(layout.layer(67, 25)).insert(
    pya.DText("VDD",
              pya.DTrans(0, False, pya.DVector(18.9, 5.905))))
cell_dac32module.shapes(layout.layer(67, 25)).insert(
    pya.DText("VSS",
              pya.DTrans(0, False, pya.DVector(18.9, 20.285))))

# Save
layout.write("output.gds")
