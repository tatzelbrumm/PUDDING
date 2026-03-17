import pya

layout = pya.Layout()

layout.dbu = 0.001

# --- layer index variables ---
L_Activ = layout.layer(pya.LayerInfo(1, 0, "Activ"))
L_GatPoly = layout.layer(pya.LayerInfo(5, 0, "GatPoly"))
L_GatPoly_pin = layout.layer(pya.LayerInfo(5, 2, "GatPoly_pin"))
L_Cont = layout.layer(pya.LayerInfo(6, 0, "Cont"))
L_Metal1 = layout.layer(pya.LayerInfo(8, 0, "Metal1"))
L_Metal1_pin = layout.layer(pya.LayerInfo(8, 2, "Metal1_pin"))
L_Metal1_label = layout.layer(pya.LayerInfo(8, 25, "Metal1_label"))
L_Metal2 = layout.layer(pya.LayerInfo(10, 0, "Metal2"))
L_Metal2_pin = layout.layer(pya.LayerInfo(10, 2, "Metal2_pin"))
L_Metal2_label = layout.layer(pya.LayerInfo(10, 25, "Metal2_label"))
L_pSD = layout.layer(pya.LayerInfo(14, 0, "pSD"))
L_Metal3 = layout.layer(pya.LayerInfo(19, 0, "Metal3"))
L_Metal4 = layout.layer(pya.LayerInfo(29, 0, "Metal4"))
L_Metal5 = layout.layer(pya.LayerInfo(30, 0, "Metal5"))
L_Metal5_pin = layout.layer(pya.LayerInfo(30, 2, "Metal5_pin"))
L_Metal5_label = layout.layer(pya.LayerInfo(30, 25, "Metal5_label"))
L_NWell = layout.layer(pya.LayerInfo(31, 0, "NWell"))
L_NoBuLay = layout.layer(pya.LayerInfo(40, 0, "NoBuLay"))
L_ThickGateOx = layout.layer(pya.LayerInfo(44, 0, "ThickGateOx"))
L_TopMetal2 = layout.layer(pya.LayerInfo(49, 0, "TopMetal2"))
L_50_0 = layout.layer(50, 0)
L_pmos = layout.layer(pya.LayerInfo(51, 0, "pmos"))
L_TopMetal1 = layout.layer(pya.LayerInfo(63, 0, "TopMetal1"))
L_Via1 = layout.layer(pya.LayerInfo(66, 0, "Via1"))
L_Via2 = layout.layer(pya.LayerInfo(67, 0, "Via2"))
L_67_2 = layout.layer(67, 2)
L_67_25 = layout.layer(67, 25)
L_prBoundary = layout.layer(pya.LayerInfo(189, 4, "prBoundary"))

# --- cell declarations ---
cell____CONTEXT_INFO___ = layout.create_cell("$$$CONTEXT_INFO$$$")
cell_via_stack_2_1_1_1 = layout.create_cell("via_stack$2$1$1$1")
cell_via_stack_3_1_1 = layout.create_cell("via_stack$3$1$1")
cell_FEOL_contacts_9_1 = layout.create_cell("FEOL$contacts$9$1")
cell_via_stack_1_1_1_1_1 = layout.create_cell("via_stack$1$1$1$1$1")
cell_FEOL_contacts_3_2_1 = layout.create_cell("FEOL$contacts$3$2$1")
cell_FEOL_contacts_1_1_1_1_1 = layout.create_cell("FEOL$contacts$1$1$1$1$1")
cell_FEOL_contacts_1_2_1_1 = layout.create_cell("FEOL$contacts$1$2$1$1")
cell_FEOL_contacts_4_1_1_1 = layout.create_cell("FEOL$contacts$4$1$1$1")
cell_FEOL_contacts_5_1_1_1 = layout.create_cell("FEOL$contacts$5$1$1$1")
cell_FEOL_contacts_7_1_1_1 = layout.create_cell("FEOL$contacts$7$1$1$1")
cell_FEOL_contacts_6_1_1_1 = layout.create_cell("FEOL$contacts$6$1$1$1")
cell_DAC_SW = layout.create_cell("DAC_SW")
cell_NONOVERLAP = layout.create_cell("NONOVERLAP")
cell_FEOL_contacts_3_1 = layout.create_cell("FEOL$contacts$3$1")
cell_FEOL_contacts_8 = layout.create_cell("FEOL$contacts$8")
cell_via_stack_5 = layout.create_cell("via_stack$5")
cell_via_stack_6 = layout.create_cell("via_stack$6")
cell_via_stack_6_2_1 = layout.create_cell("via_stack$6$2$1")
cell_via_stack_7_2 = layout.create_cell("via_stack$7$2")
cell_via_stack_4_1 = layout.create_cell("via_stack$4$1")
cell_PCSOURCE2U = layout.create_cell("PCSOURCE2U")
cell_CASCODEDRIVE = layout.create_cell("CASCODEDRIVE")
cell_via_stack_9_1 = layout.create_cell("via_stack$9$1")
cell_CASCODEBIAS = layout.create_cell("CASCODEBIAS")
cell_unitsource2u = layout.create_cell("unitsource2u")
cell_via_stack_13 = layout.create_cell("via_stack$13")
cell_pmos_buffer_cap = layout.create_cell("pmos_buffer_cap")
cell_via_stack_8 = layout.create_cell("via_stack$8")
cell_pmos_buffer_cap_1 = layout.create_cell("pmos_buffer_cap$1")
cell_via_stack_9 = layout.create_cell("via_stack$9")
cell_via_stack_4 = layout.create_cell("via_stack$4")
cell_via_stack = layout.create_cell("via_stack")
cell_dac2u16out2in = layout.create_cell("dac2u16out2in")
cell_via_stack_11 = layout.create_cell("via_stack$11")
cell_via_stack_10 = layout.create_cell("via_stack$10")
cell_via_stack_7 = layout.create_cell("via_stack$7")
cell_inputwires = layout.create_cell("inputwires")
cell_dacbuffer = layout.create_cell("dacbuffer")
cell_dacendbuffer = layout.create_cell("dacendbuffer")
cell_dac128module_vss_strap = layout.create_cell("dac128module_vss_strap")
cell_dac128module_vdd_strap = layout.create_cell("dac128module_vdd_strap")
cell_dac2u32out4in = layout.create_cell("dac2u32out4in")
cell_buffercapwires = layout.create_cell("buffercapwires")
cell_dac4x32module = layout.create_cell("dac4x32module")

# === $$$CONTEXT_INFO$$$ ===
cell____CONTEXT_INFO___.insert(pya.DCellInstArray(
    cell_via_stack_13.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(0, 0))))
cell____CONTEXT_INFO___.insert(pya.DCellInstArray(
    cell_via_stack_11.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(0, 0))))
cell____CONTEXT_INFO___.insert(pya.DCellInstArray(
    cell_via_stack_10.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(0, 0))))
cell____CONTEXT_INFO___.insert(pya.DCellInstArray(
    cell_via_stack_7.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(0, 0))))

# === via_stack$2$1$1$1 ===
cell_via_stack_2_1_1_1.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(-0.145, -0.145), pya.DPoint(-0.145, 0.145), pya.DPoint(0.145, 0.145), pya.DPoint(0.145, -0.145), pya.DPoint(-0.145, -0.145)]))
cell_via_stack_2_1_1_1.shapes(L_Metal2).insert(
    pya.DPolygon([pya.DPoint(-0.145, -0.145), pya.DPoint(-0.145, 0.145), pya.DPoint(0.145, 0.145), pya.DPoint(0.145, -0.145), pya.DPoint(-0.145, -0.145)]))
cell_via_stack_2_1_1_1.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(-0.095, -0.095), pya.DPoint(-0.095, 0.095), pya.DPoint(0.095, 0.095), pya.DPoint(0.095, -0.095), pya.DPoint(-0.095, -0.095)]))

# === via_stack$3$1$1 ===
cell_via_stack_3_1_1.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(-0.145, -0.145), pya.DPoint(-0.145, 0.145), pya.DPoint(0.145, 0.145), pya.DPoint(0.145, -0.145), pya.DPoint(-0.145, -0.145)]))
cell_via_stack_3_1_1.shapes(L_Metal2).insert(
    pya.DPolygon([pya.DPoint(-0.145, -0.145), pya.DPoint(-0.145, 0.145), pya.DPoint(0.145, 0.145), pya.DPoint(0.145, -0.145), pya.DPoint(-0.145, -0.145)]))
cell_via_stack_3_1_1.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(-0.095, -0.095), pya.DPoint(-0.095, 0.095), pya.DPoint(0.095, 0.095), pya.DPoint(0.095, -0.095), pya.DPoint(-0.095, -0.095)]))
cell_via_stack_3_1_1.shapes(L_Metal5).insert(
    pya.DPolygon([pya.DPoint(-0.145, -0.145), pya.DPoint(-0.145, 0.145), pya.DPoint(0.145, 0.145), pya.DPoint(0.145, -0.145), pya.DPoint(-0.145, -0.145)]))
cell_via_stack_3_1_1.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(-0.095, -0.095), pya.DPoint(-0.095, 0.095), pya.DPoint(0.095, 0.095), pya.DPoint(0.095, -0.095), pya.DPoint(-0.095, -0.095)]))

# === FEOL$contacts$9$1 ===
cell_FEOL_contacts_9_1.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(0, 0), pya.DPoint(0, 0.16), pya.DPoint(0.26, 0.16), pya.DPoint(0.26, 0), pya.DPoint(0, 0)]))
cell_FEOL_contacts_9_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.05, 0), pya.DPoint(0.05, 0.16), pya.DPoint(0.21, 0.16), pya.DPoint(0.21, 0), pya.DPoint(0.05, 0)]))

# === via_stack$1$1$1$1$1 ===
cell_via_stack_1_1_1_1_1.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(-0.145, -0.145), pya.DPoint(-0.145, 0.145), pya.DPoint(0.145, 0.145), pya.DPoint(0.145, -0.145), pya.DPoint(-0.145, -0.145)]))
cell_via_stack_1_1_1_1_1.shapes(L_Metal2).insert(
    pya.DPolygon([pya.DPoint(-0.145, -0.145), pya.DPoint(-0.145, 0.145), pya.DPoint(0.145, 0.145), pya.DPoint(0.145, -0.145), pya.DPoint(-0.145, -0.145)]))
cell_via_stack_1_1_1_1_1.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(-0.095, -0.095), pya.DPoint(-0.095, 0.095), pya.DPoint(0.095, 0.095), pya.DPoint(0.095, -0.095), pya.DPoint(-0.095, -0.095)]))

# === FEOL$contacts$3$2$1 ===
cell_FEOL_contacts_3_2_1.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(0, 0), pya.DPoint(0, 0.5), pya.DPoint(1.92, 0.5), pya.DPoint(1.92, 0), pya.DPoint(0, 0)]))
cell_FEOL_contacts_3_2_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.2, 0), pya.DPoint(0.2, 0.16), pya.DPoint(0.36, 0.16), pya.DPoint(0.36, 0), pya.DPoint(0.2, 0)]))
cell_FEOL_contacts_3_2_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.54, 0), pya.DPoint(0.54, 0.16), pya.DPoint(0.7, 0.16), pya.DPoint(0.7, 0), pya.DPoint(0.54, 0)]))
cell_FEOL_contacts_3_2_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.88, 0), pya.DPoint(0.88, 0.16), pya.DPoint(1.04, 0.16), pya.DPoint(1.04, 0), pya.DPoint(0.88, 0)]))
cell_FEOL_contacts_3_2_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(1.22, 0), pya.DPoint(1.22, 0.16), pya.DPoint(1.38, 0.16), pya.DPoint(1.38, 0), pya.DPoint(1.22, 0)]))
cell_FEOL_contacts_3_2_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(1.56, 0), pya.DPoint(1.56, 0.16), pya.DPoint(1.72, 0.16), pya.DPoint(1.72, 0), pya.DPoint(1.56, 0)]))
cell_FEOL_contacts_3_2_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.2, 0.34), pya.DPoint(0.2, 0.5), pya.DPoint(0.36, 0.5), pya.DPoint(0.36, 0.34), pya.DPoint(0.2, 0.34)]))
cell_FEOL_contacts_3_2_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.54, 0.34), pya.DPoint(0.54, 0.5), pya.DPoint(0.7, 0.5), pya.DPoint(0.7, 0.34), pya.DPoint(0.54, 0.34)]))
cell_FEOL_contacts_3_2_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.88, 0.34), pya.DPoint(0.88, 0.5), pya.DPoint(1.04, 0.5), pya.DPoint(1.04, 0.34), pya.DPoint(0.88, 0.34)]))
cell_FEOL_contacts_3_2_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(1.22, 0.34), pya.DPoint(1.22, 0.5), pya.DPoint(1.38, 0.5), pya.DPoint(1.38, 0.34), pya.DPoint(1.22, 0.34)]))
cell_FEOL_contacts_3_2_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(1.56, 0.34), pya.DPoint(1.56, 0.5), pya.DPoint(1.72, 0.5), pya.DPoint(1.72, 0.34), pya.DPoint(1.56, 0.34)]))

# === FEOL$contacts$1$1$1$1$1 ===
cell_FEOL_contacts_1_1_1_1_1.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(0, 0), pya.DPoint(0, 0.16), pya.DPoint(0.26, 0.16), pya.DPoint(0.26, 0), pya.DPoint(0, 0)]))
cell_FEOL_contacts_1_1_1_1_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.05, 0), pya.DPoint(0.05, 0.16), pya.DPoint(0.21, 0.16), pya.DPoint(0.21, 0), pya.DPoint(0.05, 0)]))

# === FEOL$contacts$1$2$1$1 ===
cell_FEOL_contacts_1_2_1_1.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(0, 0), pya.DPoint(0, 0.16), pya.DPoint(0.52, 0.16), pya.DPoint(0.52, 0), pya.DPoint(0, 0)]))
cell_FEOL_contacts_1_2_1_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.18, 0), pya.DPoint(0.18, 0.16), pya.DPoint(0.34, 0.16), pya.DPoint(0.34, 0), pya.DPoint(0.18, 0)]))

# === FEOL$contacts$4$1$1$1 ===
cell_FEOL_contacts_4_1_1_1.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(0, 0), pya.DPoint(0, 0.16), pya.DPoint(4.93, 0.16), pya.DPoint(4.93, 0), pya.DPoint(0, 0)]))
cell_FEOL_contacts_4_1_1_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.175, 0), pya.DPoint(0.175, 0.16), pya.DPoint(0.335, 0.16), pya.DPoint(0.335, 0), pya.DPoint(0.175, 0)]))
cell_FEOL_contacts_4_1_1_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.515, 0), pya.DPoint(0.515, 0.16), pya.DPoint(0.675, 0.16), pya.DPoint(0.675, 0), pya.DPoint(0.515, 0)]))
cell_FEOL_contacts_4_1_1_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.855, 0), pya.DPoint(0.855, 0.16), pya.DPoint(1.015, 0.16), pya.DPoint(1.015, 0), pya.DPoint(0.855, 0)]))
cell_FEOL_contacts_4_1_1_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(1.195, 0), pya.DPoint(1.195, 0.16), pya.DPoint(1.355, 0.16), pya.DPoint(1.355, 0), pya.DPoint(1.195, 0)]))
cell_FEOL_contacts_4_1_1_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(1.535, 0), pya.DPoint(1.535, 0.16), pya.DPoint(1.695, 0.16), pya.DPoint(1.695, 0), pya.DPoint(1.535, 0)]))
cell_FEOL_contacts_4_1_1_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(1.875, 0), pya.DPoint(1.875, 0.16), pya.DPoint(2.035, 0.16), pya.DPoint(2.035, 0), pya.DPoint(1.875, 0)]))
cell_FEOL_contacts_4_1_1_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(2.215, 0), pya.DPoint(2.215, 0.16), pya.DPoint(2.375, 0.16), pya.DPoint(2.375, 0), pya.DPoint(2.215, 0)]))
cell_FEOL_contacts_4_1_1_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(2.555, 0), pya.DPoint(2.555, 0.16), pya.DPoint(2.715, 0.16), pya.DPoint(2.715, 0), pya.DPoint(2.555, 0)]))
cell_FEOL_contacts_4_1_1_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(2.895, 0), pya.DPoint(2.895, 0.16), pya.DPoint(3.055, 0.16), pya.DPoint(3.055, 0), pya.DPoint(2.895, 0)]))
cell_FEOL_contacts_4_1_1_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(3.235, 0), pya.DPoint(3.235, 0.16), pya.DPoint(3.395, 0.16), pya.DPoint(3.395, 0), pya.DPoint(3.235, 0)]))
cell_FEOL_contacts_4_1_1_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(3.575, 0), pya.DPoint(3.575, 0.16), pya.DPoint(3.735, 0.16), pya.DPoint(3.735, 0), pya.DPoint(3.575, 0)]))
cell_FEOL_contacts_4_1_1_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(3.915, 0), pya.DPoint(3.915, 0.16), pya.DPoint(4.075, 0.16), pya.DPoint(4.075, 0), pya.DPoint(3.915, 0)]))
cell_FEOL_contacts_4_1_1_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(4.255, 0), pya.DPoint(4.255, 0.16), pya.DPoint(4.415, 0.16), pya.DPoint(4.415, 0), pya.DPoint(4.255, 0)]))
cell_FEOL_contacts_4_1_1_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(4.595, 0), pya.DPoint(4.595, 0.16), pya.DPoint(4.755, 0.16), pya.DPoint(4.755, 0), pya.DPoint(4.595, 0)]))

# === FEOL$contacts$5$1$1$1 ===
cell_FEOL_contacts_5_1_1_1.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(0, 0), pya.DPoint(0, 0.16), pya.DPoint(1.92, 0.16), pya.DPoint(1.92, 0), pya.DPoint(0, 0)]))
cell_FEOL_contacts_5_1_1_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.2, 0), pya.DPoint(0.2, 0.16), pya.DPoint(0.36, 0.16), pya.DPoint(0.36, 0), pya.DPoint(0.2, 0)]))
cell_FEOL_contacts_5_1_1_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.54, 0), pya.DPoint(0.54, 0.16), pya.DPoint(0.7, 0.16), pya.DPoint(0.7, 0), pya.DPoint(0.54, 0)]))
cell_FEOL_contacts_5_1_1_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.88, 0), pya.DPoint(0.88, 0.16), pya.DPoint(1.04, 0.16), pya.DPoint(1.04, 0), pya.DPoint(0.88, 0)]))
cell_FEOL_contacts_5_1_1_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(1.22, 0), pya.DPoint(1.22, 0.16), pya.DPoint(1.38, 0.16), pya.DPoint(1.38, 0), pya.DPoint(1.22, 0)]))
cell_FEOL_contacts_5_1_1_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(1.56, 0), pya.DPoint(1.56, 0.16), pya.DPoint(1.72, 0.16), pya.DPoint(1.72, 0), pya.DPoint(1.56, 0)]))

# === FEOL$contacts$7$1$1$1 ===
cell_FEOL_contacts_7_1_1_1.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(0, 0), pya.DPoint(0, 0.16), pya.DPoint(1.45, 0.16), pya.DPoint(1.45, 0), pya.DPoint(0, 0)]))
cell_FEOL_contacts_7_1_1_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.135, 0), pya.DPoint(0.135, 0.16), pya.DPoint(0.295, 0.16), pya.DPoint(0.295, 0), pya.DPoint(0.135, 0)]))
cell_FEOL_contacts_7_1_1_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.475, 0), pya.DPoint(0.475, 0.16), pya.DPoint(0.635, 0.16), pya.DPoint(0.635, 0), pya.DPoint(0.475, 0)]))
cell_FEOL_contacts_7_1_1_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.815, 0), pya.DPoint(0.815, 0.16), pya.DPoint(0.975, 0.16), pya.DPoint(0.975, 0), pya.DPoint(0.815, 0)]))
cell_FEOL_contacts_7_1_1_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(1.155, 0), pya.DPoint(1.155, 0.16), pya.DPoint(1.315, 0.16), pya.DPoint(1.315, 0), pya.DPoint(1.155, 0)]))

# === FEOL$contacts$6$1$1$1 ===
cell_FEOL_contacts_6_1_1_1.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(0, 0), pya.DPoint(0, 0.16), pya.DPoint(1.16, 0.16), pya.DPoint(1.16, 0), pya.DPoint(0, 0)]))
cell_FEOL_contacts_6_1_1_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.16, 0), pya.DPoint(0.16, 0.16), pya.DPoint(0.32, 0.16), pya.DPoint(0.32, 0), pya.DPoint(0.16, 0)]))
cell_FEOL_contacts_6_1_1_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.5, 0), pya.DPoint(0.5, 0.16), pya.DPoint(0.66, 0.16), pya.DPoint(0.66, 0), pya.DPoint(0.5, 0)]))
cell_FEOL_contacts_6_1_1_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.84, 0), pya.DPoint(0.84, 0.16), pya.DPoint(1, 0.16), pya.DPoint(1, 0), pya.DPoint(0.84, 0)]))

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
cell_DAC_SW.shapes(L_Metal1).insert(_path)
cell_DAC_SW.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(0.43, -0.13), pya.DPoint(0.43, 0.13), pya.DPoint(0.59, 0.13), pya.DPoint(0.59, -0.13), pya.DPoint(0.43, -0.13)]))
cell_DAC_SW.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(-0.59, -0.13), pya.DPoint(-0.59, 0.13), pya.DPoint(-0.43, 0.13), pya.DPoint(-0.43, -0.13), pya.DPoint(-0.59, -0.13)]))
cell_DAC_SW.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(-0.08, -0.13), pya.DPoint(-0.08, 0.13), pya.DPoint(0.08, 0.13), pya.DPoint(0.08, -0.13), pya.DPoint(-0.08, -0.13)]))
cell_DAC_SW.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(-0.49, -0.65), pya.DPoint(-0.49, -0.35), pya.DPoint(-0.19, -0.35), pya.DPoint(-0.19, -0.65), pya.DPoint(-0.49, -0.65)]))
cell_DAC_SW.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(0.19, -0.65), pya.DPoint(0.19, -0.35), pya.DPoint(0.49, -0.35), pya.DPoint(0.49, -0.65), pya.DPoint(0.19, -0.65)]))
cell_DAC_SW.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(-0.66, -0.15), pya.DPoint(-0.66, 0.15), pya.DPoint(-0.36, 0.15), pya.DPoint(-0.36, -0.15), pya.DPoint(-0.66, -0.15)]))
cell_DAC_SW.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(-0.15, -0.15), pya.DPoint(-0.15, 0.15), pya.DPoint(0.15, 0.15), pya.DPoint(0.15, -0.15), pya.DPoint(-0.15, -0.15)]))
cell_DAC_SW.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.43, -0.08), pya.DPoint(0.43, 0.08), pya.DPoint(0.59, 0.08), pya.DPoint(0.59, -0.08), pya.DPoint(0.43, -0.08)]))
cell_DAC_SW.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(-0.59, -0.08), pya.DPoint(-0.59, 0.08), pya.DPoint(-0.43, 0.08), pya.DPoint(-0.43, -0.08), pya.DPoint(-0.59, -0.08)]))
cell_DAC_SW.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(-0.08, -0.08), pya.DPoint(-0.08, 0.08), pya.DPoint(0.08, 0.08), pya.DPoint(0.08, -0.08), pya.DPoint(-0.08, -0.08)]))
_path = pya.DPath([pya.DPoint(-0.745, -1.95), pya.DPoint(-0.745, -0.545), pya.DPoint(-0.24, -0.545)], 0.2)
cell_DAC_SW.shapes(L_Metal2).insert(_path)
_path = pya.DPath([pya.DPoint(0.74, -1.95), pya.DPoint(0.74, -0.545), pya.DPoint(0.24, -0.545)], 0.2)
cell_DAC_SW.shapes(L_Metal2).insert(_path)
cell_DAC_SW.shapes(L_Metal2).insert(
    pya.DPolygon([pya.DPoint(-0.845, -0.145), pya.DPoint(-0.845, 0.205), pya.DPoint(-0.365, 0.205), pya.DPoint(-0.365, -0.145), pya.DPoint(-0.845, -0.145)]))
cell_DAC_SW.shapes(L_Activ).insert(
    pya.DPolygon([pya.DPoint(-0.66, -0.15), pya.DPoint(-0.66, 0.15), pya.DPoint(0.66, 0.15), pya.DPoint(0.66, -0.15), pya.DPoint(-0.66, -0.15)]))
cell_DAC_SW.shapes(L_GatPoly).insert(
    pya.DPolygon([pya.DPoint(-0.32, -0.375), pya.DPoint(-0.32, 0.33), pya.DPoint(-0.19, 0.33), pya.DPoint(-0.19, -0.375), pya.DPoint(-0.32, -0.375)]))
cell_DAC_SW.shapes(L_GatPoly).insert(
    pya.DPolygon([pya.DPoint(0.19, -0.375), pya.DPoint(0.19, 0.33), pya.DPoint(0.32, 0.33), pya.DPoint(0.32, -0.375), pya.DPoint(0.19, -0.375)]))
cell_DAC_SW.shapes(L_GatPoly).insert(
    pya.DPolygon([pya.DPoint(-0.49, -0.65), pya.DPoint(-0.49, -0.35), pya.DPoint(-0.19, -0.35), pya.DPoint(-0.19, -0.65), pya.DPoint(-0.49, -0.65)]))
cell_DAC_SW.shapes(L_GatPoly).insert(
    pya.DPolygon([pya.DPoint(0.19, -0.65), pya.DPoint(0.19, -0.35), pya.DPoint(0.49, -0.35), pya.DPoint(0.49, -0.65), pya.DPoint(0.19, -0.65)]))
cell_DAC_SW.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(-1, -0.45), pya.DPoint(-1, 0.45), pya.DPoint(1, 0.45), pya.DPoint(1, -0.45), pya.DPoint(-1, -0.45)]))
cell_DAC_SW.shapes(L_NWell).insert(
    pya.DPolygon([pya.DPoint(-1, -0.5), pya.DPoint(-1, 0.5), pya.DPoint(1, 0.5), pya.DPoint(1, -0.5), pya.DPoint(-1, -0.5)]))
cell_DAC_SW.shapes(L_prBoundary).insert(
    pya.DPolygon([pya.DPoint(-1, -0.36), pya.DPoint(-1, 0.36), pya.DPoint(1, 0.36), pya.DPoint(1, -0.36), pya.DPoint(-1, -0.36)]))

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
cell_NONOVERLAP.shapes(L_Metal1).insert(_path)
_path = pya.DPath([pya.DPoint(-0.745, -2.02), pya.DPoint(-0.745, -0.08)], 0.16)
cell_NONOVERLAP.shapes(L_Metal1).insert(_path)
_path = pya.DPath([pya.DPoint(0.745, -2.02), pya.DPoint(0.745, -0.08)], 0.16)
cell_NONOVERLAP.shapes(L_Metal1).insert(_path)
_path = pya.DPath([pya.DPoint(0, -2.02), pya.DPoint(0, -2.69)], 0.16)
cell_NONOVERLAP.shapes(L_Metal1).insert(_path)
_path = pya.DPath([pya.DPoint(0, 0.71), pya.DPoint(0, -0.08)], 0.16)
cell_NONOVERLAP.shapes(L_Metal1).insert(_path)
cell_NONOVERLAP.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(-1, 0.55), pya.DPoint(-1, 1.05), pya.DPoint(1, 1.05), pya.DPoint(1, 0.55), pya.DPoint(-1, 0.55)]))
cell_NONOVERLAP.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(-1, -3.03), pya.DPoint(-1, -2.53), pya.DPoint(1, -2.53), pya.DPoint(1, -3.03), pya.DPoint(-1, -3.03)]))
cell_NONOVERLAP.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(-1, 0.55), pya.DPoint(-1, 1.05), pya.DPoint(1, 1.05), pya.DPoint(1, 0.55), pya.DPoint(-1, 0.55)]))
_path = pya.DPath([pya.DPoint(0, -1.63), pya.DPoint(0, -2.18)], 0.15)
cell_NONOVERLAP.shapes(L_Activ).insert(_path)
_path = pya.DPath([pya.DPoint(0.82, -1.635), pya.DPoint(0.82, -2.18)], 0.15)
cell_NONOVERLAP.shapes(L_Activ).insert(_path)
_path = pya.DPath([pya.DPoint(-0.82, -1.63), pya.DPoint(-0.82, -2.18)], 0.15)
cell_NONOVERLAP.shapes(L_Activ).insert(_path)
cell_NONOVERLAP.shapes(L_Activ).insert(
    pya.DPolygon([pya.DPoint(-0.895, -0.15), pya.DPoint(-0.895, 0.15), pya.DPoint(0.895, 0.15), pya.DPoint(0.895, -0.15), pya.DPoint(-0.895, -0.15)]))
cell_NONOVERLAP.shapes(L_Activ).insert(
    pya.DPolygon([pya.DPoint(-1, 0.48), pya.DPoint(-1, 1.12), pya.DPoint(1, 1.12), pya.DPoint(1, 0.48), pya.DPoint(-1, 0.48)]))
cell_NONOVERLAP.shapes(L_Activ).insert(
    pya.DPolygon([pya.DPoint(-0.895, -1.7), pya.DPoint(-0.895, -1.55), pya.DPoint(0.895, -1.55), pya.DPoint(0.895, -1.7), pya.DPoint(-0.895, -1.7)]))
cell_NONOVERLAP.shapes(L_Activ).insert(
    pya.DPolygon([pya.DPoint(-0.895, -2.25), pya.DPoint(-0.895, -1.95), pya.DPoint(-0.595, -1.95), pya.DPoint(-0.595, -2.25), pya.DPoint(-0.895, -2.25)]))
cell_NONOVERLAP.shapes(L_Activ).insert(
    pya.DPolygon([pya.DPoint(0.595, -2.25), pya.DPoint(0.595, -1.95), pya.DPoint(0.895, -1.95), pya.DPoint(0.895, -2.25), pya.DPoint(0.595, -2.25)]))
cell_NONOVERLAP.shapes(L_Activ).insert(
    pya.DPolygon([pya.DPoint(-0.15, -2.25), pya.DPoint(-0.15, -1.95), pya.DPoint(0.15, -1.95), pya.DPoint(0.15, -2.25), pya.DPoint(-0.15, -2.25)]))
cell_NONOVERLAP.shapes(L_Activ).insert(
    pya.DPolygon([pya.DPoint(-1, -3.1), pya.DPoint(-1, -2.46), pya.DPoint(1, -2.46), pya.DPoint(1, -3.1), pya.DPoint(-1, -3.1)]))
_path = pya.DPath([pya.DPoint(-0.295, -1.475), pya.DPoint(-0.295, -0.85), pya.DPoint(0.745, -0.85)], 0.3)
cell_NONOVERLAP.shapes(L_GatPoly).insert(_path)
cell_NONOVERLAP.shapes(L_GatPoly).insert(
    pya.DPolygon([pya.DPoint(0.19, -0.33), pya.DPoint(0.19, 0.33), pya.DPoint(0.32, 0.33), pya.DPoint(0.32, -0.33), pya.DPoint(0.19, -0.33)]))
cell_NONOVERLAP.shapes(L_GatPoly).insert(
    pya.DPolygon([pya.DPoint(-0.32, -0.33), pya.DPoint(-0.32, 0.33), pya.DPoint(-0.19, 0.33), pya.DPoint(-0.19, -0.33), pya.DPoint(-0.32, -0.33)]))
cell_NONOVERLAP.shapes(L_GatPoly).insert(
    pya.DPolygon([pya.DPoint(-0.49, -0.52), pya.DPoint(-0.49, -0.22), pya.DPoint(-0.19, -0.22), pya.DPoint(-0.19, -0.52), pya.DPoint(-0.49, -0.52)]))
cell_NONOVERLAP.shapes(L_GatPoly).insert(
    pya.DPolygon([pya.DPoint(0.19, -0.52), pya.DPoint(0.19, -0.22), pya.DPoint(0.49, -0.22), pya.DPoint(0.49, -0.52), pya.DPoint(0.19, -0.52)]))
cell_NONOVERLAP.shapes(L_GatPoly).insert(
    pya.DPolygon([pya.DPoint(0.145, -1.88), pya.DPoint(0.145, -1.37), pya.DPoint(0.665, -1.37), pya.DPoint(0.665, -1.88), pya.DPoint(0.145, -1.88)]))
cell_NONOVERLAP.shapes(L_GatPoly).insert(
    pya.DPolygon([pya.DPoint(0.145, -1.48), pya.DPoint(0.145, -1.18), pya.DPoint(0.445, -1.18), pya.DPoint(0.445, -1.48), pya.DPoint(0.145, -1.48)]))
cell_NONOVERLAP.shapes(L_GatPoly).insert(
    pya.DPolygon([pya.DPoint(-0.665, -1.88), pya.DPoint(-0.665, -1.37), pya.DPoint(-0.145, -1.37), pya.DPoint(-0.145, -1.88), pya.DPoint(-0.665, -1.88)]))
cell_NONOVERLAP.shapes(L_GatPoly).insert(
    pya.DPolygon([pya.DPoint(0.595, -1), pya.DPoint(0.595, -0.7), pya.DPoint(0.895, -0.7), pya.DPoint(0.895, -1), pya.DPoint(0.595, -1)]))
cell_NONOVERLAP.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(-1.195, -0.45), pya.DPoint(-1.195, 0.45), pya.DPoint(1.195, 0.45), pya.DPoint(1.195, -0.45), pya.DPoint(-1.195, -0.45)]))
cell_NONOVERLAP.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(-1.195, -3.13), pya.DPoint(-1.195, -2.43), pya.DPoint(1.195, -2.43), pya.DPoint(1.195, -3.13), pya.DPoint(-1.195, -3.13)]))
cell_NONOVERLAP.shapes(L_NWell).insert(
    pya.DPolygon([pya.DPoint(-1.24, -0.505), pya.DPoint(-1.24, 1.44), pya.DPoint(1.24, 1.44), pya.DPoint(1.24, -0.505), pya.DPoint(-1.24, -0.505)]))
cell_NONOVERLAP.shapes(L_prBoundary).insert(
    pya.DPolygon([pya.DPoint(-1, -3.1), pya.DPoint(-1, 1.12), pya.DPoint(1, 1.12), pya.DPoint(1, -3.1), pya.DPoint(-1, -3.1)]))
cell_NONOVERLAP.shapes(L_Metal1_pin).insert(
    pya.DPolygon([pya.DPoint(-1, -3.03), pya.DPoint(-1, -2.53), pya.DPoint(1, -2.53), pya.DPoint(1, -3.03), pya.DPoint(-1, -3.03)]))
cell_NONOVERLAP.shapes(L_Metal1_pin).insert(
    pya.DPolygon([pya.DPoint(-1, 0.55), pya.DPoint(-1, 1.05), pya.DPoint(1, 1.05), pya.DPoint(1, 0.55), pya.DPoint(-1, 0.55)]))
cell_NONOVERLAP.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(-0.89, -0.12), pya.DPoint(-0.89, 0.17), pya.DPoint(-0.6, 0.17), pya.DPoint(-0.6, -0.12), pya.DPoint(-0.89, -0.12)]))
cell_NONOVERLAP.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(-0.42, -0.6), pya.DPoint(-0.42, -0.31), pya.DPoint(-0.13, -0.31), pya.DPoint(-0.13, -0.6), pya.DPoint(-0.42, -0.6)]))
cell_NONOVERLAP.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(0.13, -0.6), pya.DPoint(0.13, -0.31), pya.DPoint(0.42, -0.31), pya.DPoint(0.42, -0.6), pya.DPoint(0.13, -0.6)]))
cell_NONOVERLAP.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(0.6, -0.12), pya.DPoint(0.6, 0.17), pya.DPoint(0.89, 0.17), pya.DPoint(0.89, -0.12), pya.DPoint(0.6, -0.12)]))
_txt = pya.Text("VSS",
               pya.Trans(0, False, pya.Vector(0, -2780)))
_txt.halign = 1
_txt.valign = 1
cell_NONOVERLAP.shapes(L_Metal1_label).insert(_txt)
_txt = pya.Text("VDD",
               pya.Trans(0, False, pya.Vector(0, 800)))
_txt.halign = 1
_txt.valign = 1
cell_NONOVERLAP.shapes(L_Metal1_label).insert(_txt)
_txt = pya.Text("OUTN",
               pya.Trans(0, False, pya.Vector(-745, 25)))
_txt.halign = 1
_txt.valign = 1
cell_NONOVERLAP.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("INP",
               pya.Trans(0, False, pya.Vector(-275, -455)))
_txt.halign = 1
_txt.valign = 1
cell_NONOVERLAP.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("OUTP",
               pya.Trans(0, False, pya.Vector(745, 25)))
_txt.halign = 1
_txt.valign = 1
cell_NONOVERLAP.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("INN",
               pya.Trans(0, False, pya.Vector(275, -455)))
_txt.halign = 1
_txt.valign = 1
cell_NONOVERLAP.shapes(L_Metal2_label).insert(_txt)

