v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 360 -400 360 -380 {lab=VDD}
N 560 -400 560 -380 {lab=VDD}
N 360 -400 560 -400 {lab=VDD}
N 280 -400 360 -400 {lab=VDD}
N 600 -300 600 -280 {lab=C20}
N 600 -280 640 -280 {lab=C20}
N 580 -260 640 -260 {lab=C21}
N 580 -300 580 -260 {lab=C21}
N 540 -300 540 -220 {lab=C30}
N 540 -220 640 -220 {lab=C30}
N 520 -300 520 -200 {lab=C31}
N 520 -200 640 -200 {lab=C31}
N 400 -300 400 -200 {lab=C11}
N 280 -200 400 -200 {lab=C11}
N 380 -300 380 -220 {lab=C10}
N 280 -220 380 -220 {lab=C10}
N 340 -300 340 -260 {lab=C01}
N 280 -260 340 -260 {lab=C01}
N 320 -300 320 -280 {lab=C00}
N 280 -280 320 -280 {lab=C00}
C {title.sym} 160 0 0 0 {name=l1 author="Christoph Maier"}
C {iopin.sym} 280 -400 0 1 {name=p1 lab=VDD}
C {iopin.sym} 280 -280 0 1 {name=p2 lab=C00}
C {iopin.sym} 280 -260 0 1 {name=p3 lab=C01}
C {dacbuffer_2chan.sym} 360 -340 0 0 {name=x0}
C {dacbuffer_2chan.sym} 560 -340 0 1 {name=x1}
C {iopin.sym} 280 -220 0 1 {name=p4 lab=C10}
C {iopin.sym} 280 -200 0 1 {name=p5 lab=C11}
C {iopin.sym} 640 -280 0 0 {name=p6 lab=C20}
C {iopin.sym} 640 -260 0 0 {name=p7 lab=C21}
C {iopin.sym} 640 -220 0 0 {name=p8 lab=C30}
C {iopin.sym} 640 -200 0 0 {name=p9 lab=C31}
