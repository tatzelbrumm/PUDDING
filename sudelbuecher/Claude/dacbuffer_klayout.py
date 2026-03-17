import pya

layout = pya.Layout()

layout.dbu = 0.001

# --- layer index variables ---
L_Activ = layout.layer(pya.LayerInfo(1, 0, "Activ"))
L_NWell = layout.layer(pya.LayerInfo(5, 0, "NWell"))
L_NWell_pin = layout.layer(pya.LayerInfo(5, 2, "NWell_pin"))
L_pSD = layout.layer(pya.LayerInfo(6, 0, "pSD"))
L_GatPoly = layout.layer(pya.LayerInfo(8, 0, "GatPoly"))
L_GatPoly_pin = layout.layer(pya.LayerInfo(8, 2, "GatPoly_pin"))
L_GatPoly_label = layout.layer(pya.LayerInfo(8, 25, "GatPoly_label"))
L_Metal2 = layout.layer(pya.LayerInfo(14, 0, "Metal2"))
L_Metal5 = layout.layer(pya.LayerInfo(30, 0, "Metal5"))
L_Metal5_pin = layout.layer(pya.LayerInfo(30, 2, "Metal5_pin"))
L_Metal5_label = layout.layer(pya.LayerInfo(30, 25, "Metal5_label"))
L_TopMetal1 = layout.layer(pya.LayerInfo(31, 0, "TopMetal1"))
L_DNWell = layout.layer(pya.LayerInfo(40, 0, "DNWell"))
L_hvdifftap = layout.layer(pya.LayerInfo(44, 0, "hvdifftap"))
L_FILL = layout.layer(pya.LayerInfo(51, 0, "FILL"))
L_Via1 = layout.layer(pya.LayerInfo(63, 0, "Via1"))
L_prBoundary = layout.layer(pya.LayerInfo(189, 4, "prBoundary"))

# --- cell declarations ---
cell_FEOL_contacts_1 = layout.create_cell("FEOL$contacts$1")
cell_pmosHV_2 = layout.create_cell("pmosHV$2")
cell_pmos_buffer_cap = layout.create_cell("pmos_buffer_cap")
cell_dacbuffer = layout.create_cell("dacbuffer")

# === FEOL$contacts$1 ===
cell_FEOL_contacts_1.shapes(L_GatPoly).insert(
    pya.DPolygon([pya.DPoint(0, 0), pya.DPoint(0, 0.16), pya.DPoint(8, 0.16), pya.DPoint(8, 0), pya.DPoint(0, 0)]))
