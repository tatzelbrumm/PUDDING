v {xschem version=3.4.8RC file_version=1.3}
G {}
K {}
V {}
S {}
F {}
E {}
N 160 -500 650 -500 {lab=ON_N}
N 650 -500 650 -230 {lab=ON_N}
N 560 -470 560 -350 {lab=ON}
N 760 -310 910 -310 {lab=Pcascode_sw}
N 760 -310 760 -190 {lab=Pcascode_sw}
N 590 -310 760 -310 {lab=Pcascode_sw}
N 170 -190 620 -190 {lab=Pcascode}
N 170 -310 530 -310 {lab=#net1}
N 160 -470 560 -470 {lab=ON}
N 650 -190 650 -110 {lab=VDD}
N 560 -310 560 -110 {lab=VDD}
N 680 -190 760 -190 {lab=Pcascode_sw}
C {sg13g2_pr/sg13_lv_pmos.sym} 560 -330 1 0 {name=M1
l=0.13u
w=0.5u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
C {sg13g2_pr/sg13_lv_pmos.sym} 650 -210 1 0 {name=M3
l=0.13u
w=0.5u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
C {ipin.sym} 160 -470 0 0 {name=p1 lab=ON}
C {ipin.sym} 170 -190 0 0 {name=p2 lab=Pcascode}
C {opin.sym} 910 -310 0 0 {name=p6 lab=Pcascode_sw}
C {lab_wire.sym} 560 -110 3 0 {name=p7 sig_type=analog lab=VDD}
C {lab_wire.sym} 650 -110 3 0 {name=p8 sig_type=analog lab=VDD}
C {lab_wire.sym} 650 -500 0 0 {name=p9 sig_type=std_logic lab=ON_N}
C {ipin.sym} 160 -500 0 0 {name=p5 lab=ON_N}
C {ipin.sym} 170 -310 0 0 {name=p3 lab=VDD}
