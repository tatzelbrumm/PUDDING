v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 460 -260 460 -220 {lab=VDD}
N 420 -260 460 -260 {lab=VDD}
N 490 -220 500 -220 {lab=VDD}
N 500 -260 500 -220 {lab=VDD}
N 460 -260 500 -260 {lab=VDD}
N 420 -220 430 -220 {lab=VDD}
N 420 -260 420 -220 {lab=VDD}
N 400 -260 420 -260 {lab=VDD}
N 360 -260 360 -220 {lab=VDD}
N 320 -260 360 -260 {lab=VDD}
N 390 -220 400 -220 {lab=VDD}
N 400 -260 400 -220 {lab=VDD}
N 360 -260 400 -260 {lab=VDD}
N 320 -220 330 -220 {lab=VDD}
N 320 -260 320 -220 {lab=VDD}
N 360 -180 360 -140 {lab=g0}
N 460 -180 460 -100 {lab=g1}
N 120 -260 320 -260 {lab=VDD}
N 120 -140 160 -140 {lab=C0}
N 220 -140 360 -140 {lab=g0}
N 300 -100 460 -100 {lab=g1}
N 120 -100 240 -100 {lab=C1}
C {title.sym} 160 0 0 0 {name=l1 author="Christoph Maier"}
C {sg13g2_pr/sg13_hv_pmos.sym} 460 -200 1 1 {name=M1
l=4.04u
w=14.6u
ng=1
m=1
model=sg13_hv_pmos
spiceprefix=X
}
C {sg13g2_pr/sg13_hv_pmos.sym} 360 -200 1 1 {name=M0
l=4.04u
w=14.6u
ng=1
m=1
model=sg13_hv_pmos
spiceprefix=X
}
C {iopin.sym} 120 -260 0 1 {name=p1 lab=VDD}
C {iopin.sym} 120 -140 0 1 {name=p2 lab=C0}
C {iopin.sym} 120 -100 0 1 {name=p3 lab=C1}
C {vsource.sym} 190 -140 1 1 {name=V0 value=0 savecurrent=true}
C {vsource.sym} 270 -100 1 0 {name=V1 value=0 savecurrent=true}
C {lab_wire.sym} 300 -140 0 0 {name=p4 lab=g0}
C {lab_wire.sym} 400 -100 0 0 {name=p5 lab=g1}
