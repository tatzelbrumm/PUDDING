v {xschem version=3.4.4 file_version=1.2
}
G {}
K {}
V {}
S {}
E {}
N 100 -160 100 -140 {lab=VDD}
N -30 -110 60 -110 {lab=VbiasP}
N -30 -10 60 -10 {lab=VcascodeP}
N 100 -10 200 -10 {lab=VDD}
N 200 -110 200 -10 {lab=VDD}
N 100 -160 200 -160 {lab=VDD}
N 100 -200 100 -160 {lab=VDD}
N 100 -110 200 -110 {lab=VDD}
N 200 -160 200 -110 {lab=VDD}
N 100 -80 100 -40 {lab=#net1}
N 100 20 100 60 {lab=Iout}
C {sg13g2_pr/sg13_lv_pmos.sym} 80 -110 0 0 {name=M2
l=1.5u
w=0.5u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
C {sg13g2_pr/sg13_lv_pmos.sym} 80 -10 0 0 {name=M3
l=0.5u
w=0.5u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
C {ipin.sym} -30 -10 0 0 {name=p1 lab=VcascodeP}
C {ipin.sym} -30 -110 0 0 {name=p4 lab=VbiasP}
C {opin.sym} 100 60 1 0 {name=p2 lab=Iout}
C {ipin.sym} 100 -200 1 0 {name=p3 lab=VDD}
