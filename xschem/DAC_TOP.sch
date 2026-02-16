v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
P 4 1 590 -570 {}
N 970 -500 1180 -500 {lab=CASCODE_SW[255:0]}
N 1480 -450 1610 -450 {lab=Iout}
N 1330 -650 1330 -560 {lab=VDD}
N 540 -650 540 -480 {lab=VDD}
N 300 -350 400 -350 {lab=VDD}
N 400 -450 400 -350 {lab=VDD}
N 300 -450 400 -450 {lab=VDD}
N 300 -400 300 -380 {lab=Vbias}
N 300 -260 300 -170 {lab=Iref}
N 540 -650 1330 -650 {lab=VDD}
N 300 -650 300 -480 {lab=VDD}
N 160 -650 300 -650 {lab=VDD}
N 400 -650 400 -450 {lab=VDD}
N 300 -650 400 -650 {lab=VDD}
N 220 -450 260 -450 {lab=Vbias}
N 220 -450 220 -400 {lab=Vbias}
N 220 -400 300 -400 {lab=Vbias}
N 300 -420 300 -400 {lab=Vbias}
N 300 -400 1140 -400 {lab=Vbias}
N 1140 -470 1140 -400 {lab=Vbias}
N 1140 -470 1180 -470 {lab=Vbias}
N 220 -350 260 -350 {lab=Iref}
N 220 -350 220 -260 {lab=Iref}
N 220 -260 300 -260 {lab=Iref}
N 300 -320 300 -260 {lab=Iref}
N 300 -260 660 -260 {lab=Iref}
N 660 -520 660 -260 {lab=Iref}
N 660 -520 670 -520 {lab=Iref}
N 160 -560 670 -560 {lab=ON[255:0]}
N 400 -650 540 -650 {lab=VDD}
N 540 -480 670 -480 {lab=VDD}
N 160 -580 670 -580 {lab=ON_N[255:0]}
C {Pmirrors_top.sym} 1330 -460 0 0 {name=xmirror}
C {ipin.sym} 160 -650 0 0 {name=p1 lab=VDD}
C {opin.sym} 1610 -450 0 0 {name=p2 lab=Iout}
C {ipin.sym} 160 -560 0 0 {name=p4 lab=ON[255:0]}
C {sg13g2_pr/sg13_lv_pmos.sym} 280 -450 0 0 {name=M2
l=1.5u
w=0.2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
C {sg13g2_pr/sg13_lv_pmos.sym} 280 -350 0 0 {name=M3
l=1.5u
w=0.2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
C {ipin.sym} 300 -170 3 0 {name=p5 lab=Iref}
C {lab_wire.sym} 530 -400 0 0 {name=p7 sig_type=std_logic lab=Vbias}
C {lab_wire.sym} 1180 -500 0 0 {name=p6 sig_type=std_logic lab=CASCODE_SW[255:0]}
C {DAC_SW_TOP.sym} 820 -370 0 0 {name=xSW_TOP}
C {ipin.sym} 160 -580 0 0 {name=p8 lab=ON_N[255:0]}
