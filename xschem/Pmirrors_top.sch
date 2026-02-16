v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
P 4 1 -290 -170 {}
N -310 -150 -150 -150 {lab=VcascodeP[255:0]}
N -310 -110 -150 -110 {lab=Vbiasp}
N 150 -110 270 -110 {lab=Iout}
N 0 -230 -0 -200 {lab=VDD}
C {Pmirror_StdCell.sym} 0 -110 0 0 {name=XI_MIRROR[255:0]}
C {ipin.sym} -310 -110 0 0 {name=p1 lab=Vbiasp
}
C {ipin.sym} 0 -230 1 0 {name=p3 lab=VDD}
C {ipin.sym} -310 -150 0 0 {name=p4 lab=VcascodeP[255:0]}
C {opin.sym} 270 -110 0 0 {name=p5 lab=Iout}