cell_FEOL_contacts_1.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(0.18, 0), pya.DPoint(0.18, 0.16), pya.DPoint(0.34, 0.16), pya.DPoint(0.34, 0), pya.DPoint(0.18, 0)]))
cell_FEOL_contacts_1.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(0.52, 0), pya.DPoint(0.52, 0.16), pya.DPoint(0.68, 0.16), pya.DPoint(0.68, 0), pya.DPoint(0.52, 0)]))
cell_FEOL_contacts_1.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(0.86, 0), pya.DPoint(0.86, 0.16), pya.DPoint(1.02, 0.16), pya.DPoint(1.02, 0), pya.DPoint(0.86, 0)]))
cell_FEOL_contacts_1.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(1.2, 0), pya.DPoint(1.2, 0.16), pya.DPoint(1.36, 0.16), pya.DPoint(1.36, 0), pya.DPoint(1.2, 0)]))
cell_FEOL_contacts_1.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(1.54, 0), pya.DPoint(1.54, 0.16), pya.DPoint(1.7, 0.16), pya.DPoint(1.7, 0), pya.DPoint(1.54, 0)]))
cell_FEOL_contacts_1.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(1.88, 0), pya.DPoint(1.88, 0.16), pya.DPoint(2.04, 0.16), pya.DPoint(2.04, 0), pya.DPoint(1.88, 0)]))
cell_FEOL_contacts_1.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(2.22, 0), pya.DPoint(2.22, 0.16), pya.DPoint(2.38, 0.16), pya.DPoint(2.38, 0), pya.DPoint(2.22, 0)]))
cell_FEOL_contacts_1.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(2.56, 0), pya.DPoint(2.56, 0.16), pya.DPoint(2.72, 0.16), pya.DPoint(2.72, 0), pya.DPoint(2.56, 0)]))
cell_FEOL_contacts_1.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(2.9, 0), pya.DPoint(2.9, 0.16), pya.DPoint(3.06, 0.16), pya.DPoint(3.06, 0), pya.DPoint(2.9, 0)]))
cell_FEOL_contacts_1.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(3.24, 0), pya.DPoint(3.24, 0.16), pya.DPoint(3.4, 0.16), pya.DPoint(3.4, 0), pya.DPoint(3.24, 0)]))
cell_FEOL_contacts_1.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(3.58, 0), pya.DPoint(3.58, 0.16), pya.DPoint(3.74, 0.16), pya.DPoint(3.74, 0), pya.DPoint(3.58, 0)]))
cell_FEOL_contacts_1.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(3.92, 0), pya.DPoint(3.92, 0.16), pya.DPoint(4.08, 0.16), pya.DPoint(4.08, 0), pya.DPoint(3.92, 0)]))
cell_FEOL_contacts_1.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(4.26, 0), pya.DPoint(4.26, 0.16), pya.DPoint(4.42, 0.16), pya.DPoint(4.42, 0), pya.DPoint(4.26, 0)]))
cell_FEOL_contacts_1.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(4.6, 0), pya.DPoint(4.6, 0.16), pya.DPoint(4.76, 0.16), pya.DPoint(4.76, 0), pya.DPoint(4.6, 0)]))
cell_FEOL_contacts_1.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(4.94, 0), pya.DPoint(4.94, 0.16), pya.DPoint(5.1, 0.16), pya.DPoint(5.1, 0), pya.DPoint(4.94, 0)]))
cell_FEOL_contacts_1.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(5.28, 0), pya.DPoint(5.28, 0.16), pya.DPoint(5.44, 0.16), pya.DPoint(5.44, 0), pya.DPoint(5.28, 0)]))
cell_FEOL_contacts_1.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(5.62, 0), pya.DPoint(5.62, 0.16), pya.DPoint(5.78, 0.16), pya.DPoint(5.78, 0), pya.DPoint(5.62, 0)]))
cell_FEOL_contacts_1.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(5.96, 0), pya.DPoint(5.96, 0.16), pya.DPoint(6.12, 0.16), pya.DPoint(6.12, 0), pya.DPoint(5.96, 0)]))
cell_FEOL_contacts_1.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(6.3, 0), pya.DPoint(6.3, 0.16), pya.DPoint(6.46, 0.16), pya.DPoint(6.46, 0), pya.DPoint(6.3, 0)]))
cell_FEOL_contacts_1.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(6.64, 0), pya.DPoint(6.64, 0.16), pya.DPoint(6.8, 0.16), pya.DPoint(6.8, 0), pya.DPoint(6.64, 0)]))
cell_FEOL_contacts_1.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(6.98, 0), pya.DPoint(6.98, 0.16), pya.DPoint(7.14, 0.16), pya.DPoint(7.14, 0), pya.DPoint(6.98, 0)]))
cell_FEOL_contacts_1.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(7.32, 0), pya.DPoint(7.32, 0.16), pya.DPoint(7.48, 0.16), pya.DPoint(7.48, 0), pya.DPoint(7.32, 0)]))
cell_FEOL_contacts_1.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(7.66, 0), pya.DPoint(7.66, 0.16), pya.DPoint(7.82, 0.16), pya.DPoint(7.82, 0), pya.DPoint(7.66, 0)]))

# === pmosHV$2 ===
cell_pmosHV_2.shapes(L_GatPoly).insert(
    pya.DPolygon([pya.DPoint(0.07, 0), pya.DPoint(0.07, 8), pya.DPoint(0.23, 8), pya.DPoint(0.23, 0), pya.DPoint(0.07, 0)]))