# === FEOL$contacts$3$1 ===
cell_FEOL_contacts_3_1.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(0, 0), pya.DPoint(0, 0.16), pya.DPoint(5.85, 0.16), pya.DPoint(5.85, 0), pya.DPoint(0, 0)]))
cell_FEOL_contacts_3_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.125, 0), pya.DPoint(0.125, 0.16), pya.DPoint(0.285, 0.16), pya.DPoint(0.285, 0), pya.DPoint(0.125, 0)]))
cell_FEOL_contacts_3_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.465, 0), pya.DPoint(0.465, 0.16), pya.DPoint(0.625, 0.16), pya.DPoint(0.625, 0), pya.DPoint(0.465, 0)]))
cell_FEOL_contacts_3_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.805, 0), pya.DPoint(0.805, 0.16), pya.DPoint(0.965, 0.16), pya.DPoint(0.965, 0), pya.DPoint(0.805, 0)]))
cell_FEOL_contacts_3_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(1.145, 0), pya.DPoint(1.145, 0.16), pya.DPoint(1.305, 0.16), pya.DPoint(1.305, 0), pya.DPoint(1.145, 0)]))
cell_FEOL_contacts_3_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(1.485, 0), pya.DPoint(1.485, 0.16), pya.DPoint(1.645, 0.16), pya.DPoint(1.645, 0), pya.DPoint(1.485, 0)]))
cell_FEOL_contacts_3_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(1.825, 0), pya.DPoint(1.825, 0.16), pya.DPoint(1.985, 0.16), pya.DPoint(1.985, 0), pya.DPoint(1.825, 0)]))
cell_FEOL_contacts_3_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(2.165, 0), pya.DPoint(2.165, 0.16), pya.DPoint(2.325, 0.16), pya.DPoint(2.325, 0), pya.DPoint(2.165, 0)]))
cell_FEOL_contacts_3_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(2.505, 0), pya.DPoint(2.505, 0.16), pya.DPoint(2.665, 0.16), pya.DPoint(2.665, 0), pya.DPoint(2.505, 0)]))
cell_FEOL_contacts_3_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(2.845, 0), pya.DPoint(2.845, 0.16), pya.DPoint(3.005, 0.16), pya.DPoint(3.005, 0), pya.DPoint(2.845, 0)]))
cell_FEOL_contacts_3_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(3.185, 0), pya.DPoint(3.185, 0.16), pya.DPoint(3.345, 0.16), pya.DPoint(3.345, 0), pya.DPoint(3.185, 0)]))
cell_FEOL_contacts_3_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(3.525, 0), pya.DPoint(3.525, 0.16), pya.DPoint(3.685, 0.16), pya.DPoint(3.685, 0), pya.DPoint(3.525, 0)]))
cell_FEOL_contacts_3_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(3.865, 0), pya.DPoint(3.865, 0.16), pya.DPoint(4.025, 0.16), pya.DPoint(4.025, 0), pya.DPoint(3.865, 0)]))
cell_FEOL_contacts_3_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(4.205, 0), pya.DPoint(4.205, 0.16), pya.DPoint(4.365, 0.16), pya.DPoint(4.365, 0), pya.DPoint(4.205, 0)]))
cell_FEOL_contacts_3_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(4.545, 0), pya.DPoint(4.545, 0.16), pya.DPoint(4.705, 0.16), pya.DPoint(4.705, 0), pya.DPoint(4.545, 0)]))
cell_FEOL_contacts_3_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(4.885, 0), pya.DPoint(4.885, 0.16), pya.DPoint(5.045, 0.16), pya.DPoint(5.045, 0), pya.DPoint(4.885, 0)]))
cell_FEOL_contacts_3_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(5.225, 0), pya.DPoint(5.225, 0.16), pya.DPoint(5.385, 0.16), pya.DPoint(5.385, 0), pya.DPoint(5.225, 0)]))
cell_FEOL_contacts_3_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(5.565, 0), pya.DPoint(5.565, 0.16), pya.DPoint(5.725, 0.16), pya.DPoint(5.725, 0), pya.DPoint(5.565, 0)]))

# === FEOL$contacts$8 ===
cell_FEOL_contacts_8.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(0, 0), pya.DPoint(0, 0.16), pya.DPoint(0.26, 0.16), pya.DPoint(0.26, 0), pya.DPoint(0, 0)]))
cell_FEOL_contacts_8.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.05, 0), pya.DPoint(0.05, 0.16), pya.DPoint(0.21, 0.16), pya.DPoint(0.21, 0), pya.DPoint(0.05, 0)]))

# === via_stack$5 ===
cell_via_stack_5.shapes(L_Metal2).insert(
    pya.DPolygon([pya.DPoint(-0.145, -0.35), pya.DPoint(-0.145, 0.35), pya.DPoint(0.145, 0.35), pya.DPoint(0.145, -0.35), pya.DPoint(-0.145, -0.35)]))
cell_via_stack_5.shapes(L_Metal5).insert(
    pya.DPolygon([pya.DPoint(-0.145, -0.35), pya.DPoint(-0.145, 0.35), pya.DPoint(0.75, 0.35), pya.DPoint(0.75, -0.35), pya.DPoint(-0.145, -0.35)]))
cell_via_stack_5.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(-0.095, -0.3), pya.DPoint(-0.095, -0.11), pya.DPoint(0.095, -0.11), pya.DPoint(0.095, -0.3), pya.DPoint(-0.095, -0.3)]))
cell_via_stack_5.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(-0.095, 0.11), pya.DPoint(-0.095, 0.3), pya.DPoint(0.095, 0.3), pya.DPoint(0.095, 0.11), pya.DPoint(-0.095, 0.11)]))

# === via_stack$6 ===
cell_via_stack_6.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(-0.145, -3.025), pya.DPoint(-0.145, 3.025), pya.DPoint(0.145, 3.025), pya.DPoint(0.145, -3.025), pya.DPoint(-0.145, -3.025)]))
cell_via_stack_6.shapes(L_Metal2).insert(
    pya.DPolygon([pya.DPoint(-0.145, -3.025), pya.DPoint(-0.145, 3.025), pya.DPoint(0.145, 3.025), pya.DPoint(0.145, -3.025), pya.DPoint(-0.145, -3.025)]))
cell_via_stack_6.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(-0.095, -2.975), pya.DPoint(-0.095, -2.785), pya.DPoint(0.095, -2.785), pya.DPoint(0.095, -2.975), pya.DPoint(-0.095, -2.975)]))
cell_via_stack_6.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(-0.095, -2.495), pya.DPoint(-0.095, -2.305), pya.DPoint(0.095, -2.305), pya.DPoint(0.095, -2.495), pya.DPoint(-0.095, -2.495)]))
cell_via_stack_6.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(-0.095, -2.015), pya.DPoint(-0.095, -1.825), pya.DPoint(0.095, -1.825), pya.DPoint(0.095, -2.015), pya.DPoint(-0.095, -2.015)]))
cell_via_stack_6.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(-0.095, -1.535), pya.DPoint(-0.095, -1.345), pya.DPoint(0.095, -1.345), pya.DPoint(0.095, -1.535), pya.DPoint(-0.095, -1.535)]))
cell_via_stack_6.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(-0.095, -1.055), pya.DPoint(-0.095, -0.865), pya.DPoint(0.095, -0.865), pya.DPoint(0.095, -1.055), pya.DPoint(-0.095, -1.055)]))
cell_via_stack_6.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(-0.095, -0.575), pya.DPoint(-0.095, -0.385), pya.DPoint(0.095, -0.385), pya.DPoint(0.095, -0.575), pya.DPoint(-0.095, -0.575)]))
cell_via_stack_6.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(-0.095, -0.095), pya.DPoint(-0.095, 0.095), pya.DPoint(0.095, 0.095), pya.DPoint(0.095, -0.095), pya.DPoint(-0.095, -0.095)]))
cell_via_stack_6.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(-0.095, 0.385), pya.DPoint(-0.095, 0.575), pya.DPoint(0.095, 0.575), pya.DPoint(0.095, 0.385), pya.DPoint(-0.095, 0.385)]))
cell_via_stack_6.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(-0.095, 0.865), pya.DPoint(-0.095, 1.055), pya.DPoint(0.095, 1.055), pya.DPoint(0.095, 0.865), pya.DPoint(-0.095, 0.865)]))
cell_via_stack_6.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(-0.095, 1.345), pya.DPoint(-0.095, 1.535), pya.DPoint(0.095, 1.535), pya.DPoint(0.095, 1.345), pya.DPoint(-0.095, 1.345)]))
cell_via_stack_6.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(-0.095, 1.825), pya.DPoint(-0.095, 2.015), pya.DPoint(0.095, 2.015), pya.DPoint(0.095, 1.825), pya.DPoint(-0.095, 1.825)]))
cell_via_stack_6.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(-0.095, 2.305), pya.DPoint(-0.095, 2.495), pya.DPoint(0.095, 2.495), pya.DPoint(0.095, 2.305), pya.DPoint(-0.095, 2.305)]))
cell_via_stack_6.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(-0.095, 2.785), pya.DPoint(-0.095, 2.975), pya.DPoint(0.095, 2.975), pya.DPoint(0.095, 2.785), pya.DPoint(-0.095, 2.785)]))

# === via_stack$6$2$1 ===
cell_via_stack_6_2_1.shapes(L_Metal2).insert(
    pya.DPolygon([pya.DPoint(-0.145, -0.145), pya.DPoint(-0.145, 0.145), pya.DPoint(0.145, 0.145), pya.DPoint(0.145, -0.145), pya.DPoint(-0.145, -0.145)]))
cell_via_stack_6_2_1.shapes(L_Metal5).insert(
    pya.DPolygon([pya.DPoint(-0.145, -0.145), pya.DPoint(-0.145, 0.145), pya.DPoint(0.145, 0.145), pya.DPoint(0.145, -0.145), pya.DPoint(-0.145, -0.145)]))
cell_via_stack_6_2_1.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(-0.095, -0.095), pya.DPoint(-0.095, 0.095), pya.DPoint(0.095, 0.095), pya.DPoint(0.095, -0.095), pya.DPoint(-0.095, -0.095)]))

# === via_stack$7$2 ===
cell_via_stack_7_2.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(-0.145, -0.35), pya.DPoint(-0.145, 0.35), pya.DPoint(0.145, 0.35), pya.DPoint(0.145, -0.35), pya.DPoint(-0.145, -0.35)]))
cell_via_stack_7_2.shapes(L_Metal2).insert(
    pya.DPolygon([pya.DPoint(-0.145, -0.35), pya.DPoint(-0.145, 0.35), pya.DPoint(0.145, 0.35), pya.DPoint(0.145, -0.35), pya.DPoint(-0.145, -0.35)]))
cell_via_stack_7_2.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(-0.095, -0.3), pya.DPoint(-0.095, -0.11), pya.DPoint(0.095, -0.11), pya.DPoint(0.095, -0.3), pya.DPoint(-0.095, -0.3)]))
cell_via_stack_7_2.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(-0.095, 0.11), pya.DPoint(-0.095, 0.3), pya.DPoint(0.095, 0.3), pya.DPoint(0.095, 0.11), pya.DPoint(-0.095, 0.11)]))

# === via_stack$4$1 ===
cell_via_stack_4_1.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(-0.35, -0.145), pya.DPoint(-0.35, 0.145), pya.DPoint(0.35, 0.145), pya.DPoint(0.35, -0.145), pya.DPoint(-0.35, -0.145)]))
cell_via_stack_4_1.shapes(L_Metal2).insert(
    pya.DPolygon([pya.DPoint(-0.35, -0.145), pya.DPoint(-0.35, 0.145), pya.DPoint(0.35, 0.145), pya.DPoint(0.35, -0.145), pya.DPoint(-0.35, -0.145)]))
cell_via_stack_4_1.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(-0.3, -0.095), pya.DPoint(-0.3, 0.095), pya.DPoint(-0.11, 0.095), pya.DPoint(-0.11, -0.095), pya.DPoint(-0.3, -0.095)]))
cell_via_stack_4_1.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(0.11, -0.095), pya.DPoint(0.11, 0.095), pya.DPoint(0.3, 0.095), pya.DPoint(0.3, -0.095), pya.DPoint(0.11, -0.095)]))
cell_via_stack_4_1.shapes(L_Metal5).insert(
    pya.DPolygon([pya.DPoint(-0.35, -0.145), pya.DPoint(-0.35, 0.145), pya.DPoint(0.35, 0.145), pya.DPoint(0.35, -0.145), pya.DPoint(-0.35, -0.145)]))
cell_via_stack_4_1.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(-0.3, -0.095), pya.DPoint(-0.3, 0.095), pya.DPoint(-0.11, 0.095), pya.DPoint(-0.11, -0.095), pya.DPoint(-0.3, -0.095)]))
cell_via_stack_4_1.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(0.11, -0.095), pya.DPoint(0.11, 0.095), pya.DPoint(0.3, 0.095), pya.DPoint(0.3, -0.095), pya.DPoint(0.11, -0.095)]))

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
cell_PCSOURCE2U.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(-0.375, 0.625), pya.DPoint(-0.375, 0.835), pya.DPoint(0.815, 0.835), pya.DPoint(0.815, 0.625), pya.DPoint(-0.375, 0.625)]))
cell_PCSOURCE2U.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(-0.78, -0.265), pya.DPoint(-0.78, 0.445), pya.DPoint(-0.56, 0.445), pya.DPoint(-0.56, -0.265), pya.DPoint(-0.78, -0.265)]))
cell_PCSOURCE2U.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(-1, -5.38), pya.DPoint(-1, -0.45), pya.DPoint(1, -0.45), pya.DPoint(1, -5.38), pya.DPoint(-1, -5.38)]))
cell_PCSOURCE2U.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(-1, -6.23), pya.DPoint(-1, -5.56), pya.DPoint(1, -5.56), pya.DPoint(1, -6.23), pya.DPoint(-1, -6.23)]))
cell_PCSOURCE2U.shapes(L_Metal2).insert(
    pya.DPolygon([pya.DPoint(-0.78, -0.145), pya.DPoint(-0.78, 0.445), pya.DPoint(-0.56, 0.445), pya.DPoint(-0.56, -0.145), pya.DPoint(-0.78, -0.145)]))
cell_PCSOURCE2U.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(-0.765, -0.095), pya.DPoint(-0.765, 0.095), pya.DPoint(-0.575, 0.095), pya.DPoint(-0.575, -0.095), pya.DPoint(-0.765, -0.095)]))
cell_PCSOURCE2U.shapes(L_Activ).insert(
    pya.DPolygon([pya.DPoint(-1, -6.3), pya.DPoint(-1, -6), pya.DPoint(1, -6), pya.DPoint(1, -6.3), pya.DPoint(-1, -6.3)]))
cell_PCSOURCE2U.shapes(L_Activ).insert(
    pya.DPolygon([pya.DPoint(-0.63, -5.79), pya.DPoint(-0.63, -0.22), pya.DPoint(0.82, -0.22), pya.DPoint(0.82, -5.79), pya.DPoint(-0.63, -5.79)]))
cell_PCSOURCE2U.shapes(L_Activ).insert(
    pya.DPolygon([pya.DPoint(-0.38, -0.38), pya.DPoint(-0.38, 0.88), pya.DPoint(0.82, 0.88), pya.DPoint(0.82, -0.38), pya.DPoint(-0.38, -0.38)]))
cell_PCSOURCE2U.shapes(L_GatPoly).insert(
    pya.DPolygon([pya.DPoint(-0.82, -0.15), pya.DPoint(-0.82, 0.45), pya.DPoint(1, 0.45), pya.DPoint(1, -0.15), pya.DPoint(-0.82, -0.15)]))
cell_PCSOURCE2U.shapes(L_GatPoly).insert(
    pya.DPolygon([pya.DPoint(-1, -5.45), pya.DPoint(-1, -0.45), pya.DPoint(1, -0.45), pya.DPoint(1, -5.45), pya.DPoint(-1, -5.45)]))
cell_PCSOURCE2U.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(-1.12, -5.97), pya.DPoint(-1.12, 1.06), pya.DPoint(1.12, 1.06), pya.DPoint(1.12, -5.97), pya.DPoint(-1.12, -5.97)]))
cell_PCSOURCE2U.shapes(L_NWell).insert(
    pya.DPolygon([pya.DPoint(-1.24, -6.54), pya.DPoint(-1.24, 1.19), pya.DPoint(1.24, 1.19), pya.DPoint(1.24, -6.54), pya.DPoint(-1.24, -6.54)]))
cell_PCSOURCE2U.shapes(L_prBoundary).insert(
    pya.DPolygon([pya.DPoint(-1, -6.3), pya.DPoint(-1, 0.88), pya.DPoint(1, 0.88), pya.DPoint(1, -6.3), pya.DPoint(-1, -6.3)]))
cell_PCSOURCE2U.shapes(L_Metal1_pin).insert(
    pya.DPolygon([pya.DPoint(-1, -5.38), pya.DPoint(-1, -0.45), pya.DPoint(1, -0.45), pya.DPoint(1, -5.38), pya.DPoint(-1, -5.38)]))
cell_PCSOURCE2U.shapes(L_Metal1_pin).insert(
    pya.DPolygon([pya.DPoint(-1, -6.23), pya.DPoint(-1, -5.56), pya.DPoint(1, -5.56), pya.DPoint(1, -6.23), pya.DPoint(-1, -6.23)]))
cell_PCSOURCE2U.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(-0.775, -0.145), pya.DPoint(-0.775, 0.445), pya.DPoint(-0.565, 0.445), pya.DPoint(-0.565, -0.145), pya.DPoint(-0.775, -0.145)]))
cell_PCSOURCE2U.shapes(L_Metal1_label).insert(
    pya.DPolygon([pya.DPoint(-0.375, 0.625), pya.DPoint(-0.375, 0.835), pya.DPoint(0.815, 0.835), pya.DPoint(0.815, 0.625), pya.DPoint(-0.375, 0.625)]))
_txt = pya.Text("VbiasP",
               pya.Trans(0, False, pya.Vector(0, -2915)))
_txt.halign = 1
_txt.valign = 1
cell_PCSOURCE2U.shapes(L_Metal1_label).insert(_txt)
_txt = pya.Text("VDD",
               pya.Trans(0, False, pya.Vector(0, -5895)))
_txt.halign = 1
_txt.valign = 1
cell_PCSOURCE2U.shapes(L_Metal1_label).insert(_txt)
_txt = pya.Text("Iout",
               pya.Trans(0, False, pya.Vector(220, 730)))
_txt.halign = 1
_txt.valign = 1
cell_PCSOURCE2U.shapes(L_Metal1_label).insert(_txt)
_txt = pya.Text("VcascodeP",
               pya.Trans(0, False, pya.Vector(-670, 0)))
_txt.halign = 1
_txt.valign = 1
cell_PCSOURCE2U.shapes(L_Metal2_label).insert(_txt)
cell_PCSOURCE2U.shapes(L_TopMetal1).insert(
    pya.DPolygon([pya.DPoint(0.14, 0.585), pya.DPoint(0.14, 0.875), pya.DPoint(0.3, 0.875), pya.DPoint(0.3, 0.585), pya.DPoint(0.14, 0.585)]))
cell_PCSOURCE2U.shapes(L_TopMetal1).insert(
    pya.DPolygon([pya.DPoint(0.125, 0.635), pya.DPoint(0.125, 0.825), pya.DPoint(0.315, 0.825), pya.DPoint(0.315, 0.635), pya.DPoint(0.125, 0.635)]))

# === CASCODEDRIVE ===
cell_CASCODEDRIVE.insert(pya.DCellInstArray(
    cell_DAC_SW.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(0, 0))))
cell_CASCODEDRIVE.insert(pya.DCellInstArray(
    cell_NONOVERLAP.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(0, -1.88))))

# === via_stack$9$1 ===
cell_via_stack_9_1.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(-0.145, -0.145), pya.DPoint(-0.145, 0.145), pya.DPoint(0.145, 0.145), pya.DPoint(0.145, -0.145), pya.DPoint(-0.145, -0.145)]))
cell_via_stack_9_1.shapes(L_Metal2).insert(
    pya.DPolygon([pya.DPoint(-0.145, -0.145), pya.DPoint(-0.145, 0.145), pya.DPoint(0.145, 0.145), pya.DPoint(0.145, -0.145), pya.DPoint(-0.145, -0.145)]))
cell_via_stack_9_1.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(-0.095, -0.095), pya.DPoint(-0.095, 0.095), pya.DPoint(0.095, 0.095), pya.DPoint(0.095, -0.095), pya.DPoint(-0.095, -0.095)]))
cell_via_stack_9_1.shapes(L_Metal5).insert(
    pya.DPolygon([pya.DPoint(-0.145, -0.145), pya.DPoint(-0.145, 0.145), pya.DPoint(0.145, 0.145), pya.DPoint(0.145, -0.145), pya.DPoint(-0.145, -0.145)]))
cell_via_stack_9_1.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(-0.095, -0.095), pya.DPoint(-0.095, 0.095), pya.DPoint(0.095, 0.095), pya.DPoint(0.095, -0.095), pya.DPoint(-0.095, -0.095)]))

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
cell_CASCODEBIAS.shapes(L_Metal1).insert(_path)
_path = pya.DPath([pya.DPoint(-1.75, 1.61), pya.DPoint(-1.75, 1.96)], 0.16)
cell_CASCODEBIAS.shapes(L_Metal1).insert(_path)
cell_CASCODEBIAS.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(-1.3, 1.76), pya.DPoint(-1.3, 6.33), pya.DPoint(-0.77, 6.33), pya.DPoint(-0.77, 1.76), pya.DPoint(-1.3, 1.76)]))
_path = pya.DPath([pya.DPoint(-1.75, 1.93), pya.DPoint(-1.75, 0)], 0.29)
cell_CASCODEBIAS.shapes(L_Metal2).insert(_path)
cell_CASCODEBIAS.shapes(L_Activ).insert(
    pya.DPolygon([pya.DPoint(-1.9, 1.76), pya.DPoint(-1.9, 7.61), pya.DPoint(-1.07, 7.61), pya.DPoint(-1.07, 1.76), pya.DPoint(-1.9, 1.76)]))
cell_CASCODEBIAS.shapes(L_GatPoly).insert(
    pya.DPolygon([pya.DPoint(-1.56, 1.68), pya.DPoint(-1.56, 7.79), pya.DPoint(-1.41, 7.79), pya.DPoint(-1.41, 1.68), pya.DPoint(-1.56, 1.68)]))
cell_CASCODEBIAS.shapes(L_GatPoly).insert(
    pya.DPolygon([pya.DPoint(-1.9, 1.38), pya.DPoint(-1.9, 1.68), pya.DPoint(-1.41, 1.68), pya.DPoint(-1.41, 1.38), pya.DPoint(-1.9, 1.38)]))
cell_CASCODEBIAS.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(-2.08, 1.46), pya.DPoint(-2.08, 7.91), pya.DPoint(-0.89, 7.91), pya.DPoint(-0.89, 1.46), pya.DPoint(-2.08, 1.46)]))
cell_CASCODEBIAS.shapes(L_NWell).insert(
    pya.DPolygon([pya.DPoint(-2.21, 1.45), pya.DPoint(-2.21, 7.92), pya.DPoint(-0.76, 7.92), pya.DPoint(-0.76, 1.45), pya.DPoint(-2.21, 1.45)]))

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
cell_unitsource2u.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(0.43, -0.13), pya.DPoint(0.43, 0.71), pya.DPoint(0.93, 0.71), pya.DPoint(0.93, -0.13), pya.DPoint(0.43, -0.13)]))
_path = pya.DPath([pya.DPoint(-0.275, -4.91), pya.DPoint(-0.275, -2.19)], 0.2)
cell_unitsource2u.shapes(L_Metal2).insert(_path)
_path = pya.DPath([pya.DPoint(0.275, -4.91), pya.DPoint(0.275, -2.19)], 0.2)
cell_unitsource2u.shapes(L_Metal2).insert(_path)
_path = pya.DPath([pya.DPoint(-0.67, 6.685), pya.DPoint(-0.67, 0.885), pya.DPoint(0, 0.885), pya.DPoint(0, 0.095)], 0.2)
cell_unitsource2u.shapes(L_Metal2).insert(_path)
cell_unitsource2u.shapes(L_Metal2).insert(
    pya.DPolygon([pya.DPoint(-0.92, -4.91), pya.DPoint(-0.92, -4.41), pya.DPoint(-0.63, -4.41), pya.DPoint(-0.63, -4.91), pya.DPoint(-0.92, -4.91)]))
_path = pya.DPath([pya.DPoint(-1, 0), pya.DPoint(1, 0)], 0.7)
cell_unitsource2u.shapes(L_Metal5).insert(_path)
cell_unitsource2u.shapes(L_Metal5).insert(
    pya.DPolygon([pya.DPoint(-1, 0.75), pya.DPoint(-1, 2.48), pya.DPoint(1, 2.48), pya.DPoint(1, 0.75), pya.DPoint(-1, 0.75)]))
cell_unitsource2u.shapes(L_Metal5).insert(
    pya.DPolygon([pya.DPoint(-1, -2.48), pya.DPoint(-1, -0.75), pya.DPoint(1, -0.75), pya.DPoint(1, -2.48), pya.DPoint(-1, -2.48)]))
cell_unitsource2u.shapes(L_Metal5).insert(
    pya.DPolygon([pya.DPoint(-1, -4.91), pya.DPoint(-1, -3.18), pya.DPoint(1, -3.18), pya.DPoint(1, -4.91), pya.DPoint(-1, -4.91)]))
_txt = pya.Text("VDD",
               pya.Trans(0, False, pya.Vector(0, 1615)))
_txt.halign = 1
_txt.valign = 1
cell_unitsource2u.shapes(L_Metal5).insert(_txt)
cell_unitsource2u.shapes(L_NWell).insert(
    pya.DPolygon([pya.DPoint(-1.24, -2.385), pya.DPoint(-1.24, 7.97), pya.DPoint(1.24, 7.97), pya.DPoint(1.24, -2.385), pya.DPoint(-1.24, -2.385)]))
cell_unitsource2u.shapes(L_Metal1_pin).insert(
    pya.DPolygon([pya.DPoint(-1, 0.55), pya.DPoint(-1, 1.22), pya.DPoint(1, 1.22), pya.DPoint(1, 0.55), pya.DPoint(-1, 0.55)]))
cell_unitsource2u.shapes(L_Metal1_pin).insert(
    pya.DPolygon([pya.DPoint(-1, 1.4), pya.DPoint(-1, 6.33), pya.DPoint(1, 6.33), pya.DPoint(1, 1.4), pya.DPoint(-1, 1.4)]))
cell_unitsource2u.shapes(L_Metal1_pin).insert(
    pya.DPolygon([pya.DPoint(-0.375, 7.405), pya.DPoint(-0.375, 7.615), pya.DPoint(0.815, 7.615), pya.DPoint(0.815, 7.405), pya.DPoint(-0.375, 7.405)]))
cell_unitsource2u.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(0.175, -4.91), pya.DPoint(0.175, -4.62), pya.DPoint(0.375, -4.62), pya.DPoint(0.375, -4.91), pya.DPoint(0.175, -4.91)]))
cell_unitsource2u.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(-0.375, -4.91), pya.DPoint(-0.375, -4.62), pya.DPoint(-0.175, -4.62), pya.DPoint(-0.175, -4.91), pya.DPoint(-0.375, -4.91)]))
_txt = pya.Text("VbiasP",
               pya.Trans(0, False, pya.Vector(0, 3865)))
_txt.halign = 1
_txt.valign = 1
cell_unitsource2u.shapes(L_Metal1_label).insert(_txt)
_txt = pya.Text("Iout",
               pya.Trans(0, False, pya.Vector(220, 7510)))
_txt.halign = 1
_txt.valign = 1
cell_unitsource2u.shapes(L_Metal1_label).insert(_txt)
_txt = pya.Text("ON",
               pya.Trans(0, False, pya.Vector(-275, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_unitsource2u.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB",
               pya.Trans(0, False, pya.Vector(275, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_unitsource2u.shapes(L_Metal2_label).insert(_txt)
cell_unitsource2u.shapes(L_Metal5_pin).insert(
    pya.DPolygon([pya.DPoint(-1, -0.35), pya.DPoint(-1, 0.35), pya.DPoint(1, 0.35), pya.DPoint(1, -0.35), pya.DPoint(-1, -0.35)]))
cell_unitsource2u.shapes(L_Metal5_pin).insert(
    pya.DPolygon([pya.DPoint(-1, 0.75), pya.DPoint(-1, 2.48), pya.DPoint(1, 2.48), pya.DPoint(1, 0.75), pya.DPoint(-1, 0.75)]))
cell_unitsource2u.shapes(L_Metal5_pin).insert(
    pya.DPolygon([pya.DPoint(-1, -2.48), pya.DPoint(-1, -0.75), pya.DPoint(1, -0.75), pya.DPoint(1, -2.48), pya.DPoint(-1, -2.48)]))
cell_unitsource2u.shapes(L_Metal5_pin).insert(
    pya.DPolygon([pya.DPoint(-1, -4.91), pya.DPoint(-1, -3.18), pya.DPoint(1, -3.18), pya.DPoint(1, -4.91), pya.DPoint(-1, -4.91)]))
_txt = pya.Text("VSS",
               pya.Trans(0, False, pya.Vector(0, -4045)))
_txt.halign = 1
_txt.valign = 1
cell_unitsource2u.shapes(L_Metal5_label).insert(_txt)
_txt = pya.Text("VDD",
               pya.Trans(0, False, pya.Vector(0, -1615)))
_txt.halign = 1
_txt.valign = 1
cell_unitsource2u.shapes(L_Metal5_label).insert(_txt)
_txt = pya.Text("VcascP",
               pya.Trans(0, False, pya.Vector(0, 0)))
_txt.halign = 1
_txt.valign = 1
cell_unitsource2u.shapes(L_Metal5_label).insert(_txt)

# === via_stack$13 ===
cell_via_stack_13.shapes(L_Metal2).insert(
    pya.DPolygon([pya.DPoint(-0.35, -0.35), pya.DPoint(-0.35, 0.35), pya.DPoint(0.35, 0.35), pya.DPoint(0.35, -0.35), pya.DPoint(-0.35, -0.35)]))
cell_via_stack_13.shapes(L_Metal5).insert(
    pya.DPolygon([pya.DPoint(-0.35, -0.35), pya.DPoint(-0.35, 0.35), pya.DPoint(0.35, 0.35), pya.DPoint(0.35, -0.35), pya.DPoint(-0.35, -0.35)]))
cell_via_stack_13.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(-0.3, -0.3), pya.DPoint(-0.3, -0.11), pya.DPoint(-0.11, -0.11), pya.DPoint(-0.11, -0.3), pya.DPoint(-0.3, -0.3)]))
cell_via_stack_13.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(-0.3, 0.11), pya.DPoint(-0.3, 0.3), pya.DPoint(-0.11, 0.3), pya.DPoint(-0.11, 0.11), pya.DPoint(-0.3, 0.11)]))
cell_via_stack_13.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(0.11, -0.3), pya.DPoint(0.11, -0.11), pya.DPoint(0.3, -0.11), pya.DPoint(0.3, -0.3), pya.DPoint(0.11, -0.3)]))
cell_via_stack_13.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(0.11, 0.11), pya.DPoint(0.11, 0.3), pya.DPoint(0.3, 0.3), pya.DPoint(0.3, 0.11), pya.DPoint(0.11, 0.11)]))

