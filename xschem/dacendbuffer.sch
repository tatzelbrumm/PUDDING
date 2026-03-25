v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 360 -400 360 -380 {lab=VDD}
N 340 -300 340 -280 {lab=C00}
N 380 -300 380 -240 {lab=C01}
N 480 -400 480 -380 {lab=VDD}
N 460 -300 460 -200 {lab=C10}
N 500 -300 500 -160 {lab=C11}
N 360 -400 480 -400 {lab=VDD}
N 280 -400 360 -400 {lab=VDD}
N 280 -280 340 -280 {lab=C00}
N 280 -240 380 -240 {lab=C01}
N 280 -200 460 -200 {lab=C10}
N 280 -160 500 -160 {lab=C11}
C {title.sym} 160 0 0 0 {name=l1 author="Christoph Maier"}
C {iopin.sym} 280 -400 0 1 {name=p1 lab=VDD}
C {iopin.sym} 280 -280 0 1 {name=p2 lab=C00}
C {iopin.sym} 280 -240 0 1 {name=p3 lab=C01}
C {dacbuffer_1chan.sym} 360 -340 0 0 {name=x0}
C {dacbuffer_1chan.sym} 480 -340 0 0 {name=x1}
C {iopin.sym} 280 -200 0 1 {name=p4 lab=C10}
C {iopin.sym} 280 -160 0 1 {name=p5 lab=C11}
