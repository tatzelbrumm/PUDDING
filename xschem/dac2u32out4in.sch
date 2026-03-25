v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 340 -580 340 -540 {lab=VDD}
N 420 -500 420 -320 {lab=Vpbias[0]}
N 400 -500 420 -500 {lab=Vpbias[0]}
N 260 -180 440 -180 {lab=Vpcbias[0]}
N 260 -210 260 -180 {lab=Vpcbias[0]}
N 440 -240 440 -180 {lab=Vpcbias[0]}
N 300 -240 440 -240 {lab=Vpcbias[0]}
N 400 -480 440 -480 {lab=Vpcbias[0]}
N 440 -480 440 -240 {lab=Vpcbias[0]}
N 240 -580 340 -580 {lab=VDD}
N 260 -460 280 -460 {lab=Vpbias[0]}
N 260 -320 260 -270 {lab=Vpbias[0]}
N 340 -580 820 -580 {lab=VDD}
N 340 -140 820 -140 {lab=VSS}
N 820 -580 820 -540 {lab=VDD}
N 820 -380 820 -140 {lab=VSS}
N 340 -380 340 -140 {lab=VSS}
N 260 -320 420 -320 {lab=Vpbias[0]}
N 260 -460 260 -320 {lab=Vpbias[0]}
N 240 -240 260 -240 {lab=VDD}
N 240 -580 240 -240 {lab=VDD}
N 720 -440 760 -440 {lab=ON[15:0]}
N 720 -420 760 -420 {lab=ONB[15:0]}
N 140 -140 340 -140 {lab=VSS}
N 440 -480 760 -480 {lab=Vpcbias[0]}
N 420 -500 760 -500 {lab=Vpbias[0]}
N 140 -580 240 -580 {lab=VDD}
N 400 -440 460 -440 {lab=EN[1:0]}
N 400 -420 460 -420 {lab=ENB[1:0]}
N 1500 -580 1500 -540 {lab=VDD}
N 1420 -500 1420 -320 {lab=Vpbias[1]}
N 1420 -500 1440 -500 {lab=Vpbias[1]}
N 1400 -180 1580 -180 {lab=Vpcbias[1]}
N 1580 -210 1580 -180 {lab=Vpcbias[1]}
N 1400 -240 1400 -180 {lab=Vpcbias[1]}
N 1400 -240 1540 -240 {lab=Vpcbias[1]}
N 1400 -480 1440 -480 {lab=Vpcbias[1]}
N 1400 -480 1400 -240 {lab=Vpcbias[1]}
N 1500 -580 1600 -580 {lab=VDD}
N 1560 -460 1580 -460 {lab=Vpbias[1]}
N 1580 -320 1580 -270 {lab=Vpbias[1]}
N 1020 -580 1500 -580 {lab=VDD}
N 1020 -140 1500 -140 {lab=VSS}
N 1020 -580 1020 -540 {lab=VDD}
N 1020 -380 1020 -140 {lab=VSS}
N 1500 -380 1500 -140 {lab=VSS}
N 1420 -320 1580 -320 {lab=Vpbias[1]}
N 1580 -460 1580 -320 {lab=Vpbias[1]}
N 1580 -240 1600 -240 {lab=VDD}
N 1600 -580 1600 -240 {lab=VDD}
N 1080 -440 1120 -440 {lab=ON[31:16]}
N 1080 -420 1120 -420 {lab=ONB[31:16]}
N 1080 -480 1400 -480 {lab=Vpcbias[1]}
N 1080 -500 1420 -500 {lab=Vpbias[1]}
N 1380 -440 1440 -440 {lab=EN[3:2]}
N 1380 -420 1440 -420 {lab=ENB[3:2]}
N 820 -140 1020 -140 {lab=VSS}
N 820 -580 1020 -580 {lab=VDD}
N 920 -460 960 -460 {lab=Iout}
N 920 -460 920 -340 {lab=Iout}
N 880 -460 920 -460 {lab=Iout}
N 140 -180 220 -180 {lab=Vpcbias[1:0]}
N 140 -300 220 -300 {lab=Vpbias[1:0]}
C {title.sym} 160 0 0 0 {name=l1 author="Christoph Maier"}
C {lab_wire.sym} 520 -500 0 0 {name=p20 lab=Vpbias[0]}
C {sg13g2_pr/sg13_lv_pmos.sym} 280 -240 0 1 {name=Mcbias[0]
l=0.15u
w=5.85u
ng=1
m=2
model=sg13_lv_pmos
spiceprefix=X
}
C {lab_wire.sym} 620 -480 0 0 {name=p3 lab=Vpcbias[0]}
C {iopin.sym} 920 -340 1 0 {name=p4 lab=Iout}
C {unitsource2u.sym} 340 -460 0 1 {name=xref[1:0]}
C {unitsource2u.sym} 820 -460 0 0 {name=xsrc[15:0]}
C {ipin.sym} 720 -440 0 0 {name=p7 sig_type=std_logic lab=ON[15:0]}
C {ipin.sym} 720 -420 0 0 {name=p8 sig_type=std_logic lab=ONB[15:0]}
C {iopin.sym} 140 -140 0 1 {name=p2 lab=VSS}
C {iopin.sym} 140 -580 0 1 {name=p1 lab=VDD}
C {iopin.sym} 140 -180 0 1 {name=p5 lab=Vpcbias[1:0]}
C {ipin.sym} 460 -440 0 1 {name=p6 sig_type=std_logic lab=EN[1:0]}
C {ipin.sym} 460 -420 0 1 {name=p9 sig_type=std_logic lab=ENB[1:0]}
C {lab_wire.sym} 1320 -500 0 1 {name=p10 lab=Vpbias[1]}
C {sg13g2_pr/sg13_lv_pmos.sym} 1560 -240 0 0 {name=Mcbias[1]
l=0.15u
w=5.85u
ng=1
m=2
model=sg13_lv_pmos
spiceprefix=X
}
C {lab_wire.sym} 1220 -480 0 1 {name=p11 lab=Vpcbias[1]}
C {unitsource2u.sym} 1500 -460 0 0 {name=xref[3:2]}
C {unitsource2u.sym} 1020 -460 0 1 {name=xsrc[31:16]}
C {ipin.sym} 1120 -440 0 1 {name=p12 sig_type=std_logic lab=ON[31:16]}
C {ipin.sym} 1120 -420 0 1 {name=p13 sig_type=std_logic lab=ONB[31:16]}
C {ipin.sym} 1380 -440 0 0 {name=p14 sig_type=std_logic lab=EN[3:2]}
C {ipin.sym} 1380 -420 0 0 {name=p15 sig_type=std_logic lab=ENB[3:2]}
C {iopin.sym} 140 -300 0 1 {name=p17 lab=Vpbias[1:0]}
C {lab_wire.sym} 150 -180 0 1 {name=p16 lab=Vpcbias[1:0]}
C {lab_wire.sym} 150 -300 0 1 {name=p18 lab=Vpbias[1:0]}
