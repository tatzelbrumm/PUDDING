v {xschem version=3.4.8RC file_version=1.2}
G {}
K {}
V {}
S {}
F {}
E {}
N -210 -110 0 -110 {lab=VDD}
N 0 -110 0 -70 {lab=VDD}
N -210 110 0 110 {lab=VSS}
N 0 70 0 110 {lab=VSS}
N -210 0 -150 0 {lab=thermo[255:0]}
N 150 -20 280 -20 {lab=ON[255:0]}
N 150 20 280 20 {lab=ON_N[255:0]}
C {non_overlap.sym} 0 0 0 0 {name=noi_top[255:0]}
C {iopin.sym} -210 -110 2 0 {name=p1 lab=VDD}
C {iopin.sym} -210 110 2 0 {name=p2 lab=VSS}
C {ipin.sym} -210 0 0 0 {name=p3 lab=thermo[255:0]}
C {opin.sym} 280 -20 0 0 {name=p4 lab=ON[255:0]}
C {opin.sym} 280 20 0 0 {name=p5 lab=ON_N[255:0]}
