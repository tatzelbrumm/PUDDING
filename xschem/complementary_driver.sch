v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 220 -340 240 -340 {lab=OUT_N}
N 70 -520 460 -520 {lab=VDD}
N 220 -340 220 -300 {lab=OUT_N}
N 80 -120 460 -120 {lab=VSS}
N 80 -340 120 -340 {lab=IN}
N 200 -340 220 -340 {lab=OUT_N}
N 220 -300 470 -300 {lab=OUT_N}
N 320 -340 470 -340 {lab=OUT}
C {sg13g2_stdcells/sg13g2_inv_1.sym} 160 -340 2 1 {name=x0 VDD=VDD VSS=VSS prefix=sg13g2_ }
C {sg13g2_stdcells/sg13g2_inv_1.sym} 280 -340 2 1 {name=x1 VDD=VDD VSS=VSS prefix=sg13g2_ }
C {iopin.sym} 80 -120 2 0 {name=p1 lab=VSS}
C {iopin.sym} 70 -520 2 0 {name=p2 lab=VDD}
C {ipin.sym} 80 -340 0 0 {name=p3 lab=IN}
C {opin.sym} 470 -340 0 0 {name=p4 lab=OUT}
C {opin.sym} 470 -300 0 0 {name=p5 lab=OUT_N}
C {title.sym} 160 0 0 0 {name=l1 author="Christoph Maier"}
