v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 140 -80 240 -80 {lab=VSS}
N 240 -200 240 -80 {lab=VSS}
N 240 -400 240 -320 {lab=VDD}
N 140 -280 180 -280 {lab=ON}
N 140 -400 240 -400 {lab=VDD}
N 140 -240 180 -240 {lab=ONB}
N 140 -120 440 -120 {lab=VcascP}
N 440 -200 440 -120 {lab=VcascP}
N 440 -400 440 -320 {lab=VDD}
N 240 -400 440 -400 {lab=VDD}
N 500 -260 600 -260 {lab=Vcasc}
N 300 -240 320 -240 {lab=#net1}
N 320 -240 360 -280 {lab=#net1}
N 360 -280 380 -280 {lab=#net1}
N 300 -280 320 -280 {lab=#net2}
N 320 -280 360 -240 {lab=#net2}
N 360 -240 380 -240 {lab=#net2}
C {nonoverlap.sym} 240 -260 0 0 {name=xnonoverlap}
C {iopin.sym} 140 -80 2 0 {name=p1 lab=VSS}
C {iopin.sym} 140 -400 2 0 {name=p2 lab=VDD}
C {title.sym} 160 0 0 0 {name=l1 author="Christoph Maier"}
C {iopin.sym} 140 -120 0 1 {name=p6 lab=VcascP}
C {ipin.sym} 140 -280 0 0 {name=p7 lab=ON}
C {ipin.sym} 140 -240 0 0 {name=p8 lab=ONB}
C {opin.sym} 600 -260 2 1 {name=p4 lab=Vcasc}
C {cascodeswitch_pmos.sym} 440 -260 0 0 {name=xsw}
