# make_dac_m2_pins.py
# Metal2 EN/ENB/ON/ONB input pins for dac4x32module top level.
#
# Physical pin order, left → right:
#
#   TOP:    EN8  ENB8  ON64..ON79  ONB64..ONB79  EN9  ENB9
#           EN10 ENB10 ON80..ON95  ONB80..ONB95  EN11 ENB11
#           EN12 ENB12 ON96..ON111 ONB96..ONB111 EN13 ENB13
#           EN14 ENB14 ON112..ON127 ONB112..ONB127 EN15 ENB15
#
#   BOTTOM: EN7  ENB7  ONB63..ONB48 ON63..ON48  EN6  ENB6
#           EN5  ENB5  ONB47..ONB32 ON47..ON32  EN4  ENB4
#           EN3  ENB3  ONB31..ONB16 ON31..ON16  EN2  ENB2
#           EN1  ENB1  ONB15..ONB0  ON15..ON0   EN0  ENB0
#
# 4 instances of dac2u32out4in at x = 22050, 97650, 173250, 248850 nm (pitch 75600)
# Each instance contributes 32 ON + 32 ONB + 4 EN + 4 ENB pins across top+bottom.

try:
    from klayout import db as pya
except ImportError:
    import pya

layout = pya.Layout()
layout.dbu = 0.001
top = layout.create_cell("DAC4X32_M2_PINS")

l_pin   = layout.layer(pya.LayerInfo(10, 2,  "Metal2_pin"))
l_label = layout.layer(pya.LayerInfo(10, 25, "Metal2_label"))

HALF_X = 100  # 200 nm wide
HALF_Y = 145  # 290 nm tall

# ── per-instance local geometry (nm, within one dac2u32out4in) ───────────────
Y_BOT    =   145
Y_TOP    = 26045
X_EN_L   =  1625   # left  EN  x
X_ENB_L  =  2175   # left  ENB x
X_FIRST  =  3625   # first signal pin x (ON or ONB depending on row)
PITCH    =  1000   # x pitch between adjacent pins (ON and ONB alternate)
X_EN_R   = 35625   # right EN  x
X_ENB_R  = 36175   # right ENB x

# instance x origins in dac4x32module top-level (nm)
INST_X = [22050, 97650, 173250, 248850]

def place(name, lx, y, ox):
    x = lx + ox
    top.shapes(l_pin).insert(pya.Box(x - HALF_X, y - HALF_Y, x + HALF_X, y + HALF_Y))
    t = pya.Text(name, pya.Trans(pya.Vector(x, y)))
    t.halign = pya.HAlign.HAlignCenter
    t.valign = pya.VAlign.VAlignCenter
    top.shapes(l_label).insert(t)

for k, ox in enumerate(INST_X):
    # Each instance owns 4 distinct EN indices — none shared with neighbours.
    # top:    left=EN[8+2k],  right=EN[9+2k]
    # bottom: left=EN[7-2k],  right=EN[6-2k]
    en_tl = 8  + k*2    # top-left  EN index:  8, 10, 12, 14
    en_tr = 9  + k*2    # top-right EN index:  9, 11, 13, 15
    en_bl = 7  - k*2    # bot-left  EN index:  7,  5,  3,  1
    en_br = 6  - k*2    # bot-right EN index:  6,  4,  2,  0
    on_top = 64 + k*16  # ON base on top:     64, 80, 96, 112
    on_bot = 63 - k*16  # ON top  on bottom:  63, 47, 31,  15

    # ── TOP row, left → right ────────────────────────────────────────────────
    place(f"EN[{en_tl}]",  X_EN_L,  Y_TOP, ox)
    place(f"ENB[{en_tl}]", X_ENB_L, Y_TOP, ox)
    for i in range(16):
        place(f"ON[{on_top+i}]",  X_FIRST + i*2*PITCH,         Y_TOP, ox)
        place(f"ONB[{on_top+i}]", X_FIRST + i*2*PITCH + PITCH, Y_TOP, ox)
    place(f"EN[{en_tr}]",  X_EN_R,  Y_TOP, ox)
    place(f"ENB[{en_tr}]", X_ENB_R, Y_TOP, ox)

    # ── BOTTOM row, left → right ─────────────────────────────────────────────
    place(f"EN[{en_bl}]",  X_EN_L,  Y_BOT, ox)
    place(f"ENB[{en_bl}]", X_ENB_L, Y_BOT, ox)
    for i in range(16):
        place(f"ONB[{on_bot-i}]", X_FIRST + i*2*PITCH,         Y_BOT, ox)
        place(f"ON[{on_bot-i}]",  X_FIRST + i*2*PITCH + PITCH, Y_BOT, ox)
    place(f"EN[{en_br}]",  X_EN_R,  Y_BOT, ox)
    place(f"ENB[{en_br}]", X_ENB_R, Y_BOT, ox)

layout.write("dac4x32_m2_pins.gds")
print(f"Wrote dac4x32_m2_pins.gds")