# === pmos_buffer_cap ===
cell_pmos_buffer_cap.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(0, -0.44), pya.DPoint(0, 5.16), pya.DPoint(14.6, 5.16), pya.DPoint(14.6, -0.44), pya.DPoint(0, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(-0.39, 0.34), pya.DPoint(-0.39, 4.38), pya.DPoint(-0.23, 4.38), pya.DPoint(-0.23, 0.34), pya.DPoint(-0.39, 0.34)]))
cell_pmos_buffer_cap.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(14.82, 0.34), pya.DPoint(14.82, 4.38), pya.DPoint(14.98, 4.38), pya.DPoint(14.98, 0.34), pya.DPoint(14.82, 0.34)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(7.22, 0.07), pya.DPoint(7.22, 0.23), pya.DPoint(7.38, 0.23), pya.DPoint(7.38, 0.07), pya.DPoint(7.22, 0.07)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(7.22, 4.49), pya.DPoint(7.22, 4.65), pya.DPoint(7.38, 4.65), pya.DPoint(7.38, 4.49), pya.DPoint(7.22, 4.49)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(7.22, -0.44), pya.DPoint(7.22, -0.28), pya.DPoint(7.38, -0.28), pya.DPoint(7.38, -0.44), pya.DPoint(7.22, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(7.22, 5), pya.DPoint(7.22, 5.16), pya.DPoint(7.38, 5.16), pya.DPoint(7.38, 5), pya.DPoint(7.22, 5)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(8.24, 4.49), pya.DPoint(8.24, 4.65), pya.DPoint(8.4, 4.65), pya.DPoint(8.4, 4.49), pya.DPoint(8.24, 4.49)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(8.58, 4.49), pya.DPoint(8.58, 4.65), pya.DPoint(8.74, 4.65), pya.DPoint(8.74, 4.49), pya.DPoint(8.58, 4.49)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(8.92, 4.49), pya.DPoint(8.92, 4.65), pya.DPoint(9.08, 4.65), pya.DPoint(9.08, 4.49), pya.DPoint(8.92, 4.49)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(9.26, 4.49), pya.DPoint(9.26, 4.65), pya.DPoint(9.42, 4.65), pya.DPoint(9.42, 4.49), pya.DPoint(9.26, 4.49)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(9.6, 4.49), pya.DPoint(9.6, 4.65), pya.DPoint(9.76, 4.65), pya.DPoint(9.76, 4.49), pya.DPoint(9.6, 4.49)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(9.94, 4.49), pya.DPoint(9.94, 4.65), pya.DPoint(10.1, 4.65), pya.DPoint(10.1, 4.49), pya.DPoint(9.94, 4.49)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(10.28, 4.49), pya.DPoint(10.28, 4.65), pya.DPoint(10.44, 4.65), pya.DPoint(10.44, 4.49), pya.DPoint(10.28, 4.49)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(10.62, 4.49), pya.DPoint(10.62, 4.65), pya.DPoint(10.78, 4.65), pya.DPoint(10.78, 4.49), pya.DPoint(10.62, 4.49)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(10.96, 4.49), pya.DPoint(10.96, 4.65), pya.DPoint(11.12, 4.65), pya.DPoint(11.12, 4.49), pya.DPoint(10.96, 4.49)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(11.3, 4.49), pya.DPoint(11.3, 4.65), pya.DPoint(11.46, 4.65), pya.DPoint(11.46, 4.49), pya.DPoint(11.3, 4.49)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(11.64, 4.49), pya.DPoint(11.64, 4.65), pya.DPoint(11.8, 4.65), pya.DPoint(11.8, 4.49), pya.DPoint(11.64, 4.49)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(11.98, 4.49), pya.DPoint(11.98, 4.65), pya.DPoint(12.14, 4.65), pya.DPoint(12.14, 4.49), pya.DPoint(11.98, 4.49)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(12.32, 4.49), pya.DPoint(12.32, 4.65), pya.DPoint(12.48, 4.65), pya.DPoint(12.48, 4.49), pya.DPoint(12.32, 4.49)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(12.66, 4.49), pya.DPoint(12.66, 4.65), pya.DPoint(12.82, 4.65), pya.DPoint(12.82, 4.49), pya.DPoint(12.66, 4.49)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(13, 4.49), pya.DPoint(13, 4.65), pya.DPoint(13.16, 4.65), pya.DPoint(13.16, 4.49), pya.DPoint(13, 4.49)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(13.34, 4.49), pya.DPoint(13.34, 4.65), pya.DPoint(13.5, 4.65), pya.DPoint(13.5, 4.49), pya.DPoint(13.34, 4.49)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(13.68, 4.49), pya.DPoint(13.68, 4.65), pya.DPoint(13.84, 4.65), pya.DPoint(13.84, 4.49), pya.DPoint(13.68, 4.49)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(14.02, 4.49), pya.DPoint(14.02, 4.65), pya.DPoint(14.18, 4.65), pya.DPoint(14.18, 4.49), pya.DPoint(14.02, 4.49)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(14.36, 4.49), pya.DPoint(14.36, 4.65), pya.DPoint(14.52, 4.65), pya.DPoint(14.52, 4.49), pya.DPoint(14.36, 4.49)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(7.56, 4.49), pya.DPoint(7.56, 4.65), pya.DPoint(7.72, 4.65), pya.DPoint(7.72, 4.49), pya.DPoint(7.56, 4.49)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(7.9, 4.49), pya.DPoint(7.9, 4.65), pya.DPoint(8.06, 4.65), pya.DPoint(8.06, 4.49), pya.DPoint(7.9, 4.49)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(7.56, 5), pya.DPoint(7.56, 5.16), pya.DPoint(7.72, 5.16), pya.DPoint(7.72, 5), pya.DPoint(7.56, 5)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(7.9, 5), pya.DPoint(7.9, 5.16), pya.DPoint(8.06, 5.16), pya.DPoint(8.06, 5), pya.DPoint(7.9, 5)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(8.24, 5), pya.DPoint(8.24, 5.16), pya.DPoint(8.4, 5.16), pya.DPoint(8.4, 5), pya.DPoint(8.24, 5)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(8.58, 5), pya.DPoint(8.58, 5.16), pya.DPoint(8.74, 5.16), pya.DPoint(8.74, 5), pya.DPoint(8.58, 5)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(8.92, 5), pya.DPoint(8.92, 5.16), pya.DPoint(9.08, 5.16), pya.DPoint(9.08, 5), pya.DPoint(8.92, 5)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(9.26, 5), pya.DPoint(9.26, 5.16), pya.DPoint(9.42, 5.16), pya.DPoint(9.42, 5), pya.DPoint(9.26, 5)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(9.6, 5), pya.DPoint(9.6, 5.16), pya.DPoint(9.76, 5.16), pya.DPoint(9.76, 5), pya.DPoint(9.6, 5)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(9.94, 5), pya.DPoint(9.94, 5.16), pya.DPoint(10.1, 5.16), pya.DPoint(10.1, 5), pya.DPoint(9.94, 5)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(10.28, 5), pya.DPoint(10.28, 5.16), pya.DPoint(10.44, 5.16), pya.DPoint(10.44, 5), pya.DPoint(10.28, 5)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(10.62, 5), pya.DPoint(10.62, 5.16), pya.DPoint(10.78, 5.16), pya.DPoint(10.78, 5), pya.DPoint(10.62, 5)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(10.96, 5), pya.DPoint(10.96, 5.16), pya.DPoint(11.12, 5.16), pya.DPoint(11.12, 5), pya.DPoint(10.96, 5)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(11.3, 5), pya.DPoint(11.3, 5.16), pya.DPoint(11.46, 5.16), pya.DPoint(11.46, 5), pya.DPoint(11.3, 5)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(11.64, 5), pya.DPoint(11.64, 5.16), pya.DPoint(11.8, 5.16), pya.DPoint(11.8, 5), pya.DPoint(11.64, 5)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(11.98, 5), pya.DPoint(11.98, 5.16), pya.DPoint(12.14, 5.16), pya.DPoint(12.14, 5), pya.DPoint(11.98, 5)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(12.32, 5), pya.DPoint(12.32, 5.16), pya.DPoint(12.48, 5.16), pya.DPoint(12.48, 5), pya.DPoint(12.32, 5)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(12.66, 5), pya.DPoint(12.66, 5.16), pya.DPoint(12.82, 5.16), pya.DPoint(12.82, 5), pya.DPoint(12.66, 5)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(13, 5), pya.DPoint(13, 5.16), pya.DPoint(13.16, 5.16), pya.DPoint(13.16, 5), pya.DPoint(13, 5)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(13.34, 5), pya.DPoint(13.34, 5.16), pya.DPoint(13.5, 5.16), pya.DPoint(13.5, 5), pya.DPoint(13.34, 5)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(13.68, 5), pya.DPoint(13.68, 5.16), pya.DPoint(13.84, 5.16), pya.DPoint(13.84, 5), pya.DPoint(13.68, 5)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(14.02, 5), pya.DPoint(14.02, 5.16), pya.DPoint(14.18, 5.16), pya.DPoint(14.18, 5), pya.DPoint(14.02, 5)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(14.36, 5), pya.DPoint(14.36, 5.16), pya.DPoint(14.52, 5.16), pya.DPoint(14.52, 5), pya.DPoint(14.36, 5)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(14.82, 2.45), pya.DPoint(14.82, 2.61), pya.DPoint(14.98, 2.61), pya.DPoint(14.98, 2.45), pya.DPoint(14.82, 2.45)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(14.82, 2.79), pya.DPoint(14.82, 2.95), pya.DPoint(14.98, 2.95), pya.DPoint(14.98, 2.79), pya.DPoint(14.82, 2.79)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(14.82, 3.13), pya.DPoint(14.82, 3.29), pya.DPoint(14.98, 3.29), pya.DPoint(14.98, 3.13), pya.DPoint(14.82, 3.13)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(14.82, 3.47), pya.DPoint(14.82, 3.63), pya.DPoint(14.98, 3.63), pya.DPoint(14.98, 3.47), pya.DPoint(14.82, 3.47)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(14.82, 3.81), pya.DPoint(14.82, 3.97), pya.DPoint(14.98, 3.97), pya.DPoint(14.98, 3.81), pya.DPoint(14.82, 3.81)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(14.82, 4.15), pya.DPoint(14.82, 4.31), pya.DPoint(14.98, 4.31), pya.DPoint(14.98, 4.15), pya.DPoint(14.82, 4.15)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(2.46, 5), pya.DPoint(2.46, 5.16), pya.DPoint(2.62, 5.16), pya.DPoint(2.62, 5), pya.DPoint(2.46, 5)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(2.8, 5), pya.DPoint(2.8, 5.16), pya.DPoint(2.96, 5.16), pya.DPoint(2.96, 5), pya.DPoint(2.8, 5)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(3.14, 5), pya.DPoint(3.14, 5.16), pya.DPoint(3.3, 5.16), pya.DPoint(3.3, 5), pya.DPoint(3.14, 5)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(3.48, 5), pya.DPoint(3.48, 5.16), pya.DPoint(3.64, 5.16), pya.DPoint(3.64, 5), pya.DPoint(3.48, 5)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(3.82, 5), pya.DPoint(3.82, 5.16), pya.DPoint(3.98, 5.16), pya.DPoint(3.98, 5), pya.DPoint(3.82, 5)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(4.16, 5), pya.DPoint(4.16, 5.16), pya.DPoint(4.32, 5.16), pya.DPoint(4.32, 5), pya.DPoint(4.16, 5)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(4.5, 5), pya.DPoint(4.5, 5.16), pya.DPoint(4.66, 5.16), pya.DPoint(4.66, 5), pya.DPoint(4.5, 5)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(4.84, 5), pya.DPoint(4.84, 5.16), pya.DPoint(5, 5.16), pya.DPoint(5, 5), pya.DPoint(4.84, 5)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(5.18, 5), pya.DPoint(5.18, 5.16), pya.DPoint(5.34, 5.16), pya.DPoint(5.34, 5), pya.DPoint(5.18, 5)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(5.52, 5), pya.DPoint(5.52, 5.16), pya.DPoint(5.68, 5.16), pya.DPoint(5.68, 5), pya.DPoint(5.52, 5)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(5.86, 5), pya.DPoint(5.86, 5.16), pya.DPoint(6.02, 5.16), pya.DPoint(6.02, 5), pya.DPoint(5.86, 5)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(6.2, 5), pya.DPoint(6.2, 5.16), pya.DPoint(6.36, 5.16), pya.DPoint(6.36, 5), pya.DPoint(6.2, 5)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(6.54, 5), pya.DPoint(6.54, 5.16), pya.DPoint(6.7, 5.16), pya.DPoint(6.7, 5), pya.DPoint(6.54, 5)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(6.88, 5), pya.DPoint(6.88, 5.16), pya.DPoint(7.04, 5.16), pya.DPoint(7.04, 5), pya.DPoint(6.88, 5)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.76, 4.49), pya.DPoint(0.76, 4.65), pya.DPoint(0.92, 4.65), pya.DPoint(0.92, 4.49), pya.DPoint(0.76, 4.49)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(1.1, 4.49), pya.DPoint(1.1, 4.65), pya.DPoint(1.26, 4.65), pya.DPoint(1.26, 4.49), pya.DPoint(1.1, 4.49)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(1.44, 4.49), pya.DPoint(1.44, 4.65), pya.DPoint(1.6, 4.65), pya.DPoint(1.6, 4.49), pya.DPoint(1.44, 4.49)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(1.78, 4.49), pya.DPoint(1.78, 4.65), pya.DPoint(1.94, 4.65), pya.DPoint(1.94, 4.49), pya.DPoint(1.78, 4.49)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(2.12, 4.49), pya.DPoint(2.12, 4.65), pya.DPoint(2.28, 4.65), pya.DPoint(2.28, 4.49), pya.DPoint(2.12, 4.49)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(2.46, 4.49), pya.DPoint(2.46, 4.65), pya.DPoint(2.62, 4.65), pya.DPoint(2.62, 4.49), pya.DPoint(2.46, 4.49)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(2.8, 4.49), pya.DPoint(2.8, 4.65), pya.DPoint(2.96, 4.65), pya.DPoint(2.96, 4.49), pya.DPoint(2.8, 4.49)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(3.14, 4.49), pya.DPoint(3.14, 4.65), pya.DPoint(3.3, 4.65), pya.DPoint(3.3, 4.49), pya.DPoint(3.14, 4.49)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(3.48, 4.49), pya.DPoint(3.48, 4.65), pya.DPoint(3.64, 4.65), pya.DPoint(3.64, 4.49), pya.DPoint(3.48, 4.49)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(3.82, 4.49), pya.DPoint(3.82, 4.65), pya.DPoint(3.98, 4.65), pya.DPoint(3.98, 4.49), pya.DPoint(3.82, 4.49)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(4.16, 4.49), pya.DPoint(4.16, 4.65), pya.DPoint(4.32, 4.65), pya.DPoint(4.32, 4.49), pya.DPoint(4.16, 4.49)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(4.5, 4.49), pya.DPoint(4.5, 4.65), pya.DPoint(4.66, 4.65), pya.DPoint(4.66, 4.49), pya.DPoint(4.5, 4.49)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(4.84, 4.49), pya.DPoint(4.84, 4.65), pya.DPoint(5, 4.65), pya.DPoint(5, 4.49), pya.DPoint(4.84, 4.49)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(5.18, 4.49), pya.DPoint(5.18, 4.65), pya.DPoint(5.34, 4.65), pya.DPoint(5.34, 4.49), pya.DPoint(5.18, 4.49)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(5.52, 4.49), pya.DPoint(5.52, 4.65), pya.DPoint(5.68, 4.65), pya.DPoint(5.68, 4.49), pya.DPoint(5.52, 4.49)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(5.86, 4.49), pya.DPoint(5.86, 4.65), pya.DPoint(6.02, 4.65), pya.DPoint(6.02, 4.49), pya.DPoint(5.86, 4.49)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(6.2, 4.49), pya.DPoint(6.2, 4.65), pya.DPoint(6.36, 4.65), pya.DPoint(6.36, 4.49), pya.DPoint(6.2, 4.49)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(6.54, 4.49), pya.DPoint(6.54, 4.65), pya.DPoint(6.7, 4.65), pya.DPoint(6.7, 4.49), pya.DPoint(6.54, 4.49)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(6.88, 4.49), pya.DPoint(6.88, 4.65), pya.DPoint(7.04, 4.65), pya.DPoint(7.04, 4.49), pya.DPoint(6.88, 4.49)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.08, 4.49), pya.DPoint(0.08, 4.65), pya.DPoint(0.24, 4.65), pya.DPoint(0.24, 4.49), pya.DPoint(0.08, 4.49)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.42, 4.49), pya.DPoint(0.42, 4.65), pya.DPoint(0.58, 4.65), pya.DPoint(0.58, 4.49), pya.DPoint(0.42, 4.49)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.08, 5), pya.DPoint(0.08, 5.16), pya.DPoint(0.24, 5.16), pya.DPoint(0.24, 5), pya.DPoint(0.08, 5)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(-0.39, 2.45), pya.DPoint(-0.39, 2.61), pya.DPoint(-0.23, 2.61), pya.DPoint(-0.23, 2.45), pya.DPoint(-0.39, 2.45)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(-0.39, 2.79), pya.DPoint(-0.39, 2.95), pya.DPoint(-0.23, 2.95), pya.DPoint(-0.23, 2.79), pya.DPoint(-0.39, 2.79)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(-0.39, 3.13), pya.DPoint(-0.39, 3.29), pya.DPoint(-0.23, 3.29), pya.DPoint(-0.23, 3.13), pya.DPoint(-0.39, 3.13)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(-0.39, 3.47), pya.DPoint(-0.39, 3.63), pya.DPoint(-0.23, 3.63), pya.DPoint(-0.23, 3.47), pya.DPoint(-0.39, 3.47)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(-0.39, 3.81), pya.DPoint(-0.39, 3.97), pya.DPoint(-0.23, 3.97), pya.DPoint(-0.23, 3.81), pya.DPoint(-0.39, 3.81)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(-0.39, 4.15), pya.DPoint(-0.39, 4.31), pya.DPoint(-0.23, 4.31), pya.DPoint(-0.23, 4.15), pya.DPoint(-0.39, 4.15)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.42, 5), pya.DPoint(0.42, 5.16), pya.DPoint(0.58, 5.16), pya.DPoint(0.58, 5), pya.DPoint(0.42, 5)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.76, 5), pya.DPoint(0.76, 5.16), pya.DPoint(0.92, 5.16), pya.DPoint(0.92, 5), pya.DPoint(0.76, 5)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(1.1, 5), pya.DPoint(1.1, 5.16), pya.DPoint(1.26, 5.16), pya.DPoint(1.26, 5), pya.DPoint(1.1, 5)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(1.44, 5), pya.DPoint(1.44, 5.16), pya.DPoint(1.6, 5.16), pya.DPoint(1.6, 5), pya.DPoint(1.44, 5)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(1.78, 5), pya.DPoint(1.78, 5.16), pya.DPoint(1.94, 5.16), pya.DPoint(1.94, 5), pya.DPoint(1.78, 5)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(2.12, 5), pya.DPoint(2.12, 5.16), pya.DPoint(2.28, 5.16), pya.DPoint(2.28, 5), pya.DPoint(2.12, 5)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(5.52, 0.07), pya.DPoint(5.52, 0.23), pya.DPoint(5.68, 0.23), pya.DPoint(5.68, 0.07), pya.DPoint(5.52, 0.07)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(5.86, 0.07), pya.DPoint(5.86, 0.23), pya.DPoint(6.02, 0.23), pya.DPoint(6.02, 0.07), pya.DPoint(5.86, 0.07)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(6.2, 0.07), pya.DPoint(6.2, 0.23), pya.DPoint(6.36, 0.23), pya.DPoint(6.36, 0.07), pya.DPoint(6.2, 0.07)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(6.54, 0.07), pya.DPoint(6.54, 0.23), pya.DPoint(6.7, 0.23), pya.DPoint(6.7, 0.07), pya.DPoint(6.54, 0.07)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(6.88, 0.07), pya.DPoint(6.88, 0.23), pya.DPoint(7.04, 0.23), pya.DPoint(7.04, 0.07), pya.DPoint(6.88, 0.07)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.08, 0.07), pya.DPoint(0.08, 0.23), pya.DPoint(0.24, 0.23), pya.DPoint(0.24, 0.07), pya.DPoint(0.08, 0.07)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.42, 0.07), pya.DPoint(0.42, 0.23), pya.DPoint(0.58, 0.23), pya.DPoint(0.58, 0.07), pya.DPoint(0.42, 0.07)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.08, -0.44), pya.DPoint(0.08, -0.28), pya.DPoint(0.24, -0.28), pya.DPoint(0.24, -0.44), pya.DPoint(0.08, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.42, -0.44), pya.DPoint(0.42, -0.28), pya.DPoint(0.58, -0.28), pya.DPoint(0.58, -0.44), pya.DPoint(0.42, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.76, -0.44), pya.DPoint(0.76, -0.28), pya.DPoint(0.92, -0.28), pya.DPoint(0.92, -0.44), pya.DPoint(0.76, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(1.1, -0.44), pya.DPoint(1.1, -0.28), pya.DPoint(1.26, -0.28), pya.DPoint(1.26, -0.44), pya.DPoint(1.1, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(1.44, -0.44), pya.DPoint(1.44, -0.28), pya.DPoint(1.6, -0.28), pya.DPoint(1.6, -0.44), pya.DPoint(1.44, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(1.78, -0.44), pya.DPoint(1.78, -0.28), pya.DPoint(1.94, -0.28), pya.DPoint(1.94, -0.44), pya.DPoint(1.78, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(2.12, -0.44), pya.DPoint(2.12, -0.28), pya.DPoint(2.28, -0.28), pya.DPoint(2.28, -0.44), pya.DPoint(2.12, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(2.46, -0.44), pya.DPoint(2.46, -0.28), pya.DPoint(2.62, -0.28), pya.DPoint(2.62, -0.44), pya.DPoint(2.46, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(2.8, -0.44), pya.DPoint(2.8, -0.28), pya.DPoint(2.96, -0.28), pya.DPoint(2.96, -0.44), pya.DPoint(2.8, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(3.14, -0.44), pya.DPoint(3.14, -0.28), pya.DPoint(3.3, -0.28), pya.DPoint(3.3, -0.44), pya.DPoint(3.14, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(3.48, -0.44), pya.DPoint(3.48, -0.28), pya.DPoint(3.64, -0.28), pya.DPoint(3.64, -0.44), pya.DPoint(3.48, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(3.82, -0.44), pya.DPoint(3.82, -0.28), pya.DPoint(3.98, -0.28), pya.DPoint(3.98, -0.44), pya.DPoint(3.82, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(4.16, -0.44), pya.DPoint(4.16, -0.28), pya.DPoint(4.32, -0.28), pya.DPoint(4.32, -0.44), pya.DPoint(4.16, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(4.5, -0.44), pya.DPoint(4.5, -0.28), pya.DPoint(4.66, -0.28), pya.DPoint(4.66, -0.44), pya.DPoint(4.5, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(4.84, -0.44), pya.DPoint(4.84, -0.28), pya.DPoint(5, -0.28), pya.DPoint(5, -0.44), pya.DPoint(4.84, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(5.18, -0.44), pya.DPoint(5.18, -0.28), pya.DPoint(5.34, -0.28), pya.DPoint(5.34, -0.44), pya.DPoint(5.18, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(5.52, -0.44), pya.DPoint(5.52, -0.28), pya.DPoint(5.68, -0.28), pya.DPoint(5.68, -0.44), pya.DPoint(5.52, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(5.86, -0.44), pya.DPoint(5.86, -0.28), pya.DPoint(6.02, -0.28), pya.DPoint(6.02, -0.44), pya.DPoint(5.86, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(6.2, -0.44), pya.DPoint(6.2, -0.28), pya.DPoint(6.36, -0.28), pya.DPoint(6.36, -0.44), pya.DPoint(6.2, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(6.54, -0.44), pya.DPoint(6.54, -0.28), pya.DPoint(6.7, -0.28), pya.DPoint(6.7, -0.44), pya.DPoint(6.54, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(6.88, -0.44), pya.DPoint(6.88, -0.28), pya.DPoint(7.04, -0.28), pya.DPoint(7.04, -0.44), pya.DPoint(6.88, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.76, 0.07), pya.DPoint(0.76, 0.23), pya.DPoint(0.92, 0.23), pya.DPoint(0.92, 0.07), pya.DPoint(0.76, 0.07)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(1.1, 0.07), pya.DPoint(1.1, 0.23), pya.DPoint(1.26, 0.23), pya.DPoint(1.26, 0.07), pya.DPoint(1.1, 0.07)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(-0.39, 0.41), pya.DPoint(-0.39, 0.57), pya.DPoint(-0.23, 0.57), pya.DPoint(-0.23, 0.41), pya.DPoint(-0.39, 0.41)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(-0.39, 0.75), pya.DPoint(-0.39, 0.91), pya.DPoint(-0.23, 0.91), pya.DPoint(-0.23, 0.75), pya.DPoint(-0.39, 0.75)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(-0.39, 1.09), pya.DPoint(-0.39, 1.25), pya.DPoint(-0.23, 1.25), pya.DPoint(-0.23, 1.09), pya.DPoint(-0.39, 1.09)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(-0.39, 1.43), pya.DPoint(-0.39, 1.59), pya.DPoint(-0.23, 1.59), pya.DPoint(-0.23, 1.43), pya.DPoint(-0.39, 1.43)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(-0.39, 1.77), pya.DPoint(-0.39, 1.93), pya.DPoint(-0.23, 1.93), pya.DPoint(-0.23, 1.77), pya.DPoint(-0.39, 1.77)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(-0.39, 2.11), pya.DPoint(-0.39, 2.27), pya.DPoint(-0.23, 2.27), pya.DPoint(-0.23, 2.11), pya.DPoint(-0.39, 2.11)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(1.44, 0.07), pya.DPoint(1.44, 0.23), pya.DPoint(1.6, 0.23), pya.DPoint(1.6, 0.07), pya.DPoint(1.44, 0.07)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(1.78, 0.07), pya.DPoint(1.78, 0.23), pya.DPoint(1.94, 0.23), pya.DPoint(1.94, 0.07), pya.DPoint(1.78, 0.07)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(2.12, 0.07), pya.DPoint(2.12, 0.23), pya.DPoint(2.28, 0.23), pya.DPoint(2.28, 0.07), pya.DPoint(2.12, 0.07)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(2.46, 0.07), pya.DPoint(2.46, 0.23), pya.DPoint(2.62, 0.23), pya.DPoint(2.62, 0.07), pya.DPoint(2.46, 0.07)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(2.8, 0.07), pya.DPoint(2.8, 0.23), pya.DPoint(2.96, 0.23), pya.DPoint(2.96, 0.07), pya.DPoint(2.8, 0.07)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(3.14, 0.07), pya.DPoint(3.14, 0.23), pya.DPoint(3.3, 0.23), pya.DPoint(3.3, 0.07), pya.DPoint(3.14, 0.07)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(3.48, 0.07), pya.DPoint(3.48, 0.23), pya.DPoint(3.64, 0.23), pya.DPoint(3.64, 0.07), pya.DPoint(3.48, 0.07)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(3.82, 0.07), pya.DPoint(3.82, 0.23), pya.DPoint(3.98, 0.23), pya.DPoint(3.98, 0.07), pya.DPoint(3.82, 0.07)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(4.16, 0.07), pya.DPoint(4.16, 0.23), pya.DPoint(4.32, 0.23), pya.DPoint(4.32, 0.07), pya.DPoint(4.16, 0.07)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(4.5, 0.07), pya.DPoint(4.5, 0.23), pya.DPoint(4.66, 0.23), pya.DPoint(4.66, 0.07), pya.DPoint(4.5, 0.07)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(4.84, 0.07), pya.DPoint(4.84, 0.23), pya.DPoint(5, 0.23), pya.DPoint(5, 0.07), pya.DPoint(4.84, 0.07)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(5.18, 0.07), pya.DPoint(5.18, 0.23), pya.DPoint(5.34, 0.23), pya.DPoint(5.34, 0.07), pya.DPoint(5.18, 0.07)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(7.56, 0.07), pya.DPoint(7.56, 0.23), pya.DPoint(7.72, 0.23), pya.DPoint(7.72, 0.07), pya.DPoint(7.56, 0.07)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(7.9, 0.07), pya.DPoint(7.9, 0.23), pya.DPoint(8.06, 0.23), pya.DPoint(8.06, 0.07), pya.DPoint(7.9, 0.07)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(7.56, -0.44), pya.DPoint(7.56, -0.28), pya.DPoint(7.72, -0.28), pya.DPoint(7.72, -0.44), pya.DPoint(7.56, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(7.9, -0.44), pya.DPoint(7.9, -0.28), pya.DPoint(8.06, -0.28), pya.DPoint(8.06, -0.44), pya.DPoint(7.9, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(8.24, -0.44), pya.DPoint(8.24, -0.28), pya.DPoint(8.4, -0.28), pya.DPoint(8.4, -0.44), pya.DPoint(8.24, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(8.58, -0.44), pya.DPoint(8.58, -0.28), pya.DPoint(8.74, -0.28), pya.DPoint(8.74, -0.44), pya.DPoint(8.58, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(8.92, -0.44), pya.DPoint(8.92, -0.28), pya.DPoint(9.08, -0.28), pya.DPoint(9.08, -0.44), pya.DPoint(8.92, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(9.26, -0.44), pya.DPoint(9.26, -0.28), pya.DPoint(9.42, -0.28), pya.DPoint(9.42, -0.44), pya.DPoint(9.26, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(9.6, -0.44), pya.DPoint(9.6, -0.28), pya.DPoint(9.76, -0.28), pya.DPoint(9.76, -0.44), pya.DPoint(9.6, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(9.94, -0.44), pya.DPoint(9.94, -0.28), pya.DPoint(10.1, -0.28), pya.DPoint(10.1, -0.44), pya.DPoint(9.94, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(10.28, -0.44), pya.DPoint(10.28, -0.28), pya.DPoint(10.44, -0.28), pya.DPoint(10.44, -0.44), pya.DPoint(10.28, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(10.62, -0.44), pya.DPoint(10.62, -0.28), pya.DPoint(10.78, -0.28), pya.DPoint(10.78, -0.44), pya.DPoint(10.62, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(10.96, -0.44), pya.DPoint(10.96, -0.28), pya.DPoint(11.12, -0.28), pya.DPoint(11.12, -0.44), pya.DPoint(10.96, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(11.3, -0.44), pya.DPoint(11.3, -0.28), pya.DPoint(11.46, -0.28), pya.DPoint(11.46, -0.44), pya.DPoint(11.3, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(11.64, -0.44), pya.DPoint(11.64, -0.28), pya.DPoint(11.8, -0.28), pya.DPoint(11.8, -0.44), pya.DPoint(11.64, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(11.98, -0.44), pya.DPoint(11.98, -0.28), pya.DPoint(12.14, -0.28), pya.DPoint(12.14, -0.44), pya.DPoint(11.98, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(12.32, -0.44), pya.DPoint(12.32, -0.28), pya.DPoint(12.48, -0.28), pya.DPoint(12.48, -0.44), pya.DPoint(12.32, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(12.66, -0.44), pya.DPoint(12.66, -0.28), pya.DPoint(12.82, -0.28), pya.DPoint(12.82, -0.44), pya.DPoint(12.66, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(13, -0.44), pya.DPoint(13, -0.28), pya.DPoint(13.16, -0.28), pya.DPoint(13.16, -0.44), pya.DPoint(13, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(13.34, -0.44), pya.DPoint(13.34, -0.28), pya.DPoint(13.5, -0.28), pya.DPoint(13.5, -0.44), pya.DPoint(13.34, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(13.68, -0.44), pya.DPoint(13.68, -0.28), pya.DPoint(13.84, -0.28), pya.DPoint(13.84, -0.44), pya.DPoint(13.68, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(14.02, -0.44), pya.DPoint(14.02, -0.28), pya.DPoint(14.18, -0.28), pya.DPoint(14.18, -0.44), pya.DPoint(14.02, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(14.36, -0.44), pya.DPoint(14.36, -0.28), pya.DPoint(14.52, -0.28), pya.DPoint(14.52, -0.44), pya.DPoint(14.36, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(8.24, 0.07), pya.DPoint(8.24, 0.23), pya.DPoint(8.4, 0.23), pya.DPoint(8.4, 0.07), pya.DPoint(8.24, 0.07)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(8.58, 0.07), pya.DPoint(8.58, 0.23), pya.DPoint(8.74, 0.23), pya.DPoint(8.74, 0.07), pya.DPoint(8.58, 0.07)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(8.92, 0.07), pya.DPoint(8.92, 0.23), pya.DPoint(9.08, 0.23), pya.DPoint(9.08, 0.07), pya.DPoint(8.92, 0.07)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(9.26, 0.07), pya.DPoint(9.26, 0.23), pya.DPoint(9.42, 0.23), pya.DPoint(9.42, 0.07), pya.DPoint(9.26, 0.07)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(9.6, 0.07), pya.DPoint(9.6, 0.23), pya.DPoint(9.76, 0.23), pya.DPoint(9.76, 0.07), pya.DPoint(9.6, 0.07)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(9.94, 0.07), pya.DPoint(9.94, 0.23), pya.DPoint(10.1, 0.23), pya.DPoint(10.1, 0.07), pya.DPoint(9.94, 0.07)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(10.28, 0.07), pya.DPoint(10.28, 0.23), pya.DPoint(10.44, 0.23), pya.DPoint(10.44, 0.07), pya.DPoint(10.28, 0.07)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(10.62, 0.07), pya.DPoint(10.62, 0.23), pya.DPoint(10.78, 0.23), pya.DPoint(10.78, 0.07), pya.DPoint(10.62, 0.07)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(10.96, 0.07), pya.DPoint(10.96, 0.23), pya.DPoint(11.12, 0.23), pya.DPoint(11.12, 0.07), pya.DPoint(10.96, 0.07)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(11.3, 0.07), pya.DPoint(11.3, 0.23), pya.DPoint(11.46, 0.23), pya.DPoint(11.46, 0.07), pya.DPoint(11.3, 0.07)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(11.64, 0.07), pya.DPoint(11.64, 0.23), pya.DPoint(11.8, 0.23), pya.DPoint(11.8, 0.07), pya.DPoint(11.64, 0.07)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(11.98, 0.07), pya.DPoint(11.98, 0.23), pya.DPoint(12.14, 0.23), pya.DPoint(12.14, 0.07), pya.DPoint(11.98, 0.07)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(12.32, 0.07), pya.DPoint(12.32, 0.23), pya.DPoint(12.48, 0.23), pya.DPoint(12.48, 0.07), pya.DPoint(12.32, 0.07)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(14.82, 0.41), pya.DPoint(14.82, 0.57), pya.DPoint(14.98, 0.57), pya.DPoint(14.98, 0.41), pya.DPoint(14.82, 0.41)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(14.82, 0.75), pya.DPoint(14.82, 0.91), pya.DPoint(14.98, 0.91), pya.DPoint(14.98, 0.75), pya.DPoint(14.82, 0.75)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(14.82, 1.09), pya.DPoint(14.82, 1.25), pya.DPoint(14.98, 1.25), pya.DPoint(14.98, 1.09), pya.DPoint(14.82, 1.09)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(14.82, 1.43), pya.DPoint(14.82, 1.59), pya.DPoint(14.98, 1.59), pya.DPoint(14.98, 1.43), pya.DPoint(14.82, 1.43)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(14.82, 1.77), pya.DPoint(14.82, 1.93), pya.DPoint(14.98, 1.93), pya.DPoint(14.98, 1.77), pya.DPoint(14.82, 1.77)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(14.82, 2.11), pya.DPoint(14.82, 2.27), pya.DPoint(14.98, 2.27), pya.DPoint(14.98, 2.11), pya.DPoint(14.82, 2.11)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(12.66, 0.07), pya.DPoint(12.66, 0.23), pya.DPoint(12.82, 0.23), pya.DPoint(12.82, 0.07), pya.DPoint(12.66, 0.07)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(13, 0.07), pya.DPoint(13, 0.23), pya.DPoint(13.16, 0.23), pya.DPoint(13.16, 0.07), pya.DPoint(13, 0.07)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(13.34, 0.07), pya.DPoint(13.34, 0.23), pya.DPoint(13.5, 0.23), pya.DPoint(13.5, 0.07), pya.DPoint(13.34, 0.07)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(13.68, 0.07), pya.DPoint(13.68, 0.23), pya.DPoint(13.84, 0.23), pya.DPoint(13.84, 0.07), pya.DPoint(13.68, 0.07)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(14.02, 0.07), pya.DPoint(14.02, 0.23), pya.DPoint(14.18, 0.23), pya.DPoint(14.18, 0.07), pya.DPoint(14.02, 0.07)]))
cell_pmos_buffer_cap.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(14.36, 0.07), pya.DPoint(14.36, 0.23), pya.DPoint(14.52, 0.23), pya.DPoint(14.52, 0.07), pya.DPoint(14.36, 0.07)]))
cell_pmos_buffer_cap.shapes(L_Activ).insert(
    pya.DPolygon([pya.DPoint(0, 0), pya.DPoint(0, 4.72), pya.DPoint(14.6, 4.72), pya.DPoint(14.6, 0), pya.DPoint(0, 0)]))
cell_pmos_buffer_cap.shapes(L_Activ).insert(
    pya.DPolygon([pya.DPoint(0, 0), pya.DPoint(0, 0.3), pya.DPoint(0.3, 0.3), pya.DPoint(0.3, 0), pya.DPoint(0, 0)]))
cell_pmos_buffer_cap.shapes(L_Activ).insert(
    pya.DPolygon([pya.DPoint(0, 4.42), pya.DPoint(0, 4.72), pya.DPoint(0.3, 4.72), pya.DPoint(0.3, 4.42), pya.DPoint(0, 4.42)]))
cell_pmos_buffer_cap.shapes(L_Activ).insert(
    pya.DPolygon([pya.DPoint(0, -0.51), pya.DPoint(0, -0.21), pya.DPoint(14.6, -0.21), pya.DPoint(14.6, -0.51), pya.DPoint(0, -0.51)]))
cell_pmos_buffer_cap.shapes(L_Activ).insert(
    pya.DPolygon([pya.DPoint(0, 4.93), pya.DPoint(0, 5.23), pya.DPoint(14.6, 5.23), pya.DPoint(14.6, 4.93), pya.DPoint(0, 4.93)]))
cell_pmos_buffer_cap.shapes(L_GatPoly).insert(
    pya.DPolygon([pya.DPoint(-0.18, 0.34), pya.DPoint(-0.18, 4.38), pya.DPoint(14.78, 4.38), pya.DPoint(14.78, 0.34), pya.DPoint(-0.18, 0.34)]))
cell_pmos_buffer_cap.shapes(L_GatPoly).insert(
    pya.DPolygon([pya.DPoint(-0.46, 0.34), pya.DPoint(-0.46, 4.38), pya.DPoint(15.06, 4.38), pya.DPoint(15.06, 0.34), pya.DPoint(-0.46, 0.34)]))
cell_pmos_buffer_cap.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(-0.4, -0.18), pya.DPoint(-0.4, 4.9), pya.DPoint(15, 4.9), pya.DPoint(15, -0.18), pya.DPoint(-0.4, -0.18)]))
cell_pmos_buffer_cap.shapes(L_NWell).insert(
    pya.DPolygon([pya.DPoint(-0.62, -1.13), pya.DPoint(-0.62, 5.85), pya.DPoint(15.22, 5.85), pya.DPoint(15.22, -1.13), pya.DPoint(-0.62, -1.13)]))
cell_pmos_buffer_cap.shapes(L_Metal1_pin).insert(
    pya.DPolygon([pya.DPoint(0, 0.07), pya.DPoint(0, 0.23), pya.DPoint(14.6, 0.23), pya.DPoint(14.6, 0.07), pya.DPoint(0, 0.07)]))
cell_pmos_buffer_cap.shapes(L_Metal1_pin).insert(
    pya.DPolygon([pya.DPoint(0, 4.49), pya.DPoint(0, 4.65), pya.DPoint(14.6, 4.65), pya.DPoint(14.6, 4.49), pya.DPoint(0, 4.49)]))
cell_pmos_buffer_cap.shapes(L_ThickGateOx).insert(
    pya.DPolygon([pya.DPoint(-0.62, -1.13), pya.DPoint(-0.62, 5.85), pya.DPoint(15.22, 5.85), pya.DPoint(15.22, -1.13), pya.DPoint(-0.62, -1.13)]))
cell_pmos_buffer_cap.shapes(L_pmos).insert(
    pya.DPolygon([pya.DPoint(-0.18, 0.34), pya.DPoint(-0.18, 4.38), pya.DPoint(14.78, 4.38), pya.DPoint(14.78, 0.34), pya.DPoint(-0.18, 0.34)]))
cell_pmos_buffer_cap.shapes(L_NoBuLay).insert(
    pya.DPolygon([pya.DPoint(0, 4.42), pya.DPoint(0, 4.72), pya.DPoint(0.3, 4.72), pya.DPoint(0.3, 4.42), pya.DPoint(0, 4.42)]))
cell_pmos_buffer_cap.shapes(L_GatPoly_pin).insert(
    pya.DPolygon([pya.DPoint(-0.18, 0.34), pya.DPoint(-0.18, 4.38), pya.DPoint(14.78, 4.38), pya.DPoint(14.78, 0.34), pya.DPoint(-0.18, 0.34)]))

# === via_stack$8 ===
cell_via_stack_8.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(-0.865, -0.865), pya.DPoint(-0.865, 0.865), pya.DPoint(0.865, 0.865), pya.DPoint(0.865, -0.865), pya.DPoint(-0.865, -0.865)]))
cell_via_stack_8.shapes(L_Metal2).insert(
    pya.DPolygon([pya.DPoint(-0.865, -0.865), pya.DPoint(-0.865, 0.865), pya.DPoint(0.865, 0.865), pya.DPoint(0.865, -0.865), pya.DPoint(-0.865, -0.865)]))
cell_via_stack_8.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(-0.815, -0.815), pya.DPoint(-0.815, -0.625), pya.DPoint(-0.625, -0.625), pya.DPoint(-0.625, -0.815), pya.DPoint(-0.815, -0.815)]))
cell_via_stack_8.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(-0.815, -0.335), pya.DPoint(-0.815, -0.145), pya.DPoint(-0.625, -0.145), pya.DPoint(-0.625, -0.335), pya.DPoint(-0.815, -0.335)]))
cell_via_stack_8.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(-0.815, 0.145), pya.DPoint(-0.815, 0.335), pya.DPoint(-0.625, 0.335), pya.DPoint(-0.625, 0.145), pya.DPoint(-0.815, 0.145)]))
cell_via_stack_8.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(-0.815, 0.625), pya.DPoint(-0.815, 0.815), pya.DPoint(-0.625, 0.815), pya.DPoint(-0.625, 0.625), pya.DPoint(-0.815, 0.625)]))
cell_via_stack_8.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(-0.335, -0.815), pya.DPoint(-0.335, -0.625), pya.DPoint(-0.145, -0.625), pya.DPoint(-0.145, -0.815), pya.DPoint(-0.335, -0.815)]))
cell_via_stack_8.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(-0.335, -0.335), pya.DPoint(-0.335, -0.145), pya.DPoint(-0.145, -0.145), pya.DPoint(-0.145, -0.335), pya.DPoint(-0.335, -0.335)]))
cell_via_stack_8.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(-0.335, 0.145), pya.DPoint(-0.335, 0.335), pya.DPoint(-0.145, 0.335), pya.DPoint(-0.145, 0.145), pya.DPoint(-0.335, 0.145)]))
cell_via_stack_8.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(-0.335, 0.625), pya.DPoint(-0.335, 0.815), pya.DPoint(-0.145, 0.815), pya.DPoint(-0.145, 0.625), pya.DPoint(-0.335, 0.625)]))
cell_via_stack_8.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(0.145, -0.815), pya.DPoint(0.145, -0.625), pya.DPoint(0.335, -0.625), pya.DPoint(0.335, -0.815), pya.DPoint(0.145, -0.815)]))
cell_via_stack_8.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(0.145, -0.335), pya.DPoint(0.145, -0.145), pya.DPoint(0.335, -0.145), pya.DPoint(0.335, -0.335), pya.DPoint(0.145, -0.335)]))
cell_via_stack_8.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(0.145, 0.145), pya.DPoint(0.145, 0.335), pya.DPoint(0.335, 0.335), pya.DPoint(0.335, 0.145), pya.DPoint(0.145, 0.145)]))
cell_via_stack_8.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(0.145, 0.625), pya.DPoint(0.145, 0.815), pya.DPoint(0.335, 0.815), pya.DPoint(0.335, 0.625), pya.DPoint(0.145, 0.625)]))
cell_via_stack_8.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(0.625, -0.815), pya.DPoint(0.625, -0.625), pya.DPoint(0.815, -0.625), pya.DPoint(0.815, -0.815), pya.DPoint(0.625, -0.815)]))
cell_via_stack_8.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(0.625, -0.335), pya.DPoint(0.625, -0.145), pya.DPoint(0.815, -0.145), pya.DPoint(0.815, -0.335), pya.DPoint(0.625, -0.335)]))
cell_via_stack_8.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(0.625, 0.145), pya.DPoint(0.625, 0.335), pya.DPoint(0.815, 0.335), pya.DPoint(0.815, 0.145), pya.DPoint(0.625, 0.145)]))
cell_via_stack_8.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(0.625, 0.625), pya.DPoint(0.625, 0.815), pya.DPoint(0.815, 0.815), pya.DPoint(0.815, 0.625), pya.DPoint(0.625, 0.625)]))
cell_via_stack_8.shapes(L_Metal5).insert(
    pya.DPolygon([pya.DPoint(-0.865, -0.865), pya.DPoint(-0.865, 0.865), pya.DPoint(0.865, 0.865), pya.DPoint(0.865, -0.865), pya.DPoint(-0.865, -0.865)]))
