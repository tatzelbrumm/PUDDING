v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 620 -580 620 -540 {lab=VDD}
N 700 -500 700 -320 {lab=Vpbias}
N 680 -500 700 -500 {lab=Vpbias}
N 540 -180 720 -180 {lab=Vpcbias}
N 540 -210 540 -180 {lab=Vpcbias}
N 720 -240 720 -180 {lab=Vpcbias}
N 580 -240 720 -240 {lab=Vpcbias}
N 680 -480 720 -480 {lab=Vpcbias}
N 720 -480 720 -240 {lab=Vpcbias}
N 520 -580 620 -580 {lab=VDD}
N 540 -460 560 -460 {lab=Vpbias}
N 540 -320 540 -270 {lab=Vpbias}
N 620 -580 1100 -580 {lab=VDD}
N 620 -140 1100 -140 {lab=VSS}
N 1100 -580 1100 -540 {lab=VDD}
N 1100 -380 1100 -140 {lab=VSS}
N 620 -380 620 -140 {lab=VSS}
N 540 -320 700 -320 {lab=Vpbias}
N 540 -460 540 -320 {lab=Vpbias}
N 520 -240 540 -240 {lab=VDD}
N 520 -580 520 -240 {lab=VDD}
N 1000 -440 1040 -440 {lab=ON[63:0]}
N 1000 -420 1040 -420 {lab=ONB[63:0]}
N 420 -140 620 -140 {lab=VSS}
N 720 -480 1040 -480 {lab=Vpcbias}
N 700 -500 1040 -500 {lab=Vpbias}
N 1160 -460 1220 -460 {lab=Iout}
N 420 -580 520 -580 {lab=VDD}
N 420 -180 540 -180 {lab=Vpcbias}
N 680 -440 800 -440 {lab=EN[1:0]}
N 680 -420 800 -420 {lab=ENB[1:0]}
C {title.sym} 160 0 0 0 {name=l1 author="Christoph Maier"}
C {lab_wire.sym} 800 -500 0 0 {name=p20 lab=Vpbias}
C {sg13g2_pr/sg13_lv_pmos.sym} 560 -240 0 1 {name=Mcbias
l=0.15u
w=5.85u
ng=1
m=2
model=sg13_lv_pmos
spiceprefix=X
}
C {lab_wire.sym} 900 -480 0 0 {name=p3 lab=Vpcbias}
C {opin.sym} 1220 -460 0 0 {name=p4 lab=Iout}
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
C {iopin.sym} 420 -180 0 1 {name=p5 lab=Vpcbias}
C {ipin.sym} 800 -440 0 1 {name=p6 sig_type=std_logic lab=EN[1:0]}
C {ipin.sym} 800 -420 0 1 {name=p9 sig_type=std_logic lab=ENB[1:0]}