cell_pmosHV_2.shapes(L_GatPoly).insert(
    pya.DPolygon([pya.DPoint(8.45, 0), pya.DPoint(8.45, 8), pya.DPoint(8.61, 8), pya.DPoint(8.61, 0), pya.DPoint(8.45, 0)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(0.07, 0.07), pya.DPoint(0.07, 0.23), pya.DPoint(0.23, 0.23), pya.DPoint(0.23, 0.07), pya.DPoint(0.07, 0.07)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(0.07, 0.42), pya.DPoint(0.07, 0.58), pya.DPoint(0.23, 0.58), pya.DPoint(0.23, 0.42), pya.DPoint(0.07, 0.42)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(0.07, 0.77), pya.DPoint(0.07, 0.93), pya.DPoint(0.23, 0.93), pya.DPoint(0.23, 0.77), pya.DPoint(0.07, 0.77)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(0.07, 1.12), pya.DPoint(0.07, 1.28), pya.DPoint(0.23, 1.28), pya.DPoint(0.23, 1.12), pya.DPoint(0.07, 1.12)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(0.07, 1.47), pya.DPoint(0.07, 1.63), pya.DPoint(0.23, 1.63), pya.DPoint(0.23, 1.47), pya.DPoint(0.07, 1.47)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(0.07, 1.82), pya.DPoint(0.07, 1.98), pya.DPoint(0.23, 1.98), pya.DPoint(0.23, 1.82), pya.DPoint(0.07, 1.82)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(0.07, 2.17), pya.DPoint(0.07, 2.33), pya.DPoint(0.23, 2.33), pya.DPoint(0.23, 2.17), pya.DPoint(0.07, 2.17)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(0.07, 2.52), pya.DPoint(0.07, 2.68), pya.DPoint(0.23, 2.68), pya.DPoint(0.23, 2.52), pya.DPoint(0.07, 2.52)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(0.07, 2.87), pya.DPoint(0.07, 3.03), pya.DPoint(0.23, 3.03), pya.DPoint(0.23, 2.87), pya.DPoint(0.07, 2.87)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(0.07, 3.22), pya.DPoint(0.07, 3.38), pya.DPoint(0.23, 3.38), pya.DPoint(0.23, 3.22), pya.DPoint(0.07, 3.22)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(0.07, 3.57), pya.DPoint(0.07, 3.73), pya.DPoint(0.23, 3.73), pya.DPoint(0.23, 3.57), pya.DPoint(0.07, 3.57)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(0.07, 3.92), pya.DPoint(0.07, 4.08), pya.DPoint(0.23, 4.08), pya.DPoint(0.23, 3.92), pya.DPoint(0.07, 3.92)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(0.07, 4.27), pya.DPoint(0.07, 4.43), pya.DPoint(0.23, 4.43), pya.DPoint(0.23, 4.27), pya.DPoint(0.07, 4.27)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(0.07, 4.62), pya.DPoint(0.07, 4.78), pya.DPoint(0.23, 4.78), pya.DPoint(0.23, 4.62), pya.DPoint(0.07, 4.62)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(0.07, 4.97), pya.DPoint(0.07, 5.13), pya.DPoint(0.23, 5.13), pya.DPoint(0.23, 4.97), pya.DPoint(0.07, 4.97)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(0.07, 5.32), pya.DPoint(0.07, 5.48), pya.DPoint(0.23, 5.48), pya.DPoint(0.23, 5.32), pya.DPoint(0.07, 5.32)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(0.07, 5.67), pya.DPoint(0.07, 5.83), pya.DPoint(0.23, 5.83), pya.DPoint(0.23, 5.67), pya.DPoint(0.07, 5.67)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(0.07, 6.02), pya.DPoint(0.07, 6.18), pya.DPoint(0.23, 6.18), pya.DPoint(0.23, 6.02), pya.DPoint(0.07, 6.02)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(0.07, 6.37), pya.DPoint(0.07, 6.53), pya.DPoint(0.23, 6.53), pya.DPoint(0.23, 6.37), pya.DPoint(0.07, 6.37)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(0.07, 6.72), pya.DPoint(0.07, 6.88), pya.DPoint(0.23, 6.88), pya.DPoint(0.23, 6.72), pya.DPoint(0.07, 6.72)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(0.07, 7.07), pya.DPoint(0.07, 7.23), pya.DPoint(0.23, 7.23), pya.DPoint(0.23, 7.07), pya.DPoint(0.07, 7.07)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(0.07, 7.42), pya.DPoint(0.07, 7.58), pya.DPoint(0.23, 7.58), pya.DPoint(0.23, 7.42), pya.DPoint(0.07, 7.42)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(0.07, 7.77), pya.DPoint(0.07, 7.93), pya.DPoint(0.23, 7.93), pya.DPoint(0.23, 7.77), pya.DPoint(0.07, 7.77)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(8.45, 0.07), pya.DPoint(8.45, 0.23), pya.DPoint(8.61, 0.23), pya.DPoint(8.61, 0.07), pya.DPoint(8.45, 0.07)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(8.45, 0.42), pya.DPoint(8.45, 0.58), pya.DPoint(8.61, 0.58), pya.DPoint(8.61, 0.42), pya.DPoint(8.45, 0.42)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(8.45, 0.77), pya.DPoint(8.45, 0.93), pya.DPoint(8.61, 0.93), pya.DPoint(8.61, 0.77), pya.DPoint(8.45, 0.77)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(8.45, 1.12), pya.DPoint(8.45, 1.28), pya.DPoint(8.61, 1.28), pya.DPoint(8.61, 1.12), pya.DPoint(8.45, 1.12)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(8.45, 1.47), pya.DPoint(8.45, 1.63), pya.DPoint(8.61, 1.63), pya.DPoint(8.61, 1.47), pya.DPoint(8.45, 1.47)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(8.45, 1.82), pya.DPoint(8.45, 1.98), pya.DPoint(8.61, 1.98), pya.DPoint(8.61, 1.82), pya.DPoint(8.45, 1.82)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(8.45, 2.17), pya.DPoint(8.45, 2.33), pya.DPoint(8.61, 2.33), pya.DPoint(8.61, 2.17), pya.DPoint(8.45, 2.17)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(8.45, 2.52), pya.DPoint(8.45, 2.68), pya.DPoint(8.61, 2.68), pya.DPoint(8.61, 2.52), pya.DPoint(8.45, 2.52)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(8.45, 2.87), pya.DPoint(8.45, 3.03), pya.DPoint(8.61, 3.03), pya.DPoint(8.61, 2.87), pya.DPoint(8.45, 2.87)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(8.45, 3.22), pya.DPoint(8.45, 3.38), pya.DPoint(8.61, 3.38), pya.DPoint(8.61, 3.22), pya.DPoint(8.45, 3.22)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(8.45, 3.57), pya.DPoint(8.45, 3.73), pya.DPoint(8.61, 3.73), pya.DPoint(8.61, 3.57), pya.DPoint(8.45, 3.57)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(8.45, 3.92), pya.DPoint(8.45, 4.08), pya.DPoint(8.61, 4.08), pya.DPoint(8.61, 3.92), pya.DPoint(8.45, 3.92)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(8.45, 4.27), pya.DPoint(8.45, 4.43), pya.DPoint(8.61, 4.43), pya.DPoint(8.61, 4.27), pya.DPoint(8.45, 4.27)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(8.45, 4.62), pya.DPoint(8.45, 4.78), pya.DPoint(8.61, 4.78), pya.DPoint(8.61, 4.62), pya.DPoint(8.45, 4.62)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(8.45, 4.97), pya.DPoint(8.45, 5.13), pya.DPoint(8.61, 5.13), pya.DPoint(8.61, 4.97), pya.DPoint(8.45, 4.97)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(8.45, 5.32), pya.DPoint(8.45, 5.48), pya.DPoint(8.61, 5.48), pya.DPoint(8.61, 5.32), pya.DPoint(8.45, 5.32)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(8.45, 5.67), pya.DPoint(8.45, 5.83), pya.DPoint(8.61, 5.83), pya.DPoint(8.61, 5.67), pya.DPoint(8.45, 5.67)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(8.45, 6.02), pya.DPoint(8.45, 6.18), pya.DPoint(8.61, 6.18), pya.DPoint(8.61, 6.02), pya.DPoint(8.45, 6.02)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(8.45, 6.37), pya.DPoint(8.45, 6.53), pya.DPoint(8.61, 6.53), pya.DPoint(8.61, 6.37), pya.DPoint(8.45, 6.37)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(8.45, 6.72), pya.DPoint(8.45, 6.88), pya.DPoint(8.61, 6.88), pya.DPoint(8.61, 6.72), pya.DPoint(8.45, 6.72)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(8.45, 7.07), pya.DPoint(8.45, 7.23), pya.DPoint(8.61, 7.23), pya.DPoint(8.61, 7.07), pya.DPoint(8.45, 7.07)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(8.45, 7.42), pya.DPoint(8.45, 7.58), pya.DPoint(8.61, 7.58), pya.DPoint(8.61, 7.42), pya.DPoint(8.45, 7.42)]))
