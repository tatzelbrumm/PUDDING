v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 620 -580 620 -540 {lab=VDD}
N 700 -500 700 -320 {lab=Vpbias[0]}
N 680 -500 700 -500 {lab=Vpbias[0]}
N 540 -180 720 -180 {lab=Vpcbias[0]}
N 540 -210 540 -180 {lab=Vpcbias[0]}
N 720 -240 720 -180 {lab=Vpcbias[0]}
N 580 -240 720 -240 {lab=Vpcbias[0]}
N 680 -480 720 -480 {lab=Vpcbias[0]}
N 720 -480 720 -240 {lab=Vpcbias[0]}
N 520 -580 620 -580 {lab=VDD}
N 540 -460 560 -460 {lab=Vpbias[0]}
N 540 -300 540 -270 {lab=Vpbias[0]}
N 620 -580 1100 -580 {lab=VDD}
N 620 -140 1100 -140 {lab=VSS}
N 1100 -580 1100 -540 {lab=VDD}
N 1100 -380 1100 -140 {lab=VSS}
N 620 -380 620 -140 {lab=VSS}
N 540 -320 700 -320 {lab=Vpbias[0]}
N 540 -460 540 -320 {lab=Vpbias[0]}
N 520 -240 540 -240 {lab=VDD}
N 520 -580 520 -240 {lab=VDD}
N 1000 -440 1040 -440 {lab=ON[63:0]}
N 1000 -420 1040 -420 {lab=ONB[63:0]}
N 420 -140 620 -140 {lab=VSS}
N 720 -480 1040 -480 {lab=Vpcbias[0]}
N 700 -500 1040 -500 {lab=Vpbias[0]}
N 420 -580 520 -580 {lab=VDD}
N 420 -180 540 -180 {lab=Vpcbias[0]}
N 680 -440 740 -440 {lab=EN[1:0]}
N 680 -420 740 -420 {lab=ENB[1:0]}
N 1780 -580 1780 -540 {lab=VDD}
N 1700 -500 1700 -320 {lab=Vpbias[1]}
N 1700 -500 1720 -500 {lab=Vpbias[1]}
N 1680 -180 1860 -180 {lab=Vpcbias[1]}
N 1860 -210 1860 -180 {lab=Vpcbias[1]}
N 1680 -240 1680 -180 {lab=Vpcbias[1]}
N 1680 -240 1820 -240 {lab=Vpcbias[1]}
N 1680 -480 1720 -480 {lab=Vpcbias[1]}
N 1680 -480 1680 -240 {lab=Vpcbias[1]}
N 1780 -580 1880 -580 {lab=VDD}
N 1840 -460 1860 -460 {lab=Vpbias[1]}
N 1860 -320 1860 -270 {lab=Vpbias[1]}
N 1300 -580 1780 -580 {lab=VDD}
N 1300 -140 1780 -140 {lab=VSS}
N 1300 -580 1300 -540 {lab=VDD}
N 1300 -380 1300 -140 {lab=VSS}
N 1780 -380 1780 -140 {lab=VSS}
N 1700 -320 1860 -320 {lab=Vpbias[1]}
N 1860 -460 1860 -320 {lab=Vpbias[1]}
N 1860 -240 1880 -240 {lab=VDD}
N 1880 -580 1880 -240 {lab=VDD}
N 1360 -440 1400 -440 {lab=ON[127:64]}
N 1360 -420 1400 -420 {lab=ONB[127:64]}
N 1360 -480 1680 -480 {lab=Vpcbias[1]}
N 1360 -500 1700 -500 {lab=Vpbias[1]}
N 1660 -440 1720 -440 {lab=EN[3:2]}
N 1660 -420 1720 -420 {lab=ENB[3:2]}
N 1100 -140 1300 -140 {lab=VSS}
N 1100 -580 1300 -580 {lab=VDD}
N 1200 -460 1240 -460 {lab=Iout}
N 1200 -460 1200 -340 {lab=Iout}
N 1160 -460 1200 -460 {lab=Iout}
N 1560 -180 1680 -180 {lab=Vpcbias[1]}
N 420 -300 540 -300 {lab=Vpbias[0]}
N 540 -320 540 -300 {lab=Vpbias[0]}
N 1560 -320 1700 -320 {lab=Vpbias[1]}
C {title.sym} 160 0 0 0 {name=l1 author="Christoph Maier"}
C {lab_wire.sym} 800 -500 0 0 {name=p20 lab=Vpbias[0]}
C {sg13g2_pr/sg13_lv_pmos.sym} 560 -240 0 1 {name=Mcbias[0]
l=0.15u
w=5.85u
ng=1
m=2
model=sg13_lv_pmos
spiceprefix=X
}
C {lab_wire.sym} 900 -480 0 0 {name=p3 lab=Vpcbias[0]}
C {opin.sym} 1200 -340 1 0 {name=p4 lab=Iout}
C {devices/code_shown.sym} 60 -650 0 0 {name=params only_toplevel=false value="* device parameters
.param l      = 5u
.param w      = 1.45u
.param lc     = 0.6u
.param wc     = 1.2u
.param lb     = 0.15u
.param wb     = 5.85u
.param lplogic= 0.13u
.param wplogic= 0.5u
.param lnlogic= 0.13u
.param wnlogic= 0.15u
"}
C {unitsource2u.sym} 620 -460 0 1 {name=xref[1:0]}
C {unitsource2u.sym} 1100 -460 0 0 {name=xsrc[63:0]}
C {ipin.sym} 1000 -440 0 0 {name=p7 sig_type=std_logic lab=ON[63:0]}
C {ipin.sym} 1000 -420 0 0 {name=p8 sig_type=std_logic lab=ONB[63:0]}
C {iopin.sym} 420 -140 0 1 {name=p2 lab=VSS}
C {iopin.sym} 420 -580 0 1 {name=p1 lab=VDD}
C {iopin.sym} 420 -180 0 1 {name=p5 lab=Vpcbias[0]}
C {ipin.sym} 740 -440 0 1 {name=p6 sig_type=std_logic lab=EN[1:0]}
C {ipin.sym} 740 -420 0 1 {name=p9 sig_type=std_logic lab=ENB[1:0]}
C {lab_wire.sym} 1600 -500 0 1 {name=p10 lab=Vpbias[1]}
C {sg13g2_pr/sg13_lv_pmos.sym} 1840 -240 0 0 {name=Mcbias[1]
l=0.15u
w=5.85u
ng=1
m=2
model=sg13_lv_pmos
spiceprefix=X
}
C {lab_wire.sym} 1500 -480 0 1 {name=p11 lab=Vpcbias[1]}
C {unitsource2u.sym} 1780 -460 0 0 {name=xref1[3:2]}
C {unitsource2u.sym} 1300 -460 0 1 {name=xsrc1[127:64]}
C {ipin.sym} 1400 -440 0 1 {name=p12 sig_type=std_logic lab=ON[127:64]}
C {ipin.sym} 1400 -420 0 1 {name=p13 sig_type=std_logic lab=ONB[127:64]}
C {ipin.sym} 1660 -440 0 0 {name=p14 sig_type=std_logic lab=EN[3:2]}
C {ipin.sym} 1660 -420 0 0 {name=p15 sig_type=std_logic lab=ENB[3:2]}
C {iopin.sym} 1560 -180 0 1 {name=p16 lab=Vpcbias[1]}
C {iopin.sym} 420 -300 0 1 {name=p17 lab=Vpbias[0]}
C {iopin.sym} 1560 -320 0 1 {name=p18 lab=Vpbias[1]}
