v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 220 -340 240 -340 {lab=EN_N}
N 70 -520 460 -520 {lab=VDD}
N 220 -340 220 -300 {lab=EN_N}
N 220 -300 400 -300 {lab=EN_N}
N 320 -340 400 -340 {lab=EN_P}
N 80 -120 460 -120 {lab=VSS}
N 80 -340 120 -340 {lab=EN}
N 200 -340 220 -340 {lab=EN_N}
N 520 -340 600 -340 {lab=ON_N}
N 520 -300 600 -300 {lab=OFF_N}
N 460 -260 460 -120 {lab=VSS}
N 460 -520 460 -380 {lab=VDD}
C {sg13g2_stdcells/sg13g2_inv_1.sym} 160 -340 2 1 {name=x0 VDD=VDD VSS=VSS prefix=sg13g2_ }
C {sg13g2_stdcells/sg13g2_inv_1.sym} 280 -340 2 1 {name=x1 VDD=VDD VSS=VSS prefix=sg13g2_ }
C {nonoverlap.sym} 460 -320 0 0 {name=xnonoverlap}
C {iopin.sym} 80 -120 2 0 {name=p1 lab=VSS}
C {iopin.sym} 70 -520 2 0 {name=p2 lab=VDD}
C {ipin.sym} 80 -340 0 0 {name=p3 lab=EN}
C {opin.sym} 600 -340 0 0 {name=p4 lab=ON_N}
C {opin.sym} 600 -300 0 0 {name=p5 lab=OFF_N}
C {lab_wire.sym} 370 -300 0 0 {name=p6 lab=EN_N}
C {lab_wire.sym} 370 -340 0 0 {name=p7 lab=EN_P}
C {title.sym} 160 0 0 0 {name=l1 author="Christoph Maier"}