cell_pmosHV_2.shapes(L_pSD).insert(
    pya.DPolygon([pya.DPoint(8.45, 7.77), pya.DPoint(8.45, 7.93), pya.DPoint(8.61, 7.93), pya.DPoint(8.61, 7.77), pya.DPoint(8.45, 7.77)]))
cell_pmosHV_2.shapes(L_Activ).insert(
    pya.DPolygon([pya.DPoint(0, 0), pya.DPoint(0, 0.3), pya.DPoint(0.3, 0.3), pya.DPoint(0.3, 0), pya.DPoint(0, 0)]))
cell_pmosHV_2.shapes(L_Activ).insert(
    pya.DPolygon([pya.DPoint(8.38, 0), pya.DPoint(8.38, 0.3), pya.DPoint(8.68, 0.3), pya.DPoint(8.68, 0), pya.DPoint(8.38, 0)]))
cell_pmosHV_2.shapes(L_Activ).insert(
    pya.DPolygon([pya.DPoint(0, 0), pya.DPoint(0, 8), pya.DPoint(8.68, 8), pya.DPoint(8.68, 0), pya.DPoint(0, 0)]))
cell_pmosHV_2.shapes(L_NWell).insert(
    pya.DPolygon([pya.DPoint(0.34, -0.18), pya.DPoint(0.34, 8.18), pya.DPoint(8.34, 8.18), pya.DPoint(8.34, -0.18), pya.DPoint(0.34, -0.18)]))
