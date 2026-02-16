v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 360 -360 460 -360 {lab=VbiasP}
N 360 -240 460 -240 {lab=VcascodeP}
N 520 -360 520 -240 {lab=VDD}
N 500 -420 500 -390 {lab=VDD}
N 500 -330 500 -270 {lab=drain}
N 500 -210 500 -180 {lab=Iout}
N 500 -360 520 -360 {lab=VDD}
N 500 -240 520 -240 {lab=VDD}
N 360 -420 500 -420 {lab=VDD}
N 500 -420 520 -420 {lab=VDD}
N 520 -420 520 -360 {lab=VDD}
C {title.sym} 160 0 0 0 {name=l1 author="Christoph Maier"}
C {sg13g2_pr/sg13_lv_pmos.sym} 480 -360 0 0 {name=Msrc
l=2u
w=0.55u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
C {sg13g2_pr/sg13_lv_pmos.sym} 480 -240 0 0 {name=Mcasc
l=0.3u
w=0.3u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
C {ipin.sym} 360 -240 0 0 {name=p1 lab=VcascodeP}
C {ipin.sym} 360 -360 0 0 {name=p4 lab=VbiasP}
C {opin.sym} 500 -180 1 0 {name=p2 lab=Iout}
C {ipin.sym} 360 -420 0 0 {name=p3 lab=VDD}
C {lab_wire.sym} 500 -290 0 0 {name=p5 sig_type=std_logic lab=drain}
