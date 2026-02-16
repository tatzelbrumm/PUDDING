v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 680 -360 700 -360 {lab=SUB}
N 700 -240 700 -120 {lab=SUB}
N 500 -120 700 -120 {lab=SUB}
N 680 -240 700 -240 {lab=SUB}
N 700 -360 700 -240 {lab=SUB}
N 680 -330 680 -270 {lab=vd_2}
N 480 -330 480 -270 {lab=vd_1}
N 280 -330 280 -270 {lab=vd_in}
N 680 -210 680 -160 {lab=VSSA}
N 480 -160 680 -160 {lab=VSSA}
N 280 -210 280 -160 {lab=VSSA}
N 480 -210 480 -160 {lab=VSSA}
N 280 -160 480 -160 {lab=VSSA}
N 480 -360 500 -360 {lab=SUB}
N 500 -240 500 -120 {lab=SUB}
N 260 -120 500 -120 {lab=SUB}
N 480 -240 500 -240 {lab=SUB}
N 500 -360 500 -240 {lab=SUB}
N 260 -360 280 -360 {lab=SUB}
N 260 -240 260 -120 {lab=SUB}
N 140 -120 260 -120 {lab=SUB}
N 260 -240 280 -240 {lab=SUB}
N 260 -360 260 -240 {lab=SUB}
N 280 -420 280 -390 {lab=Iin}
N 420 -420 620 -420 {lab=Iin}
N 620 -360 620 -240 {lab=Iin}
N 620 -240 640 -240 {lab=Iin}
N 620 -360 640 -360 {lab=Iin}
N 620 -420 620 -360 {lab=Iin}
N 420 -360 420 -240 {lab=Iin}
N 420 -240 440 -240 {lab=Iin}
N 420 -360 440 -360 {lab=Iin}
N 420 -420 420 -360 {lab=Iin}
N 340 -420 420 -420 {lab=Iin}
N 340 -360 340 -240 {lab=Iin}
N 320 -240 340 -240 {lab=Iin}
N 320 -360 340 -360 {lab=Iin}
N 340 -420 340 -360 {lab=Iin}
N 280 -420 340 -420 {lab=Iin}
N 140 -160 280 -160 {lab=VSSA}
N 280 -460 280 -420 {lab=Iin}
N 480 -460 480 -390 {lab=Iout1}
N 680 -460 680 -390 {lab=Iout2}
C {title.sym} 160 0 0 0 {name=l1 author="Christoph Maier"}
C {sg13g2_pr/sg13_lv_nmos.sym} 300 -240 0 1 {name=M1
l=4.0u
w=0.4u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
C {sg13g2_pr/sg13_lv_nmos.sym} 460 -240 0 0 {name=M3
l=4.0u
w=0.4u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
C {sg13g2_pr/sg13_lv_nmos.sym} 300 -360 0 1 {name=M2
l=0.26u
w=4u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
C {sg13g2_pr/sg13_lv_nmos.sym} 460 -360 0 0 {name=M4
l=0.26u
w=4u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 -240 0 0 {name=M5
l=4.0u
w=0.4u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
C {sg13g2_pr/sg13_lv_nmos.sym} 660 -360 0 0 {name=M6
l=0.26u
w=4u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
C {iopin.sym} 140 -160 0 1 {name=p1 lab=VSSA}
C {iopin.sym} 140 -120 0 1 {name=p2 lab=SUB}
C {iopin.sym} 280 -460 3 0 {name=p3 lab=Iin}
C {iopin.sym} 480 -460 3 0 {name=p4 lab=Iout1}
C {iopin.sym} 680 -460 3 0 {name=p5 lab=Iout2}
C {lab_wire.sym} 280 -290 0 1 {name=p6 sig_type=std_logic lab=vd_in}
C {lab_wire.sym} 480 -290 0 0 {name=p7 sig_type=std_logic lab=vd_1}
C {lab_wire.sym} 680 -290 0 0 {name=p8 sig_type=std_logic lab=vd_2}
