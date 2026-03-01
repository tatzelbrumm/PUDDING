v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 620 -780 620 -740 {lab=VDD}
N 680 -700 700 -700 {lab=Vpbias[0]}
N 540 -400 720 -400 {lab=Vpcbias[0]}
N 540 -430 540 -400 {lab=Vpcbias[0]}
N 720 -460 720 -400 {lab=Vpcbias[0]}
N 580 -460 720 -460 {lab=Vpcbias[0]}
N 680 -680 720 -680 {lab=Vpcbias[0]}
N 720 -680 720 -460 {lab=Vpcbias[0]}
N 520 -780 620 -780 {lab=VDD}
N 540 -660 560 -660 {lab=Vpbias[0]}
N 620 -780 1100 -780 {lab=VDD}
N 620 -60 1100 -60 {lab=VSS}
N 1100 -780 1100 -740 {lab=VDD}
N 540 -540 540 -490 {lab=Vpbias[0]}
N 520 -460 540 -460 {lab=VDD}
N 520 -780 520 -460 {lab=VDD}
N 1000 -620 1040 -620 {lab=ONB[63:0]}
N 420 -60 620 -60 {lab=VSS}
N 720 -680 1040 -680 {lab=Vpcbias[0]}
N 700 -700 1040 -700 {lab=Vpbias[0]}
N 420 -780 520 -780 {lab=VDD}
N 680 -640 760 -640 {lab=EN[1:0]}
N 680 -620 740 -620 {lab=ENB[1:0]}
N 1780 -780 1780 -740 {lab=VDD}
N 1700 -700 1720 -700 {lab=Vpbias[1]}
N 1680 -400 1860 -400 {lab=Vpcbias[1]}
N 1860 -430 1860 -400 {lab=Vpcbias[1]}
N 1680 -460 1680 -400 {lab=Vpcbias[1]}
N 1680 -460 1820 -460 {lab=Vpcbias[1]}
N 1680 -680 1720 -680 {lab=Vpcbias[1]}
N 1680 -680 1680 -460 {lab=Vpcbias[1]}
N 1780 -780 1880 -780 {lab=VDD}
N 1840 -660 1860 -660 {lab=Vpbias[1]}
N 1300 -780 1780 -780 {lab=VDD}
N 1300 -780 1300 -740 {lab=VDD}
N 1780 -580 1780 -60 {lab=VSS}
N 1860 -540 1860 -490 {lab=Vpbias[1]}
N 1860 -460 1880 -460 {lab=VDD}
N 1880 -780 1880 -460 {lab=VDD}
N 1360 -640 1420 -640 {lab=ON[127:64]}
N 1360 -620 1400 -620 {lab=ONB[127:64]}
N 1360 -680 1680 -680 {lab=Vpcbias[1]}
N 1360 -700 1700 -700 {lab=Vpbias[1]}
N 1660 -620 1720 -620 {lab=ENB[3:2]}
N 1100 -60 1300 -60 {lab=VSS}
N 1100 -780 1300 -780 {lab=VDD}
N 1200 -660 1240 -660 {lab=Iout}
N 1200 -660 1200 -560 {lab=Iout}
N 1160 -660 1200 -660 {lab=Iout}
N 420 -340 1700 -340 {lab=Vpbias[1:0]}
N 620 -580 620 -60 {lab=VSS}
N 1100 -580 1100 -60 {lab=VSS}
N 1300 -580 1300 -60 {lab=VSS}
N 1700 -540 1860 -540 {lab=Vpbias[1]}
N 1700 -700 1700 -540 {lab=Vpbias[1]}
N 1860 -660 1860 -540 {lab=Vpbias[1]}
N 540 -540 700 -540 {lab=Vpbias[0]}
N 540 -660 540 -540 {lab=Vpbias[0]}
N 700 -700 700 -540 {lab=Vpbias[0]}
N 1300 -60 1780 -60 {lab=VSS}
N 420 -300 1860 -300 {lab=Vpcbias[1:0]}
N 1640 -640 1720 -640 {lab=EN[3:2]}
N 420 -100 1400 -100 {lab=ONB[127:0]}
N 980 -640 1040 -640 {lab=ON[63:0]}
N 420 -140 1420 -140 {lab=ON[127:0]}
N 420 -220 1660 -220 {lab=ENB[3:0]}
N 420 -260 1640 -260 {lab=EN[3:0]}
N 1660 -620 1660 -230 {lab=ENB[3:2]}
N 1640 -640 1640 -270 {lab=EN[3:2]}
N 1400 -620 1400 -110 {lab=ONB[127:64]}
N 1420 -640 1420 -150 {lab=ON[127:64]}
N 1000 -620 1000 -110 {lab=ONB[63:0]}
N 980 -640 980 -150 {lab=ON[63:0]}
N 740 -620 740 -230 {lab=ENB[1:0]}
N 760 -640 760 -270 {lab=EN[1:0]}
N 700 -540 700 -350 {lab=Vpbias[0]}
N 720 -400 720 -310 {lab=Vpcbias[0]}
N 1860 -400 1860 -310 {lab=Vpcbias[1]}
N 1700 -540 1700 -350 {lab=Vpbias[1]}
C {title.sym} 160 0 0 0 {name=l1 author="Christoph Maier"}
C {sg13g2_pr/sg13_lv_pmos.sym} 560 -460 0 1 {name=Mcbias[0]
l=0.15u
w=5.85u
ng=1
m=2
model=sg13_lv_pmos
spiceprefix=X
}
C {opin.sym} 1200 -560 1 0 {name=p4 lab=Iout}
C {devices/code_shown.sym} 60 -730 0 0 {name=params only_toplevel=false value="* device parameters
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
C {unitsource2u.sym} 620 -660 0 1 {name=xref[1:0]}
C {unitsource2u.sym} 1100 -660 0 0 {name=xsrc[63:0]}
C {ipin.sym} 420 -140 0 0 {name=p7 sig_type=std_logic lab=ON[127:0]}
C {ipin.sym} 420 -100 0 0 {name=p8 sig_type=std_logic lab=ONB[127:0]}
C {iopin.sym} 420 -60 0 1 {name=p2 lab=VSS}
C {iopin.sym} 420 -780 0 1 {name=p1 lab=VDD}
C {iopin.sym} 420 -300 0 1 {name=p5 lab=Vpcbias[1:0]}
C {sg13g2_pr/sg13_lv_pmos.sym} 1840 -460 0 0 {name=Mcbias[1]
l=0.15u
w=5.85u
ng=1
m=2
model=sg13_lv_pmos
spiceprefix=X
}
C {unitsource2u.sym} 1780 -660 0 0 {name=xref1[3:2]}
C {unitsource2u.sym} 1300 -660 0 1 {name=xsrc1[127:64]}
C {ipin.sym} 420 -260 0 0 {name=p14 sig_type=std_logic lab=EN[3:0]}
C {ipin.sym} 420 -220 0 0 {name=p15 sig_type=std_logic lab=ENB[3:0]}
C {iopin.sym} 420 -340 0 1 {name=p17 lab=Vpbias[1:0]}
C {lab_wire.sym} 440 -340 0 1 {name=p18 lab=Vpbias[1:0]}
C {lab_wire.sym} 440 -300 0 1 {name=p16 lab=Vpcbias[1:0]}
C {lab_wire.sym} 440 -260 0 1 {name=p26 lab=EN[3:0]}
C {lab_wire.sym} 440 -220 0 1 {name=p27 lab=ENB[3:0]}
C {lab_wire.sym} 440 -140 0 1 {name=p28 lab=ON[127:0]}
C {lab_wire.sym} 440 -100 0 1 {name=p29 lab=ONB[127:0]}
C {bus_tap.sym} 750 -260 0 0 {name=l2 lab=[1:0]}
C {bus_tap.sym} 730 -220 0 0 {name=l3 lab=[1:0]}
C {bus_tap.sym} 1650 -220 0 0 {name=l4 lab=[3:2]}
C {bus_tap.sym} 1630 -260 0 0 {name=l5 lab=[3:2]}
C {bus_tap.sym} 970 -140 0 0 {name=l6 lab=[63:0]}
C {bus_tap.sym} 990 -100 0 0 {name=l7 lab=[63:0]}
C {bus_tap.sym} 1410 -140 0 0 {name=l8 lab=[127:64]}
C {bus_tap.sym} 1390 -100 0 0 {name=l9 lab=[127:64]}
C {bus_tap.sym} 690 -340 0 0 {name=l10 lab=[0]}
C {bus_tap.sym} 710 -300 0 0 {name=l11 lab=[0]}
C {bus_tap.sym} 1690 -340 0 0 {name=l12 lab=[1]}
C {bus_tap.sym} 1850 -300 0 0 {name=l13 lab=[1]}
