v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 140 -280 200 -280 {lab=EN}
N 300 -280 320 -280 {lab=ON_N}
N 400 -280 440 -280 {lab=OFF_N}
N 440 -380 440 -280 {lab=OFF_N}
N 440 -380 480 -380 {lab=OFF_N}
N 300 -280 300 -180 {lab=ON_N}
N 280 -280 300 -280 {lab=ON_N}
N 300 -180 480 -180 {lab=ON_N}
C {title.sym} 160 0 0 0 {name=l1 author="Christoph Maier"}
C {iopin.sym} 140 -120 0 1 {name=p1 lab=VSS}
C {iopin.sym} 140 -440 0 1 {name=p2 lab=VDD}
C {ipin.sym} 140 -280 0 0 {name=p3 lab=EN}
C {opin.sym} 480 -380 0 0 {name=p4 lab=OFF_N}
C {opin.sym} 480 -180 0 0 {name=p5 lab=ON_N}
C {sg13g2_stdcells/sg13g2_inv_1.sym} 240 -280 0 0 {name=x1 VDD=VDD VSS=VSS prefix=sg13g2_ }
C {sg13g2_stdcells/sg13g2_inv_1.sym} 360 -280 0 0 {name=x2 VDD=VDD VSS=VSS prefix=sg13g2_ }