cell_pmosHV_2.shapes(L_Metal2).insert(
    pya.DPolygon([pya.DPoint(-0.18, -0.4), pya.DPoint(-0.18, 8.4), pya.DPoint(8.86, 8.4), pya.DPoint(8.86, -0.4), pya.DPoint(-0.18, -0.4)]))
cell_pmosHV_2.shapes(L_TopMetal1).insert(
    pya.DPolygon([pya.DPoint(-1.13, -0.62), pya.DPoint(-1.13, 8.62), pya.DPoint(9.81, 8.62), pya.DPoint(9.81, -0.62), pya.DPoint(-1.13, -0.62)]))
cell_pmosHV_2.shapes(L_GatPoly_pin).insert(
    pya.DPolygon([pya.DPoint(0.07, 0), pya.DPoint(0.07, 8), pya.DPoint(0.23, 8), pya.DPoint(0.23, 0), pya.DPoint(0.07, 0)]))
cell_pmosHV_2.shapes(L_GatPoly_pin).insert(
    pya.DPolygon([pya.DPoint(8.45, 0), pya.DPoint(8.45, 8), pya.DPoint(8.61, 8), pya.DPoint(8.61, 0), pya.DPoint(8.45, 0)]))
_txt = pya.Text("pmosHV",
               pya.Trans(1, False, pya.Vector(4340, 4000)))
_txt.halign = 1
_txt.valign = 1
cell_pmosHV_2.shapes(L_Via1).insert(_txt)
cell_pmosHV_2.shapes(L_hvdifftap).insert(
    pya.DPolygon([pya.DPoint(-1.13, -0.62), pya.DPoint(-1.13, 8.62), pya.DPoint(9.81, 8.62), pya.DPoint(9.81, -0.62), pya.DPoint(-1.13, -0.62)]))
cell_pmosHV_2.shapes(L_FILL).insert(
    pya.DPolygon([pya.DPoint(0.34, -0.18), pya.DPoint(0.34, 8.18), pya.DPoint(8.34, 8.18), pya.DPoint(8.34, -0.18), pya.DPoint(0.34, -0.18)]))
_txt = pya.Text("pmos",
               pya.Trans(0, False, pya.Vector(4340, 4000)))
_txt.halign = 1
_txt.valign = 1
cell_pmosHV_2.shapes(L_FILL).insert(_txt)
cell_pmosHV_2.shapes(L_DNWell).insert(
    pya.DPolygon([pya.DPoint(8.38, 0), pya.DPoint(8.38, 0.3), pya.DPoint(8.68, 0.3), pya.DPoint(8.68, 0), pya.DPoint(8.38, 0)]))
cell_pmosHV_2.shapes(L_NWell_pin).insert(
    pya.DPolygon([pya.DPoint(0.34, -0.18), pya.DPoint(0.34, 8.18), pya.DPoint(8.34, 8.18), pya.DPoint(8.34, -0.18), pya.DPoint(0.34, -0.18)]))

