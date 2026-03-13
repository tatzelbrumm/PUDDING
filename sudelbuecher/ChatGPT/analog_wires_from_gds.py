import pya

layout = pya.Layout()
layout.dbu = 0.001

top = layout.create_cell('analog_wires')

L_30_0 = layout.layer(30, 0)
L_30_2 = layout.layer(30, 2)
L_30_25 = layout.layer(30, 25)
L_189_4 = layout.layer(189, 4)

# PATHS

top.shapes(L_30_0).insert(pya.Path([pya.Point(0, 39900), pya.Point(10910, 39900)], 700))
top.shapes(L_30_0).insert(pya.Path([pya.Point(0, 23530), pya.Point(10910, 23530)], 700))
top.shapes(L_30_0).insert(pya.Path([pya.Point(0, 31715), pya.Point(21910, 31715)], 700))
top.shapes(L_30_0).insert(pya.Path([pya.Point(0, 25145), pya.Point(20700, 25145)], 1730))
top.shapes(L_30_0).insert(pya.Path([pya.Point(0, 38285), pya.Point(20700, 38285)], 1730))
top.shapes(L_30_0).insert(pya.Path([pya.Point(0, 33015), pya.Point(21910, 33015)], 700))
top.shapes(L_30_0).insert(pya.Path([pya.Point(0, 30415), pya.Point(21910, 30415)], 700))
top.shapes(L_30_0).insert(pya.Path([pya.Point(0, 153425), pya.Point(20700, 153425)], 1730))
top.shapes(L_30_0).insert(pya.Path([pya.Point(0, 166565), pya.Point(20700, 166565)], 1730))
top.shapes(L_30_0).insert(pya.Path([pya.Point(0, 161295), pya.Point(21910, 161295)], 700))
top.shapes(L_30_0).insert(pya.Path([pya.Point(0, 158695), pya.Point(21910, 158695)], 700))
top.shapes(L_30_0).insert(pya.Path([pya.Point(0, 159995), pya.Point(21910, 159995)], 700))
top.shapes(L_30_0).insert(pya.Path([pya.Point(0, 168180), pya.Point(10910, 168180)], 700))
top.shapes(L_30_0).insert(pya.Path([pya.Point(0, 151810), pya.Point(10910, 151810)], 700))
top.shapes(L_30_0).insert(pya.Path([pya.Point(0, 96095), pya.Point(99600, 96095)], 700))
top.shapes(L_30_0).insert(pya.Path([pya.Point(0, 104280), pya.Point(99600, 104280)], 700))

# BOUNDARIES

top.shapes(L_189_4).insert(pya.Polygon([
    pya.Point(0, 0),
    pya.Point(0, 188000),
    pya.Point(99600, 188000),
    pya.Point(99600, 0),
    pya.Point(0, 0),
]))

top.shapes(L_30_2).insert(pya.Polygon([
    pya.Point(99200, 103930),
    pya.Point(99200, 104630),
    pya.Point(99600, 104630),
    pya.Point(99600, 103930),
    pya.Point(99200, 103930),
]))

top.shapes(L_30_2).insert(pya.Polygon([
    pya.Point(99200, 95745),
    pya.Point(99200, 96445),
    pya.Point(99600, 96445),
    pya.Point(99600, 95745),
    pya.Point(99200, 95745),
]))

top.shapes(L_30_2).insert(pya.Polygon([
    pya.Point(0, 167830),
    pya.Point(0, 168530),
    pya.Point(400, 168530),
    pya.Point(400, 167830),
    pya.Point(0, 167830),
]))

top.shapes(L_30_2).insert(pya.Polygon([
    pya.Point(0, 151460),
    pya.Point(0, 152160),
    pya.Point(400, 152160),
    pya.Point(400, 151460),
    pya.Point(0, 151460),
]))

top.shapes(L_30_2).insert(pya.Polygon([
    pya.Point(0, 159645),
    pya.Point(0, 160345),
    pya.Point(400, 160345),
    pya.Point(400, 159645),
    pya.Point(0, 159645),
]))

top.shapes(L_30_2).insert(pya.Polygon([
    pya.Point(0, 152560),
    pya.Point(0, 154290),
    pya.Point(400, 154290),
    pya.Point(400, 152560),
    pya.Point(0, 152560),
]))

