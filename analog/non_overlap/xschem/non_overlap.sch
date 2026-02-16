v {xschem version=3.4.8RC file_version=1.2}
G {}
K {}
V {}
S {}
F {}
E {}
N -100 -170 -70 -170 {lab=#net1}
N 270 -170 300 -170 {lab=#net2}
N 170 -170 190 -170 {lab=#net3}
N 40 -170 70 -170 {lab=#net4}
N -100 160 -70 160 {lab=#net5}
N 270 160 300 160 {lab=#net6}
N 170 160 190 160 {lab=#net7}
N 40 160 70 160 {lab=#net8}
N 170 -170 170 -80 {lab=#net3}
N 150 -170 170 -170 {lab=#net3}
N 170 70 170 160 {lab=#net7}
N 150 160 170 160 {lab=#net7}
N -250 40 -250 140 {lab=#net3}
N -250 140 -220 140 {lab=#net3}
N -250 -150 -250 -50 {lab=#net7}
N -250 -150 -220 -150 {lab=#net7}
N -330 -190 -220 -190 {lab=thermo}
N -330 -190 -330 -50 {lab=thermo}
N -410 -190 -330 -190 {lab=thermo}
N -330 180 -220 180 {lab=#net9}
N -330 30 -330 180 {lab=#net9}
N 380 -170 460 -170 {lab=ON_N}
N 380 160 460 160 {lab=ON}
N -470 150 -420 150 {lab=VSS}
N -470 120 -420 120 {lab=VDD}
N -250 40 170 -80 {lab=#net3}
N -250 -50 170 70 {lab=#net7}
N 40 -100 40 -70 {lab=VSS}
N 40 -170 40 -160 {lab=#net4}
N 10 -170 40 -170 {lab=#net4}
N 40 230 40 260 {lab=VSS}
N 40 160 40 170 {lab=#net8}
N 10 160 40 160 {lab=#net8}
C {sg13g2_stdcells/sg13g2_inv_1.sym} -30 -170 0 0 {name=x1 VDD=VDD VSS=VSS prefix=sg13g2_ }
C {sg13g2_stdcells/sg13g2_nor2_1.sym} -160 -170 0 0 {name=x2 VDD=VDD VSS=VSS prefix=sg13g2_ }
C {sg13g2_stdcells/sg13g2_inv_1.sym} 110 -170 0 0 {name=x4 VDD=VDD VSS=VSS prefix=sg13g2_ }
C {sg13g2_stdcells/sg13g2_inv_1.sym} 230 -170 0 0 {name=x5 VDD=VDD VSS=VSS prefix=sg13g2_ }
C {sg13g2_stdcells/sg13g2_inv_1.sym} 340 -170 0 0 {name=x6 VDD=VDD VSS=VSS prefix=sg13g2_ }
C {iopin.sym} -470 150 2 0 {name=p1 lab=VSS}
C {sg13g2_stdcells/sg13g2_inv_1.sym} -30 160 0 0 {name=x7 VDD=VDD VSS=VSS prefix=sg13g2_ }
C {sg13g2_stdcells/sg13g2_nor2_1.sym} -160 160 0 0 {name=x8 VDD=VDD VSS=VSS prefix=sg13g2_ }
C {sg13g2_stdcells/sg13g2_inv_1.sym} 110 160 0 0 {name=x10 VDD=VDD VSS=VSS prefix=sg13g2_ }
C {sg13g2_stdcells/sg13g2_inv_1.sym} 230 160 0 0 {name=x11 VDD=VDD VSS=VSS prefix=sg13g2_ }
C {sg13g2_stdcells/sg13g2_inv_1.sym} 340 160 0 0 {name=x12 VDD=VDD VSS=VSS prefix=sg13g2_ }
C {sg13g2_stdcells/sg13g2_inv_1.sym} -330 -10 1 0 {name=x13 VDD=VDD VSS=VSS prefix=sg13g2_ }
C {ipin.sym} -410 -190 0 0 {name=p3 lab=thermo}
C {opin.sym} 460 160 0 0 {name=p4 lab=ON}
C {opin.sym} 460 -170 0 0 {name=p5 lab=ON_N}
C {iopin.sym} -470 120 2 0 {name=p2 lab=VDD}
C {title.sym} -390 350 0 0 {name=l1 author="Luis Ardila"}
C {lab_wire.sym} -420 150 0 0 {name=p8 sig_type=std_logic lab=VSS}
C {lab_wire.sym} -420 120 0 0 {name=p9 sig_type=std_logic lab=VDD}
C {capa.sym} 40 -130 0 0 {name=C1
m=1
value=1p
footprint=1206
device="ceramic capacitor"}
C {lab_wire.sym} 40 -70 0 0 {name=p6 sig_type=std_logic lab=VSS}
C {capa.sym} 40 200 0 0 {name=C2
m=1
value=1p
footprint=1206
device="ceramic capacitor"}
C {lab_wire.sym} 40 260 0 0 {name=p7 sig_type=std_logic lab=VSS}
