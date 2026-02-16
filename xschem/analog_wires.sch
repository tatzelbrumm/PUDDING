v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 360 -340 400 -340 {lab=vdda}
N 440 -340 440 -300 {lab=vdda}
N 400 -340 440 -340 {lab=vdda}
N 470 -300 480 -300 {lab=vdda}
N 480 -340 480 -300 {lab=vdda}
N 440 -340 480 -340 {lab=vdda}
N 400 -300 410 -300 {lab=vdda}
N 400 -340 400 -300 {lab=vdda}
N 320 -340 320 -300 {lab=vdda}
N 280 -340 320 -340 {lab=vdda}
N 350 -300 360 -300 {lab=vdda}
N 360 -340 360 -300 {lab=vdda}
N 320 -340 360 -340 {lab=vdda}
N 280 -300 290 -300 {lab=vdda}
N 280 -340 280 -300 {lab=vdda}
N 320 -240 320 -200 {lab=bias}
N 440 -120 520 -120 {lab=i_in}
N 440 -160 440 -120 {lab=i_in}
N 260 -200 320 -200 {lab=bias}
N 160 -200 200 -200 {lab=VbiasP[1:0]}
N 160 -240 200 -240 {lab=VbiasP[1:0]}
N 260 -240 320 -240 {lab=bias}
N 320 -260 320 -240 {lab=bias}
N 160 -300 200 -300 {lab=VDDA[1:0]}
N 160 -340 200 -340 {lab=VDDA[1:0]}
N 260 -340 280 -340 {lab=vdda}
N 260 -300 280 -300 {lab=vdda}
N 260 -80 520 -80 {lab=i_out}
N 260 -120 440 -120 {lab=i_in}
N 260 -160 440 -160 {lab=i_in}
N 440 -260 440 -160 {lab=i_in}
N 160 -160 200 -160 {lab=VcascP[1:0]}
N 160 -120 200 -120 {lab=VcascP[1:0]}
N 160 -80 200 -80 {lab=Iout}
C {title.sym} 160 0 0 0 {name=l1 author="Christoph Maier"}
C {sg13g2_pr/sg13_hv_pmos.sym} 440 -280 1 1 {name=Mcbuffer
l=8u
w=8u
ng=1
m=19
model=sg13_hv_pmos
spiceprefix=X
}
C {sg13g2_pr/sg13_hv_pmos.sym} 320 -280 1 1 {name=Mbbuffer
l=8u
w=8u
ng=1
m=19
model=sg13_hv_pmos
spiceprefix=X
}
C {iopin.sym} 160 -200 0 1 {name=p2 lab=VbiasP[1:0]}
C {iopin.sym} 160 -340 0 1 {name=p3 lab=VDDA[1:0]}
C {iopin.sym} 160 -120 0 1 {name=p5 lab=VcascP[1:0]}
C {iopin.sym} 160 -80 0 1 {name=p1 lab=Iout}
C {iopin.sym} 520 -80 0 0 {name=p4 lab=i_out}
C {iopin.sym} 520 -120 0 0 {name=p6 lab=i_in}
C {iopin.sym} 160 -300 0 1 {name=p7 lab=VDDA[1:0]}
C {iopin.sym} 160 -240 0 1 {name=p8 lab=VbiasP[1:0]}
C {iopin.sym} 160 -160 0 1 {name=p9 lab=VcascP[1:0]}
C {lab_wire.sym} 380 -340 0 0 {name=p10 sig_type=std_logic lab=vdda}
C {lab_wire.sym} 300 -200 0 0 {name=p11 sig_type=std_logic lab=bias}
C {res.sym} 230 -340 1 0 {name=R1
value=0
device=resistor
m=1}
C {res.sym} 230 -300 1 0 {name=R2
value=0
device=resistor
m=1}
C {res.sym} 230 -240 1 0 {name=R3
value=0
device=resistor
m=1}
C {res.sym} 230 -200 1 0 {name=R4
value=0
device=resistor
m=1}
C {res.sym} 230 -160 1 0 {name=R5
value=0
device=resistor
m=1}
C {res.sym} 230 -120 1 0 {name=R6
value=0
device=resistor
m=1}
C {res.sym} 230 -80 1 0 {name=R7
value=0
device=resistor
m=1}
