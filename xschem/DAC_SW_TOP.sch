v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 120 -10 220 -10 {lab=SW_OUT[255:0]}
N -260 10 -180 10 {lab=VDD}
N -260 -30 -180 -30 {lab=PCASCODE}
N -260 -70 -180 -70 {lab=IN[255:0]}
N -260 -90 -180 -90 {lab=IN[255:0]}
C {DAC_SW.sym} -30 -10 0 0 {name=XSW[255:0]}
C {opin.sym} 220 -10 0 0 {name=p1 lab=SW_OUT[255:0]}
C {ipin.sym} -260 -70 0 0 {name=p2 lab=IN[255:0]}
C {ipin.sym} -260 -30 0 0 {name=p3 lab=PCASCODE}
C {ipin.sym} -260 10 0 0 {name=p4 lab=VDD}
C {ipin.sym} -260 -90 0 0 {name=p6 lab=IN_N[255:0]}
