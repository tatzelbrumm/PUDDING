# make_gds.py
import pya

# Create layout
layout = pya.Layout()
layout.dbu = 0.001  # 1 nm units
top = layout.create_cell("SWITCHED_PMOS_CASCODE")

# Parameters
l = 300
w = 300

# Layers
l_active = layout.layer(pya.LayerInfo(1, 0))
l_po     = layout.layer(pya.LayerInfo(5, 0))
l_co     = layout.layer(pya.LayerInfo(6, 0))
l_m1     = layout.layer(pya.LayerInfo(8, 0))
l_pimp   = layout.layer(pya.LayerInfo(14, 0))
l_nwell  = layout.layer(pya.LayerInfo(31, 0))
l_label  = layout.layer(pya.LayerInfo(63, 0))


# Draw shapes
top.shapes(l_active).insert(pya.Box(290, -(l/2+230), 290+w, (l/2+340)))
top.shapes(l_po).insert(    pya.Box(-150, -l/2, 470+w, l/2))
top.shapes(l_co).insert(    pya.Box(-80,  -80,   80,  80))
top.shapes(l_co).insert(    pya.Box(w/2+210,  l/2+110, w/2+370, l/2+270))
top.shapes(l_m1).insert(    pya.Box(-80, -130,   80, 130))
top.shapes(l_m1).insert(    pya.Box(w/2+160, l/2+110, w/2+420, l/2+270))
top.shapes(l_pimp).insert(  pya.Box(-10, -(l/2+410),  590+w, (l/2+520)))
top.shapes(l_nwell).insert( pya.Box(-30, -(l/2+640),  610+w, (l/2+650)))
top.shapes(l_label).insert( pya.Box(-190, -(l/2+640),  610+w, (l/2+650)))

# Save GDS
layout.write("switched_pmos_cascode.gds")
print("Wrote switched_pmos_cascode.gds")