# === pmos_buffer_cap ===
cell_pmos_buffer_cap.insert(pya.DCellInstArray(
    cell_FEOL_contacts_1.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(0, -0.44))))
cell_pmos_buffer_cap.insert(pya.DCellInstArray(
    cell_FEOL_contacts_1.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(0, 8.96))))
cell_pmos_buffer_cap.insert(pya.DCellInstArray(
    cell_FEOL_contacts_1.cell_index(),
    pya.DCplxTrans(1, 90, True,
                  pya.DVector(-0.38, 0.34))))
cell_pmos_buffer_cap.insert(pya.DCellInstArray(
    cell_FEOL_contacts_1.cell_index(),
    pya.DCplxTrans(1, 90, True,
                  pya.DVector(8.22, 0.34))))
cell_pmos_buffer_cap.insert(pya.DCellInstArray(
    cell_pmosHV_2.cell_index(),
    pya.DCplxTrans(1, 90, True,
                  pya.DVector(0, 0))))
cell_pmos_buffer_cap.shapes(L_GatPoly).insert(
    pya.DPolygon([pya.DPoint(0, -0.44), pya.DPoint(0, 9.12), pya.DPoint(8, 9.12), pya.DPoint(8, -0.44), pya.DPoint(0, -0.44)]))
cell_pmos_buffer_cap.shapes(L_Activ).insert(
    pya.DPolygon([pya.DPoint(0, -0.51), pya.DPoint(0, -0.21), pya.DPoint(8, -0.21), pya.DPoint(8, -0.51), pya.DPoint(0, -0.51)]))
cell_pmos_buffer_cap.shapes(L_Activ).insert(
    pya.DPolygon([pya.DPoint(0, 8.89), pya.DPoint(0, 9.19), pya.DPoint(8, 9.19), pya.DPoint(8, 8.89), pya.DPoint(0, 8.89)]))
cell_pmos_buffer_cap.shapes(L_NWell).insert(
    pya.DPolygon([pya.DPoint(-0.45, 0.34), pya.DPoint(-0.45, 8.34), pya.DPoint(8.45, 8.34), pya.DPoint(8.45, 0.34), pya.DPoint(-0.45, 0.34)]))

# === dacbuffer ===
cell_dacbuffer.insert(pya.DCellInstArray(
    cell_pmos_buffer_cap.cell_index(),
    pya.DCplxTrans(1, 0, False,
                  pya.DVector(13.725, 16.39))))
_path = pya.DPath([pya.DPoint(0, 0.25), pya.DPoint(37.8, 0.25)], 0.5)
cell_dacbuffer.shapes(L_GatPoly).insert(_path)
_path = pya.DPath([pya.DPoint(0, 13.095), pya.DPoint(37.8, 13.095)], 0.7)
cell_dacbuffer.shapes(L_GatPoly).insert(_path)
_path = pya.DPath([pya.DPoint(0, 25.94), pya.DPoint(37.8, 25.94)], 0.5)
cell_dacbuffer.shapes(L_GatPoly).insert(_path)
cell_dacbuffer.shapes(L_GatPoly_pin).insert(
    pya.DPolygon([pya.DPoint(0, 12.745), pya.DPoint(0, 13.445), pya.DPoint(37.8, 13.445), pya.DPoint(37.8, 12.745), pya.DPoint(0, 12.745)]))
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
cell_dacbuffer.shapes(L_prBoundary).insert(
    pya.DPolygon([pya.DPoint(0, -0.07), pya.DPoint(0, 26.26), pya.DPoint(37.8, 26.26), pya.DPoint(37.8, -0.07), pya.DPoint(0, -0.07)]))
cell_dacbuffer.shapes(L_prBoundary).insert(
    pya.DPolygon([pya.DPoint(3.105, 15.26), pya.DPoint(3.105, 26.2), pya.DPoint(12.345, 26.2), pya.DPoint(12.345, 15.26), pya.DPoint(3.105, 15.26)]))
_txt = pya.Text("Iout",
               pya.Trans(0, False, pya.Vector(18900, 13095)))
_txt.halign = 1
_txt.valign = 1
cell_dacbuffer.shapes(L_GatPoly_label).insert(_txt)
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

# Save
layout.write("output.gds")