cell_via_stack_8.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(-0.815, -0.815), pya.DPoint(-0.815, -0.625), pya.DPoint(-0.625, -0.625), pya.DPoint(-0.625, -0.815), pya.DPoint(-0.815, -0.815)]))
cell_via_stack_8.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(-0.815, -0.335), pya.DPoint(-0.815, -0.145), pya.DPoint(-0.625, -0.145), pya.DPoint(-0.625, -0.335), pya.DPoint(-0.815, -0.335)]))
cell_via_stack_8.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(-0.815, 0.145), pya.DPoint(-0.815, 0.335), pya.DPoint(-0.625, 0.335), pya.DPoint(-0.625, 0.145), pya.DPoint(-0.815, 0.145)]))
cell_via_stack_8.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(-0.815, 0.625), pya.DPoint(-0.815, 0.815), pya.DPoint(-0.625, 0.815), pya.DPoint(-0.625, 0.625), pya.DPoint(-0.815, 0.625)]))
cell_via_stack_8.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(-0.335, -0.815), pya.DPoint(-0.335, -0.625), pya.DPoint(-0.145, -0.625), pya.DPoint(-0.145, -0.815), pya.DPoint(-0.335, -0.815)]))
cell_via_stack_8.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(-0.335, -0.335), pya.DPoint(-0.335, -0.145), pya.DPoint(-0.145, -0.145), pya.DPoint(-0.145, -0.335), pya.DPoint(-0.335, -0.335)]))
cell_via_stack_8.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(-0.335, 0.145), pya.DPoint(-0.335, 0.335), pya.DPoint(-0.145, 0.335), pya.DPoint(-0.145, 0.145), pya.DPoint(-0.335, 0.145)]))
cell_via_stack_8.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(-0.335, 0.625), pya.DPoint(-0.335, 0.815), pya.DPoint(-0.145, 0.815), pya.DPoint(-0.145, 0.625), pya.DPoint(-0.335, 0.625)]))
cell_via_stack_8.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(0.145, -0.815), pya.DPoint(0.145, -0.625), pya.DPoint(0.335, -0.625), pya.DPoint(0.335, -0.815), pya.DPoint(0.145, -0.815)]))
cell_via_stack_8.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(0.145, -0.335), pya.DPoint(0.145, -0.145), pya.DPoint(0.335, -0.145), pya.DPoint(0.335, -0.335), pya.DPoint(0.145, -0.335)]))
cell_via_stack_8.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(0.145, 0.145), pya.DPoint(0.145, 0.335), pya.DPoint(0.335, 0.335), pya.DPoint(0.335, 0.145), pya.DPoint(0.145, 0.145)]))
cell_via_stack_8.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(0.145, 0.625), pya.DPoint(0.145, 0.815), pya.DPoint(0.335, 0.815), pya.DPoint(0.335, 0.625), pya.DPoint(0.145, 0.625)]))
cell_via_stack_8.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(0.625, -0.815), pya.DPoint(0.625, -0.625), pya.DPoint(0.815, -0.625), pya.DPoint(0.815, -0.815), pya.DPoint(0.625, -0.815)]))
cell_via_stack_8.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(0.625, -0.335), pya.DPoint(0.625, -0.145), pya.DPoint(0.815, -0.145), pya.DPoint(0.815, -0.335), pya.DPoint(0.625, -0.335)]))
cell_via_stack_8.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(0.625, 0.145), pya.DPoint(0.625, 0.335), pya.DPoint(0.815, 0.335), pya.DPoint(0.815, 0.145), pya.DPoint(0.625, 0.145)]))
cell_via_stack_8.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(0.625, 0.625), pya.DPoint(0.625, 0.815), pya.DPoint(0.815, 0.815), pya.DPoint(0.815, 0.625), pya.DPoint(0.625, 0.625)]))

# === pmos_buffer_cap$1 ===
cell_pmos_buffer_cap_1.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(0, -0.44), pya.DPoint(0, 5.16), pya.DPoint(14.6, 5.16), pya.DPoint(14.6, -0.44), pya.DPoint(0, -0.44)]))
cell_pmos_buffer_cap_1.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(-0.39, 0.34), pya.DPoint(-0.39, 4.38), pya.DPoint(-0.23, 4.38), pya.DPoint(-0.23, 0.34), pya.DPoint(-0.39, 0.34)]))
cell_pmos_buffer_cap_1.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(14.82, 0.34), pya.DPoint(14.82, 4.38), pya.DPoint(14.98, 4.38), pya.DPoint(14.98, 0.34), pya.DPoint(14.82, 0.34)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(7.22, 0.07), pya.DPoint(7.22, 0.23), pya.DPoint(7.38, 0.23), pya.DPoint(7.38, 0.07), pya.DPoint(7.22, 0.07)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(7.22, 4.49), pya.DPoint(7.22, 4.65), pya.DPoint(7.38, 4.65), pya.DPoint(7.38, 4.49), pya.DPoint(7.22, 4.49)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(7.22, -0.44), pya.DPoint(7.22, -0.28), pya.DPoint(7.38, -0.28), pya.DPoint(7.38, -0.44), pya.DPoint(7.22, -0.44)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(7.22, 5), pya.DPoint(7.22, 5.16), pya.DPoint(7.38, 5.16), pya.DPoint(7.38, 5), pya.DPoint(7.22, 5)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(8.24, 4.49), pya.DPoint(8.24, 4.65), pya.DPoint(8.4, 4.65), pya.DPoint(8.4, 4.49), pya.DPoint(8.24, 4.49)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(8.58, 4.49), pya.DPoint(8.58, 4.65), pya.DPoint(8.74, 4.65), pya.DPoint(8.74, 4.49), pya.DPoint(8.58, 4.49)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(8.92, 4.49), pya.DPoint(8.92, 4.65), pya.DPoint(9.08, 4.65), pya.DPoint(9.08, 4.49), pya.DPoint(8.92, 4.49)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(9.26, 4.49), pya.DPoint(9.26, 4.65), pya.DPoint(9.42, 4.65), pya.DPoint(9.42, 4.49), pya.DPoint(9.26, 4.49)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(9.6, 4.49), pya.DPoint(9.6, 4.65), pya.DPoint(9.76, 4.65), pya.DPoint(9.76, 4.49), pya.DPoint(9.6, 4.49)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(9.94, 4.49), pya.DPoint(9.94, 4.65), pya.DPoint(10.1, 4.65), pya.DPoint(10.1, 4.49), pya.DPoint(9.94, 4.49)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(10.28, 4.49), pya.DPoint(10.28, 4.65), pya.DPoint(10.44, 4.65), pya.DPoint(10.44, 4.49), pya.DPoint(10.28, 4.49)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(10.62, 4.49), pya.DPoint(10.62, 4.65), pya.DPoint(10.78, 4.65), pya.DPoint(10.78, 4.49), pya.DPoint(10.62, 4.49)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(10.96, 4.49), pya.DPoint(10.96, 4.65), pya.DPoint(11.12, 4.65), pya.DPoint(11.12, 4.49), pya.DPoint(10.96, 4.49)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(11.3, 4.49), pya.DPoint(11.3, 4.65), pya.DPoint(11.46, 4.65), pya.DPoint(11.46, 4.49), pya.DPoint(11.3, 4.49)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(11.64, 4.49), pya.DPoint(11.64, 4.65), pya.DPoint(11.8, 4.65), pya.DPoint(11.8, 4.49), pya.DPoint(11.64, 4.49)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(11.98, 4.49), pya.DPoint(11.98, 4.65), pya.DPoint(12.14, 4.65), pya.DPoint(12.14, 4.49), pya.DPoint(11.98, 4.49)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(12.32, 4.49), pya.DPoint(12.32, 4.65), pya.DPoint(12.48, 4.65), pya.DPoint(12.48, 4.49), pya.DPoint(12.32, 4.49)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(12.66, 4.49), pya.DPoint(12.66, 4.65), pya.DPoint(12.82, 4.65), pya.DPoint(12.82, 4.49), pya.DPoint(12.66, 4.49)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(13, 4.49), pya.DPoint(13, 4.65), pya.DPoint(13.16, 4.65), pya.DPoint(13.16, 4.49), pya.DPoint(13, 4.49)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(13.34, 4.49), pya.DPoint(13.34, 4.65), pya.DPoint(13.5, 4.65), pya.DPoint(13.5, 4.49), pya.DPoint(13.34, 4.49)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(13.68, 4.49), pya.DPoint(13.68, 4.65), pya.DPoint(13.84, 4.65), pya.DPoint(13.84, 4.49), pya.DPoint(13.68, 4.49)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(14.02, 4.49), pya.DPoint(14.02, 4.65), pya.DPoint(14.18, 4.65), pya.DPoint(14.18, 4.49), pya.DPoint(14.02, 4.49)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(14.36, 4.49), pya.DPoint(14.36, 4.65), pya.DPoint(14.52, 4.65), pya.DPoint(14.52, 4.49), pya.DPoint(14.36, 4.49)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(7.56, 4.49), pya.DPoint(7.56, 4.65), pya.DPoint(7.72, 4.65), pya.DPoint(7.72, 4.49), pya.DPoint(7.56, 4.49)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(7.9, 4.49), pya.DPoint(7.9, 4.65), pya.DPoint(8.06, 4.65), pya.DPoint(8.06, 4.49), pya.DPoint(7.9, 4.49)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(7.56, 5), pya.DPoint(7.56, 5.16), pya.DPoint(7.72, 5.16), pya.DPoint(7.72, 5), pya.DPoint(7.56, 5)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(7.9, 5), pya.DPoint(7.9, 5.16), pya.DPoint(8.06, 5.16), pya.DPoint(8.06, 5), pya.DPoint(7.9, 5)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(8.24, 5), pya.DPoint(8.24, 5.16), pya.DPoint(8.4, 5.16), pya.DPoint(8.4, 5), pya.DPoint(8.24, 5)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(8.58, 5), pya.DPoint(8.58, 5.16), pya.DPoint(8.74, 5.16), pya.DPoint(8.74, 5), pya.DPoint(8.58, 5)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(8.92, 5), pya.DPoint(8.92, 5.16), pya.DPoint(9.08, 5.16), pya.DPoint(9.08, 5), pya.DPoint(8.92, 5)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(9.26, 5), pya.DPoint(9.26, 5.16), pya.DPoint(9.42, 5.16), pya.DPoint(9.42, 5), pya.DPoint(9.26, 5)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(9.6, 5), pya.DPoint(9.6, 5.16), pya.DPoint(9.76, 5.16), pya.DPoint(9.76, 5), pya.DPoint(9.6, 5)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(9.94, 5), pya.DPoint(9.94, 5.16), pya.DPoint(10.1, 5.16), pya.DPoint(10.1, 5), pya.DPoint(9.94, 5)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(10.28, 5), pya.DPoint(10.28, 5.16), pya.DPoint(10.44, 5.16), pya.DPoint(10.44, 5), pya.DPoint(10.28, 5)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(10.62, 5), pya.DPoint(10.62, 5.16), pya.DPoint(10.78, 5.16), pya.DPoint(10.78, 5), pya.DPoint(10.62, 5)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(10.96, 5), pya.DPoint(10.96, 5.16), pya.DPoint(11.12, 5.16), pya.DPoint(11.12, 5), pya.DPoint(10.96, 5)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(11.3, 5), pya.DPoint(11.3, 5.16), pya.DPoint(11.46, 5.16), pya.DPoint(11.46, 5), pya.DPoint(11.3, 5)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(11.64, 5), pya.DPoint(11.64, 5.16), pya.DPoint(11.8, 5.16), pya.DPoint(11.8, 5), pya.DPoint(11.64, 5)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(11.98, 5), pya.DPoint(11.98, 5.16), pya.DPoint(12.14, 5.16), pya.DPoint(12.14, 5), pya.DPoint(11.98, 5)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(12.32, 5), pya.DPoint(12.32, 5.16), pya.DPoint(12.48, 5.16), pya.DPoint(12.48, 5), pya.DPoint(12.32, 5)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(12.66, 5), pya.DPoint(12.66, 5.16), pya.DPoint(12.82, 5.16), pya.DPoint(12.82, 5), pya.DPoint(12.66, 5)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(13, 5), pya.DPoint(13, 5.16), pya.DPoint(13.16, 5.16), pya.DPoint(13.16, 5), pya.DPoint(13, 5)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(13.34, 5), pya.DPoint(13.34, 5.16), pya.DPoint(13.5, 5.16), pya.DPoint(13.5, 5), pya.DPoint(13.34, 5)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(13.68, 5), pya.DPoint(13.68, 5.16), pya.DPoint(13.84, 5.16), pya.DPoint(13.84, 5), pya.DPoint(13.68, 5)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(14.02, 5), pya.DPoint(14.02, 5.16), pya.DPoint(14.18, 5.16), pya.DPoint(14.18, 5), pya.DPoint(14.02, 5)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(14.36, 5), pya.DPoint(14.36, 5.16), pya.DPoint(14.52, 5.16), pya.DPoint(14.52, 5), pya.DPoint(14.36, 5)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(14.82, 2.45), pya.DPoint(14.82, 2.61), pya.DPoint(14.98, 2.61), pya.DPoint(14.98, 2.45), pya.DPoint(14.82, 2.45)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(14.82, 2.79), pya.DPoint(14.82, 2.95), pya.DPoint(14.98, 2.95), pya.DPoint(14.98, 2.79), pya.DPoint(14.82, 2.79)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(14.82, 3.13), pya.DPoint(14.82, 3.29), pya.DPoint(14.98, 3.29), pya.DPoint(14.98, 3.13), pya.DPoint(14.82, 3.13)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(14.82, 3.47), pya.DPoint(14.82, 3.63), pya.DPoint(14.98, 3.63), pya.DPoint(14.98, 3.47), pya.DPoint(14.82, 3.47)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(14.82, 3.81), pya.DPoint(14.82, 3.97), pya.DPoint(14.98, 3.97), pya.DPoint(14.98, 3.81), pya.DPoint(14.82, 3.81)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(14.82, 4.15), pya.DPoint(14.82, 4.31), pya.DPoint(14.98, 4.31), pya.DPoint(14.98, 4.15), pya.DPoint(14.82, 4.15)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(2.46, 5), pya.DPoint(2.46, 5.16), pya.DPoint(2.62, 5.16), pya.DPoint(2.62, 5), pya.DPoint(2.46, 5)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(2.8, 5), pya.DPoint(2.8, 5.16), pya.DPoint(2.96, 5.16), pya.DPoint(2.96, 5), pya.DPoint(2.8, 5)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(3.14, 5), pya.DPoint(3.14, 5.16), pya.DPoint(3.3, 5.16), pya.DPoint(3.3, 5), pya.DPoint(3.14, 5)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(3.48, 5), pya.DPoint(3.48, 5.16), pya.DPoint(3.64, 5.16), pya.DPoint(3.64, 5), pya.DPoint(3.48, 5)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(3.82, 5), pya.DPoint(3.82, 5.16), pya.DPoint(3.98, 5.16), pya.DPoint(3.98, 5), pya.DPoint(3.82, 5)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(4.16, 5), pya.DPoint(4.16, 5.16), pya.DPoint(4.32, 5.16), pya.DPoint(4.32, 5), pya.DPoint(4.16, 5)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(4.5, 5), pya.DPoint(4.5, 5.16), pya.DPoint(4.66, 5.16), pya.DPoint(4.66, 5), pya.DPoint(4.5, 5)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(4.84, 5), pya.DPoint(4.84, 5.16), pya.DPoint(5, 5.16), pya.DPoint(5, 5), pya.DPoint(4.84, 5)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(5.18, 5), pya.DPoint(5.18, 5.16), pya.DPoint(5.34, 5.16), pya.DPoint(5.34, 5), pya.DPoint(5.18, 5)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(5.52, 5), pya.DPoint(5.52, 5.16), pya.DPoint(5.68, 5.16), pya.DPoint(5.68, 5), pya.DPoint(5.52, 5)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(5.86, 5), pya.DPoint(5.86, 5.16), pya.DPoint(6.02, 5.16), pya.DPoint(6.02, 5), pya.DPoint(5.86, 5)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(6.2, 5), pya.DPoint(6.2, 5.16), pya.DPoint(6.36, 5.16), pya.DPoint(6.36, 5), pya.DPoint(6.2, 5)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(6.54, 5), pya.DPoint(6.54, 5.16), pya.DPoint(6.7, 5.16), pya.DPoint(6.7, 5), pya.DPoint(6.54, 5)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(6.88, 5), pya.DPoint(6.88, 5.16), pya.DPoint(7.04, 5.16), pya.DPoint(7.04, 5), pya.DPoint(6.88, 5)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.76, 4.49), pya.DPoint(0.76, 4.65), pya.DPoint(0.92, 4.65), pya.DPoint(0.92, 4.49), pya.DPoint(0.76, 4.49)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(1.1, 4.49), pya.DPoint(1.1, 4.65), pya.DPoint(1.26, 4.65), pya.DPoint(1.26, 4.49), pya.DPoint(1.1, 4.49)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(1.44, 4.49), pya.DPoint(1.44, 4.65), pya.DPoint(1.6, 4.65), pya.DPoint(1.6, 4.49), pya.DPoint(1.44, 4.49)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(1.78, 4.49), pya.DPoint(1.78, 4.65), pya.DPoint(1.94, 4.65), pya.DPoint(1.94, 4.49), pya.DPoint(1.78, 4.49)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(2.12, 4.49), pya.DPoint(2.12, 4.65), pya.DPoint(2.28, 4.65), pya.DPoint(2.28, 4.49), pya.DPoint(2.12, 4.49)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(2.46, 4.49), pya.DPoint(2.46, 4.65), pya.DPoint(2.62, 4.65), pya.DPoint(2.62, 4.49), pya.DPoint(2.46, 4.49)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(2.8, 4.49), pya.DPoint(2.8, 4.65), pya.DPoint(2.96, 4.65), pya.DPoint(2.96, 4.49), pya.DPoint(2.8, 4.49)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(3.14, 4.49), pya.DPoint(3.14, 4.65), pya.DPoint(3.3, 4.65), pya.DPoint(3.3, 4.49), pya.DPoint(3.14, 4.49)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(3.48, 4.49), pya.DPoint(3.48, 4.65), pya.DPoint(3.64, 4.65), pya.DPoint(3.64, 4.49), pya.DPoint(3.48, 4.49)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(3.82, 4.49), pya.DPoint(3.82, 4.65), pya.DPoint(3.98, 4.65), pya.DPoint(3.98, 4.49), pya.DPoint(3.82, 4.49)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(4.16, 4.49), pya.DPoint(4.16, 4.65), pya.DPoint(4.32, 4.65), pya.DPoint(4.32, 4.49), pya.DPoint(4.16, 4.49)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(4.5, 4.49), pya.DPoint(4.5, 4.65), pya.DPoint(4.66, 4.65), pya.DPoint(4.66, 4.49), pya.DPoint(4.5, 4.49)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(4.84, 4.49), pya.DPoint(4.84, 4.65), pya.DPoint(5, 4.65), pya.DPoint(5, 4.49), pya.DPoint(4.84, 4.49)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(5.18, 4.49), pya.DPoint(5.18, 4.65), pya.DPoint(5.34, 4.65), pya.DPoint(5.34, 4.49), pya.DPoint(5.18, 4.49)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(5.52, 4.49), pya.DPoint(5.52, 4.65), pya.DPoint(5.68, 4.65), pya.DPoint(5.68, 4.49), pya.DPoint(5.52, 4.49)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(5.86, 4.49), pya.DPoint(5.86, 4.65), pya.DPoint(6.02, 4.65), pya.DPoint(6.02, 4.49), pya.DPoint(5.86, 4.49)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(6.2, 4.49), pya.DPoint(6.2, 4.65), pya.DPoint(6.36, 4.65), pya.DPoint(6.36, 4.49), pya.DPoint(6.2, 4.49)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(6.54, 4.49), pya.DPoint(6.54, 4.65), pya.DPoint(6.7, 4.65), pya.DPoint(6.7, 4.49), pya.DPoint(6.54, 4.49)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(6.88, 4.49), pya.DPoint(6.88, 4.65), pya.DPoint(7.04, 4.65), pya.DPoint(7.04, 4.49), pya.DPoint(6.88, 4.49)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.08, 4.49), pya.DPoint(0.08, 4.65), pya.DPoint(0.24, 4.65), pya.DPoint(0.24, 4.49), pya.DPoint(0.08, 4.49)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.42, 4.49), pya.DPoint(0.42, 4.65), pya.DPoint(0.58, 4.65), pya.DPoint(0.58, 4.49), pya.DPoint(0.42, 4.49)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.08, 5), pya.DPoint(0.08, 5.16), pya.DPoint(0.24, 5.16), pya.DPoint(0.24, 5), pya.DPoint(0.08, 5)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(-0.39, 2.45), pya.DPoint(-0.39, 2.61), pya.DPoint(-0.23, 2.61), pya.DPoint(-0.23, 2.45), pya.DPoint(-0.39, 2.45)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(-0.39, 2.79), pya.DPoint(-0.39, 2.95), pya.DPoint(-0.23, 2.95), pya.DPoint(-0.23, 2.79), pya.DPoint(-0.39, 2.79)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(-0.39, 3.13), pya.DPoint(-0.39, 3.29), pya.DPoint(-0.23, 3.29), pya.DPoint(-0.23, 3.13), pya.DPoint(-0.39, 3.13)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(-0.39, 3.47), pya.DPoint(-0.39, 3.63), pya.DPoint(-0.23, 3.63), pya.DPoint(-0.23, 3.47), pya.DPoint(-0.39, 3.47)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(-0.39, 3.81), pya.DPoint(-0.39, 3.97), pya.DPoint(-0.23, 3.97), pya.DPoint(-0.23, 3.81), pya.DPoint(-0.39, 3.81)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(-0.39, 4.15), pya.DPoint(-0.39, 4.31), pya.DPoint(-0.23, 4.31), pya.DPoint(-0.23, 4.15), pya.DPoint(-0.39, 4.15)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.42, 5), pya.DPoint(0.42, 5.16), pya.DPoint(0.58, 5.16), pya.DPoint(0.58, 5), pya.DPoint(0.42, 5)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.76, 5), pya.DPoint(0.76, 5.16), pya.DPoint(0.92, 5.16), pya.DPoint(0.92, 5), pya.DPoint(0.76, 5)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(1.1, 5), pya.DPoint(1.1, 5.16), pya.DPoint(1.26, 5.16), pya.DPoint(1.26, 5), pya.DPoint(1.1, 5)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(1.44, 5), pya.DPoint(1.44, 5.16), pya.DPoint(1.6, 5.16), pya.DPoint(1.6, 5), pya.DPoint(1.44, 5)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(1.78, 5), pya.DPoint(1.78, 5.16), pya.DPoint(1.94, 5.16), pya.DPoint(1.94, 5), pya.DPoint(1.78, 5)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(2.12, 5), pya.DPoint(2.12, 5.16), pya.DPoint(2.28, 5.16), pya.DPoint(2.28, 5), pya.DPoint(2.12, 5)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(5.52, 0.07), pya.DPoint(5.52, 0.23), pya.DPoint(5.68, 0.23), pya.DPoint(5.68, 0.07), pya.DPoint(5.52, 0.07)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(5.86, 0.07), pya.DPoint(5.86, 0.23), pya.DPoint(6.02, 0.23), pya.DPoint(6.02, 0.07), pya.DPoint(5.86, 0.07)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(6.2, 0.07), pya.DPoint(6.2, 0.23), pya.DPoint(6.36, 0.23), pya.DPoint(6.36, 0.07), pya.DPoint(6.2, 0.07)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(6.54, 0.07), pya.DPoint(6.54, 0.23), pya.DPoint(6.7, 0.23), pya.DPoint(6.7, 0.07), pya.DPoint(6.54, 0.07)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(6.88, 0.07), pya.DPoint(6.88, 0.23), pya.DPoint(7.04, 0.23), pya.DPoint(7.04, 0.07), pya.DPoint(6.88, 0.07)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.08, 0.07), pya.DPoint(0.08, 0.23), pya.DPoint(0.24, 0.23), pya.DPoint(0.24, 0.07), pya.DPoint(0.08, 0.07)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.42, 0.07), pya.DPoint(0.42, 0.23), pya.DPoint(0.58, 0.23), pya.DPoint(0.58, 0.07), pya.DPoint(0.42, 0.07)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.08, -0.44), pya.DPoint(0.08, -0.28), pya.DPoint(0.24, -0.28), pya.DPoint(0.24, -0.44), pya.DPoint(0.08, -0.44)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.42, -0.44), pya.DPoint(0.42, -0.28), pya.DPoint(0.58, -0.28), pya.DPoint(0.58, -0.44), pya.DPoint(0.42, -0.44)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.76, -0.44), pya.DPoint(0.76, -0.28), pya.DPoint(0.92, -0.28), pya.DPoint(0.92, -0.44), pya.DPoint(0.76, -0.44)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(1.1, -0.44), pya.DPoint(1.1, -0.28), pya.DPoint(1.26, -0.28), pya.DPoint(1.26, -0.44), pya.DPoint(1.1, -0.44)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(1.44, -0.44), pya.DPoint(1.44, -0.28), pya.DPoint(1.6, -0.28), pya.DPoint(1.6, -0.44), pya.DPoint(1.44, -0.44)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(1.78, -0.44), pya.DPoint(1.78, -0.28), pya.DPoint(1.94, -0.28), pya.DPoint(1.94, -0.44), pya.DPoint(1.78, -0.44)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(2.12, -0.44), pya.DPoint(2.12, -0.28), pya.DPoint(2.28, -0.28), pya.DPoint(2.28, -0.44), pya.DPoint(2.12, -0.44)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(2.46, -0.44), pya.DPoint(2.46, -0.28), pya.DPoint(2.62, -0.28), pya.DPoint(2.62, -0.44), pya.DPoint(2.46, -0.44)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(2.8, -0.44), pya.DPoint(2.8, -0.28), pya.DPoint(2.96, -0.28), pya.DPoint(2.96, -0.44), pya.DPoint(2.8, -0.44)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(3.14, -0.44), pya.DPoint(3.14, -0.28), pya.DPoint(3.3, -0.28), pya.DPoint(3.3, -0.44), pya.DPoint(3.14, -0.44)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(3.48, -0.44), pya.DPoint(3.48, -0.28), pya.DPoint(3.64, -0.28), pya.DPoint(3.64, -0.44), pya.DPoint(3.48, -0.44)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(3.82, -0.44), pya.DPoint(3.82, -0.28), pya.DPoint(3.98, -0.28), pya.DPoint(3.98, -0.44), pya.DPoint(3.82, -0.44)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(4.16, -0.44), pya.DPoint(4.16, -0.28), pya.DPoint(4.32, -0.28), pya.DPoint(4.32, -0.44), pya.DPoint(4.16, -0.44)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(4.5, -0.44), pya.DPoint(4.5, -0.28), pya.DPoint(4.66, -0.28), pya.DPoint(4.66, -0.44), pya.DPoint(4.5, -0.44)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(4.84, -0.44), pya.DPoint(4.84, -0.28), pya.DPoint(5, -0.28), pya.DPoint(5, -0.44), pya.DPoint(4.84, -0.44)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(5.18, -0.44), pya.DPoint(5.18, -0.28), pya.DPoint(5.34, -0.28), pya.DPoint(5.34, -0.44), pya.DPoint(5.18, -0.44)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(5.52, -0.44), pya.DPoint(5.52, -0.28), pya.DPoint(5.68, -0.28), pya.DPoint(5.68, -0.44), pya.DPoint(5.52, -0.44)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(5.86, -0.44), pya.DPoint(5.86, -0.28), pya.DPoint(6.02, -0.28), pya.DPoint(6.02, -0.44), pya.DPoint(5.86, -0.44)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(6.2, -0.44), pya.DPoint(6.2, -0.28), pya.DPoint(6.36, -0.28), pya.DPoint(6.36, -0.44), pya.DPoint(6.2, -0.44)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(6.54, -0.44), pya.DPoint(6.54, -0.28), pya.DPoint(6.7, -0.28), pya.DPoint(6.7, -0.44), pya.DPoint(6.54, -0.44)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(6.88, -0.44), pya.DPoint(6.88, -0.28), pya.DPoint(7.04, -0.28), pya.DPoint(7.04, -0.44), pya.DPoint(6.88, -0.44)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(0.76, 0.07), pya.DPoint(0.76, 0.23), pya.DPoint(0.92, 0.23), pya.DPoint(0.92, 0.07), pya.DPoint(0.76, 0.07)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(1.1, 0.07), pya.DPoint(1.1, 0.23), pya.DPoint(1.26, 0.23), pya.DPoint(1.26, 0.07), pya.DPoint(1.1, 0.07)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(-0.39, 0.41), pya.DPoint(-0.39, 0.57), pya.DPoint(-0.23, 0.57), pya.DPoint(-0.23, 0.41), pya.DPoint(-0.39, 0.41)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(-0.39, 0.75), pya.DPoint(-0.39, 0.91), pya.DPoint(-0.23, 0.91), pya.DPoint(-0.23, 0.75), pya.DPoint(-0.39, 0.75)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(-0.39, 1.09), pya.DPoint(-0.39, 1.25), pya.DPoint(-0.23, 1.25), pya.DPoint(-0.23, 1.09), pya.DPoint(-0.39, 1.09)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(-0.39, 1.43), pya.DPoint(-0.39, 1.59), pya.DPoint(-0.23, 1.59), pya.DPoint(-0.23, 1.43), pya.DPoint(-0.39, 1.43)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(-0.39, 1.77), pya.DPoint(-0.39, 1.93), pya.DPoint(-0.23, 1.93), pya.DPoint(-0.23, 1.77), pya.DPoint(-0.39, 1.77)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(-0.39, 2.11), pya.DPoint(-0.39, 2.27), pya.DPoint(-0.23, 2.27), pya.DPoint(-0.23, 2.11), pya.DPoint(-0.39, 2.11)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(1.44, 0.07), pya.DPoint(1.44, 0.23), pya.DPoint(1.6, 0.23), pya.DPoint(1.6, 0.07), pya.DPoint(1.44, 0.07)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(1.78, 0.07), pya.DPoint(1.78, 0.23), pya.DPoint(1.94, 0.23), pya.DPoint(1.94, 0.07), pya.DPoint(1.78, 0.07)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(2.12, 0.07), pya.DPoint(2.12, 0.23), pya.DPoint(2.28, 0.23), pya.DPoint(2.28, 0.07), pya.DPoint(2.12, 0.07)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(2.46, 0.07), pya.DPoint(2.46, 0.23), pya.DPoint(2.62, 0.23), pya.DPoint(2.62, 0.07), pya.DPoint(2.46, 0.07)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(2.8, 0.07), pya.DPoint(2.8, 0.23), pya.DPoint(2.96, 0.23), pya.DPoint(2.96, 0.07), pya.DPoint(2.8, 0.07)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(3.14, 0.07), pya.DPoint(3.14, 0.23), pya.DPoint(3.3, 0.23), pya.DPoint(3.3, 0.07), pya.DPoint(3.14, 0.07)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(3.48, 0.07), pya.DPoint(3.48, 0.23), pya.DPoint(3.64, 0.23), pya.DPoint(3.64, 0.07), pya.DPoint(3.48, 0.07)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(3.82, 0.07), pya.DPoint(3.82, 0.23), pya.DPoint(3.98, 0.23), pya.DPoint(3.98, 0.07), pya.DPoint(3.82, 0.07)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(4.16, 0.07), pya.DPoint(4.16, 0.23), pya.DPoint(4.32, 0.23), pya.DPoint(4.32, 0.07), pya.DPoint(4.16, 0.07)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(4.5, 0.07), pya.DPoint(4.5, 0.23), pya.DPoint(4.66, 0.23), pya.DPoint(4.66, 0.07), pya.DPoint(4.5, 0.07)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(4.84, 0.07), pya.DPoint(4.84, 0.23), pya.DPoint(5, 0.23), pya.DPoint(5, 0.07), pya.DPoint(4.84, 0.07)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(5.18, 0.07), pya.DPoint(5.18, 0.23), pya.DPoint(5.34, 0.23), pya.DPoint(5.34, 0.07), pya.DPoint(5.18, 0.07)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(7.56, 0.07), pya.DPoint(7.56, 0.23), pya.DPoint(7.72, 0.23), pya.DPoint(7.72, 0.07), pya.DPoint(7.56, 0.07)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(7.9, 0.07), pya.DPoint(7.9, 0.23), pya.DPoint(8.06, 0.23), pya.DPoint(8.06, 0.07), pya.DPoint(7.9, 0.07)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(7.56, -0.44), pya.DPoint(7.56, -0.28), pya.DPoint(7.72, -0.28), pya.DPoint(7.72, -0.44), pya.DPoint(7.56, -0.44)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(7.9, -0.44), pya.DPoint(7.9, -0.28), pya.DPoint(8.06, -0.28), pya.DPoint(8.06, -0.44), pya.DPoint(7.9, -0.44)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(8.24, -0.44), pya.DPoint(8.24, -0.28), pya.DPoint(8.4, -0.28), pya.DPoint(8.4, -0.44), pya.DPoint(8.24, -0.44)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(8.58, -0.44), pya.DPoint(8.58, -0.28), pya.DPoint(8.74, -0.28), pya.DPoint(8.74, -0.44), pya.DPoint(8.58, -0.44)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(8.92, -0.44), pya.DPoint(8.92, -0.28), pya.DPoint(9.08, -0.28), pya.DPoint(9.08, -0.44), pya.DPoint(8.92, -0.44)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(9.26, -0.44), pya.DPoint(9.26, -0.28), pya.DPoint(9.42, -0.28), pya.DPoint(9.42, -0.44), pya.DPoint(9.26, -0.44)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(9.6, -0.44), pya.DPoint(9.6, -0.28), pya.DPoint(9.76, -0.28), pya.DPoint(9.76, -0.44), pya.DPoint(9.6, -0.44)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(9.94, -0.44), pya.DPoint(9.94, -0.28), pya.DPoint(10.1, -0.28), pya.DPoint(10.1, -0.44), pya.DPoint(9.94, -0.44)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(10.28, -0.44), pya.DPoint(10.28, -0.28), pya.DPoint(10.44, -0.28), pya.DPoint(10.44, -0.44), pya.DPoint(10.28, -0.44)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(10.62, -0.44), pya.DPoint(10.62, -0.28), pya.DPoint(10.78, -0.28), pya.DPoint(10.78, -0.44), pya.DPoint(10.62, -0.44)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(10.96, -0.44), pya.DPoint(10.96, -0.28), pya.DPoint(11.12, -0.28), pya.DPoint(11.12, -0.44), pya.DPoint(10.96, -0.44)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(11.3, -0.44), pya.DPoint(11.3, -0.28), pya.DPoint(11.46, -0.28), pya.DPoint(11.46, -0.44), pya.DPoint(11.3, -0.44)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(11.64, -0.44), pya.DPoint(11.64, -0.28), pya.DPoint(11.8, -0.28), pya.DPoint(11.8, -0.44), pya.DPoint(11.64, -0.44)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(11.98, -0.44), pya.DPoint(11.98, -0.28), pya.DPoint(12.14, -0.28), pya.DPoint(12.14, -0.44), pya.DPoint(11.98, -0.44)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(12.32, -0.44), pya.DPoint(12.32, -0.28), pya.DPoint(12.48, -0.28), pya.DPoint(12.48, -0.44), pya.DPoint(12.32, -0.44)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(12.66, -0.44), pya.DPoint(12.66, -0.28), pya.DPoint(12.82, -0.28), pya.DPoint(12.82, -0.44), pya.DPoint(12.66, -0.44)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(13, -0.44), pya.DPoint(13, -0.28), pya.DPoint(13.16, -0.28), pya.DPoint(13.16, -0.44), pya.DPoint(13, -0.44)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(13.34, -0.44), pya.DPoint(13.34, -0.28), pya.DPoint(13.5, -0.28), pya.DPoint(13.5, -0.44), pya.DPoint(13.34, -0.44)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(13.68, -0.44), pya.DPoint(13.68, -0.28), pya.DPoint(13.84, -0.28), pya.DPoint(13.84, -0.44), pya.DPoint(13.68, -0.44)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(14.02, -0.44), pya.DPoint(14.02, -0.28), pya.DPoint(14.18, -0.28), pya.DPoint(14.18, -0.44), pya.DPoint(14.02, -0.44)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(14.36, -0.44), pya.DPoint(14.36, -0.28), pya.DPoint(14.52, -0.28), pya.DPoint(14.52, -0.44), pya.DPoint(14.36, -0.44)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(8.24, 0.07), pya.DPoint(8.24, 0.23), pya.DPoint(8.4, 0.23), pya.DPoint(8.4, 0.07), pya.DPoint(8.24, 0.07)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(8.58, 0.07), pya.DPoint(8.58, 0.23), pya.DPoint(8.74, 0.23), pya.DPoint(8.74, 0.07), pya.DPoint(8.58, 0.07)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(8.92, 0.07), pya.DPoint(8.92, 0.23), pya.DPoint(9.08, 0.23), pya.DPoint(9.08, 0.07), pya.DPoint(8.92, 0.07)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(9.26, 0.07), pya.DPoint(9.26, 0.23), pya.DPoint(9.42, 0.23), pya.DPoint(9.42, 0.07), pya.DPoint(9.26, 0.07)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(9.6, 0.07), pya.DPoint(9.6, 0.23), pya.DPoint(9.76, 0.23), pya.DPoint(9.76, 0.07), pya.DPoint(9.6, 0.07)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(9.94, 0.07), pya.DPoint(9.94, 0.23), pya.DPoint(10.1, 0.23), pya.DPoint(10.1, 0.07), pya.DPoint(9.94, 0.07)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(10.28, 0.07), pya.DPoint(10.28, 0.23), pya.DPoint(10.44, 0.23), pya.DPoint(10.44, 0.07), pya.DPoint(10.28, 0.07)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(10.62, 0.07), pya.DPoint(10.62, 0.23), pya.DPoint(10.78, 0.23), pya.DPoint(10.78, 0.07), pya.DPoint(10.62, 0.07)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(10.96, 0.07), pya.DPoint(10.96, 0.23), pya.DPoint(11.12, 0.23), pya.DPoint(11.12, 0.07), pya.DPoint(10.96, 0.07)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(11.3, 0.07), pya.DPoint(11.3, 0.23), pya.DPoint(11.46, 0.23), pya.DPoint(11.46, 0.07), pya.DPoint(11.3, 0.07)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(11.64, 0.07), pya.DPoint(11.64, 0.23), pya.DPoint(11.8, 0.23), pya.DPoint(11.8, 0.07), pya.DPoint(11.64, 0.07)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(11.98, 0.07), pya.DPoint(11.98, 0.23), pya.DPoint(12.14, 0.23), pya.DPoint(12.14, 0.07), pya.DPoint(11.98, 0.07)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(12.32, 0.07), pya.DPoint(12.32, 0.23), pya.DPoint(12.48, 0.23), pya.DPoint(12.48, 0.07), pya.DPoint(12.32, 0.07)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(14.82, 0.41), pya.DPoint(14.82, 0.57), pya.DPoint(14.98, 0.57), pya.DPoint(14.98, 0.41), pya.DPoint(14.82, 0.41)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(14.82, 0.75), pya.DPoint(14.82, 0.91), pya.DPoint(14.98, 0.91), pya.DPoint(14.98, 0.75), pya.DPoint(14.82, 0.75)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(14.82, 1.09), pya.DPoint(14.82, 1.25), pya.DPoint(14.98, 1.25), pya.DPoint(14.98, 1.09), pya.DPoint(14.82, 1.09)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(14.82, 1.43), pya.DPoint(14.82, 1.59), pya.DPoint(14.98, 1.59), pya.DPoint(14.98, 1.43), pya.DPoint(14.82, 1.43)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(14.82, 1.77), pya.DPoint(14.82, 1.93), pya.DPoint(14.98, 1.93), pya.DPoint(14.98, 1.77), pya.DPoint(14.82, 1.77)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(14.82, 2.11), pya.DPoint(14.82, 2.27), pya.DPoint(14.98, 2.27), pya.DPoint(14.98, 2.11), pya.DPoint(14.82, 2.11)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(12.66, 0.07), pya.DPoint(12.66, 0.23), pya.DPoint(12.82, 0.23), pya.DPoint(12.82, 0.07), pya.DPoint(12.66, 0.07)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(13, 0.07), pya.DPoint(13, 0.23), pya.DPoint(13.16, 0.23), pya.DPoint(13.16, 0.07), pya.DPoint(13, 0.07)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(13.34, 0.07), pya.DPoint(13.34, 0.23), pya.DPoint(13.5, 0.23), pya.DPoint(13.5, 0.07), pya.DPoint(13.34, 0.07)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(13.68, 0.07), pya.DPoint(13.68, 0.23), pya.DPoint(13.84, 0.23), pya.DPoint(13.84, 0.07), pya.DPoint(13.68, 0.07)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(14.02, 0.07), pya.DPoint(14.02, 0.23), pya.DPoint(14.18, 0.23), pya.DPoint(14.18, 0.07), pya.DPoint(14.02, 0.07)]))
cell_pmos_buffer_cap_1.shapes(L_Cont).insert(
    pya.DPolygon([pya.DPoint(14.36, 0.07), pya.DPoint(14.36, 0.23), pya.DPoint(14.52, 0.23), pya.DPoint(14.52, 0.07), pya.DPoint(14.36, 0.07)]))
