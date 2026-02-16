v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 520 -360 520 -320 {lab=VDD}
N 380 -360 520 -360 {lab=VDD}
N 380 -280 460 -280 {lab=Vbp}
N 380 -240 460 -240 {lab=Vcp[15:0]}
N 520 -200 520 -140 {lab=Iout}
C {title.sym} 160 0 0 0 {name=l1 author="Christoph Maier"}
C {pcsource2u.sym} 520 -260 0 0 {name=xsrc[15:0]}
C {ipin.sym} 380 -240 0 0 {name=p1 lab=Vcp[15:0]}
C {ipin.sym} 380 -280 0 0 {name=p4 lab=Vbp}
C {opin.sym} 520 -140 1 0 {name=p2 lab=Iout}
C {ipin.sym} 380 -360 0 0 {name=p3 lab=VDD}
