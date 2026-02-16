v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 220 -340 240 -340 {lab=EN_N}
N 420 -120 620 -120 {lab=VSS}
N 620 -520 620 -490 {lab=VDD}
N 600 -520 620 -520 {lab=VDD}
N 420 -520 420 -490 {lab=VDD}
N 70 -520 420 -520 {lab=VDD}
N 600 -460 620 -460 {lab=VDD}
N 600 -520 600 -460 {lab=VDD}
N 440 -520 600 -520 {lab=VDD}
N 420 -460 440 -460 {lab=VDD}
N 440 -520 440 -460 {lab=VDD}
N 420 -520 440 -520 {lab=VDD}
N 220 -460 220 -340 {lab=EN_N}
N 220 -460 380 -460 {lab=EN_N}
N 660 -460 680 -460 {lab=EN_B}
N 340 -400 680 -400 {lab=EN_B}
N 340 -400 340 -340 {lab=EN_B}
N 680 -460 680 -400 {lab=EN_B}
N 320 -340 340 -340 {lab=EN_B}
N 620 -150 620 -120 {lab=VSS}
N 620 -180 640 -180 {lab=VSS}
N 640 -180 640 -120 {lab=VSS}
N 620 -120 640 -120 {lab=VSS}
N 400 -180 420 -180 {lab=VSS}
N 400 -180 400 -120 {lab=VSS}
N 80 -120 400 -120 {lab=VSS}
N 420 -150 420 -120 {lab=VSS}
N 400 -120 420 -120 {lab=VSS}
N 420 -260 420 -210 {lab=ON_N}
N 620 -260 620 -210 {lab=OFF_N}
N 420 -360 740 -360 {lab=ON_N}
N 420 -430 420 -360 {lab=ON_N}
N 620 -320 740 -320 {lab=OFF_N}
N 620 -430 620 -320 {lab=OFF_N}
N 460 -180 480 -180 {lab=OFF_N}
N 480 -180 560 -260 {lab=OFF_N}
N 560 -260 620 -260 {lab=OFF_N}
N 620 -320 620 -260 {lab=OFF_N}
N 560 -180 580 -180 {lab=ON_N}
N 480 -260 560 -180 {lab=ON_N}
N 420 -260 480 -260 {lab=ON_N}
N 420 -360 420 -260 {lab=ON_N}
N 80 -340 120 -340 {lab=EN}
N 200 -340 220 -340 {lab=EN_N}
C {sg13g2_stdcells/sg13g2_inv_1.sym} 160 -340 2 1 {name=x0 VDD=VDD VSS=VSS prefix=sg13g2_ }
C {iopin.sym} 80 -120 2 0 {name=p1 lab=VSS}
C {ipin.sym} 80 -340 0 0 {name=p3 lab=EN}
C {opin.sym} 740 -360 0 0 {name=p4 lab=ON_N}
C {opin.sym} 740 -320 0 0 {name=p5 lab=OFF_N}
C {iopin.sym} 70 -520 2 0 {name=p2 lab=VDD}
C {title.sym} 160 0 0 0 {name=l1 author="Christoph Maier"}
C {lab_wire.sym} 220 -460 0 0 {name=p6 sig_type=std_logic lab=EN_N}
C {sg13g2_pr/sg13_lv_pmos.sym} 400 -460 0 0 {name=M1
l=\{lenp\}
w=\{wp\}
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
C {sg13g2_pr/sg13_lv_pmos.sym} 640 -460 0 1 {name=M2
l=\{lenp\}
w=\{wp\}
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 -180 0 1 {name=M3
l=\{lenn\}
w=\{wn\}
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
C {sg13g2_pr/sg13_lv_nmos.sym} 600 -180 0 0 {name=M4
l=\{lenn\}
w=\{wn\}
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
C {sg13g2_stdcells/sg13g2_inv_1.sym} 280 -340 2 1 {name=x1 VDD=VDD VSS=VSS prefix=sg13g2_ }
C {lab_wire.sym} 340 -400 0 0 {name=p7 sig_type=std_logic lab=EN_B}