cell_pmos_buffer_cap_1.shapes(L_Activ).insert(
    pya.DPolygon([pya.DPoint(0, 0), pya.DPoint(0, 4.72), pya.DPoint(14.6, 4.72), pya.DPoint(14.6, 0), pya.DPoint(0, 0)]))
cell_pmos_buffer_cap_1.shapes(L_Activ).insert(
    pya.DPolygon([pya.DPoint(0, 0), pya.DPoint(0, 0.3), pya.DPoint(0.3, 0.3), pya.DPoint(0.3, 0), pya.DPoint(0, 0)]))
cell_pmos_buffer_cap_1.shapes(L_Activ).insert(
    pya.DPolygon([pya.DPoint(0, 4.42), pya.DPoint(0, 4.72), pya.DPoint(0.3, 4.72), pya.DPoint(0.3, 4.42), pya.DPoint(0, 4.42)]))
cell_pmos_buffer_cap_1.shapes(L_Activ).insert(
    pya.DPolygon([pya.DPoint(0, -0.51), pya.DPoint(0, -0.21), pya.DPoint(14.6, -0.21), pya.DPoint(14.6, -0.51), pya.DPoint(0, -0.51)]))
cell_pmos_buffer_cap_1.shapes(L_Activ).insert(
    pya.DPolygon([pya.DPoint(0, 4.93), pya.DPoint(0, 5.23), pya.DPoint(14.6, 5.23), pya.DPoint(14.6, 4.93), pya.DPoint(0, 4.93)]))
cell_pmos_buffer_cap_1.shapes(L_GatPoly).insert(
    pya.DPolygon([pya.DPoint(-0.18, 0.34), pya.DPoint(-0.18, 4.38), pya.DPoint(14.78, 4.38), pya.DPoint(14.78, 0.34), pya.DPoint(-0.18, 0.34)]))
cell_pmos_buffer_cap_1.shapes(L_GatPoly).insert(
    pya.DPolygon([pya.DPoint(-0.46, 0.34), pya.DPoint(-0.46, 4.38), pya.DPoint(15.06, 4.38), pya.DPoint(15.06, 0.34), pya.DPoint(-0.46, 0.34)]))
cell_pmos_buffer_cap_1.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(-0.4, -0.18), pya.DPoint(-0.4, 4.9), pya.DPoint(15, 4.9), pya.DPoint(15, -0.18), pya.DPoint(-0.4, -0.18)]))
cell_pmos_buffer_cap_1.shapes(L_NWell).insert(
    pya.DPolygon([pya.DPoint(-0.62, -1.13), pya.DPoint(-0.62, 5.85), pya.DPoint(15.22, 5.85), pya.DPoint(15.22, -1.13), pya.DPoint(-0.62, -1.13)]))
cell_pmos_buffer_cap_1.shapes(L_Metal1_pin).insert(
    pya.DPolygon([pya.DPoint(0, 0.07), pya.DPoint(0, 0.23), pya.DPoint(14.6, 0.23), pya.DPoint(14.6, 0.07), pya.DPoint(0, 0.07)]))
cell_pmos_buffer_cap_1.shapes(L_Metal1_pin).insert(
    pya.DPolygon([pya.DPoint(0, 4.49), pya.DPoint(0, 4.65), pya.DPoint(14.6, 4.65), pya.DPoint(14.6, 4.49), pya.DPoint(0, 4.49)]))
cell_pmos_buffer_cap_1.shapes(L_ThickGateOx).insert(
    pya.DPolygon([pya.DPoint(-0.62, -1.13), pya.DPoint(-0.62, 5.85), pya.DPoint(15.22, 5.85), pya.DPoint(15.22, -1.13), pya.DPoint(-0.62, -1.13)]))
cell_pmos_buffer_cap_1.shapes(L_pmos).insert(
    pya.DPolygon([pya.DPoint(-0.18, 0.34), pya.DPoint(-0.18, 4.38), pya.DPoint(14.78, 4.38), pya.DPoint(14.78, 0.34), pya.DPoint(-0.18, 0.34)]))
cell_pmos_buffer_cap_1.shapes(L_NoBuLay).insert(
    pya.DPolygon([pya.DPoint(0, 4.42), pya.DPoint(0, 4.72), pya.DPoint(0.3, 4.72), pya.DPoint(0.3, 4.42), pya.DPoint(0, 4.42)]))
cell_pmos_buffer_cap_1.shapes(L_GatPoly_pin).insert(
    pya.DPolygon([pya.DPoint(-0.18, 0.34), pya.DPoint(-0.18, 4.38), pya.DPoint(14.78, 4.38), pya.DPoint(14.78, 0.34), pya.DPoint(-0.18, 0.34)]))

# === via_stack$9 ===
cell_via_stack_9.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(-0.865, -0.865), pya.DPoint(-0.865, 0.865), pya.DPoint(0.865, 0.865), pya.DPoint(0.865, -0.865), pya.DPoint(-0.865, -0.865)]))
cell_via_stack_9.shapes(L_Metal2).insert(
    pya.DPolygon([pya.DPoint(-0.865, -0.865), pya.DPoint(-0.865, 0.865), pya.DPoint(0.865, 0.865), pya.DPoint(0.865, -0.865), pya.DPoint(-0.865, -0.865)]))
cell_via_stack_9.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(-0.815, -0.815), pya.DPoint(-0.815, -0.625), pya.DPoint(-0.625, -0.625), pya.DPoint(-0.625, -0.815), pya.DPoint(-0.815, -0.815)]))
cell_via_stack_9.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(-0.815, -0.335), pya.DPoint(-0.815, -0.145), pya.DPoint(-0.625, -0.145), pya.DPoint(-0.625, -0.335), pya.DPoint(-0.815, -0.335)]))
cell_via_stack_9.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(-0.815, 0.145), pya.DPoint(-0.815, 0.335), pya.DPoint(-0.625, 0.335), pya.DPoint(-0.625, 0.145), pya.DPoint(-0.815, 0.145)]))
cell_via_stack_9.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(-0.815, 0.625), pya.DPoint(-0.815, 0.815), pya.DPoint(-0.625, 0.815), pya.DPoint(-0.625, 0.625), pya.DPoint(-0.815, 0.625)]))
cell_via_stack_9.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(-0.335, -0.815), pya.DPoint(-0.335, -0.625), pya.DPoint(-0.145, -0.625), pya.DPoint(-0.145, -0.815), pya.DPoint(-0.335, -0.815)]))
cell_via_stack_9.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(-0.335, -0.335), pya.DPoint(-0.335, -0.145), pya.DPoint(-0.145, -0.145), pya.DPoint(-0.145, -0.335), pya.DPoint(-0.335, -0.335)]))
cell_via_stack_9.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(-0.335, 0.145), pya.DPoint(-0.335, 0.335), pya.DPoint(-0.145, 0.335), pya.DPoint(-0.145, 0.145), pya.DPoint(-0.335, 0.145)]))
cell_via_stack_9.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(-0.335, 0.625), pya.DPoint(-0.335, 0.815), pya.DPoint(-0.145, 0.815), pya.DPoint(-0.145, 0.625), pya.DPoint(-0.335, 0.625)]))
cell_via_stack_9.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(0.145, -0.815), pya.DPoint(0.145, -0.625), pya.DPoint(0.335, -0.625), pya.DPoint(0.335, -0.815), pya.DPoint(0.145, -0.815)]))
cell_via_stack_9.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(0.145, -0.335), pya.DPoint(0.145, -0.145), pya.DPoint(0.335, -0.145), pya.DPoint(0.335, -0.335), pya.DPoint(0.145, -0.335)]))
cell_via_stack_9.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(0.145, 0.145), pya.DPoint(0.145, 0.335), pya.DPoint(0.335, 0.335), pya.DPoint(0.335, 0.145), pya.DPoint(0.145, 0.145)]))
cell_via_stack_9.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(0.145, 0.625), pya.DPoint(0.145, 0.815), pya.DPoint(0.335, 0.815), pya.DPoint(0.335, 0.625), pya.DPoint(0.145, 0.625)]))
cell_via_stack_9.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(0.625, -0.815), pya.DPoint(0.625, -0.625), pya.DPoint(0.815, -0.625), pya.DPoint(0.815, -0.815), pya.DPoint(0.625, -0.815)]))
cell_via_stack_9.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(0.625, -0.335), pya.DPoint(0.625, -0.145), pya.DPoint(0.815, -0.145), pya.DPoint(0.815, -0.335), pya.DPoint(0.625, -0.335)]))
cell_via_stack_9.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(0.625, 0.145), pya.DPoint(0.625, 0.335), pya.DPoint(0.815, 0.335), pya.DPoint(0.815, 0.145), pya.DPoint(0.625, 0.145)]))
cell_via_stack_9.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(0.625, 0.625), pya.DPoint(0.625, 0.815), pya.DPoint(0.815, 0.815), pya.DPoint(0.815, 0.625), pya.DPoint(0.625, 0.625)]))
cell_via_stack_9.shapes(L_Metal5).insert(
    pya.DPolygon([pya.DPoint(-0.865, -0.865), pya.DPoint(-0.865, 0.865), pya.DPoint(0.865, 0.865), pya.DPoint(0.865, -0.865), pya.DPoint(-0.865, -0.865)]))
cell_via_stack_9.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(-0.815, -0.815), pya.DPoint(-0.815, -0.625), pya.DPoint(-0.625, -0.625), pya.DPoint(-0.625, -0.815), pya.DPoint(-0.815, -0.815)]))
cell_via_stack_9.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(-0.815, -0.335), pya.DPoint(-0.815, -0.145), pya.DPoint(-0.625, -0.145), pya.DPoint(-0.625, -0.335), pya.DPoint(-0.815, -0.335)]))
cell_via_stack_9.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(-0.815, 0.145), pya.DPoint(-0.815, 0.335), pya.DPoint(-0.625, 0.335), pya.DPoint(-0.625, 0.145), pya.DPoint(-0.815, 0.145)]))
cell_via_stack_9.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(-0.815, 0.625), pya.DPoint(-0.815, 0.815), pya.DPoint(-0.625, 0.815), pya.DPoint(-0.625, 0.625), pya.DPoint(-0.815, 0.625)]))
cell_via_stack_9.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(-0.335, -0.815), pya.DPoint(-0.335, -0.625), pya.DPoint(-0.145, -0.625), pya.DPoint(-0.145, -0.815), pya.DPoint(-0.335, -0.815)]))
cell_via_stack_9.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(-0.335, -0.335), pya.DPoint(-0.335, -0.145), pya.DPoint(-0.145, -0.145), pya.DPoint(-0.145, -0.335), pya.DPoint(-0.335, -0.335)]))
cell_via_stack_9.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(-0.335, 0.145), pya.DPoint(-0.335, 0.335), pya.DPoint(-0.145, 0.335), pya.DPoint(-0.145, 0.145), pya.DPoint(-0.335, 0.145)]))
cell_via_stack_9.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(-0.335, 0.625), pya.DPoint(-0.335, 0.815), pya.DPoint(-0.145, 0.815), pya.DPoint(-0.145, 0.625), pya.DPoint(-0.335, 0.625)]))
cell_via_stack_9.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(0.145, -0.815), pya.DPoint(0.145, -0.625), pya.DPoint(0.335, -0.625), pya.DPoint(0.335, -0.815), pya.DPoint(0.145, -0.815)]))
cell_via_stack_9.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(0.145, -0.335), pya.DPoint(0.145, -0.145), pya.DPoint(0.335, -0.145), pya.DPoint(0.335, -0.335), pya.DPoint(0.145, -0.335)]))
cell_via_stack_9.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(0.145, 0.145), pya.DPoint(0.145, 0.335), pya.DPoint(0.335, 0.335), pya.DPoint(0.335, 0.145), pya.DPoint(0.145, 0.145)]))
cell_via_stack_9.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(0.145, 0.625), pya.DPoint(0.145, 0.815), pya.DPoint(0.335, 0.815), pya.DPoint(0.335, 0.625), pya.DPoint(0.145, 0.625)]))
cell_via_stack_9.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(0.625, -0.815), pya.DPoint(0.625, -0.625), pya.DPoint(0.815, -0.625), pya.DPoint(0.815, -0.815), pya.DPoint(0.625, -0.815)]))
cell_via_stack_9.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(0.625, -0.335), pya.DPoint(0.625, -0.145), pya.DPoint(0.815, -0.145), pya.DPoint(0.815, -0.335), pya.DPoint(0.625, -0.335)]))
cell_via_stack_9.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(0.625, 0.145), pya.DPoint(0.625, 0.335), pya.DPoint(0.815, 0.335), pya.DPoint(0.815, 0.145), pya.DPoint(0.625, 0.145)]))
cell_via_stack_9.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(0.625, 0.625), pya.DPoint(0.625, 0.815), pya.DPoint(0.815, 0.815), pya.DPoint(0.815, 0.625), pya.DPoint(0.625, 0.625)]))

# === via_stack$4 ===
cell_via_stack_4.shapes(L_50_0).insert(
    pya.DPolygon([pya.DPoint(-1.825, -5.905), pya.DPoint(-1.825, 5.905), pya.DPoint(1.825, 5.905), pya.DPoint(1.825, -5.905), pya.DPoint(-1.825, -5.905)]))
cell_via_stack_4.shapes(L_Via2).insert(
    pya.DPolygon([pya.DPoint(-1.825, -5.905), pya.DPoint(-1.825, 5.905), pya.DPoint(1.825, 5.905), pya.DPoint(1.825, -5.905), pya.DPoint(-1.825, -5.905)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.775, -0.095), pya.DPoint(-1.775, 0.095), pya.DPoint(-1.585, 0.095), pya.DPoint(-1.585, -0.095), pya.DPoint(-1.775, -0.095)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.295, -0.095), pya.DPoint(-1.295, 0.095), pya.DPoint(-1.105, 0.095), pya.DPoint(-1.105, -0.095), pya.DPoint(-1.295, -0.095)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.815, -0.095), pya.DPoint(-0.815, 0.095), pya.DPoint(-0.625, 0.095), pya.DPoint(-0.625, -0.095), pya.DPoint(-0.815, -0.095)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.335, -0.095), pya.DPoint(-0.335, 0.095), pya.DPoint(-0.145, 0.095), pya.DPoint(-0.145, -0.095), pya.DPoint(-0.335, -0.095)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.145, -0.095), pya.DPoint(0.145, 0.095), pya.DPoint(0.335, 0.095), pya.DPoint(0.335, -0.095), pya.DPoint(0.145, -0.095)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.625, -0.095), pya.DPoint(0.625, 0.095), pya.DPoint(0.815, 0.095), pya.DPoint(0.815, -0.095), pya.DPoint(0.625, -0.095)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.105, -0.095), pya.DPoint(1.105, 0.095), pya.DPoint(1.295, 0.095), pya.DPoint(1.295, -0.095), pya.DPoint(1.105, -0.095)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.585, -0.095), pya.DPoint(1.585, 0.095), pya.DPoint(1.775, 0.095), pya.DPoint(1.775, -0.095), pya.DPoint(1.585, -0.095)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.145, 1.825), pya.DPoint(0.145, 2.015), pya.DPoint(0.335, 2.015), pya.DPoint(0.335, 1.825), pya.DPoint(0.145, 1.825)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.145, 2.305), pya.DPoint(0.145, 2.495), pya.DPoint(0.335, 2.495), pya.DPoint(0.335, 2.305), pya.DPoint(0.145, 2.305)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.145, 2.785), pya.DPoint(0.145, 2.975), pya.DPoint(0.335, 2.975), pya.DPoint(0.335, 2.785), pya.DPoint(0.145, 2.785)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.145, 3.265), pya.DPoint(0.145, 3.455), pya.DPoint(0.335, 3.455), pya.DPoint(0.335, 3.265), pya.DPoint(0.145, 3.265)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.145, 3.745), pya.DPoint(0.145, 3.935), pya.DPoint(0.335, 3.935), pya.DPoint(0.335, 3.745), pya.DPoint(0.145, 3.745)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.145, 4.225), pya.DPoint(0.145, 4.415), pya.DPoint(0.335, 4.415), pya.DPoint(0.335, 4.225), pya.DPoint(0.145, 4.225)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.145, 4.705), pya.DPoint(0.145, 4.895), pya.DPoint(0.335, 4.895), pya.DPoint(0.335, 4.705), pya.DPoint(0.145, 4.705)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.145, 5.185), pya.DPoint(0.145, 5.375), pya.DPoint(0.335, 5.375), pya.DPoint(0.335, 5.185), pya.DPoint(0.145, 5.185)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.145, 5.665), pya.DPoint(0.145, 5.855), pya.DPoint(0.335, 5.855), pya.DPoint(0.335, 5.665), pya.DPoint(0.145, 5.665)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.145, 0.385), pya.DPoint(0.145, 0.575), pya.DPoint(0.335, 0.575), pya.DPoint(0.335, 0.385), pya.DPoint(0.145, 0.385)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.625, 0.385), pya.DPoint(0.625, 0.575), pya.DPoint(0.815, 0.575), pya.DPoint(0.815, 0.385), pya.DPoint(0.625, 0.385)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.625, 0.865), pya.DPoint(0.625, 1.055), pya.DPoint(0.815, 1.055), pya.DPoint(0.815, 0.865), pya.DPoint(0.625, 0.865)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.625, 1.345), pya.DPoint(0.625, 1.535), pya.DPoint(0.815, 1.535), pya.DPoint(0.815, 1.345), pya.DPoint(0.625, 1.345)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.625, 1.825), pya.DPoint(0.625, 2.015), pya.DPoint(0.815, 2.015), pya.DPoint(0.815, 1.825), pya.DPoint(0.625, 1.825)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.625, 2.305), pya.DPoint(0.625, 2.495), pya.DPoint(0.815, 2.495), pya.DPoint(0.815, 2.305), pya.DPoint(0.625, 2.305)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.625, 2.785), pya.DPoint(0.625, 2.975), pya.DPoint(0.815, 2.975), pya.DPoint(0.815, 2.785), pya.DPoint(0.625, 2.785)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.625, 3.265), pya.DPoint(0.625, 3.455), pya.DPoint(0.815, 3.455), pya.DPoint(0.815, 3.265), pya.DPoint(0.625, 3.265)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.625, 3.745), pya.DPoint(0.625, 3.935), pya.DPoint(0.815, 3.935), pya.DPoint(0.815, 3.745), pya.DPoint(0.625, 3.745)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.625, 4.225), pya.DPoint(0.625, 4.415), pya.DPoint(0.815, 4.415), pya.DPoint(0.815, 4.225), pya.DPoint(0.625, 4.225)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.625, 4.705), pya.DPoint(0.625, 4.895), pya.DPoint(0.815, 4.895), pya.DPoint(0.815, 4.705), pya.DPoint(0.625, 4.705)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.625, 5.185), pya.DPoint(0.625, 5.375), pya.DPoint(0.815, 5.375), pya.DPoint(0.815, 5.185), pya.DPoint(0.625, 5.185)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.625, 5.665), pya.DPoint(0.625, 5.855), pya.DPoint(0.815, 5.855), pya.DPoint(0.815, 5.665), pya.DPoint(0.625, 5.665)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.145, 0.865), pya.DPoint(0.145, 1.055), pya.DPoint(0.335, 1.055), pya.DPoint(0.335, 0.865), pya.DPoint(0.145, 0.865)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.105, 0.385), pya.DPoint(1.105, 0.575), pya.DPoint(1.295, 0.575), pya.DPoint(1.295, 0.385), pya.DPoint(1.105, 0.385)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.105, 0.865), pya.DPoint(1.105, 1.055), pya.DPoint(1.295, 1.055), pya.DPoint(1.295, 0.865), pya.DPoint(1.105, 0.865)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.105, 1.345), pya.DPoint(1.105, 1.535), pya.DPoint(1.295, 1.535), pya.DPoint(1.295, 1.345), pya.DPoint(1.105, 1.345)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.105, 1.825), pya.DPoint(1.105, 2.015), pya.DPoint(1.295, 2.015), pya.DPoint(1.295, 1.825), pya.DPoint(1.105, 1.825)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.105, 2.305), pya.DPoint(1.105, 2.495), pya.DPoint(1.295, 2.495), pya.DPoint(1.295, 2.305), pya.DPoint(1.105, 2.305)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.105, 2.785), pya.DPoint(1.105, 2.975), pya.DPoint(1.295, 2.975), pya.DPoint(1.295, 2.785), pya.DPoint(1.105, 2.785)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.105, 3.265), pya.DPoint(1.105, 3.455), pya.DPoint(1.295, 3.455), pya.DPoint(1.295, 3.265), pya.DPoint(1.105, 3.265)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.105, 3.745), pya.DPoint(1.105, 3.935), pya.DPoint(1.295, 3.935), pya.DPoint(1.295, 3.745), pya.DPoint(1.105, 3.745)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.105, 4.225), pya.DPoint(1.105, 4.415), pya.DPoint(1.295, 4.415), pya.DPoint(1.295, 4.225), pya.DPoint(1.105, 4.225)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.105, 4.705), pya.DPoint(1.105, 4.895), pya.DPoint(1.295, 4.895), pya.DPoint(1.295, 4.705), pya.DPoint(1.105, 4.705)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.105, 5.185), pya.DPoint(1.105, 5.375), pya.DPoint(1.295, 5.375), pya.DPoint(1.295, 5.185), pya.DPoint(1.105, 5.185)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.105, 5.665), pya.DPoint(1.105, 5.855), pya.DPoint(1.295, 5.855), pya.DPoint(1.295, 5.665), pya.DPoint(1.105, 5.665)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.145, 1.345), pya.DPoint(0.145, 1.535), pya.DPoint(0.335, 1.535), pya.DPoint(0.335, 1.345), pya.DPoint(0.145, 1.345)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.585, 0.385), pya.DPoint(1.585, 0.575), pya.DPoint(1.775, 0.575), pya.DPoint(1.775, 0.385), pya.DPoint(1.585, 0.385)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.585, 0.865), pya.DPoint(1.585, 1.055), pya.DPoint(1.775, 1.055), pya.DPoint(1.775, 0.865), pya.DPoint(1.585, 0.865)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.585, 1.345), pya.DPoint(1.585, 1.535), pya.DPoint(1.775, 1.535), pya.DPoint(1.775, 1.345), pya.DPoint(1.585, 1.345)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.585, 1.825), pya.DPoint(1.585, 2.015), pya.DPoint(1.775, 2.015), pya.DPoint(1.775, 1.825), pya.DPoint(1.585, 1.825)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.585, 2.305), pya.DPoint(1.585, 2.495), pya.DPoint(1.775, 2.495), pya.DPoint(1.775, 2.305), pya.DPoint(1.585, 2.305)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.585, 2.785), pya.DPoint(1.585, 2.975), pya.DPoint(1.775, 2.975), pya.DPoint(1.775, 2.785), pya.DPoint(1.585, 2.785)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.585, 3.265), pya.DPoint(1.585, 3.455), pya.DPoint(1.775, 3.455), pya.DPoint(1.775, 3.265), pya.DPoint(1.585, 3.265)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.585, 3.745), pya.DPoint(1.585, 3.935), pya.DPoint(1.775, 3.935), pya.DPoint(1.775, 3.745), pya.DPoint(1.585, 3.745)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.585, 4.225), pya.DPoint(1.585, 4.415), pya.DPoint(1.775, 4.415), pya.DPoint(1.775, 4.225), pya.DPoint(1.585, 4.225)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.585, 4.705), pya.DPoint(1.585, 4.895), pya.DPoint(1.775, 4.895), pya.DPoint(1.775, 4.705), pya.DPoint(1.585, 4.705)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.585, 5.185), pya.DPoint(1.585, 5.375), pya.DPoint(1.775, 5.375), pya.DPoint(1.775, 5.185), pya.DPoint(1.585, 5.185)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.585, 5.665), pya.DPoint(1.585, 5.855), pya.DPoint(1.775, 5.855), pya.DPoint(1.775, 5.665), pya.DPoint(1.585, 5.665)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.775, 3.745), pya.DPoint(-1.775, 3.935), pya.DPoint(-1.585, 3.935), pya.DPoint(-1.585, 3.745), pya.DPoint(-1.775, 3.745)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.775, 4.225), pya.DPoint(-1.775, 4.415), pya.DPoint(-1.585, 4.415), pya.DPoint(-1.585, 4.225), pya.DPoint(-1.775, 4.225)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.775, 4.705), pya.DPoint(-1.775, 4.895), pya.DPoint(-1.585, 4.895), pya.DPoint(-1.585, 4.705), pya.DPoint(-1.775, 4.705)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.775, 5.185), pya.DPoint(-1.775, 5.375), pya.DPoint(-1.585, 5.375), pya.DPoint(-1.585, 5.185), pya.DPoint(-1.775, 5.185)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.775, 5.665), pya.DPoint(-1.775, 5.855), pya.DPoint(-1.585, 5.855), pya.DPoint(-1.585, 5.665), pya.DPoint(-1.775, 5.665)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.775, 0.385), pya.DPoint(-1.775, 0.575), pya.DPoint(-1.585, 0.575), pya.DPoint(-1.585, 0.385), pya.DPoint(-1.775, 0.385)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.295, 0.385), pya.DPoint(-1.295, 0.575), pya.DPoint(-1.105, 0.575), pya.DPoint(-1.105, 0.385), pya.DPoint(-1.295, 0.385)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.295, 0.865), pya.DPoint(-1.295, 1.055), pya.DPoint(-1.105, 1.055), pya.DPoint(-1.105, 0.865), pya.DPoint(-1.295, 0.865)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.295, 1.345), pya.DPoint(-1.295, 1.535), pya.DPoint(-1.105, 1.535), pya.DPoint(-1.105, 1.345), pya.DPoint(-1.295, 1.345)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.295, 1.825), pya.DPoint(-1.295, 2.015), pya.DPoint(-1.105, 2.015), pya.DPoint(-1.105, 1.825), pya.DPoint(-1.295, 1.825)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.295, 2.305), pya.DPoint(-1.295, 2.495), pya.DPoint(-1.105, 2.495), pya.DPoint(-1.105, 2.305), pya.DPoint(-1.295, 2.305)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.295, 2.785), pya.DPoint(-1.295, 2.975), pya.DPoint(-1.105, 2.975), pya.DPoint(-1.105, 2.785), pya.DPoint(-1.295, 2.785)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.295, 3.265), pya.DPoint(-1.295, 3.455), pya.DPoint(-1.105, 3.455), pya.DPoint(-1.105, 3.265), pya.DPoint(-1.295, 3.265)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.295, 3.745), pya.DPoint(-1.295, 3.935), pya.DPoint(-1.105, 3.935), pya.DPoint(-1.105, 3.745), pya.DPoint(-1.295, 3.745)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.295, 4.225), pya.DPoint(-1.295, 4.415), pya.DPoint(-1.105, 4.415), pya.DPoint(-1.105, 4.225), pya.DPoint(-1.295, 4.225)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.295, 4.705), pya.DPoint(-1.295, 4.895), pya.DPoint(-1.105, 4.895), pya.DPoint(-1.105, 4.705), pya.DPoint(-1.295, 4.705)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.295, 5.185), pya.DPoint(-1.295, 5.375), pya.DPoint(-1.105, 5.375), pya.DPoint(-1.105, 5.185), pya.DPoint(-1.295, 5.185)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.295, 5.665), pya.DPoint(-1.295, 5.855), pya.DPoint(-1.105, 5.855), pya.DPoint(-1.105, 5.665), pya.DPoint(-1.295, 5.665)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.775, 0.865), pya.DPoint(-1.775, 1.055), pya.DPoint(-1.585, 1.055), pya.DPoint(-1.585, 0.865), pya.DPoint(-1.775, 0.865)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.815, 0.385), pya.DPoint(-0.815, 0.575), pya.DPoint(-0.625, 0.575), pya.DPoint(-0.625, 0.385), pya.DPoint(-0.815, 0.385)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.815, 0.865), pya.DPoint(-0.815, 1.055), pya.DPoint(-0.625, 1.055), pya.DPoint(-0.625, 0.865), pya.DPoint(-0.815, 0.865)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.815, 1.345), pya.DPoint(-0.815, 1.535), pya.DPoint(-0.625, 1.535), pya.DPoint(-0.625, 1.345), pya.DPoint(-0.815, 1.345)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.815, 1.825), pya.DPoint(-0.815, 2.015), pya.DPoint(-0.625, 2.015), pya.DPoint(-0.625, 1.825), pya.DPoint(-0.815, 1.825)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.815, 2.305), pya.DPoint(-0.815, 2.495), pya.DPoint(-0.625, 2.495), pya.DPoint(-0.625, 2.305), pya.DPoint(-0.815, 2.305)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.815, 2.785), pya.DPoint(-0.815, 2.975), pya.DPoint(-0.625, 2.975), pya.DPoint(-0.625, 2.785), pya.DPoint(-0.815, 2.785)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.815, 3.265), pya.DPoint(-0.815, 3.455), pya.DPoint(-0.625, 3.455), pya.DPoint(-0.625, 3.265), pya.DPoint(-0.815, 3.265)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.815, 3.745), pya.DPoint(-0.815, 3.935), pya.DPoint(-0.625, 3.935), pya.DPoint(-0.625, 3.745), pya.DPoint(-0.815, 3.745)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.815, 4.225), pya.DPoint(-0.815, 4.415), pya.DPoint(-0.625, 4.415), pya.DPoint(-0.625, 4.225), pya.DPoint(-0.815, 4.225)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.815, 4.705), pya.DPoint(-0.815, 4.895), pya.DPoint(-0.625, 4.895), pya.DPoint(-0.625, 4.705), pya.DPoint(-0.815, 4.705)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.815, 5.185), pya.DPoint(-0.815, 5.375), pya.DPoint(-0.625, 5.375), pya.DPoint(-0.625, 5.185), pya.DPoint(-0.815, 5.185)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.815, 5.665), pya.DPoint(-0.815, 5.855), pya.DPoint(-0.625, 5.855), pya.DPoint(-0.625, 5.665), pya.DPoint(-0.815, 5.665)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.775, 1.345), pya.DPoint(-1.775, 1.535), pya.DPoint(-1.585, 1.535), pya.DPoint(-1.585, 1.345), pya.DPoint(-1.775, 1.345)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.335, 0.385), pya.DPoint(-0.335, 0.575), pya.DPoint(-0.145, 0.575), pya.DPoint(-0.145, 0.385), pya.DPoint(-0.335, 0.385)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.335, 0.865), pya.DPoint(-0.335, 1.055), pya.DPoint(-0.145, 1.055), pya.DPoint(-0.145, 0.865), pya.DPoint(-0.335, 0.865)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.335, 1.345), pya.DPoint(-0.335, 1.535), pya.DPoint(-0.145, 1.535), pya.DPoint(-0.145, 1.345), pya.DPoint(-0.335, 1.345)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.335, 1.825), pya.DPoint(-0.335, 2.015), pya.DPoint(-0.145, 2.015), pya.DPoint(-0.145, 1.825), pya.DPoint(-0.335, 1.825)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.335, 2.305), pya.DPoint(-0.335, 2.495), pya.DPoint(-0.145, 2.495), pya.DPoint(-0.145, 2.305), pya.DPoint(-0.335, 2.305)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.335, 2.785), pya.DPoint(-0.335, 2.975), pya.DPoint(-0.145, 2.975), pya.DPoint(-0.145, 2.785), pya.DPoint(-0.335, 2.785)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.335, 3.265), pya.DPoint(-0.335, 3.455), pya.DPoint(-0.145, 3.455), pya.DPoint(-0.145, 3.265), pya.DPoint(-0.335, 3.265)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.335, 3.745), pya.DPoint(-0.335, 3.935), pya.DPoint(-0.145, 3.935), pya.DPoint(-0.145, 3.745), pya.DPoint(-0.335, 3.745)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.335, 4.225), pya.DPoint(-0.335, 4.415), pya.DPoint(-0.145, 4.415), pya.DPoint(-0.145, 4.225), pya.DPoint(-0.335, 4.225)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.335, 4.705), pya.DPoint(-0.335, 4.895), pya.DPoint(-0.145, 4.895), pya.DPoint(-0.145, 4.705), pya.DPoint(-0.335, 4.705)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.335, 5.185), pya.DPoint(-0.335, 5.375), pya.DPoint(-0.145, 5.375), pya.DPoint(-0.145, 5.185), pya.DPoint(-0.335, 5.185)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.335, 5.665), pya.DPoint(-0.335, 5.855), pya.DPoint(-0.145, 5.855), pya.DPoint(-0.145, 5.665), pya.DPoint(-0.335, 5.665)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.775, 1.825), pya.DPoint(-1.775, 2.015), pya.DPoint(-1.585, 2.015), pya.DPoint(-1.585, 1.825), pya.DPoint(-1.775, 1.825)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.775, 2.305), pya.DPoint(-1.775, 2.495), pya.DPoint(-1.585, 2.495), pya.DPoint(-1.585, 2.305), pya.DPoint(-1.775, 2.305)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.775, 2.785), pya.DPoint(-1.775, 2.975), pya.DPoint(-1.585, 2.975), pya.DPoint(-1.585, 2.785), pya.DPoint(-1.775, 2.785)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.775, 3.265), pya.DPoint(-1.775, 3.455), pya.DPoint(-1.585, 3.455), pya.DPoint(-1.585, 3.265), pya.DPoint(-1.775, 3.265)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.815, -2.975), pya.DPoint(-0.815, -2.785), pya.DPoint(-0.625, -2.785), pya.DPoint(-0.625, -2.975), pya.DPoint(-0.815, -2.975)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.815, -2.495), pya.DPoint(-0.815, -2.305), pya.DPoint(-0.625, -2.305), pya.DPoint(-0.625, -2.495), pya.DPoint(-0.815, -2.495)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.815, -2.015), pya.DPoint(-0.815, -1.825), pya.DPoint(-0.625, -1.825), pya.DPoint(-0.625, -2.015), pya.DPoint(-0.815, -2.015)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.815, -1.535), pya.DPoint(-0.815, -1.345), pya.DPoint(-0.625, -1.345), pya.DPoint(-0.625, -1.535), pya.DPoint(-0.815, -1.535)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.815, -1.055), pya.DPoint(-0.815, -0.865), pya.DPoint(-0.625, -0.865), pya.DPoint(-0.625, -1.055), pya.DPoint(-0.815, -1.055)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.815, -0.575), pya.DPoint(-0.815, -0.385), pya.DPoint(-0.625, -0.385), pya.DPoint(-0.625, -0.575), pya.DPoint(-0.815, -0.575)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.295, -5.375), pya.DPoint(-1.295, -5.185), pya.DPoint(-1.105, -5.185), pya.DPoint(-1.105, -5.375), pya.DPoint(-1.295, -5.375)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.295, -4.895), pya.DPoint(-1.295, -4.705), pya.DPoint(-1.105, -4.705), pya.DPoint(-1.105, -4.895), pya.DPoint(-1.295, -4.895)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.295, -4.415), pya.DPoint(-1.295, -4.225), pya.DPoint(-1.105, -4.225), pya.DPoint(-1.105, -4.415), pya.DPoint(-1.295, -4.415)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.295, -3.935), pya.DPoint(-1.295, -3.745), pya.DPoint(-1.105, -3.745), pya.DPoint(-1.105, -3.935), pya.DPoint(-1.295, -3.935)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.295, -3.455), pya.DPoint(-1.295, -3.265), pya.DPoint(-1.105, -3.265), pya.DPoint(-1.105, -3.455), pya.DPoint(-1.295, -3.455)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.295, -2.975), pya.DPoint(-1.295, -2.785), pya.DPoint(-1.105, -2.785), pya.DPoint(-1.105, -2.975), pya.DPoint(-1.295, -2.975)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.295, -2.495), pya.DPoint(-1.295, -2.305), pya.DPoint(-1.105, -2.305), pya.DPoint(-1.105, -2.495), pya.DPoint(-1.295, -2.495)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.295, -2.015), pya.DPoint(-1.295, -1.825), pya.DPoint(-1.105, -1.825), pya.DPoint(-1.105, -2.015), pya.DPoint(-1.295, -2.015)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.295, -1.535), pya.DPoint(-1.295, -1.345), pya.DPoint(-1.105, -1.345), pya.DPoint(-1.105, -1.535), pya.DPoint(-1.295, -1.535)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.295, -1.055), pya.DPoint(-1.295, -0.865), pya.DPoint(-1.105, -0.865), pya.DPoint(-1.105, -1.055), pya.DPoint(-1.295, -1.055)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.295, -0.575), pya.DPoint(-1.295, -0.385), pya.DPoint(-1.105, -0.385), pya.DPoint(-1.105, -0.575), pya.DPoint(-1.295, -0.575)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.775, -5.375), pya.DPoint(-1.775, -5.185), pya.DPoint(-1.585, -5.185), pya.DPoint(-1.585, -5.375), pya.DPoint(-1.775, -5.375)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.775, -4.895), pya.DPoint(-1.775, -4.705), pya.DPoint(-1.585, -4.705), pya.DPoint(-1.585, -4.895), pya.DPoint(-1.775, -4.895)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.335, -5.855), pya.DPoint(-0.335, -5.665), pya.DPoint(-0.145, -5.665), pya.DPoint(-0.145, -5.855), pya.DPoint(-0.335, -5.855)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.335, -5.375), pya.DPoint(-0.335, -5.185), pya.DPoint(-0.145, -5.185), pya.DPoint(-0.145, -5.375), pya.DPoint(-0.335, -5.375)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.335, -4.895), pya.DPoint(-0.335, -4.705), pya.DPoint(-0.145, -4.705), pya.DPoint(-0.145, -4.895), pya.DPoint(-0.335, -4.895)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.335, -4.415), pya.DPoint(-0.335, -4.225), pya.DPoint(-0.145, -4.225), pya.DPoint(-0.145, -4.415), pya.DPoint(-0.335, -4.415)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.335, -3.935), pya.DPoint(-0.335, -3.745), pya.DPoint(-0.145, -3.745), pya.DPoint(-0.145, -3.935), pya.DPoint(-0.335, -3.935)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.335, -3.455), pya.DPoint(-0.335, -3.265), pya.DPoint(-0.145, -3.265), pya.DPoint(-0.145, -3.455), pya.DPoint(-0.335, -3.455)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.335, -2.975), pya.DPoint(-0.335, -2.785), pya.DPoint(-0.145, -2.785), pya.DPoint(-0.145, -2.975), pya.DPoint(-0.335, -2.975)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.335, -2.495), pya.DPoint(-0.335, -2.305), pya.DPoint(-0.145, -2.305), pya.DPoint(-0.145, -2.495), pya.DPoint(-0.335, -2.495)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.335, -2.015), pya.DPoint(-0.335, -1.825), pya.DPoint(-0.145, -1.825), pya.DPoint(-0.145, -2.015), pya.DPoint(-0.335, -2.015)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.335, -1.535), pya.DPoint(-0.335, -1.345), pya.DPoint(-0.145, -1.345), pya.DPoint(-0.145, -1.535), pya.DPoint(-0.335, -1.535)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.335, -1.055), pya.DPoint(-0.335, -0.865), pya.DPoint(-0.145, -0.865), pya.DPoint(-0.145, -1.055), pya.DPoint(-0.335, -1.055)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.335, -0.575), pya.DPoint(-0.335, -0.385), pya.DPoint(-0.145, -0.385), pya.DPoint(-0.145, -0.575), pya.DPoint(-0.335, -0.575)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.775, -4.415), pya.DPoint(-1.775, -4.225), pya.DPoint(-1.585, -4.225), pya.DPoint(-1.585, -4.415), pya.DPoint(-1.775, -4.415)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.775, -3.935), pya.DPoint(-1.775, -3.745), pya.DPoint(-1.585, -3.745), pya.DPoint(-1.585, -3.935), pya.DPoint(-1.775, -3.935)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.775, -3.455), pya.DPoint(-1.775, -3.265), pya.DPoint(-1.585, -3.265), pya.DPoint(-1.585, -3.455), pya.DPoint(-1.775, -3.455)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.775, -2.975), pya.DPoint(-1.775, -2.785), pya.DPoint(-1.585, -2.785), pya.DPoint(-1.585, -2.975), pya.DPoint(-1.775, -2.975)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.775, -2.495), pya.DPoint(-1.775, -2.305), pya.DPoint(-1.585, -2.305), pya.DPoint(-1.585, -2.495), pya.DPoint(-1.775, -2.495)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.775, -2.015), pya.DPoint(-1.775, -1.825), pya.DPoint(-1.585, -1.825), pya.DPoint(-1.585, -2.015), pya.DPoint(-1.775, -2.015)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.775, -1.535), pya.DPoint(-1.775, -1.345), pya.DPoint(-1.585, -1.345), pya.DPoint(-1.585, -1.535), pya.DPoint(-1.775, -1.535)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.775, -1.055), pya.DPoint(-1.775, -0.865), pya.DPoint(-1.585, -0.865), pya.DPoint(-1.585, -1.055), pya.DPoint(-1.775, -1.055)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.775, -0.575), pya.DPoint(-1.775, -0.385), pya.DPoint(-1.585, -0.385), pya.DPoint(-1.585, -0.575), pya.DPoint(-1.775, -0.575)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.775, -5.855), pya.DPoint(-1.775, -5.665), pya.DPoint(-1.585, -5.665), pya.DPoint(-1.585, -5.855), pya.DPoint(-1.775, -5.855)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-1.295, -5.855), pya.DPoint(-1.295, -5.665), pya.DPoint(-1.105, -5.665), pya.DPoint(-1.105, -5.855), pya.DPoint(-1.295, -5.855)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.815, -5.855), pya.DPoint(-0.815, -5.665), pya.DPoint(-0.625, -5.665), pya.DPoint(-0.625, -5.855), pya.DPoint(-0.815, -5.855)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.815, -5.375), pya.DPoint(-0.815, -5.185), pya.DPoint(-0.625, -5.185), pya.DPoint(-0.625, -5.375), pya.DPoint(-0.815, -5.375)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.815, -4.895), pya.DPoint(-0.815, -4.705), pya.DPoint(-0.625, -4.705), pya.DPoint(-0.625, -4.895), pya.DPoint(-0.815, -4.895)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.815, -4.415), pya.DPoint(-0.815, -4.225), pya.DPoint(-0.625, -4.225), pya.DPoint(-0.625, -4.415), pya.DPoint(-0.815, -4.415)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.815, -3.935), pya.DPoint(-0.815, -3.745), pya.DPoint(-0.625, -3.745), pya.DPoint(-0.625, -3.935), pya.DPoint(-0.815, -3.935)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(-0.815, -3.455), pya.DPoint(-0.815, -3.265), pya.DPoint(-0.625, -3.265), pya.DPoint(-0.625, -3.455), pya.DPoint(-0.815, -3.455)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.105, -4.895), pya.DPoint(1.105, -4.705), pya.DPoint(1.295, -4.705), pya.DPoint(1.295, -4.895), pya.DPoint(1.105, -4.895)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.105, -4.415), pya.DPoint(1.105, -4.225), pya.DPoint(1.295, -4.225), pya.DPoint(1.295, -4.415), pya.DPoint(1.105, -4.415)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.105, -3.935), pya.DPoint(1.105, -3.745), pya.DPoint(1.295, -3.745), pya.DPoint(1.295, -3.935), pya.DPoint(1.105, -3.935)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.105, -3.455), pya.DPoint(1.105, -3.265), pya.DPoint(1.295, -3.265), pya.DPoint(1.295, -3.455), pya.DPoint(1.105, -3.455)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.105, -2.975), pya.DPoint(1.105, -2.785), pya.DPoint(1.295, -2.785), pya.DPoint(1.295, -2.975), pya.DPoint(1.105, -2.975)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.105, -2.495), pya.DPoint(1.105, -2.305), pya.DPoint(1.295, -2.305), pya.DPoint(1.295, -2.495), pya.DPoint(1.105, -2.495)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.105, -2.015), pya.DPoint(1.105, -1.825), pya.DPoint(1.295, -1.825), pya.DPoint(1.295, -2.015), pya.DPoint(1.105, -2.015)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.105, -1.535), pya.DPoint(1.105, -1.345), pya.DPoint(1.295, -1.345), pya.DPoint(1.295, -1.535), pya.DPoint(1.105, -1.535)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.105, -1.055), pya.DPoint(1.105, -0.865), pya.DPoint(1.295, -0.865), pya.DPoint(1.295, -1.055), pya.DPoint(1.105, -1.055)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.105, -0.575), pya.DPoint(1.105, -0.385), pya.DPoint(1.295, -0.385), pya.DPoint(1.295, -0.575), pya.DPoint(1.105, -0.575)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.625, -5.375), pya.DPoint(0.625, -5.185), pya.DPoint(0.815, -5.185), pya.DPoint(0.815, -5.375), pya.DPoint(0.625, -5.375)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.625, -4.895), pya.DPoint(0.625, -4.705), pya.DPoint(0.815, -4.705), pya.DPoint(0.815, -4.895), pya.DPoint(0.625, -4.895)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.625, -4.415), pya.DPoint(0.625, -4.225), pya.DPoint(0.815, -4.225), pya.DPoint(0.815, -4.415), pya.DPoint(0.625, -4.415)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.625, -3.935), pya.DPoint(0.625, -3.745), pya.DPoint(0.815, -3.745), pya.DPoint(0.815, -3.935), pya.DPoint(0.625, -3.935)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.625, -3.455), pya.DPoint(0.625, -3.265), pya.DPoint(0.815, -3.265), pya.DPoint(0.815, -3.455), pya.DPoint(0.625, -3.455)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.625, -2.975), pya.DPoint(0.625, -2.785), pya.DPoint(0.815, -2.785), pya.DPoint(0.815, -2.975), pya.DPoint(0.625, -2.975)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.625, -2.495), pya.DPoint(0.625, -2.305), pya.DPoint(0.815, -2.305), pya.DPoint(0.815, -2.495), pya.DPoint(0.625, -2.495)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.625, -2.015), pya.DPoint(0.625, -1.825), pya.DPoint(0.815, -1.825), pya.DPoint(0.815, -2.015), pya.DPoint(0.625, -2.015)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.625, -1.535), pya.DPoint(0.625, -1.345), pya.DPoint(0.815, -1.345), pya.DPoint(0.815, -1.535), pya.DPoint(0.625, -1.535)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.625, -1.055), pya.DPoint(0.625, -0.865), pya.DPoint(0.815, -0.865), pya.DPoint(0.815, -1.055), pya.DPoint(0.625, -1.055)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.625, -0.575), pya.DPoint(0.625, -0.385), pya.DPoint(0.815, -0.385), pya.DPoint(0.815, -0.575), pya.DPoint(0.625, -0.575)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.145, -5.375), pya.DPoint(0.145, -5.185), pya.DPoint(0.335, -5.185), pya.DPoint(0.335, -5.375), pya.DPoint(0.145, -5.375)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.145, -4.895), pya.DPoint(0.145, -4.705), pya.DPoint(0.335, -4.705), pya.DPoint(0.335, -4.895), pya.DPoint(0.145, -4.895)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.585, -5.855), pya.DPoint(1.585, -5.665), pya.DPoint(1.775, -5.665), pya.DPoint(1.775, -5.855), pya.DPoint(1.585, -5.855)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.585, -5.375), pya.DPoint(1.585, -5.185), pya.DPoint(1.775, -5.185), pya.DPoint(1.775, -5.375), pya.DPoint(1.585, -5.375)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.585, -4.895), pya.DPoint(1.585, -4.705), pya.DPoint(1.775, -4.705), pya.DPoint(1.775, -4.895), pya.DPoint(1.585, -4.895)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.585, -4.415), pya.DPoint(1.585, -4.225), pya.DPoint(1.775, -4.225), pya.DPoint(1.775, -4.415), pya.DPoint(1.585, -4.415)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.585, -3.935), pya.DPoint(1.585, -3.745), pya.DPoint(1.775, -3.745), pya.DPoint(1.775, -3.935), pya.DPoint(1.585, -3.935)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.585, -3.455), pya.DPoint(1.585, -3.265), pya.DPoint(1.775, -3.265), pya.DPoint(1.775, -3.455), pya.DPoint(1.585, -3.455)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.585, -2.975), pya.DPoint(1.585, -2.785), pya.DPoint(1.775, -2.785), pya.DPoint(1.775, -2.975), pya.DPoint(1.585, -2.975)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.585, -2.495), pya.DPoint(1.585, -2.305), pya.DPoint(1.775, -2.305), pya.DPoint(1.775, -2.495), pya.DPoint(1.585, -2.495)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.585, -2.015), pya.DPoint(1.585, -1.825), pya.DPoint(1.775, -1.825), pya.DPoint(1.775, -2.015), pya.DPoint(1.585, -2.015)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.585, -1.535), pya.DPoint(1.585, -1.345), pya.DPoint(1.775, -1.345), pya.DPoint(1.775, -1.535), pya.DPoint(1.585, -1.535)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.585, -1.055), pya.DPoint(1.585, -0.865), pya.DPoint(1.775, -0.865), pya.DPoint(1.775, -1.055), pya.DPoint(1.585, -1.055)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.585, -0.575), pya.DPoint(1.585, -0.385), pya.DPoint(1.775, -0.385), pya.DPoint(1.775, -0.575), pya.DPoint(1.585, -0.575)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.145, -4.415), pya.DPoint(0.145, -4.225), pya.DPoint(0.335, -4.225), pya.DPoint(0.335, -4.415), pya.DPoint(0.145, -4.415)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.145, -3.935), pya.DPoint(0.145, -3.745), pya.DPoint(0.335, -3.745), pya.DPoint(0.335, -3.935), pya.DPoint(0.145, -3.935)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.145, -3.455), pya.DPoint(0.145, -3.265), pya.DPoint(0.335, -3.265), pya.DPoint(0.335, -3.455), pya.DPoint(0.145, -3.455)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.145, -2.975), pya.DPoint(0.145, -2.785), pya.DPoint(0.335, -2.785), pya.DPoint(0.335, -2.975), pya.DPoint(0.145, -2.975)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.145, -2.495), pya.DPoint(0.145, -2.305), pya.DPoint(0.335, -2.305), pya.DPoint(0.335, -2.495), pya.DPoint(0.145, -2.495)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.145, -2.015), pya.DPoint(0.145, -1.825), pya.DPoint(0.335, -1.825), pya.DPoint(0.335, -2.015), pya.DPoint(0.145, -2.015)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.145, -1.535), pya.DPoint(0.145, -1.345), pya.DPoint(0.335, -1.345), pya.DPoint(0.335, -1.535), pya.DPoint(0.145, -1.535)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.145, -1.055), pya.DPoint(0.145, -0.865), pya.DPoint(0.335, -0.865), pya.DPoint(0.335, -1.055), pya.DPoint(0.145, -1.055)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.145, -0.575), pya.DPoint(0.145, -0.385), pya.DPoint(0.335, -0.385), pya.DPoint(0.335, -0.575), pya.DPoint(0.145, -0.575)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.145, -5.855), pya.DPoint(0.145, -5.665), pya.DPoint(0.335, -5.665), pya.DPoint(0.335, -5.855), pya.DPoint(0.145, -5.855)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(0.625, -5.855), pya.DPoint(0.625, -5.665), pya.DPoint(0.815, -5.665), pya.DPoint(0.815, -5.855), pya.DPoint(0.625, -5.855)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.105, -5.855), pya.DPoint(1.105, -5.665), pya.DPoint(1.295, -5.665), pya.DPoint(1.295, -5.855), pya.DPoint(1.105, -5.855)]))
