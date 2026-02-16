v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 140 -80 240 -80 {lab=VSS}
N 240 -160 240 -80 {lab=VSS}
N 240 -400 240 -280 {lab=VDD}
N 140 -240 180 -240 {lab=ON}
N 140 -400 240 -400 {lab=VDD}
N 140 -200 180 -200 {lab=ONB}
N 140 -120 440 -120 {lab=VcascP}
N 440 -160 440 -120 {lab=VcascP}
N 440 -400 440 -280 {lab=VDD}
N 240 -400 440 -400 {lab=VDD}
N 440 -400 660 -400 {lab=VDD}
N 660 -400 660 -300 {lab=VDD}
N 140 -360 560 -360 {lab=VbiasP}
N 560 -360 560 -260 {lab=VbiasP}
N 560 -260 600 -260 {lab=VbiasP}
N 660 -180 660 -140 {lab=Iout}
N 660 -140 740 -140 {lab=Iout}
N 500 -220 600 -220 {lab=Vcasc}
N 300 -240 320 -240 {lab=on_n}
N 320 -240 360 -200 {lab=on_n}
N 360 -200 380 -200 {lab=on_n}
N 300 -200 320 -200 {lab=off_n}
N 320 -200 360 -240 {lab=off_n}
N 360 -240 380 -240 {lab=off_n}
C {nonoverlap.sym} 240 -220 0 0 {name=xnonoverlap}
C {iopin.sym} 140 -80 2 0 {name=p1 lab=VSS}
C {iopin.sym} 140 -400 2 0 {name=p2 lab=VDD}
C {iopin.sym} 140 -360 0 1 {name=p3 lab=VbiasP}
C {title.sym} 160 0 0 0 {name=l1 author="Christoph Maier"}
C {iopin.sym} 140 -120 0 1 {name=p6 lab=VcascP}
C {ipin.sym} 140 -240 0 0 {name=p7 lab=ON}
C {ipin.sym} 140 -200 0 0 {name=p8 lab=ONB}
C {iopin.sym} 740 -140 2 1 {name=p4 lab=Iout}
C {cascodeswitch_pmos.sym} 440 -220 0 0 {name=xsw}
C {pcsource2u.sym} 660 -240 0 0 {name=xsrc}
C {lab_wire.sym} 360 -240 0 0 {name=p5 lab=off_n}
C {lab_wire.sym} 580 -220 0 0 {name=p9 lab=Vcasc}
C {lab_wire.sym} 360 -200 0 0 {name=p10 lab=on_n}
