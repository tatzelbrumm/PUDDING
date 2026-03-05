v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 500 -330 500 -270 {lab=drain}
N 500 -210 500 -180 {lab=Iout}
N 500 -360 580 -360 {lab=#net1}
N 500 -240 660 -240 {lab=#net2}
N 360 -460 500 -460 {lab=VDD}
N 580 -460 660 -460 {lab=VDD}
N 440 -240 460 -240 {lab=#net3}
N 360 -240 380 -240 {lab=VcascodeP}
N 360 -360 380 -360 {lab=VbiasP}
N 440 -360 460 -360 {lab=#net4}
N 500 -460 500 -390 {lab=VDD}
N 660 -460 660 -440 {lab=VDD}
N 660 -380 660 -240 {lab=#net2}
N 580 -460 580 -440 {lab=VDD}
N 500 -460 580 -460 {lab=VDD}
N 580 -380 580 -360 {lab=#net1}
C {title.sym} 160 0 0 0 {name=l1 author="Christoph Maier"}
C {sg13g2_pr/sg13_lv_pmos.sym} 480 -360 0 0 {name=Msrc
l=5u
w=1.45u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
C {sg13g2_pr/sg13_lv_pmos.sym} 480 -240 0 0 {name=Mcasc
l=0.6u
w=1.2u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
C {ipin.sym} 360 -240 0 0 {name=p1 lab=VcascodeP}
C {ipin.sym} 360 -360 0 0 {name=p4 lab=VbiasP}
C {opin.sym} 500 -180 1 0 {name=p2 lab=Iout}
C {ipin.sym} 360 -460 0 0 {name=p3 lab=VDD}
C {lab_wire.sym} 500 -290 0 0 {name=p5 sig_type=std_logic lab=drain}
C {vsource.sym} 410 -360 1 0 {name=Vgsrc value=0 savecurrent=true}
C {vsource.sym} 410 -240 1 0 {name=Vgcasc value=0 savecurrent=true}
C {vsource.sym} 580 -410 0 0 {name=Vbsrc value=0 savecurrent=true}
C {vsource.sym} 660 -410 0 0 {name=Vbcasc value=0 savecurrent=true}