top.shapes(L_30_2).insert(pya.Polygon([
    pya.Point(0, 165700),
    pya.Point(0, 167430),
    pya.Point(400, 167430),
    pya.Point(400, 165700),
    pya.Point(0, 165700),
]))

top.shapes(L_30_2).insert(pya.Polygon([
    pya.Point(0, 158345),
    pya.Point(0, 159045),
    pya.Point(400, 159045),
    pya.Point(400, 158345),
    pya.Point(0, 158345),
]))

top.shapes(L_30_2).insert(pya.Polygon([
    pya.Point(0, 160945),
    pya.Point(0, 161645),
    pya.Point(400, 161645),
    pya.Point(400, 160945),
    pya.Point(0, 160945),
]))

top.shapes(L_30_2).insert(pya.Polygon([
    pya.Point(0, 39550),
    pya.Point(0, 40250),
    pya.Point(400, 40250),
    pya.Point(400, 39550),
    pya.Point(0, 39550),
]))

top.shapes(L_30_2).insert(pya.Polygon([
    pya.Point(0, 23180),
    pya.Point(0, 23880),
    pya.Point(400, 23880),
    pya.Point(400, 23180),
    pya.Point(0, 23180),
]))

top.shapes(L_30_2).insert(pya.Polygon([
    pya.Point(0, 31365),
    pya.Point(0, 32065),
    pya.Point(400, 32065),
    pya.Point(400, 31365),
    pya.Point(0, 31365),
]))

top.shapes(L_30_2).insert(pya.Polygon([
    pya.Point(0, 24280),
    pya.Point(0, 26010),
    pya.Point(400, 26010),
    pya.Point(400, 24280),
    pya.Point(0, 24280),
]))

top.shapes(L_30_2).insert(pya.Polygon([
    pya.Point(0, 37420),
    pya.Point(0, 39150),
    pya.Point(400, 39150),
    pya.Point(400, 37420),
    pya.Point(0, 37420),
]))

top.shapes(L_30_2).insert(pya.Polygon([
    pya.Point(0, 30065),
    pya.Point(0, 30765),
    pya.Point(400, 30765),
    pya.Point(400, 30065),
    pya.Point(0, 30065),
]))

top.shapes(L_30_2).insert(pya.Polygon([
    pya.Point(0, 32665),
    pya.Point(0, 33365),
    pya.Point(400, 33365),
    pya.Point(400, 32665),
    pya.Point(0, 32665),
]))

# TEXTS

t = pya.Text('VcascP[0]', 200, 23530)
t.size = 400
top.shapes(L_30_25).insert(t)

t = pya.Text('VcascP[1]', 200, 39900)
t.size = 400
top.shapes(L_30_25).insert(t)

t = pya.Text('Iout[0]', 200, 31715)
t.size = 400
top.shapes(L_30_25).insert(t)

t = pya.Text('VDDA[0]', 200, 25145)
t.size = 400
top.shapes(L_30_25).insert(t)

t = pya.Text('VDDA[1]', 200, 38285)
t.size = 400
top.shapes(L_30_25).insert(t)

t = pya.Text('VbiasP[1]', 200, 33015)
t.size = 400
top.shapes(L_30_25).insert(t)

t = pya.Text('VbiasP[0]', 200, 30415)
t.size = 400
top.shapes(L_30_25).insert(t)

t = pya.Text('VcascP[2]', 200, 151810)
t.size = 400
top.shapes(L_30_25).insert(t)

t = pya.Text('VcascP[3]', 200, 168180)
t.size = 400
top.shapes(L_30_25).insert(t)

t = pya.Text('Iout[1]', 200, 159995)
t.size = 400
top.shapes(L_30_25).insert(t)

t = pya.Text('VDDA[2]', 200, 153425)
t.size = 400
top.shapes(L_30_25).insert(t)

t = pya.Text('VDDA[3]', 200, 166565)
t.size = 400
top.shapes(L_30_25).insert(t)

t = pya.Text('VbiasP[3]', 200, 161295)
t.size = 400
top.shapes(L_30_25).insert(t)

t = pya.Text('VbiasP[2]', 200, 158695)
t.size = 400
top.shapes(L_30_25).insert(t)

t = pya.Text('i_in', 99400, 104280)
t.size = 400
top.shapes(L_30_25).insert(t)

t = pya.Text('i_out', 99400, 96095)
t.size = 400
top.shapes(L_30_25).insert(t)

layout.write('analog_wires_roundtrip.gds')