cell_via_stack_4.shapes(L_Via1).insert(
    pya.DPolygon([pya.DPoint(1.105, -5.375), pya.DPoint(1.105, -5.185), pya.DPoint(1.295, -5.185), pya.DPoint(1.295, -5.375), pya.DPoint(1.105, -5.375)]))

# === via_stack ===
cell_via_stack.shapes(L_Metal5).insert(
    pya.DPolygon([pya.DPoint(-1.825, -0.865), pya.DPoint(-1.825, 0.865), pya.DPoint(1.825, 0.865), pya.DPoint(1.825, -0.865), pya.DPoint(-1.825, -0.865)]))
cell_via_stack.shapes(L_50_0).insert(
    pya.DPolygon([pya.DPoint(-1.825, -0.865), pya.DPoint(-1.825, 0.865), pya.DPoint(1.825, 0.865), pya.DPoint(1.825, -0.865), pya.DPoint(-1.825, -0.865)]))
cell_via_stack.shapes(L_TopMetal2).insert(
    pya.DPolygon([pya.DPoint(-1.775, -0.815), pya.DPoint(-1.775, -0.625), pya.DPoint(-1.585, -0.625), pya.DPoint(-1.585, -0.815), pya.DPoint(-1.775, -0.815)]))
cell_via_stack.shapes(L_TopMetal2).insert(
    pya.DPolygon([pya.DPoint(-1.775, -0.335), pya.DPoint(-1.775, -0.145), pya.DPoint(-1.585, -0.145), pya.DPoint(-1.585, -0.335), pya.DPoint(-1.775, -0.335)]))
cell_via_stack.shapes(L_TopMetal2).insert(
    pya.DPolygon([pya.DPoint(-1.775, 0.145), pya.DPoint(-1.775, 0.335), pya.DPoint(-1.585, 0.335), pya.DPoint(-1.585, 0.145), pya.DPoint(-1.775, 0.145)]))
cell_via_stack.shapes(L_TopMetal2).insert(
    pya.DPolygon([pya.DPoint(-1.775, 0.625), pya.DPoint(-1.775, 0.815), pya.DPoint(-1.585, 0.815), pya.DPoint(-1.585, 0.625), pya.DPoint(-1.775, 0.625)]))
cell_via_stack.shapes(L_TopMetal2).insert(
    pya.DPolygon([pya.DPoint(-1.295, -0.815), pya.DPoint(-1.295, -0.625), pya.DPoint(-1.105, -0.625), pya.DPoint(-1.105, -0.815), pya.DPoint(-1.295, -0.815)]))
cell_via_stack.shapes(L_TopMetal2).insert(
    pya.DPolygon([pya.DPoint(-1.295, -0.335), pya.DPoint(-1.295, -0.145), pya.DPoint(-1.105, -0.145), pya.DPoint(-1.105, -0.335), pya.DPoint(-1.295, -0.335)]))
cell_via_stack.shapes(L_TopMetal2).insert(
    pya.DPolygon([pya.DPoint(-1.295, 0.145), pya.DPoint(-1.295, 0.335), pya.DPoint(-1.105, 0.335), pya.DPoint(-1.105, 0.145), pya.DPoint(-1.295, 0.145)]))
cell_via_stack.shapes(L_TopMetal2).insert(
    pya.DPolygon([pya.DPoint(-1.295, 0.625), pya.DPoint(-1.295, 0.815), pya.DPoint(-1.105, 0.815), pya.DPoint(-1.105, 0.625), pya.DPoint(-1.295, 0.625)]))
cell_via_stack.shapes(L_TopMetal2).insert(
    pya.DPolygon([pya.DPoint(-0.815, -0.815), pya.DPoint(-0.815, -0.625), pya.DPoint(-0.625, -0.625), pya.DPoint(-0.625, -0.815), pya.DPoint(-0.815, -0.815)]))
cell_via_stack.shapes(L_TopMetal2).insert(
    pya.DPolygon([pya.DPoint(-0.815, -0.335), pya.DPoint(-0.815, -0.145), pya.DPoint(-0.625, -0.145), pya.DPoint(-0.625, -0.335), pya.DPoint(-0.815, -0.335)]))
cell_via_stack.shapes(L_TopMetal2).insert(
    pya.DPolygon([pya.DPoint(-0.815, 0.145), pya.DPoint(-0.815, 0.335), pya.DPoint(-0.625, 0.335), pya.DPoint(-0.625, 0.145), pya.DPoint(-0.815, 0.145)]))
cell_via_stack.shapes(L_TopMetal2).insert(
    pya.DPolygon([pya.DPoint(-0.815, 0.625), pya.DPoint(-0.815, 0.815), pya.DPoint(-0.625, 0.815), pya.DPoint(-0.625, 0.625), pya.DPoint(-0.815, 0.625)]))
cell_via_stack.shapes(L_TopMetal2).insert(
    pya.DPolygon([pya.DPoint(-0.335, -0.815), pya.DPoint(-0.335, -0.625), pya.DPoint(-0.145, -0.625), pya.DPoint(-0.145, -0.815), pya.DPoint(-0.335, -0.815)]))
cell_via_stack.shapes(L_TopMetal2).insert(
    pya.DPolygon([pya.DPoint(-0.335, -0.335), pya.DPoint(-0.335, -0.145), pya.DPoint(-0.145, -0.145), pya.DPoint(-0.145, -0.335), pya.DPoint(-0.335, -0.335)]))
cell_via_stack.shapes(L_TopMetal2).insert(
    pya.DPolygon([pya.DPoint(-0.335, 0.145), pya.DPoint(-0.335, 0.335), pya.DPoint(-0.145, 0.335), pya.DPoint(-0.145, 0.145), pya.DPoint(-0.335, 0.145)]))
cell_via_stack.shapes(L_TopMetal2).insert(
    pya.DPolygon([pya.DPoint(-0.335, 0.625), pya.DPoint(-0.335, 0.815), pya.DPoint(-0.145, 0.815), pya.DPoint(-0.145, 0.625), pya.DPoint(-0.335, 0.625)]))
cell_via_stack.shapes(L_TopMetal2).insert(
    pya.DPolygon([pya.DPoint(0.145, -0.815), pya.DPoint(0.145, -0.625), pya.DPoint(0.335, -0.625), pya.DPoint(0.335, -0.815), pya.DPoint(0.145, -0.815)]))
cell_via_stack.shapes(L_TopMetal2).insert(
    pya.DPolygon([pya.DPoint(0.145, -0.335), pya.DPoint(0.145, -0.145), pya.DPoint(0.335, -0.145), pya.DPoint(0.335, -0.335), pya.DPoint(0.145, -0.335)]))
cell_via_stack.shapes(L_TopMetal2).insert(
    pya.DPolygon([pya.DPoint(0.145, 0.145), pya.DPoint(0.145, 0.335), pya.DPoint(0.335, 0.335), pya.DPoint(0.335, 0.145), pya.DPoint(0.145, 0.145)]))
cell_via_stack.shapes(L_TopMetal2).insert(
    pya.DPolygon([pya.DPoint(0.145, 0.625), pya.DPoint(0.145, 0.815), pya.DPoint(0.335, 0.815), pya.DPoint(0.335, 0.625), pya.DPoint(0.145, 0.625)]))
cell_via_stack.shapes(L_TopMetal2).insert(
    pya.DPolygon([pya.DPoint(0.625, -0.815), pya.DPoint(0.625, -0.625), pya.DPoint(0.815, -0.625), pya.DPoint(0.815, -0.815), pya.DPoint(0.625, -0.815)]))
cell_via_stack.shapes(L_TopMetal2).insert(
    pya.DPolygon([pya.DPoint(0.625, -0.335), pya.DPoint(0.625, -0.145), pya.DPoint(0.815, -0.145), pya.DPoint(0.815, -0.335), pya.DPoint(0.625, -0.335)]))
cell_via_stack.shapes(L_TopMetal2).insert(
    pya.DPolygon([pya.DPoint(0.625, 0.145), pya.DPoint(0.625, 0.335), pya.DPoint(0.815, 0.335), pya.DPoint(0.815, 0.145), pya.DPoint(0.625, 0.145)]))
cell_via_stack.shapes(L_TopMetal2).insert(
    pya.DPolygon([pya.DPoint(0.625, 0.625), pya.DPoint(0.625, 0.815), pya.DPoint(0.815, 0.815), pya.DPoint(0.815, 0.625), pya.DPoint(0.625, 0.625)]))
cell_via_stack.shapes(L_TopMetal2).insert(
    pya.DPolygon([pya.DPoint(1.105, -0.815), pya.DPoint(1.105, -0.625), pya.DPoint(1.295, -0.625), pya.DPoint(1.295, -0.815), pya.DPoint(1.105, -0.815)]))
cell_via_stack.shapes(L_TopMetal2).insert(
    pya.DPolygon([pya.DPoint(1.105, -0.335), pya.DPoint(1.105, -0.145), pya.DPoint(1.295, -0.145), pya.DPoint(1.295, -0.335), pya.DPoint(1.105, -0.335)]))
cell_via_stack.shapes(L_TopMetal2).insert(
    pya.DPolygon([pya.DPoint(1.105, 0.145), pya.DPoint(1.105, 0.335), pya.DPoint(1.295, 0.335), pya.DPoint(1.295, 0.145), pya.DPoint(1.105, 0.145)]))
cell_via_stack.shapes(L_TopMetal2).insert(
    pya.DPolygon([pya.DPoint(1.105, 0.625), pya.DPoint(1.105, 0.815), pya.DPoint(1.295, 0.815), pya.DPoint(1.295, 0.625), pya.DPoint(1.105, 0.625)]))
cell_via_stack.shapes(L_TopMetal2).insert(
    pya.DPolygon([pya.DPoint(1.585, -0.815), pya.DPoint(1.585, -0.625), pya.DPoint(1.775, -0.625), pya.DPoint(1.775, -0.815), pya.DPoint(1.585, -0.815)]))
cell_via_stack.shapes(L_TopMetal2).insert(
    pya.DPolygon([pya.DPoint(1.585, -0.335), pya.DPoint(1.585, -0.145), pya.DPoint(1.775, -0.145), pya.DPoint(1.775, -0.335), pya.DPoint(1.585, -0.335)]))
cell_via_stack.shapes(L_TopMetal2).insert(
    pya.DPolygon([pya.DPoint(1.585, 0.145), pya.DPoint(1.585, 0.335), pya.DPoint(1.775, 0.335), pya.DPoint(1.775, 0.145), pya.DPoint(1.585, 0.145)]))
cell_via_stack.shapes(L_TopMetal2).insert(
    pya.DPolygon([pya.DPoint(1.585, 0.625), pya.DPoint(1.585, 0.815), pya.DPoint(1.775, 0.815), pya.DPoint(1.775, 0.625), pya.DPoint(1.585, 0.625)]))

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
cell_dac2u16out2in.shapes(L_Metal1).insert(_path)
_path = pya.DPath([pya.DPoint(-1.9, -4.66), pya.DPoint(35.9, -4.66)], 0.5)
cell_dac2u16out2in.shapes(L_Metal1).insert(_path)
cell_dac2u16out2in.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(-0.375, 6.2), pya.DPoint(-0.375, 7.615), pya.DPoint(0.815, 7.615), pya.DPoint(0.815, 6.2), pya.DPoint(-0.375, 6.2)]))
cell_dac2u16out2in.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(33.625, 6.2), pya.DPoint(33.625, 7.615), pya.DPoint(34.815, 7.615), pya.DPoint(34.815, 6.2), pya.DPoint(33.625, 6.2)]))
cell_dac2u16out2in.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(1.625, 7.405), pya.DPoint(1.625, 8.535), pya.DPoint(32.815, 8.535), pya.DPoint(32.815, 7.405), pya.DPoint(1.625, 7.405)]))
_path = pya.DPath([pya.DPoint(-1.9, 1.615), pya.DPoint(35.9, 1.615)], 1.73)
cell_dac2u16out2in.shapes(L_Metal5).insert(_path)
_path = pya.DPath([pya.DPoint(-1.9, 0), pya.DPoint(35.9, 0)], 0.7)
cell_dac2u16out2in.shapes(L_Metal5).insert(_path)
_path = pya.DPath([pya.DPoint(-1.9, -1.615), pya.DPoint(35.9, -1.615)], 1.73)
cell_dac2u16out2in.shapes(L_Metal5).insert(_path)
_path = pya.DPath([pya.DPoint(-1.9, -4.045), pya.DPoint(35.9, -4.045)], 1.73)
cell_dac2u16out2in.shapes(L_Metal5).insert(_path)
cell_dac2u16out2in.shapes(L_Metal1_pin).insert(
    pya.DPolygon([pya.DPoint(-1, 1.4), pya.DPoint(-1, 6.33), pya.DPoint(35, 6.33), pya.DPoint(35, 1.4), pya.DPoint(-1, 1.4)]))
cell_dac2u16out2in.shapes(L_Metal1_pin).insert(
    pya.DPolygon([pya.DPoint(-1.9, 7.835), pya.DPoint(-1.9, 8.535), pya.DPoint(35.9, 8.535), pya.DPoint(35.9, 7.835), pya.DPoint(-1.9, 7.835)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(32.175, -4.91), pya.DPoint(32.175, -4.62), pya.DPoint(32.375, -4.62), pya.DPoint(32.375, -4.91), pya.DPoint(32.175, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(32.175, -4.91), pya.DPoint(32.175, -4.62), pya.DPoint(32.375, -4.62), pya.DPoint(32.375, -4.91), pya.DPoint(32.175, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(34.175, -4.91), pya.DPoint(34.175, -4.62), pya.DPoint(34.375, -4.62), pya.DPoint(34.375, -4.91), pya.DPoint(34.175, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(33.625, -4.91), pya.DPoint(33.625, -4.62), pya.DPoint(33.825, -4.62), pya.DPoint(33.825, -4.91), pya.DPoint(33.625, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(33.625, -4.91), pya.DPoint(33.625, -4.62), pya.DPoint(33.825, -4.62), pya.DPoint(33.825, -4.91), pya.DPoint(33.625, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(34.175, -4.91), pya.DPoint(34.175, -4.62), pya.DPoint(34.375, -4.62), pya.DPoint(34.375, -4.91), pya.DPoint(34.175, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(3.625, -4.91), pya.DPoint(3.625, -4.62), pya.DPoint(3.825, -4.62), pya.DPoint(3.825, -4.91), pya.DPoint(3.625, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(4.175, -4.91), pya.DPoint(4.175, -4.62), pya.DPoint(4.375, -4.62), pya.DPoint(4.375, -4.91), pya.DPoint(4.175, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(5.625, -4.91), pya.DPoint(5.625, -4.62), pya.DPoint(5.825, -4.62), pya.DPoint(5.825, -4.91), pya.DPoint(5.625, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(6.175, -4.91), pya.DPoint(6.175, -4.62), pya.DPoint(6.375, -4.62), pya.DPoint(6.375, -4.91), pya.DPoint(6.175, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(7.625, -4.91), pya.DPoint(7.625, -4.62), pya.DPoint(7.825, -4.62), pya.DPoint(7.825, -4.91), pya.DPoint(7.625, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(8.175, -4.91), pya.DPoint(8.175, -4.62), pya.DPoint(8.375, -4.62), pya.DPoint(8.375, -4.91), pya.DPoint(8.175, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(9.625, -4.91), pya.DPoint(9.625, -4.62), pya.DPoint(9.825, -4.62), pya.DPoint(9.825, -4.91), pya.DPoint(9.625, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(10.175, -4.91), pya.DPoint(10.175, -4.62), pya.DPoint(10.375, -4.62), pya.DPoint(10.375, -4.91), pya.DPoint(10.175, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(11.625, -4.91), pya.DPoint(11.625, -4.62), pya.DPoint(11.825, -4.62), pya.DPoint(11.825, -4.91), pya.DPoint(11.625, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(12.175, -4.91), pya.DPoint(12.175, -4.62), pya.DPoint(12.375, -4.62), pya.DPoint(12.375, -4.91), pya.DPoint(12.175, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(13.625, -4.91), pya.DPoint(13.625, -4.62), pya.DPoint(13.825, -4.62), pya.DPoint(13.825, -4.91), pya.DPoint(13.625, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(14.175, -4.91), pya.DPoint(14.175, -4.62), pya.DPoint(14.375, -4.62), pya.DPoint(14.375, -4.91), pya.DPoint(14.175, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(15.625, -4.91), pya.DPoint(15.625, -4.62), pya.DPoint(15.825, -4.62), pya.DPoint(15.825, -4.91), pya.DPoint(15.625, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(16.175, -4.91), pya.DPoint(16.175, -4.62), pya.DPoint(16.375, -4.62), pya.DPoint(16.375, -4.91), pya.DPoint(16.175, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(17.625, -4.91), pya.DPoint(17.625, -4.62), pya.DPoint(17.825, -4.62), pya.DPoint(17.825, -4.91), pya.DPoint(17.625, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(18.175, -4.91), pya.DPoint(18.175, -4.62), pya.DPoint(18.375, -4.62), pya.DPoint(18.375, -4.91), pya.DPoint(18.175, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(19.625, -4.91), pya.DPoint(19.625, -4.62), pya.DPoint(19.825, -4.62), pya.DPoint(19.825, -4.91), pya.DPoint(19.625, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(20.175, -4.91), pya.DPoint(20.175, -4.62), pya.DPoint(20.375, -4.62), pya.DPoint(20.375, -4.91), pya.DPoint(20.175, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(21.625, -4.91), pya.DPoint(21.625, -4.62), pya.DPoint(21.825, -4.62), pya.DPoint(21.825, -4.91), pya.DPoint(21.625, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(22.175, -4.91), pya.DPoint(22.175, -4.62), pya.DPoint(22.375, -4.62), pya.DPoint(22.375, -4.91), pya.DPoint(22.175, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(23.625, -4.91), pya.DPoint(23.625, -4.62), pya.DPoint(23.825, -4.62), pya.DPoint(23.825, -4.91), pya.DPoint(23.625, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(24.175, -4.91), pya.DPoint(24.175, -4.62), pya.DPoint(24.375, -4.62), pya.DPoint(24.375, -4.91), pya.DPoint(24.175, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(25.625, -4.91), pya.DPoint(25.625, -4.62), pya.DPoint(25.825, -4.62), pya.DPoint(25.825, -4.91), pya.DPoint(25.625, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(26.175, -4.91), pya.DPoint(26.175, -4.62), pya.DPoint(26.375, -4.62), pya.DPoint(26.375, -4.91), pya.DPoint(26.175, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(27.625, -4.91), pya.DPoint(27.625, -4.62), pya.DPoint(27.825, -4.62), pya.DPoint(27.825, -4.91), pya.DPoint(27.625, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(28.175, -4.91), pya.DPoint(28.175, -4.62), pya.DPoint(28.375, -4.62), pya.DPoint(28.375, -4.91), pya.DPoint(28.175, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(29.625, -4.91), pya.DPoint(29.625, -4.62), pya.DPoint(29.825, -4.62), pya.DPoint(29.825, -4.91), pya.DPoint(29.625, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(30.175, -4.91), pya.DPoint(30.175, -4.62), pya.DPoint(30.375, -4.62), pya.DPoint(30.375, -4.91), pya.DPoint(30.175, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(31.625, -4.91), pya.DPoint(31.625, -4.62), pya.DPoint(31.825, -4.62), pya.DPoint(31.825, -4.91), pya.DPoint(31.625, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(-0.375, -4.91), pya.DPoint(-0.375, -4.62), pya.DPoint(-0.175, -4.62), pya.DPoint(-0.175, -4.91), pya.DPoint(-0.375, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(0.175, -4.91), pya.DPoint(0.175, -4.62), pya.DPoint(0.375, -4.62), pya.DPoint(0.375, -4.91), pya.DPoint(0.175, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(1.625, -4.91), pya.DPoint(1.625, -4.62), pya.DPoint(1.825, -4.62), pya.DPoint(1.825, -4.91), pya.DPoint(1.625, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(2.175, -4.91), pya.DPoint(2.175, -4.62), pya.DPoint(2.375, -4.62), pya.DPoint(2.375, -4.91), pya.DPoint(2.175, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(3.625, -4.91), pya.DPoint(3.625, -4.62), pya.DPoint(3.825, -4.62), pya.DPoint(3.825, -4.91), pya.DPoint(3.625, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(4.175, -4.91), pya.DPoint(4.175, -4.62), pya.DPoint(4.375, -4.62), pya.DPoint(4.375, -4.91), pya.DPoint(4.175, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(5.625, -4.91), pya.DPoint(5.625, -4.62), pya.DPoint(5.825, -4.62), pya.DPoint(5.825, -4.91), pya.DPoint(5.625, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(6.175, -4.91), pya.DPoint(6.175, -4.62), pya.DPoint(6.375, -4.62), pya.DPoint(6.375, -4.91), pya.DPoint(6.175, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(7.625, -4.91), pya.DPoint(7.625, -4.62), pya.DPoint(7.825, -4.62), pya.DPoint(7.825, -4.91), pya.DPoint(7.625, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(8.175, -4.91), pya.DPoint(8.175, -4.62), pya.DPoint(8.375, -4.62), pya.DPoint(8.375, -4.91), pya.DPoint(8.175, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(9.625, -4.91), pya.DPoint(9.625, -4.62), pya.DPoint(9.825, -4.62), pya.DPoint(9.825, -4.91), pya.DPoint(9.625, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(10.175, -4.91), pya.DPoint(10.175, -4.62), pya.DPoint(10.375, -4.62), pya.DPoint(10.375, -4.91), pya.DPoint(10.175, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(11.625, -4.91), pya.DPoint(11.625, -4.62), pya.DPoint(11.825, -4.62), pya.DPoint(11.825, -4.91), pya.DPoint(11.625, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(12.175, -4.91), pya.DPoint(12.175, -4.62), pya.DPoint(12.375, -4.62), pya.DPoint(12.375, -4.91), pya.DPoint(12.175, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(13.625, -4.91), pya.DPoint(13.625, -4.62), pya.DPoint(13.825, -4.62), pya.DPoint(13.825, -4.91), pya.DPoint(13.625, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(14.175, -4.91), pya.DPoint(14.175, -4.62), pya.DPoint(14.375, -4.62), pya.DPoint(14.375, -4.91), pya.DPoint(14.175, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(15.625, -4.91), pya.DPoint(15.625, -4.62), pya.DPoint(15.825, -4.62), pya.DPoint(15.825, -4.91), pya.DPoint(15.625, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(16.175, -4.91), pya.DPoint(16.175, -4.62), pya.DPoint(16.375, -4.62), pya.DPoint(16.375, -4.91), pya.DPoint(16.175, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(17.625, -4.91), pya.DPoint(17.625, -4.62), pya.DPoint(17.825, -4.62), pya.DPoint(17.825, -4.91), pya.DPoint(17.625, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(18.175, -4.91), pya.DPoint(18.175, -4.62), pya.DPoint(18.375, -4.62), pya.DPoint(18.375, -4.91), pya.DPoint(18.175, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(19.625, -4.91), pya.DPoint(19.625, -4.62), pya.DPoint(19.825, -4.62), pya.DPoint(19.825, -4.91), pya.DPoint(19.625, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(20.175, -4.91), pya.DPoint(20.175, -4.62), pya.DPoint(20.375, -4.62), pya.DPoint(20.375, -4.91), pya.DPoint(20.175, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(21.625, -4.91), pya.DPoint(21.625, -4.62), pya.DPoint(21.825, -4.62), pya.DPoint(21.825, -4.91), pya.DPoint(21.625, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(22.175, -4.91), pya.DPoint(22.175, -4.62), pya.DPoint(22.375, -4.62), pya.DPoint(22.375, -4.91), pya.DPoint(22.175, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(23.625, -4.91), pya.DPoint(23.625, -4.62), pya.DPoint(23.825, -4.62), pya.DPoint(23.825, -4.91), pya.DPoint(23.625, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(24.175, -4.91), pya.DPoint(24.175, -4.62), pya.DPoint(24.375, -4.62), pya.DPoint(24.375, -4.91), pya.DPoint(24.175, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(25.625, -4.91), pya.DPoint(25.625, -4.62), pya.DPoint(25.825, -4.62), pya.DPoint(25.825, -4.91), pya.DPoint(25.625, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(26.175, -4.91), pya.DPoint(26.175, -4.62), pya.DPoint(26.375, -4.62), pya.DPoint(26.375, -4.91), pya.DPoint(26.175, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(27.625, -4.91), pya.DPoint(27.625, -4.62), pya.DPoint(27.825, -4.62), pya.DPoint(27.825, -4.91), pya.DPoint(27.625, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(28.175, -4.91), pya.DPoint(28.175, -4.62), pya.DPoint(28.375, -4.62), pya.DPoint(28.375, -4.91), pya.DPoint(28.175, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(29.625, -4.91), pya.DPoint(29.625, -4.62), pya.DPoint(29.825, -4.62), pya.DPoint(29.825, -4.91), pya.DPoint(29.625, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(30.175, -4.91), pya.DPoint(30.175, -4.62), pya.DPoint(30.375, -4.62), pya.DPoint(30.375, -4.91), pya.DPoint(30.175, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(31.625, -4.91), pya.DPoint(31.625, -4.62), pya.DPoint(31.825, -4.62), pya.DPoint(31.825, -4.91), pya.DPoint(31.625, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(-0.375, -4.91), pya.DPoint(-0.375, -4.62), pya.DPoint(-0.175, -4.62), pya.DPoint(-0.175, -4.91), pya.DPoint(-0.375, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(0.175, -4.91), pya.DPoint(0.175, -4.62), pya.DPoint(0.375, -4.62), pya.DPoint(0.375, -4.91), pya.DPoint(0.175, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(1.625, -4.91), pya.DPoint(1.625, -4.62), pya.DPoint(1.825, -4.62), pya.DPoint(1.825, -4.91), pya.DPoint(1.625, -4.91)]))
cell_dac2u16out2in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(2.175, -4.91), pya.DPoint(2.175, -4.62), pya.DPoint(2.375, -4.62), pya.DPoint(2.375, -4.91), pya.DPoint(2.175, -4.91)]))
_txt = pya.Text("VbiasP",
               pya.Trans(0, False, pya.Vector(17000, 3865)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal1_label).insert(_txt)
_txt = pya.Text("Iout",
               pya.Trans(0, False, pya.Vector(17000, 8185)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal1_label).insert(_txt)
_txt = pya.Text("EN[1]",
               pya.Trans(0, False, pya.Vector(33725, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ENB[1]",
               pya.Trans(0, False, pya.Vector(34275, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[0]",
               pya.Trans(0, False, pya.Vector(1725, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[0]",
               pya.Trans(0, False, pya.Vector(2275, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[1]",
               pya.Trans(0, False, pya.Vector(3725, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[1]",
               pya.Trans(0, False, pya.Vector(4275, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[2]",
               pya.Trans(0, False, pya.Vector(5725, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[2]",
               pya.Trans(0, False, pya.Vector(6275, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[3]",
               pya.Trans(0, False, pya.Vector(7725, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[3]",
               pya.Trans(0, False, pya.Vector(8275, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[4]",
               pya.Trans(0, False, pya.Vector(9725, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[4]",
               pya.Trans(0, False, pya.Vector(10275, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("EN[0]",
               pya.Trans(0, False, pya.Vector(-275, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ENB[0]",
               pya.Trans(0, False, pya.Vector(275, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON",
               pya.Trans(0, False, pya.Vector(-275, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB",
               pya.Trans(0, False, pya.Vector(275, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON",
               pya.Trans(0, False, pya.Vector(1725, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB",
               pya.Trans(0, False, pya.Vector(2275, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON",
               pya.Trans(0, False, pya.Vector(3725, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB",
               pya.Trans(0, False, pya.Vector(4275, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON",
               pya.Trans(0, False, pya.Vector(5725, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB",
               pya.Trans(0, False, pya.Vector(6275, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON",
               pya.Trans(0, False, pya.Vector(7725, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB",
               pya.Trans(0, False, pya.Vector(8275, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON",
               pya.Trans(0, False, pya.Vector(9725, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB",
               pya.Trans(0, False, pya.Vector(10275, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[5]",
               pya.Trans(0, False, pya.Vector(11725, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[5]",
               pya.Trans(0, False, pya.Vector(12275, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[6]",
               pya.Trans(0, False, pya.Vector(13725, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[6]",
               pya.Trans(0, False, pya.Vector(14275, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[7]",
               pya.Trans(0, False, pya.Vector(15725, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[7]",
               pya.Trans(0, False, pya.Vector(16275, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[8]",
               pya.Trans(0, False, pya.Vector(17725, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[8]",
               pya.Trans(0, False, pya.Vector(18275, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[9]",
               pya.Trans(0, False, pya.Vector(19725, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[9]",
               pya.Trans(0, False, pya.Vector(20275, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[10]",
               pya.Trans(0, False, pya.Vector(21725, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[10]",
               pya.Trans(0, False, pya.Vector(22275, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON",
               pya.Trans(0, False, pya.Vector(11725, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB",
               pya.Trans(0, False, pya.Vector(12275, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON",
               pya.Trans(0, False, pya.Vector(13725, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB",
               pya.Trans(0, False, pya.Vector(14275, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON",
               pya.Trans(0, False, pya.Vector(15725, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB",
               pya.Trans(0, False, pya.Vector(16275, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON",
               pya.Trans(0, False, pya.Vector(17725, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB",
               pya.Trans(0, False, pya.Vector(18275, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON",
               pya.Trans(0, False, pya.Vector(19725, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB",
               pya.Trans(0, False, pya.Vector(20275, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON",
               pya.Trans(0, False, pya.Vector(21725, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB",
               pya.Trans(0, False, pya.Vector(22275, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[11]",
               pya.Trans(0, False, pya.Vector(23725, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[11]",
               pya.Trans(0, False, pya.Vector(24275, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[12]",
               pya.Trans(0, False, pya.Vector(25725, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[12]",
               pya.Trans(0, False, pya.Vector(26275, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[13]",
               pya.Trans(0, False, pya.Vector(27725, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[13]",
               pya.Trans(0, False, pya.Vector(28275, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[14]",
               pya.Trans(0, False, pya.Vector(29725, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[14]",
               pya.Trans(0, False, pya.Vector(30275, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[15]",
               pya.Trans(0, False, pya.Vector(31725, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[15]",
               pya.Trans(0, False, pya.Vector(32275, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON",
               pya.Trans(0, False, pya.Vector(23725, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB",
               pya.Trans(0, False, pya.Vector(24275, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON",
               pya.Trans(0, False, pya.Vector(25725, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB",
               pya.Trans(0, False, pya.Vector(26275, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON",
               pya.Trans(0, False, pya.Vector(27725, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB",
               pya.Trans(0, False, pya.Vector(28275, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON",
               pya.Trans(0, False, pya.Vector(29725, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB",
               pya.Trans(0, False, pya.Vector(30275, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON",
               pya.Trans(0, False, pya.Vector(31725, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB",
               pya.Trans(0, False, pya.Vector(32275, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON",
               pya.Trans(0, False, pya.Vector(33725, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB",
               pya.Trans(0, False, pya.Vector(34275, -4765)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal2_label).insert(_txt)
cell_dac2u16out2in.shapes(L_Metal5_pin).insert(
    pya.DPolygon([pya.DPoint(-1.9, -0.35), pya.DPoint(-1.9, 0.35), pya.DPoint(35.9, 0.35), pya.DPoint(35.9, -0.35), pya.DPoint(-1.9, -0.35)]))
cell_dac2u16out2in.shapes(L_Metal5_pin).insert(
    pya.DPolygon([pya.DPoint(-1.9, 0.75), pya.DPoint(-1.9, 2.48), pya.DPoint(35.9, 2.48), pya.DPoint(35.9, 0.75), pya.DPoint(-1.9, 0.75)]))
cell_dac2u16out2in.shapes(L_Metal5_pin).insert(
    pya.DPolygon([pya.DPoint(-1.9, -2.48), pya.DPoint(-1.9, -0.75), pya.DPoint(35.9, -0.75), pya.DPoint(35.9, -2.48), pya.DPoint(-1.9, -2.48)]))
cell_dac2u16out2in.shapes(L_Metal5_pin).insert(
    pya.DPolygon([pya.DPoint(-1.9, -4.91), pya.DPoint(-1.9, -3.18), pya.DPoint(35.9, -3.18), pya.DPoint(35.9, -4.91), pya.DPoint(-1.9, -4.91)]))
_txt = pya.Text("VDD",
               pya.Trans(0, False, pya.Vector(17000, 1615)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal5_label).insert(_txt)
_txt = pya.Text("VcascP",
               pya.Trans(0, False, pya.Vector(17000, 0)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal5_label).insert(_txt)
_txt = pya.Text("VDD",
               pya.Trans(0, False, pya.Vector(17000, -1615)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal5_label).insert(_txt)
_txt = pya.Text("VSS",
               pya.Trans(0, False, pya.Vector(17000, -4045)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u16out2in.shapes(L_Metal5_label).insert(_txt)

# === via_stack$11 ===
cell_via_stack_11.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(-0.145, -0.35), pya.DPoint(-0.145, 0.35), pya.DPoint(0.145, 0.35), pya.DPoint(0.145, -0.35), pya.DPoint(-0.145, -0.35)]))
cell_via_stack_11.shapes(L_Metal2).insert(
    pya.DPolygon([pya.DPoint(-0.145, -0.35), pya.DPoint(-0.145, 0.35), pya.DPoint(0.145, 0.35), pya.DPoint(0.145, -0.35), pya.DPoint(-0.145, -0.35)]))
cell_via_stack_11.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(-0.095, -0.3), pya.DPoint(-0.095, -0.11), pya.DPoint(0.095, -0.11), pya.DPoint(0.095, -0.3), pya.DPoint(-0.095, -0.3)]))
cell_via_stack_11.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(-0.095, 0.11), pya.DPoint(-0.095, 0.3), pya.DPoint(0.095, 0.3), pya.DPoint(0.095, 0.11), pya.DPoint(-0.095, 0.11)]))
cell_via_stack_11.shapes(L_Metal5).insert(
    pya.DPolygon([pya.DPoint(-0.145, -0.35), pya.DPoint(-0.145, 0.35), pya.DPoint(0.145, 0.35), pya.DPoint(0.145, -0.35), pya.DPoint(-0.145, -0.35)]))
cell_via_stack_11.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(-0.095, -0.3), pya.DPoint(-0.095, -0.11), pya.DPoint(0.095, -0.11), pya.DPoint(0.095, -0.3), pya.DPoint(-0.095, -0.3)]))
cell_via_stack_11.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(-0.095, 0.11), pya.DPoint(-0.095, 0.3), pya.DPoint(0.095, 0.3), pya.DPoint(0.095, 0.11), pya.DPoint(-0.095, 0.11)]))

# === via_stack$10 ===
cell_via_stack_10.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(-0.35, -0.145), pya.DPoint(-0.35, 0.145), pya.DPoint(0.35, 0.145), pya.DPoint(0.35, -0.145), pya.DPoint(-0.35, -0.145)]))
cell_via_stack_10.shapes(L_Metal2).insert(
    pya.DPolygon([pya.DPoint(-0.35, -0.145), pya.DPoint(-0.35, 0.145), pya.DPoint(0.35, 0.145), pya.DPoint(0.35, -0.145), pya.DPoint(-0.35, -0.145)]))
cell_via_stack_10.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(-0.3, -0.095), pya.DPoint(-0.3, 0.095), pya.DPoint(-0.11, 0.095), pya.DPoint(-0.11, -0.095), pya.DPoint(-0.3, -0.095)]))
cell_via_stack_10.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(0.11, -0.095), pya.DPoint(0.11, 0.095), pya.DPoint(0.3, 0.095), pya.DPoint(0.3, -0.095), pya.DPoint(0.11, -0.095)]))
cell_via_stack_10.shapes(L_Metal5).insert(
    pya.DPolygon([pya.DPoint(-0.35, -0.145), pya.DPoint(-0.35, 0.145), pya.DPoint(0.35, 0.145), pya.DPoint(0.35, -0.145), pya.DPoint(-0.35, -0.145)]))
cell_via_stack_10.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(-0.3, -0.095), pya.DPoint(-0.3, 0.095), pya.DPoint(-0.11, 0.095), pya.DPoint(-0.11, -0.095), pya.DPoint(-0.3, -0.095)]))
cell_via_stack_10.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(0.11, -0.095), pya.DPoint(0.11, 0.095), pya.DPoint(0.3, 0.095), pya.DPoint(0.3, -0.095), pya.DPoint(0.11, -0.095)]))

# === via_stack$7 ===
cell_via_stack_7.shapes(L_Metal1).insert(
    pya.DPolygon([pya.DPoint(-0.35, -0.35), pya.DPoint(-0.35, 0.35), pya.DPoint(0.35, 0.35), pya.DPoint(0.35, -0.35), pya.DPoint(-0.35, -0.35)]))
cell_via_stack_7.shapes(L_Metal2).insert(
    pya.DPolygon([pya.DPoint(-0.35, -0.35), pya.DPoint(-0.35, 0.35), pya.DPoint(0.35, 0.35), pya.DPoint(0.35, -0.35), pya.DPoint(-0.35, -0.35)]))
cell_via_stack_7.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(-0.3, -0.3), pya.DPoint(-0.3, -0.11), pya.DPoint(-0.11, -0.11), pya.DPoint(-0.11, -0.3), pya.DPoint(-0.3, -0.3)]))
cell_via_stack_7.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(-0.3, 0.11), pya.DPoint(-0.3, 0.3), pya.DPoint(-0.11, 0.3), pya.DPoint(-0.11, 0.11), pya.DPoint(-0.3, 0.11)]))
cell_via_stack_7.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(0.11, -0.3), pya.DPoint(0.11, -0.11), pya.DPoint(0.3, -0.11), pya.DPoint(0.3, -0.3), pya.DPoint(0.11, -0.3)]))
cell_via_stack_7.shapes(L_Metal3).insert(
    pya.DPolygon([pya.DPoint(0.11, 0.11), pya.DPoint(0.11, 0.3), pya.DPoint(0.3, 0.3), pya.DPoint(0.3, 0.11), pya.DPoint(0.11, 0.11)]))
cell_via_stack_7.shapes(L_Metal5).insert(
    pya.DPolygon([pya.DPoint(-0.35, -0.35), pya.DPoint(-0.35, 0.35), pya.DPoint(0.35, 0.35), pya.DPoint(0.35, -0.35), pya.DPoint(-0.35, -0.35)]))
cell_via_stack_7.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(-0.3, -0.3), pya.DPoint(-0.3, -0.11), pya.DPoint(-0.11, -0.11), pya.DPoint(-0.11, -0.3), pya.DPoint(-0.3, -0.3)]))
cell_via_stack_7.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(-0.3, 0.11), pya.DPoint(-0.3, 0.3), pya.DPoint(-0.11, 0.3), pya.DPoint(-0.11, 0.11), pya.DPoint(-0.3, 0.11)]))
cell_via_stack_7.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(0.11, -0.3), pya.DPoint(0.11, -0.11), pya.DPoint(0.3, -0.11), pya.DPoint(0.3, -0.3), pya.DPoint(0.11, -0.3)]))
cell_via_stack_7.shapes(L_Metal4).insert(
    pya.DPolygon([pya.DPoint(0.11, 0.11), pya.DPoint(0.11, 0.3), pya.DPoint(0.3, 0.3), pya.DPoint(0.3, 0.11), pya.DPoint(0.11, 0.11)]))

# === inputwires ===
cell_inputwires.insert(pya.DCellInstArray(
    cell_via_stack_11.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(0.145, 0.35))))
cell_inputwires.insert(pya.DCellInstArray(
    cell_via_stack_13.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(7.65, 0.35))))
cell_inputwires.insert(pya.DCellInstArray(
    cell_via_stack_13.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(7.65, 10.595))))
cell_inputwires.insert(pya.DCellInstArray(
    cell_via_stack_13.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(7.65, 16.72))))
cell_inputwires.insert(pya.DCellInstArray(
    cell_via_stack_13.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(7.65, 6.47))))
cell_inputwires.insert(pya.DCellInstArray(
    cell_via_stack_13.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(83.25, 0.35))))
cell_inputwires.insert(pya.DCellInstArray(
    cell_via_stack_13.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(83.25, 11.695))))
cell_inputwires.insert(pya.DCellInstArray(
    cell_via_stack_13.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(83.25, 16.72))))
cell_inputwires.insert(pya.DCellInstArray(
    cell_via_stack_13.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(83.25, 5.37))))
cell_inputwires.insert(pya.DCellInstArray(
    cell_via_stack_13.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(158.85, 0.35))))
cell_inputwires.insert(pya.DCellInstArray(
    cell_via_stack_13.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(158.85, 12.795))))
cell_inputwires.insert(pya.DCellInstArray(
    cell_via_stack_13.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(158.85, 16.72))))
cell_inputwires.insert(pya.DCellInstArray(
    cell_via_stack_13.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(158.85, 4.27))))
_path = pya.DPath([pya.DPoint(7.65, 17.07), pya.DPoint(7.65, 10.245)], 0.7)
cell_inputwires.shapes(L_Metal2).insert(_path)
_path = pya.DPath([pya.DPoint(7.65, 6.82), pya.DPoint(7.65, 0.005)], 0.7)
cell_inputwires.shapes(L_Metal2).insert(_path)
_path = pya.DPath([pya.DPoint(83.25, 17.07), pya.DPoint(83.25, 11.345)], 0.7)
cell_inputwires.shapes(L_Metal2).insert(_path)
_path = pya.DPath([pya.DPoint(83.25, 5.72), pya.DPoint(83.25, 0.005)], 0.7)
cell_inputwires.shapes(L_Metal2).insert(_path)
_path = pya.DPath([pya.DPoint(158.85, 17.07), pya.DPoint(158.85, 12.445)], 0.7)
cell_inputwires.shapes(L_Metal2).insert(_path)
_path = pya.DPath([pya.DPoint(158.85, 4.62), pya.DPoint(158.85, 0.005)], 0.7)
cell_inputwires.shapes(L_Metal2).insert(_path)
_path = pya.DPath([pya.DPoint(158.5, 12.795), pya.DPoint(245.635, 12.795)], 0.7)
cell_inputwires.shapes(L_Metal5).insert(_path)
_path = pya.DPath([pya.DPoint(82.9, 11.695), pya.DPoint(245.635, 11.695)], 0.7)
cell_inputwires.shapes(L_Metal5).insert(_path)
_path = pya.DPath([pya.DPoint(7.3, 10.595), pya.DPoint(245.635, 10.595)], 0.7)
cell_inputwires.shapes(L_Metal5).insert(_path)
_path = pya.DPath([pya.DPoint(7.3, 6.47), pya.DPoint(245.635, 6.47)], 0.7)
cell_inputwires.shapes(L_Metal5).insert(_path)
_path = pya.DPath([pya.DPoint(82.9, 5.37), pya.DPoint(245.635, 5.37)], 0.7)
cell_inputwires.shapes(L_Metal5).insert(_path)
_path = pya.DPath([pya.DPoint(158.5, 4.27), pya.DPoint(245.635, 4.27)], 0.7)
cell_inputwires.shapes(L_Metal5).insert(_path)
_path = pya.DPath([pya.DPoint(0, 0.35), pya.DPoint(8, 0.35)], 0.7)
cell_inputwires.shapes(L_Metal5).insert(_path)
_path = pya.DPath([pya.DPoint(0, 16.72), pya.DPoint(8, 16.72)], 0.7)
cell_inputwires.shapes(L_Metal5).insert(_path)
_path = pya.DPath([pya.DPoint(75.6, 0.35), pya.DPoint(83.6, 0.35)], 0.7)
cell_inputwires.shapes(L_Metal5).insert(_path)
_path = pya.DPath([pya.DPoint(75.6, 16.72), pya.DPoint(83.6, 16.72)], 0.7)
cell_inputwires.shapes(L_Metal5).insert(_path)
_path = pya.DPath([pya.DPoint(151.2, 0.35), pya.DPoint(159.2, 0.35)], 0.7)
cell_inputwires.shapes(L_Metal5).insert(_path)
_path = pya.DPath([pya.DPoint(151.2, 16.72), pya.DPoint(159.2, 16.72)], 0.7)
cell_inputwires.shapes(L_Metal5).insert(_path)
_path = pya.DPath([pya.DPoint(226.8, 16.72), pya.DPoint(245.635, 16.72)], 0.7)
cell_inputwires.shapes(L_Metal5).insert(_path)
_path = pya.DPath([pya.DPoint(226.8, 0.35), pya.DPoint(245.635, 0.35)], 0.7)
cell_inputwires.shapes(L_Metal5).insert(_path)

# === dacbuffer ===
cell_dacbuffer.insert(pya.DCellInstArray(
    cell_pmos_buffer_cap.cell_index(),
    pya.DCplxTrans(1, 180, False,
                  pya.DVector(34.025, 11.7)),
    pya.DVector(-15.7, 0),
    pya.DVector(0, -5.44),
    2, 2))
cell_dacbuffer.insert(pya.DCellInstArray(
    cell_pmos_buffer_cap.cell_index(),
    pya.DCplxTrans(1, 0, True,
                  pya.DVector(3.725, 24.65)),
    pya.DVector(15.7, 0),
    pya.DVector(0, -5.44),
    2, 2))
cell_dacbuffer.insert(pya.DCellInstArray(
    cell_via_stack_8.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(17.21, 19.665))))
cell_dacbuffer.insert(pya.DCellInstArray(
    cell_via_stack_8.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(17.21, 22.895))))
cell_dacbuffer.insert(pya.DCellInstArray(
    cell_via_stack_8.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(17.21, 3.295))))
cell_dacbuffer.insert(pya.DCellInstArray(
    cell_via_stack_8.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(17.21, 6.525))))
cell_dacbuffer.insert(pya.DCellInstArray(
    cell_via_stack_8.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(4.79, 19.665))))
cell_dacbuffer.insert(pya.DCellInstArray(
    cell_via_stack_8.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(4.79, 22.895))))
cell_dacbuffer.insert(pya.DCellInstArray(
    cell_via_stack_8.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(4.79, 3.295))))
cell_dacbuffer.insert(pya.DCellInstArray(
    cell_via_stack_8.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(4.79, 6.525))))
cell_dacbuffer.insert(pya.DCellInstArray(
    cell_via_stack_8.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(33.01, 19.665))))
cell_dacbuffer.insert(pya.DCellInstArray(
    cell_via_stack_8.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(33.01, 22.895))))
cell_dacbuffer.insert(pya.DCellInstArray(
    cell_via_stack_8.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(33.01, 3.295))))
cell_dacbuffer.insert(pya.DCellInstArray(
    cell_via_stack_8.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(33.01, 6.525))))
cell_dacbuffer.insert(pya.DCellInstArray(
    cell_via_stack_8.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(20.64, 19.665))))
cell_dacbuffer.insert(pya.DCellInstArray(
    cell_via_stack_8.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(20.64, 22.895))))
cell_dacbuffer.insert(pya.DCellInstArray(
    cell_via_stack_8.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(20.64, 3.295))))
cell_dacbuffer.insert(pya.DCellInstArray(
    cell_via_stack_8.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(20.64, 6.525))))
_path = pya.DPath([pya.DPoint(0, 0.25), pya.DPoint(37.8, 0.25)], 0.5)
cell_dacbuffer.shapes(L_Metal1).insert(_path)
_path = pya.DPath([pya.DPoint(0, 13.095), pya.DPoint(37.8, 13.095)], 0.7)
cell_dacbuffer.shapes(L_Metal1).insert(_path)
_path = pya.DPath([pya.DPoint(0, 25.94), pya.DPoint(37.8, 25.94)], 0.5)
cell_dacbuffer.shapes(L_Metal1).insert(_path)
_path = pya.DPath([pya.DPoint(20.64, 23.76), pya.DPoint(20.64, 2.43)], 1.73)
cell_dacbuffer.shapes(L_Metal2).insert(_path)
_path = pya.DPath([pya.DPoint(4.79, 23.76), pya.DPoint(4.79, 2.43)], 1.73)
cell_dacbuffer.shapes(L_Metal2).insert(_path)
_path = pya.DPath([pya.DPoint(17.21, 23.76), pya.DPoint(17.21, 2.43)], 1.73)
cell_dacbuffer.shapes(L_Metal2).insert(_path)
_path = pya.DPath([pya.DPoint(33.01, 23.76), pya.DPoint(33.01, 2.43)], 1.73)
cell_dacbuffer.shapes(L_Metal2).insert(_path)
_path = pya.DPath([pya.DPoint(0, 0.865), pya.DPoint(37.8, 0.865)], 1.73)
cell_dacbuffer.shapes(L_Metal5).insert(_path)
_path = pya.DPath([pya.DPoint(0, 3.295), pya.DPoint(37.8, 3.295)], 1.73)
cell_dacbuffer.shapes(L_Metal5).insert(_path)
_path = pya.DPath([pya.DPoint(0, 6.525), pya.DPoint(37.8, 6.525)], 1.73)
cell_dacbuffer.shapes(L_Metal5).insert(_path)
_path = pya.DPath([pya.DPoint(0, 19.665), pya.DPoint(37.8, 19.665)], 1.73)
cell_dacbuffer.shapes(L_Metal5).insert(_path)
_path = pya.DPath([pya.DPoint(0, 22.895), pya.DPoint(37.8, 22.895)], 1.73)
cell_dacbuffer.shapes(L_Metal5).insert(_path)
_path = pya.DPath([pya.DPoint(0, 25.325), pya.DPoint(37.8, 25.325)], 1.73)
cell_dacbuffer.shapes(L_Metal5).insert(_path)
cell_dacbuffer.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(3.325, 1.36), pya.DPoint(3.325, 24.83), pya.DPoint(34.425, 24.83), pya.DPoint(34.425, 1.36), pya.DPoint(3.325, 1.36)]))
cell_dacbuffer.shapes(L_NWell).insert(
    pya.DPolygon([pya.DPoint(3.105, 0.41), pya.DPoint(3.105, 25.78), pya.DPoint(34.645, 25.78), pya.DPoint(34.645, 0.41), pya.DPoint(3.105, 0.41)]))
cell_dacbuffer.shapes(L_prBoundary).insert(
    pya.DPolygon([pya.DPoint(0, -0.07), pya.DPoint(0, 26.26), pya.DPoint(37.8, 26.26), pya.DPoint(37.8, -0.07), pya.DPoint(0, -0.07)]))
cell_dacbuffer.shapes(L_Metal1_pin).insert(
    pya.DPolygon([pya.DPoint(0, 12.745), pya.DPoint(0, 13.445), pya.DPoint(37.8, 13.445), pya.DPoint(37.8, 12.745), pya.DPoint(0, 12.745)]))
_txt = pya.Text("Iout",
               pya.Trans(0, False, pya.Vector(18900, 13095)))
_txt.halign = 1
_txt.valign = 1
cell_dacbuffer.shapes(L_Metal1_label).insert(_txt)
cell_dacbuffer.shapes(L_Metal5_pin).insert(
    pya.DPolygon([pya.DPoint(0, 0), pya.DPoint(0, 1.73), pya.DPoint(37.8, 1.73), pya.DPoint(37.8, 0), pya.DPoint(0, 0)]))
cell_dacbuffer.shapes(L_Metal5_pin).insert(
    pya.DPolygon([pya.DPoint(0, 2.43), pya.DPoint(0, 4.16), pya.DPoint(37.8, 4.16), pya.DPoint(37.8, 2.43), pya.DPoint(0, 2.43)]))
cell_dacbuffer.shapes(L_Metal5_pin).insert(
    pya.DPolygon([pya.DPoint(0, 5.66), pya.DPoint(0, 7.39), pya.DPoint(37.8, 7.39), pya.DPoint(37.8, 5.66), pya.DPoint(0, 5.66)]))
cell_dacbuffer.shapes(L_Metal5_pin).insert(
    pya.DPolygon([pya.DPoint(0, 18.8), pya.DPoint(0, 20.53), pya.DPoint(37.8, 20.53), pya.DPoint(37.8, 18.8), pya.DPoint(0, 18.8)]))
cell_dacbuffer.shapes(L_Metal5_pin).insert(
    pya.DPolygon([pya.DPoint(0, 22.03), pya.DPoint(0, 23.76), pya.DPoint(37.8, 23.76), pya.DPoint(37.8, 22.03), pya.DPoint(0, 22.03)]))
cell_dacbuffer.shapes(L_Metal5_pin).insert(
    pya.DPolygon([pya.DPoint(0, 24.46), pya.DPoint(0, 26.19), pya.DPoint(37.8, 26.19), pya.DPoint(37.8, 24.46), pya.DPoint(0, 24.46)]))
_txt = pya.Text("VSS",
               pya.Trans(0, False, pya.Vector(18900, 865)))
_txt.halign = 1
_txt.valign = 1
cell_dacbuffer.shapes(L_Metal5_label).insert(_txt)
_txt = pya.Text("VDD",
               pya.Trans(0, False, pya.Vector(18900, 3295)))
_txt.halign = 1
_txt.valign = 1
cell_dacbuffer.shapes(L_Metal5_label).insert(_txt)
_txt = pya.Text("VDD",
               pya.Trans(0, False, pya.Vector(18900, 6525)))
_txt.halign = 1
_txt.valign = 1
cell_dacbuffer.shapes(L_Metal5_label).insert(_txt)
_txt = pya.Text("VDD",
               pya.Trans(0, False, pya.Vector(18900, 19665)))
_txt.halign = 1
_txt.valign = 1
cell_dacbuffer.shapes(L_Metal5_label).insert(_txt)
_txt = pya.Text("VDD",
               pya.Trans(0, False, pya.Vector(18900, 22895)))
_txt.halign = 1
_txt.valign = 1
cell_dacbuffer.shapes(L_Metal5_label).insert(_txt)
_txt = pya.Text("VSS",
               pya.Trans(0, False, pya.Vector(18900, 25325)))
_txt.halign = 1
_txt.valign = 1
cell_dacbuffer.shapes(L_Metal5_label).insert(_txt)
cell_dacbuffer.shapes(L_ThickGateOx).insert(
    pya.DPolygon([pya.DPoint(3.105, 0.41), pya.DPoint(3.105, 25.78), pya.DPoint(34.645, 25.78), pya.DPoint(34.645, 0.41), pya.DPoint(3.105, 0.41)]))

# === dacendbuffer ===
cell_dacendbuffer.insert(pya.DCellInstArray(
    cell_pmos_buffer_cap_1.cell_index(),
    pya.DCplxTrans(1, 180, False,
                  pya.DVector(18.325, 11.7)),
    pya.DVector(0, 0),
    pya.DVector(0, -5.44),
    1, 2))
cell_dacendbuffer.insert(pya.DCellInstArray(
    cell_pmos_buffer_cap_1.cell_index(),
    pya.DCplxTrans(1, 0, True,
                  pya.DVector(3.725, 24.65)),
    pya.DVector(0, 0),
    pya.DVector(0, -5.44),
    1, 2))
cell_dacendbuffer.insert(pya.DCellInstArray(
    cell_via_stack_9.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(17.21, 19.665))))
cell_dacendbuffer.insert(pya.DCellInstArray(
    cell_via_stack_9.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(17.21, 22.895))))
cell_dacendbuffer.insert(pya.DCellInstArray(
    cell_via_stack_9.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(17.21, 3.295))))
cell_dacendbuffer.insert(pya.DCellInstArray(
    cell_via_stack_9.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(17.21, 6.525))))
cell_dacendbuffer.insert(pya.DCellInstArray(
    cell_via_stack_9.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(4.79, 19.665))))
cell_dacendbuffer.insert(pya.DCellInstArray(
    cell_via_stack_9.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(4.79, 22.895))))
cell_dacendbuffer.insert(pya.DCellInstArray(
    cell_via_stack_9.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(4.79, 3.295))))
cell_dacendbuffer.insert(pya.DCellInstArray(
    cell_via_stack_9.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(4.79, 6.525))))
_path = pya.DPath([pya.DPoint(0, 0.25), pya.DPoint(22.05, 0.25)], 0.5)
cell_dacendbuffer.shapes(L_Metal1).insert(_path)
_path = pya.DPath([pya.DPoint(0, 13.095), pya.DPoint(22.05, 13.095)], 0.7)
cell_dacendbuffer.shapes(L_Metal1).insert(_path)
_path = pya.DPath([pya.DPoint(0, 25.94), pya.DPoint(22.05, 25.94)], 0.5)
cell_dacendbuffer.shapes(L_Metal1).insert(_path)
_path = pya.DPath([pya.DPoint(4.79, 23.76), pya.DPoint(4.79, 2.43)], 1.73)
cell_dacendbuffer.shapes(L_Metal2).insert(_path)
_path = pya.DPath([pya.DPoint(17.21, 23.76), pya.DPoint(17.21, 2.43)], 1.73)
cell_dacendbuffer.shapes(L_Metal2).insert(_path)
_path = pya.DPath([pya.DPoint(0, 0.865), pya.DPoint(22.05, 0.865)], 1.73)
cell_dacendbuffer.shapes(L_Metal5).insert(_path)
_path = pya.DPath([pya.DPoint(0, 3.295), pya.DPoint(22.05, 3.295)], 1.73)
cell_dacendbuffer.shapes(L_Metal5).insert(_path)
_path = pya.DPath([pya.DPoint(0, 6.525), pya.DPoint(22.05, 6.525)], 1.73)
cell_dacendbuffer.shapes(L_Metal5).insert(_path)
_path = pya.DPath([pya.DPoint(0, 19.665), pya.DPoint(22.05, 19.665)], 1.73)
cell_dacendbuffer.shapes(L_Metal5).insert(_path)
_path = pya.DPath([pya.DPoint(0, 22.895), pya.DPoint(22.05, 22.895)], 1.73)
cell_dacendbuffer.shapes(L_Metal5).insert(_path)
_path = pya.DPath([pya.DPoint(0, 25.325), pya.DPoint(22.05, 25.325)], 1.73)
cell_dacendbuffer.shapes(L_Metal5).insert(_path)
cell_dacendbuffer.shapes(L_NWell).insert(
    pya.DPolygon([pya.DPoint(3.105, 0.41), pya.DPoint(3.105, 25.78), pya.DPoint(18.945, 25.78), pya.DPoint(18.945, 0.41), pya.DPoint(3.105, 0.41)]))
cell_dacendbuffer.shapes(L_prBoundary).insert(
    pya.DPolygon([pya.DPoint(0, -0.07), pya.DPoint(0, 26.26), pya.DPoint(22.05, 26.26), pya.DPoint(22.05, -0.07), pya.DPoint(0, -0.07)]))
cell_dacendbuffer.shapes(L_Metal1_pin).insert(
    pya.DPolygon([pya.DPoint(0, 12.745), pya.DPoint(0, 13.445), pya.DPoint(22.05, 13.445), pya.DPoint(22.05, 12.745), pya.DPoint(0, 12.745)]))
_txt = pya.Text("Iout",
               pya.Trans(0, False, pya.Vector(11025, 13095)))
_txt.halign = 1
_txt.valign = 1
cell_dacendbuffer.shapes(L_Metal1_label).insert(_txt)
cell_dacendbuffer.shapes(L_Metal5_pin).insert(
    pya.DPolygon([pya.DPoint(0, 0), pya.DPoint(0, 1.73), pya.DPoint(22.05, 1.73), pya.DPoint(22.05, 0), pya.DPoint(0, 0)]))
cell_dacendbuffer.shapes(L_Metal5_pin).insert(
    pya.DPolygon([pya.DPoint(0, 2.43), pya.DPoint(0, 4.16), pya.DPoint(22.05, 4.16), pya.DPoint(22.05, 2.43), pya.DPoint(0, 2.43)]))
cell_dacendbuffer.shapes(L_Metal5_pin).insert(
    pya.DPolygon([pya.DPoint(0, 5.66), pya.DPoint(0, 7.39), pya.DPoint(22.05, 7.39), pya.DPoint(22.05, 5.66), pya.DPoint(0, 5.66)]))
cell_dacendbuffer.shapes(L_Metal5_pin).insert(
    pya.DPolygon([pya.DPoint(0, 18.8), pya.DPoint(0, 20.53), pya.DPoint(22.05, 20.53), pya.DPoint(22.05, 18.8), pya.DPoint(0, 18.8)]))
cell_dacendbuffer.shapes(L_Metal5_pin).insert(
    pya.DPolygon([pya.DPoint(0, 22.03), pya.DPoint(0, 23.76), pya.DPoint(22.05, 23.76), pya.DPoint(22.05, 22.03), pya.DPoint(0, 22.03)]))
cell_dacendbuffer.shapes(L_Metal5_pin).insert(
    pya.DPolygon([pya.DPoint(0, 24.46), pya.DPoint(0, 26.19), pya.DPoint(22.05, 26.19), pya.DPoint(22.05, 24.46), pya.DPoint(0, 24.46)]))
_txt = pya.Text("VSS",
               pya.Trans(0, False, pya.Vector(11025, 865)))
_txt.halign = 1
_txt.valign = 1
cell_dacendbuffer.shapes(L_Metal5_label).insert(_txt)
_txt = pya.Text("VDD",
               pya.Trans(0, False, pya.Vector(11025, 3295)))
_txt.halign = 1
_txt.valign = 1
cell_dacendbuffer.shapes(L_Metal5_label).insert(_txt)
_txt = pya.Text("VDD",
               pya.Trans(0, False, pya.Vector(11025, 6525)))
_txt.halign = 1
_txt.valign = 1
cell_dacendbuffer.shapes(L_Metal5_label).insert(_txt)
_txt = pya.Text("VDD",
               pya.Trans(0, False, pya.Vector(11025, 19665)))
_txt.halign = 1
_txt.valign = 1
cell_dacendbuffer.shapes(L_Metal5_label).insert(_txt)
_txt = pya.Text("VDD",
               pya.Trans(0, False, pya.Vector(11025, 22895)))
_txt.halign = 1
_txt.valign = 1
cell_dacendbuffer.shapes(L_Metal5_label).insert(_txt)
_txt = pya.Text("VSS",
               pya.Trans(0, False, pya.Vector(11025, 25325)))
_txt.halign = 1
_txt.valign = 1
cell_dacendbuffer.shapes(L_Metal5_label).insert(_txt)
cell_dacendbuffer.shapes(L_ThickGateOx).insert(
    pya.DPolygon([pya.DPoint(3.105, 0.41), pya.DPoint(3.105, 25.78), pya.DPoint(18.945, 25.78), pya.DPoint(18.945, 0.41), pya.DPoint(3.105, 0.41)]))

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
cell_dac128module_vss_strap.shapes(L_50_0).insert(_path)

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
cell_dac128module_vdd_strap.shapes(L_50_0).insert(_path)

# === dac2u32out4in ===
cell_dac2u32out4in.insert(pya.DCellInstArray(
    cell_dac2u16out2in.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(1.9, 4.91))))
cell_dac2u32out4in.insert(pya.DCellInstArray(
    cell_dac2u16out2in.cell_index(),
    pya.DCplxTrans(1, 180, False,
                  pya.DVector(35.9, 21.28))))
cell_dac2u32out4in.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(-0.18, 5.72), pya.DPoint(-0.18, 20.47), pya.DPoint(37.98, 20.47), pya.DPoint(37.98, 5.72), pya.DPoint(-0.18, 5.72)]))
cell_dac2u32out4in.shapes(L_NWell).insert(
    pya.DPolygon([pya.DPoint(-0.31, 2.525), pya.DPoint(-0.31, 23.665), pya.DPoint(38.11, 23.665), pya.DPoint(38.11, 2.525), pya.DPoint(-0.31, 2.525)]))
cell_dac2u32out4in.shapes(L_prBoundary).insert(
    pya.DPolygon([pya.DPoint(0, -0.07), pya.DPoint(0, 26.26), pya.DPoint(37.8, 26.26), pya.DPoint(37.8, -0.07), pya.DPoint(0, -0.07)]))
cell_dac2u32out4in.shapes(L_Metal1_pin).insert(
    pya.DPolygon([pya.DPoint(0.9, 14.95), pya.DPoint(0.9, 19.88), pya.DPoint(36.9, 19.88), pya.DPoint(36.9, 14.95), pya.DPoint(0.9, 14.95)]))
cell_dac2u32out4in.shapes(L_Metal1_pin).insert(
    pya.DPolygon([pya.DPoint(0, 12.745), pya.DPoint(0, 13.445), pya.DPoint(37.8, 13.445), pya.DPoint(37.8, 12.745), pya.DPoint(0, 12.745)]))
cell_dac2u32out4in.shapes(L_Metal1_pin).insert(
    pya.DPolygon([pya.DPoint(0.9, 6.31), pya.DPoint(0.9, 11.24), pya.DPoint(36.9, 11.24), pya.DPoint(36.9, 6.31), pya.DPoint(0.9, 6.31)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(34.075, 25.9), pya.DPoint(34.075, 26.19), pya.DPoint(34.275, 26.19), pya.DPoint(34.275, 25.9), pya.DPoint(34.075, 25.9)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(34.075, 0), pya.DPoint(34.075, 0.29), pya.DPoint(34.275, 0.29), pya.DPoint(34.275, 0), pya.DPoint(34.075, 0)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(36.075, 25.9), pya.DPoint(36.075, 26.19), pya.DPoint(36.275, 26.19), pya.DPoint(36.275, 25.9), pya.DPoint(36.075, 25.9)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(35.525, 25.9), pya.DPoint(35.525, 26.19), pya.DPoint(35.725, 26.19), pya.DPoint(35.725, 25.9), pya.DPoint(35.525, 25.9)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(2.075, 25.9), pya.DPoint(2.075, 26.19), pya.DPoint(2.275, 26.19), pya.DPoint(2.275, 25.9), pya.DPoint(2.075, 25.9)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(3.525, 25.9), pya.DPoint(3.525, 26.19), pya.DPoint(3.725, 26.19), pya.DPoint(3.725, 25.9), pya.DPoint(3.525, 25.9)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(4.075, 25.9), pya.DPoint(4.075, 26.19), pya.DPoint(4.275, 26.19), pya.DPoint(4.275, 25.9), pya.DPoint(4.075, 25.9)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(5.525, 25.9), pya.DPoint(5.525, 26.19), pya.DPoint(5.725, 26.19), pya.DPoint(5.725, 25.9), pya.DPoint(5.525, 25.9)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(6.075, 25.9), pya.DPoint(6.075, 26.19), pya.DPoint(6.275, 26.19), pya.DPoint(6.275, 25.9), pya.DPoint(6.075, 25.9)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(7.525, 25.9), pya.DPoint(7.525, 26.19), pya.DPoint(7.725, 26.19), pya.DPoint(7.725, 25.9), pya.DPoint(7.525, 25.9)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(8.075, 25.9), pya.DPoint(8.075, 26.19), pya.DPoint(8.275, 26.19), pya.DPoint(8.275, 25.9), pya.DPoint(8.075, 25.9)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(9.525, 25.9), pya.DPoint(9.525, 26.19), pya.DPoint(9.725, 26.19), pya.DPoint(9.725, 25.9), pya.DPoint(9.525, 25.9)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(10.075, 25.9), pya.DPoint(10.075, 26.19), pya.DPoint(10.275, 26.19), pya.DPoint(10.275, 25.9), pya.DPoint(10.075, 25.9)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(11.525, 25.9), pya.DPoint(11.525, 26.19), pya.DPoint(11.725, 26.19), pya.DPoint(11.725, 25.9), pya.DPoint(11.525, 25.9)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(12.075, 25.9), pya.DPoint(12.075, 26.19), pya.DPoint(12.275, 26.19), pya.DPoint(12.275, 25.9), pya.DPoint(12.075, 25.9)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(13.525, 25.9), pya.DPoint(13.525, 26.19), pya.DPoint(13.725, 26.19), pya.DPoint(13.725, 25.9), pya.DPoint(13.525, 25.9)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(14.075, 25.9), pya.DPoint(14.075, 26.19), pya.DPoint(14.275, 26.19), pya.DPoint(14.275, 25.9), pya.DPoint(14.075, 25.9)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(15.525, 25.9), pya.DPoint(15.525, 26.19), pya.DPoint(15.725, 26.19), pya.DPoint(15.725, 25.9), pya.DPoint(15.525, 25.9)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(16.075, 25.9), pya.DPoint(16.075, 26.19), pya.DPoint(16.275, 26.19), pya.DPoint(16.275, 25.9), pya.DPoint(16.075, 25.9)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(17.525, 25.9), pya.DPoint(17.525, 26.19), pya.DPoint(17.725, 26.19), pya.DPoint(17.725, 25.9), pya.DPoint(17.525, 25.9)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(18.075, 25.9), pya.DPoint(18.075, 26.19), pya.DPoint(18.275, 26.19), pya.DPoint(18.275, 25.9), pya.DPoint(18.075, 25.9)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(19.525, 25.9), pya.DPoint(19.525, 26.19), pya.DPoint(19.725, 26.19), pya.DPoint(19.725, 25.9), pya.DPoint(19.525, 25.9)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(20.075, 25.9), pya.DPoint(20.075, 26.19), pya.DPoint(20.275, 26.19), pya.DPoint(20.275, 25.9), pya.DPoint(20.075, 25.9)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(21.525, 25.9), pya.DPoint(21.525, 26.19), pya.DPoint(21.725, 26.19), pya.DPoint(21.725, 25.9), pya.DPoint(21.525, 25.9)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(22.075, 25.9), pya.DPoint(22.075, 26.19), pya.DPoint(22.275, 26.19), pya.DPoint(22.275, 25.9), pya.DPoint(22.075, 25.9)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(23.525, 25.9), pya.DPoint(23.525, 26.19), pya.DPoint(23.725, 26.19), pya.DPoint(23.725, 25.9), pya.DPoint(23.525, 25.9)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(24.075, 25.9), pya.DPoint(24.075, 26.19), pya.DPoint(24.275, 26.19), pya.DPoint(24.275, 25.9), pya.DPoint(24.075, 25.9)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(25.525, 25.9), pya.DPoint(25.525, 26.19), pya.DPoint(25.725, 26.19), pya.DPoint(25.725, 25.9), pya.DPoint(25.525, 25.9)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(26.075, 25.9), pya.DPoint(26.075, 26.19), pya.DPoint(26.275, 26.19), pya.DPoint(26.275, 25.9), pya.DPoint(26.075, 25.9)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(27.525, 25.9), pya.DPoint(27.525, 26.19), pya.DPoint(27.725, 26.19), pya.DPoint(27.725, 25.9), pya.DPoint(27.525, 25.9)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(28.075, 25.9), pya.DPoint(28.075, 26.19), pya.DPoint(28.275, 26.19), pya.DPoint(28.275, 25.9), pya.DPoint(28.075, 25.9)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(29.525, 25.9), pya.DPoint(29.525, 26.19), pya.DPoint(29.725, 26.19), pya.DPoint(29.725, 25.9), pya.DPoint(29.525, 25.9)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(30.075, 25.9), pya.DPoint(30.075, 26.19), pya.DPoint(30.275, 26.19), pya.DPoint(30.275, 25.9), pya.DPoint(30.075, 25.9)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(31.525, 25.9), pya.DPoint(31.525, 26.19), pya.DPoint(31.725, 26.19), pya.DPoint(31.725, 25.9), pya.DPoint(31.525, 25.9)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(32.075, 25.9), pya.DPoint(32.075, 26.19), pya.DPoint(32.275, 26.19), pya.DPoint(32.275, 25.9), pya.DPoint(32.075, 25.9)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(33.525, 25.9), pya.DPoint(33.525, 26.19), pya.DPoint(33.725, 26.19), pya.DPoint(33.725, 25.9), pya.DPoint(33.525, 25.9)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(1.525, 25.9), pya.DPoint(1.525, 26.19), pya.DPoint(1.725, 26.19), pya.DPoint(1.725, 25.9), pya.DPoint(1.525, 25.9)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(8.075, 0), pya.DPoint(8.075, 0.29), pya.DPoint(8.275, 0.29), pya.DPoint(8.275, 0), pya.DPoint(8.075, 0)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(4.075, 0), pya.DPoint(4.075, 0.29), pya.DPoint(4.275, 0.29), pya.DPoint(4.275, 0), pya.DPoint(4.075, 0)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(3.525, 0), pya.DPoint(3.525, 0.29), pya.DPoint(3.725, 0.29), pya.DPoint(3.725, 0), pya.DPoint(3.525, 0)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(7.525, 0), pya.DPoint(7.525, 0.29), pya.DPoint(7.725, 0.29), pya.DPoint(7.725, 0), pya.DPoint(7.525, 0)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(6.075, 0), pya.DPoint(6.075, 0.29), pya.DPoint(6.275, 0.29), pya.DPoint(6.275, 0), pya.DPoint(6.075, 0)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(2.075, 0), pya.DPoint(2.075, 0.29), pya.DPoint(2.275, 0.29), pya.DPoint(2.275, 0), pya.DPoint(2.075, 0)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(1.525, 0), pya.DPoint(1.525, 0.29), pya.DPoint(1.725, 0.29), pya.DPoint(1.725, 0), pya.DPoint(1.525, 0)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(5.525, 0), pya.DPoint(5.525, 0.29), pya.DPoint(5.725, 0.29), pya.DPoint(5.725, 0), pya.DPoint(5.525, 0)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(33.525, 0), pya.DPoint(33.525, 0.29), pya.DPoint(33.725, 0.29), pya.DPoint(33.725, 0), pya.DPoint(33.525, 0)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(32.075, 0), pya.DPoint(32.075, 0.29), pya.DPoint(32.275, 0.29), pya.DPoint(32.275, 0), pya.DPoint(32.075, 0)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(31.525, 0), pya.DPoint(31.525, 0.29), pya.DPoint(31.725, 0.29), pya.DPoint(31.725, 0), pya.DPoint(31.525, 0)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(30.075, 0), pya.DPoint(30.075, 0.29), pya.DPoint(30.275, 0.29), pya.DPoint(30.275, 0), pya.DPoint(30.075, 0)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(29.525, 0), pya.DPoint(29.525, 0.29), pya.DPoint(29.725, 0.29), pya.DPoint(29.725, 0), pya.DPoint(29.525, 0)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(28.075, 0), pya.DPoint(28.075, 0.29), pya.DPoint(28.275, 0.29), pya.DPoint(28.275, 0), pya.DPoint(28.075, 0)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(27.525, 0), pya.DPoint(27.525, 0.29), pya.DPoint(27.725, 0.29), pya.DPoint(27.725, 0), pya.DPoint(27.525, 0)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(26.075, 0), pya.DPoint(26.075, 0.29), pya.DPoint(26.275, 0.29), pya.DPoint(26.275, 0), pya.DPoint(26.075, 0)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(25.525, 0), pya.DPoint(25.525, 0.29), pya.DPoint(25.725, 0.29), pya.DPoint(25.725, 0), pya.DPoint(25.525, 0)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(24.075, 0), pya.DPoint(24.075, 0.29), pya.DPoint(24.275, 0.29), pya.DPoint(24.275, 0), pya.DPoint(24.075, 0)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(23.525, 0), pya.DPoint(23.525, 0.29), pya.DPoint(23.725, 0.29), pya.DPoint(23.725, 0), pya.DPoint(23.525, 0)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(22.075, 0), pya.DPoint(22.075, 0.29), pya.DPoint(22.275, 0.29), pya.DPoint(22.275, 0), pya.DPoint(22.075, 0)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(21.525, 0), pya.DPoint(21.525, 0.29), pya.DPoint(21.725, 0.29), pya.DPoint(21.725, 0), pya.DPoint(21.525, 0)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(20.075, 0), pya.DPoint(20.075, 0.29), pya.DPoint(20.275, 0.29), pya.DPoint(20.275, 0), pya.DPoint(20.075, 0)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(19.525, 0), pya.DPoint(19.525, 0.29), pya.DPoint(19.725, 0.29), pya.DPoint(19.725, 0), pya.DPoint(19.525, 0)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(18.075, 0), pya.DPoint(18.075, 0.29), pya.DPoint(18.275, 0.29), pya.DPoint(18.275, 0), pya.DPoint(18.075, 0)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(17.525, 0), pya.DPoint(17.525, 0.29), pya.DPoint(17.725, 0.29), pya.DPoint(17.725, 0), pya.DPoint(17.525, 0)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(16.075, 0), pya.DPoint(16.075, 0.29), pya.DPoint(16.275, 0.29), pya.DPoint(16.275, 0), pya.DPoint(16.075, 0)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(15.525, 0), pya.DPoint(15.525, 0.29), pya.DPoint(15.725, 0.29), pya.DPoint(15.725, 0), pya.DPoint(15.525, 0)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(14.075, 0), pya.DPoint(14.075, 0.29), pya.DPoint(14.275, 0.29), pya.DPoint(14.275, 0), pya.DPoint(14.075, 0)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(13.525, 0), pya.DPoint(13.525, 0.29), pya.DPoint(13.725, 0.29), pya.DPoint(13.725, 0), pya.DPoint(13.525, 0)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(12.075, 0), pya.DPoint(12.075, 0.29), pya.DPoint(12.275, 0.29), pya.DPoint(12.275, 0), pya.DPoint(12.075, 0)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(11.525, 0), pya.DPoint(11.525, 0.29), pya.DPoint(11.725, 0.29), pya.DPoint(11.725, 0), pya.DPoint(11.525, 0)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(10.075, 0), pya.DPoint(10.075, 0.29), pya.DPoint(10.275, 0.29), pya.DPoint(10.275, 0), pya.DPoint(10.075, 0)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(9.525, 0), pya.DPoint(9.525, 0.29), pya.DPoint(9.725, 0.29), pya.DPoint(9.725, 0), pya.DPoint(9.525, 0)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(36.075, 0), pya.DPoint(36.075, 0.29), pya.DPoint(36.275, 0.29), pya.DPoint(36.275, 0), pya.DPoint(36.075, 0)]))
cell_dac2u32out4in.shapes(L_Metal2_pin).insert(
    pya.DPolygon([pya.DPoint(35.525, 0), pya.DPoint(35.525, 0.29), pya.DPoint(35.725, 0.29), pya.DPoint(35.725, 0), pya.DPoint(35.525, 0)]))
_txt = pya.Text("VbiasP[1]",
               pya.Trans(2, False, pya.Vector(18900, 17415)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal1_label).insert(_txt)
_txt = pya.Text("Iout",
               pya.Trans(2, False, pya.Vector(18900, 13095)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal1_label).insert(_txt)
_txt = pya.Text("VbiasP[0]",
               pya.Trans(0, False, pya.Vector(18900, 8775)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal1_label).insert(_txt)
_txt = pya.Text("EN[1]",
               pya.Trans(0, False, pya.Vector(35625, 145)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ENB[1]",
               pya.Trans(0, False, pya.Vector(36175, 145)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("EN[2]",
               pya.Trans(0, False, pya.Vector(36175, 26045)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ENB[2]",
               pya.Trans(0, False, pya.Vector(35625, 26045)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[16]",
               pya.Trans(0, False, pya.Vector(34175, 26045)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[16]",
               pya.Trans(0, False, pya.Vector(33625, 26045)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[17]",
               pya.Trans(0, False, pya.Vector(32175, 26045)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[17]",
               pya.Trans(0, False, pya.Vector(31625, 26045)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[18]",
               pya.Trans(0, False, pya.Vector(30175, 26045)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[18]",
               pya.Trans(0, False, pya.Vector(29625, 26045)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[19]",
               pya.Trans(0, False, pya.Vector(28175, 26045)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[19]",
               pya.Trans(0, False, pya.Vector(27625, 26045)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[20]",
               pya.Trans(0, False, pya.Vector(26175, 26045)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[20]",
               pya.Trans(0, False, pya.Vector(25625, 26045)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[21]",
               pya.Trans(0, False, pya.Vector(24175, 26045)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[21]",
               pya.Trans(0, False, pya.Vector(23625, 26045)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[22]",
               pya.Trans(0, False, pya.Vector(22175, 26045)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[22]",
               pya.Trans(0, False, pya.Vector(21625, 26045)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[23]",
               pya.Trans(0, False, pya.Vector(20175, 26045)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[23]",
               pya.Trans(0, False, pya.Vector(19625, 26045)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[24]",
               pya.Trans(0, False, pya.Vector(18175, 26045)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[24]",
               pya.Trans(0, False, pya.Vector(17625, 26045)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[25]",
               pya.Trans(0, False, pya.Vector(16175, 26045)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[25]",
               pya.Trans(0, False, pya.Vector(15625, 26045)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[26]",
               pya.Trans(0, False, pya.Vector(14175, 26045)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[26]",
               pya.Trans(0, False, pya.Vector(13625, 26045)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[27]",
               pya.Trans(0, False, pya.Vector(12175, 26045)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[27]",
               pya.Trans(0, False, pya.Vector(11625, 26045)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[28]",
               pya.Trans(0, False, pya.Vector(10175, 26045)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[28]",
               pya.Trans(0, False, pya.Vector(9625, 26045)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[29]",
               pya.Trans(0, False, pya.Vector(8175, 26045)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[29]",
               pya.Trans(0, False, pya.Vector(7625, 26045)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[30]",
               pya.Trans(0, False, pya.Vector(6175, 26045)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[30]",
               pya.Trans(0, False, pya.Vector(5625, 26045)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[31]",
               pya.Trans(0, False, pya.Vector(4175, 26045)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[31]",
               pya.Trans(0, False, pya.Vector(3625, 26045)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("EN[3]",
               pya.Trans(0, False, pya.Vector(2175, 26045)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ENB[3]",
               pya.Trans(0, False, pya.Vector(1625, 26045)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[0]",
               pya.Trans(0, False, pya.Vector(3625, 145)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[0]",
               pya.Trans(0, False, pya.Vector(4175, 145)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[1]",
               pya.Trans(0, False, pya.Vector(5625, 145)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[1]",
               pya.Trans(0, False, pya.Vector(6175, 145)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[2]",
               pya.Trans(0, False, pya.Vector(7625, 145)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[2]",
               pya.Trans(0, False, pya.Vector(8175, 145)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[3]",
               pya.Trans(0, False, pya.Vector(9625, 145)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[3]",
               pya.Trans(0, False, pya.Vector(10175, 145)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[4]",
               pya.Trans(0, False, pya.Vector(11625, 145)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[4]",
               pya.Trans(0, False, pya.Vector(12175, 145)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[5]",
               pya.Trans(0, False, pya.Vector(13625, 145)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[5]",
               pya.Trans(0, False, pya.Vector(14175, 145)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[6]",
               pya.Trans(0, False, pya.Vector(15625, 145)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("EN[0]",
               pya.Trans(0, False, pya.Vector(1625, 145)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ENB[0]",
               pya.Trans(0, False, pya.Vector(2175, 145)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[6]",
               pya.Trans(0, False, pya.Vector(16175, 145)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[7]",
               pya.Trans(0, False, pya.Vector(17625, 145)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[7]",
               pya.Trans(0, False, pya.Vector(18175, 145)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[8]",
               pya.Trans(0, False, pya.Vector(19625, 145)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[8]",
               pya.Trans(0, False, pya.Vector(20175, 145)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[9]",
               pya.Trans(0, False, pya.Vector(21625, 145)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[9]",
               pya.Trans(0, False, pya.Vector(22175, 145)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[10]",
               pya.Trans(0, False, pya.Vector(23625, 145)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[10]",
               pya.Trans(0, False, pya.Vector(24175, 145)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[11]",
               pya.Trans(0, False, pya.Vector(25625, 145)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[11]",
               pya.Trans(0, False, pya.Vector(26175, 145)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[12]",
               pya.Trans(0, False, pya.Vector(27625, 145)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[12]",
               pya.Trans(0, False, pya.Vector(28175, 145)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[13]",
               pya.Trans(0, False, pya.Vector(29625, 145)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[13]",
               pya.Trans(0, False, pya.Vector(30175, 145)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[14]",
               pya.Trans(0, False, pya.Vector(31625, 145)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[14]",
               pya.Trans(0, False, pya.Vector(32175, 145)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ON[15]",
               pya.Trans(0, False, pya.Vector(33625, 145)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
_txt = pya.Text("ONB[15]",
               pya.Trans(0, False, pya.Vector(34175, 145)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal2_label).insert(_txt)
cell_dac2u32out4in.shapes(L_Metal5_pin).insert(
    pya.DPolygon([pya.DPoint(0, 20.93), pya.DPoint(0, 21.63), pya.DPoint(37.8, 21.63), pya.DPoint(37.8, 20.93), pya.DPoint(0, 20.93)]))
cell_dac2u32out4in.shapes(L_Metal5_pin).insert(
    pya.DPolygon([pya.DPoint(0, 4.56), pya.DPoint(0, 5.26), pya.DPoint(37.8, 5.26), pya.DPoint(37.8, 4.56), pya.DPoint(0, 4.56)]))
cell_dac2u32out4in.shapes(L_Metal5_pin).insert(
    pya.DPolygon([pya.DPoint(0, 22.03), pya.DPoint(0, 23.76), pya.DPoint(37.8, 23.76), pya.DPoint(37.8, 22.03), pya.DPoint(0, 22.03)]))
cell_dac2u32out4in.shapes(L_Metal5_pin).insert(
    pya.DPolygon([pya.DPoint(0, 5.66), pya.DPoint(0, 7.39), pya.DPoint(37.8, 7.39), pya.DPoint(37.8, 5.66), pya.DPoint(0, 5.66)]))
cell_dac2u32out4in.shapes(L_Metal5_pin).insert(
    pya.DPolygon([pya.DPoint(0, 2.43), pya.DPoint(0, 4.16), pya.DPoint(37.8, 4.16), pya.DPoint(37.8, 2.43), pya.DPoint(0, 2.43)]))
cell_dac2u32out4in.shapes(L_Metal5_pin).insert(
    pya.DPolygon([pya.DPoint(0, 18.8), pya.DPoint(0, 20.53), pya.DPoint(37.8, 20.53), pya.DPoint(37.8, 18.8), pya.DPoint(0, 18.8)]))
cell_dac2u32out4in.shapes(L_Metal5_pin).insert(
    pya.DPolygon([pya.DPoint(0, 0), pya.DPoint(0, 1.73), pya.DPoint(37.8, 1.73), pya.DPoint(37.8, 0), pya.DPoint(0, 0)]))
cell_dac2u32out4in.shapes(L_Metal5_pin).insert(
    pya.DPolygon([pya.DPoint(0, 24.46), pya.DPoint(0, 26.19), pya.DPoint(37.8, 26.19), pya.DPoint(37.8, 24.46), pya.DPoint(0, 24.46)]))
_txt = pya.Text("VcascP[0]",
               pya.Trans(0, False, pya.Vector(18900, 4910)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal5_label).insert(_txt)
_txt = pya.Text("VSS",
               pya.Trans(0, False, pya.Vector(18900, 865)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal5_label).insert(_txt)
_txt = pya.Text("VSS",
               pya.Trans(2, False, pya.Vector(18900, 25325)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal5_label).insert(_txt)
_txt = pya.Text("VDD",
               pya.Trans(0, False, pya.Vector(18900, 3295)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal5_label).insert(_txt)
_txt = pya.Text("VDD",
               pya.Trans(0, False, pya.Vector(18900, 6525)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal5_label).insert(_txt)
_txt = pya.Text("VDD",
               pya.Trans(2, False, pya.Vector(18900, 22895)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal5_label).insert(_txt)
_txt = pya.Text("VDD",
               pya.Trans(2, False, pya.Vector(18900, 19665)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal5_label).insert(_txt)
_txt = pya.Text("VcascP[1]",
               pya.Trans(2, False, pya.Vector(18900, 21280)))
_txt.halign = 1
_txt.valign = 1
cell_dac2u32out4in.shapes(L_Metal5_label).insert(_txt)

# === buffercapwires ===
cell_buffercapwires.insert(pya.DCellInstArray(
    cell_via_stack_11.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(4.26, 0.35))))
cell_buffercapwires.insert(pya.DCellInstArray(
    cell_via_stack_11.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(4.26, 16.72))))
cell_buffercapwires.insert(pya.DCellInstArray(
    cell_via_stack_10.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(4.055, 3.375))))
cell_buffercapwires.insert(pya.DCellInstArray(
    cell_via_stack_10.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(-0.58, 3.375))))
cell_buffercapwires.insert(pya.DCellInstArray(
    cell_via_stack_10.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(4.055, 13.695))))
cell_buffercapwires.insert(pya.DCellInstArray(
    cell_via_stack_10.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(-0.58, 13.695))))
_path = pya.DPath([pya.DPoint(0, 0.35), pya.DPoint(4.405, 0.35)], 0.7)
cell_buffercapwires.shapes(L_Metal5).insert(_path)
_path = pya.DPath([pya.DPoint(0, 16.72), pya.DPoint(4.405, 16.72)], 0.7)
cell_buffercapwires.shapes(L_Metal5).insert(_path)
_path = pya.DPath([pya.DPoint(4.405, 3.375), pya.DPoint(-0.93, 3.375), pya.DPoint(-0.93, 3.375)], 0.29)
cell_buffercapwires.shapes(L_Metal5).insert(_path)
_path = pya.DPath([pya.DPoint(4.405, 13.695), pya.DPoint(-0.93, 13.695), pya.DPoint(-0.93, 13.695)], 0.29)
cell_buffercapwires.shapes(L_Metal5).insert(_path)

# === dac4x32module ===
cell_dac4x32module.insert(pya.DCellInstArray(
    cell_dac2u32out4in.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(22.05, 0)),
    pya.DVector(75.6, 0),
    pya.DVector(0, 0),
    4, 1))
cell_dac4x32module.insert(pya.DCellInstArray(
    cell_dac128module_vss_strap.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(22.05, 0)),
    pya.DVector(31.35, 0),
    pya.DVector(0, 0),
    9, 1))
cell_dac4x32module.insert(pya.DCellInstArray(
    cell_dac128module_vdd_strap.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(32.2, 0)),
    pya.DVector(31.35, 0),
    pya.DVector(0, 0),
    9, 1))
cell_dac4x32module.insert(pya.DCellInstArray(
    cell_via_stack_7.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(308.35, 13.095))))
cell_dac4x32module.insert(pya.DCellInstArray(
    cell_dacbuffer.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(59.85, 0)),
    pya.DVector(75.6, 0),
    pya.DVector(0, 0),
    3, 1))
cell_dac4x32module.insert(pya.DCellInstArray(
    cell_dacendbuffer.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(0, 0)),
    pya.DVector(286.65, 0),
    pya.DVector(0, 0),
    2, 1))
cell_dac4x32module.insert(pya.DCellInstArray(
    cell_buffercapwires.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(58.95, 4.56)),
    pya.DVector(75.6, 0),
    pya.DVector(0, 0),
    4, 1))
cell_dac4x32module.insert(pya.DCellInstArray(
    cell_buffercapwires.cell_index(),
    pya.DCplxTrans(1, 180, True,
                  pya.DVector(249.76, 4.56)),
    pya.DVector(-75.6, 0),
    pya.DVector(0, 0),
    4, 1))
cell_dac4x32module.insert(pya.DCellInstArray(
    cell_inputwires.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(63.065, 4.56))))
cell_dac4x32module.shapes(L_prBoundary).insert(
    pya.DPolygon([pya.DPoint(0, -0.07), pya.DPoint(0, 26.26), pya.DPoint(308.7, 26.26), pya.DPoint(308.7, -0.07), pya.DPoint(0, -0.07)]))
cell_dac4x32module.shapes(L_Metal5_pin).insert(
    pya.DPolygon([pya.DPoint(308, 12.745), pya.DPoint(308, 13.445), pya.DPoint(308.7, 13.445), pya.DPoint(308.7, 12.745), pya.DPoint(308, 12.745)]))
cell_dac4x32module.shapes(L_Metal5_pin).insert(
    pya.DPolygon([pya.DPoint(308, 4.56), pya.DPoint(308, 5.26), pya.DPoint(308.7, 5.26), pya.DPoint(308.7, 4.56), pya.DPoint(308, 4.56)]))
cell_dac4x32module.shapes(L_Metal5_pin).insert(
    pya.DPolygon([pya.DPoint(308, 8.48), pya.DPoint(308, 9.18), pya.DPoint(308.7, 9.18), pya.DPoint(308.7, 8.48), pya.DPoint(308, 8.48)]))
cell_dac4x32module.shapes(L_Metal5_pin).insert(
    pya.DPolygon([pya.DPoint(308, 9.58), pya.DPoint(308, 10.28), pya.DPoint(308.7, 10.28), pya.DPoint(308.7, 9.58), pya.DPoint(308, 9.58)]))
cell_dac4x32module.shapes(L_Metal5_pin).insert(
    pya.DPolygon([pya.DPoint(308, 10.68), pya.DPoint(308, 11.38), pya.DPoint(308.7, 11.38), pya.DPoint(308.7, 10.68), pya.DPoint(308, 10.68)]))
cell_dac4x32module.shapes(L_Metal5_pin).insert(
    pya.DPolygon([pya.DPoint(308, 14.805), pya.DPoint(308, 15.505), pya.DPoint(308.7, 15.505), pya.DPoint(308.7, 14.805), pya.DPoint(308, 14.805)]))
cell_dac4x32module.shapes(L_Metal5_pin).insert(
    pya.DPolygon([pya.DPoint(308, 15.905), pya.DPoint(308, 16.605), pya.DPoint(308.7, 16.605), pya.DPoint(308.7, 15.905), pya.DPoint(308, 15.905)]))
cell_dac4x32module.shapes(L_Metal5_pin).insert(
    pya.DPolygon([pya.DPoint(308, 17.005), pya.DPoint(308, 17.705), pya.DPoint(308.7, 17.705), pya.DPoint(308.7, 17.005), pya.DPoint(308, 17.005)]))
cell_dac4x32module.shapes(L_Metal5_pin).insert(
    pya.DPolygon([pya.DPoint(308, 20.93), pya.DPoint(308, 21.63), pya.DPoint(308.7, 21.63), pya.DPoint(308.7, 20.93), pya.DPoint(308, 20.93)]))
_txt = pya.Text("Iout",
               pya.Trans(0, False, pya.Vector(308350, 13095)))
_txt.halign = 1
_txt.valign = 1
cell_dac4x32module.shapes(L_Metal5_label).insert(_txt)
_txt = pya.Text("VbiasP[3]",
               pya.Trans(0, False, pya.Vector(308350, 4910)))
_txt.halign = 1
_txt.valign = 1
cell_dac4x32module.shapes(L_Metal5_label).insert(_txt)
_txt = pya.Text("VbiasP[2]",
               pya.Trans(0, False, pya.Vector(308350, 8830)))
_txt.halign = 1
_txt.valign = 1
cell_dac4x32module.shapes(L_Metal5_label).insert(_txt)
_txt = pya.Text("VbiasP[1]",
               pya.Trans(0, False, pya.Vector(308350, 9930)))
_txt.halign = 1
_txt.valign = 1
cell_dac4x32module.shapes(L_Metal5_label).insert(_txt)
_txt = pya.Text("VbiasP[0]",
               pya.Trans(0, False, pya.Vector(308350, 11030)))
_txt.halign = 1
_txt.valign = 1
cell_dac4x32module.shapes(L_Metal5_label).insert(_txt)
_txt = pya.Text("VbiasP[7]",
               pya.Trans(0, False, pya.Vector(308350, 15155)))
_txt.halign = 1
_txt.valign = 1
cell_dac4x32module.shapes(L_Metal5_label).insert(_txt)
_txt = pya.Text("VbiasP[6]",
               pya.Trans(0, False, pya.Vector(308350, 16255)))
_txt.halign = 1
_txt.valign = 1
cell_dac4x32module.shapes(L_Metal5_label).insert(_txt)
_txt = pya.Text("VbiasP[5]",
               pya.Trans(0, False, pya.Vector(308350, 17355)))
_txt.halign = 1
_txt.valign = 1
cell_dac4x32module.shapes(L_Metal5_label).insert(_txt)
_txt = pya.Text("VbiasP[4]",
               pya.Trans(0, False, pya.Vector(308350, 21280)))
_txt.halign = 1
_txt.valign = 1
cell_dac4x32module.shapes(L_Metal5_label).insert(_txt)
cell_dac4x32module.shapes(L_Via2).insert(
    pya.DPolygon([pya.DPoint(0, 14.38), pya.DPoint(0, 26.19), pya.DPoint(308.7, 26.19), pya.DPoint(308.7, 14.38), pya.DPoint(0, 14.38)]))
cell_dac4x32module.shapes(L_Via2).insert(
    pya.DPolygon([pya.DPoint(0, 0), pya.DPoint(0, 11.81), pya.DPoint(308.7, 11.81), pya.DPoint(308.7, 0), pya.DPoint(0, 0)]))
cell_dac4x32module.shapes(L_67_2).insert(
    pya.DPolygon([pya.DPoint(0, 0), pya.DPoint(0, 11.81), pya.DPoint(308.7, 11.81), pya.DPoint(308.7, 0), pya.DPoint(0, 0)]))
cell_dac4x32module.shapes(L_67_2).insert(
    pya.DPolygon([pya.DPoint(0, 14.38), pya.DPoint(0, 26.19), pya.DPoint(308.7, 26.19), pya.DPoint(308.7, 14.38), pya.DPoint(0, 14.38)]))
_txt = pya.Text("VDD",
               pya.Trans(0, False, pya.Vector(154350, 5905)))
_txt.halign = 1
_txt.valign = 1
cell_dac4x32module.shapes(L_67_25).insert(_txt)
_txt = pya.Text("VSS",
               pya.Trans(0, False, pya.Vector(154350, 20285)))
_txt.halign = 1
_txt.valign = 1
cell_dac4x32module.shapes(L_67_25).insert(_txt)

# Save
layout.write("output.gds")
