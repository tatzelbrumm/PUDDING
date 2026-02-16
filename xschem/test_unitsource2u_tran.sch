v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 1160 -160 1160 -140 {lab=GND}
N 620 -780 620 -660 {lab=VDD}
N 700 -620 700 -440 {lab=Vpbias}
N 680 -620 700 -620 {lab=Vpbias}
N 1340 -220 1340 -100 {lab=VSS}
N 540 -220 540 -180 {lab=#net1}
N 540 -120 540 -100 {lab=VSS}
N 460 -120 460 -100 {lab=VSS}
N 460 -200 460 -180 {lab=logI}
N 1100 -620 1140 -620 {lab=Vpbleak}
N 540 -300 540 -280 {lab=Vpcbias}
N 540 -300 720 -300 {lab=Vpcbias}
N 540 -330 540 -300 {lab=Vpcbias}
N 720 -360 720 -300 {lab=Vpcbias}
N 580 -360 720 -360 {lab=Vpcbias}
N 680 -600 720 -600 {lab=Vpcbias}
N 420 -220 420 -100 {lab=VSS}
N 420 -360 420 -280 {lab=VDD}
N 900 -220 900 -100 {lab=VSS}
N 900 -300 900 -280 {lab=switch}
N 1000 -780 1200 -780 {lab=VDD}
N 720 -600 720 -360 {lab=Vpcbias}
N 920 -780 920 -740 {lab=VDD}
N 880 -780 920 -780 {lab=VDD}
N 950 -740 960 -740 {lab=VDD}
N 960 -780 960 -740 {lab=VDD}
N 920 -780 960 -780 {lab=VDD}
N 880 -740 890 -740 {lab=VDD}
N 880 -780 880 -740 {lab=VDD}
N 860 -780 880 -780 {lab=VDD}
N 820 -780 820 -740 {lab=VDD}
N 780 -780 820 -780 {lab=VDD}
N 850 -740 860 -740 {lab=VDD}
N 860 -780 860 -740 {lab=VDD}
N 820 -780 860 -780 {lab=VDD}
N 780 -740 790 -740 {lab=VDD}
N 780 -780 780 -740 {lab=VDD}
N 820 -620 1040 -620 {lab=Vpbias}
N 420 -780 620 -780 {lab=VDD}
N 540 -580 560 -580 {lab=Vpbias}
N 540 -440 540 -390 {lab=Vpbias}
N 740 -780 780 -780 {lab=VDD}
N 1080 -600 1140 -600 {lab=Vpcleak}
N 920 -600 1020 -600 {lab=Vpcbias}
N 1300 -580 1340 -580 {lab=Vout}
N 1340 -580 1340 -280 {lab=Vout}
N 1300 -100 1340 -100 {lab=VSS}
N 680 -560 740 -560 {lab=VDD}
N 740 -780 740 -560 {lab=VDD}
N 620 -780 740 -780 {lab=VDD}
N 680 -540 740 -540 {lab=VSS}
N 740 -540 740 -100 {lab=VSS}
N 620 -100 740 -100 {lab=VSS}
N 1200 -680 1200 -660 {lab=sw_p}
N 1200 -780 1200 -740 {lab=VDD}
N 1200 -500 1200 -480 {lab=sw_n}
N 1200 -240 1200 -100 {lab=VSS}
N 1000 -100 1200 -100 {lab=VSS}
N 1300 -580 1300 -280 {lab=Vout}
N 1260 -580 1300 -580 {lab=Vout}
N 1300 -220 1300 -100 {lab=VSS}
N 1200 -100 1300 -100 {lab=VSS}
N 1160 -240 1160 -220 {lab=VSS}
N 1160 -240 1200 -240 {lab=VSS}
N 1200 -420 1200 -240 {lab=VSS}
N 460 -100 540 -100 {lab=VSS}
N 620 -500 620 -100 {lab=VSS}
N 540 -100 620 -100 {lab=VSS}
N 540 -440 700 -440 {lab=Vpbias}
N 540 -580 540 -440 {lab=Vpbias}
N 420 -360 540 -360 {lab=VDD}
N 420 -780 420 -360 {lab=VDD}
N 1100 -560 1140 -560 {lab=on[63:0]}
N 1100 -560 1100 -520 {lab=on[63:0]}
N 1120 -540 1140 -540 {lab=on_n[63:0]}
N 1120 -540 1120 -480 {lab=on_n[63:0]}
N 1060 -480 1120 -480 {lab=on_n[63:0]}
N 1060 -520 1100 -520 {lab=on[63:0]}
N 1000 -780 1000 -560 {lab=VDD}
N 960 -780 1000 -780 {lab=VDD}
N 420 -100 460 -100 {lab=VSS}
N 1000 -440 1000 -100 {lab=VSS}
N 900 -100 1000 -100 {lab=VSS}
N 920 -700 920 -600 {lab=Vpcbias}
N 820 -700 820 -620 {lab=Vpbias}
N 740 -100 900 -100 {lab=VSS}
N 780 -500 940 -500 {lab=(63*VDD,switch)}
N 720 -600 920 -600 {lab=Vpcbias}
N 700 -620 820 -620 {lab=Vpbias}
C {title.sym} 160 0 0 0 {name=l1 author="Christoph Maier"}
C {vsource.sym} 1340 -250 0 0 {name=Vout value=\{vdd-vout\} savecurrent=true}
C {gnd.sym} 1160 -140 0 0 {name=l2 lab=GND}
C {devices/code_shown.sym} 1380 -730 0 0 {name=NGSPICE only_toplevel=true 
value="
.include test_unitsource2u_tran.save
.temp=27
.options gmin=1e-15 abstol=1p method=gear
*.options savecurrents
.control
save all 
op
write test_unitsource2u_tran.raw
set appendwrite
*dc Vout 0 1.6 10m VlogI -8 -6 0.5
tran 10p 200n
write test_switchedsources_tran.raw
plot title \\"voltages\\" vdd vpbias vpcbias switch \\"on_n[0]\\" \\"on[0]\\" vout 
plot title \\"switch voltages\\" switch \\"on[0]\\" \\"on_n[0]\\" \\"xsrc.on_n[0]\\" \\"xsrc.off_n[0]\\" \\"xsrc[0].vcasc\\" \\"xref[0].xsrc.drain\\" \\"xsrc[0].xsrc.drain\\"
*plot @n.xsw.xmbias.nsg13_lv_pmos[ids] @n.xsw.xmpullup.nsg13_lv_pmos[ids]
plot title \\"analog switch currents\\" viswp#branch-vout#branch viswn#branch
plot title \\"switch cross and difference currents\\" 0.5*(viswp#branch+viswn#branch-vout#branch) viswp#branch-viswn#branch-vout#branch
plot title \\"gate leakage currents\\" vpbleak#branch vpcleak#branch
plot title \\"output and reference currents\\" vout#branch vprobe#branch
plot title \\"output current accuracy\\" 2*(vout#branch/32-vprobe#branch)/(vprobe#branch+vout#branch/32)
plot title \\"output current accuracy\\" ylimit -50m 50m 2*(vout#branch/32-vprobe#branch)/(vprobe#branch+vout#branch/32)
.endc
"}
C {simulator_commands_shown.sym} 60 -230 0 0 {
name=Libs_Ngspice
simulator=ngspice
only_toplevel=false
value=".include sg13g2_stdcell.spice
.lib cornerMOSlv.lib mos_tt
.lib cornerMOShv.lib mos_tt"
      }
C {launcher.sym} 130 -130 0 0 {name=h3
descr=SimulateNGSPICE
tclcommand="
# Setup the default simulation commands if not already set up
# for example by already launched simulations.
set_sim_defaults
puts $sim(spice,1,cmd) 

# Change the Xyce command. In the spice category there are currently
# 5 commands (0, 1, 2, 3, 4). Command 3 is the Xyce batch
# you can get the number by querying $sim(spice,n)
set sim(spice,1,cmd) \{ngspice  \\"$N\\" -a\}

# change the simulator to be used (Xyce)
set sim(spice,default) 0

# Create FET and BIP .save file
exec mkdir -p $netlist_dir
write_data [save_params] $netlist_dir/[file rootname [file tail [xschem get current_name]]].save

# run netlist and simulation
xschem netlist
simulate
"}
C {devices/launcher.sym} 130 -100 0 0 {name=h1
descr="OP annotate" 
tclcommand="xschem annotate_op"
}
C {devices/launcher.sym} 130 -70 0 0 {name=h2
descr="Load waves" 
tclcommand="
xschem raw_read $netlist_dir/[file rootname [file tail [xschem get current_name]]].raw dc
xschem setprop rect 2 0 fullxzoom
"
}
C {vsource.sym} 540 -150 0 1 {name=Vprobe value=0 savecurrent=true}
C {isource_arith.sym} 540 -250 0 0 {name=G1 CUR=10**V(logI)}
C {vsource.sym} 460 -150 0 1 {name=VlogI value=\{logI\} savecurrent=true}
C {lab_pin.sym} 460 -200 0 0 {name=p6 lab=logI}
C {vsource.sym} 420 -250 0 1 {name=VDDA value=\{vdd\} savecurrent=true}
C {lab_wire.sym} 800 -620 0 0 {name=p2 lab=Vpbias}
C {sg13g2_pr/sg13_lv_pmos.sym} 560 -360 0 1 {name=Mcbias
l=\{lb\}
w=\{wb\}
ng=1
m=2
model=sg13_lv_pmos
spiceprefix=X
}
C {lab_wire.sym} 900 -600 0 0 {name=p3 lab=Vpcbias}
C {lab_wire.sym} 680 -780 0 0 {name=p1 lab=VDD}
C {lab_wire.sym} 1320 -580 0 0 {name=p4 lab=Vout}
C {vsource.sym} 900 -250 0 0 {name=VSW value="DC \{vdd\} PULSE(0 \{vdd\} \{td\} \{tr\} \{tf\} \{ton\} \{tcyc\})" savecurrent=true}
C {devices/code_shown.sym} 60 -770 0 0 {name=params only_toplevel=false value="* device parameters
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
* instrumentation parameters
.param logI=-7
.param vdd=1.6
.param vout=1
* simulation parameters
.param td     = 25n
.param tr     = 10p
.param tf     = 10p
.param ton    = 50n
.param tcyc   = 100n
"}
C {sg13g2_pr/sg13_hv_pmos.sym} 920 -720 1 1 {name=Mcbuffer
l=6u
w=6u
ng=1
m=32
model=sg13_hv_pmos
spiceprefix=X
}
C {sg13g2_pr/sg13_hv_pmos.sym} 820 -720 1 1 {name=Mbbuffer
l=6u
w=6u
ng=1
m=32
model=sg13_hv_pmos
spiceprefix=X
}
C {unitsource2u.sym} 620 -580 0 1 {name=xref[1:0]}
C {unitsource2u.sym} 1200 -580 0 0 {name=xsrc[63:0]}
C {lab_wire.sym} 900 -300 0 0 {name=p5 sig_type=std_logic lab=switch}
C {vsource.sym} 1200 -710 0 0 {name=Viswp value=0 savecurrent=true}
C {vsource.sym} 1200 -450 0 0 {name=Viswn value=0 savecurrent=true}
C {lab_wire.sym} 1200 -480 0 0 {name=p10 lab=sw_n}
C {lab_wire.sym} 1200 -660 0 0 {name=p11 lab=sw_p}
C {capa.sym} 1300 -250 0 1 {name=C1
m=1
value=1a}
C {lab_wire.sym} 680 -100 0 0 {name=p9 lab=VSS}
C {vsource.sym} 1160 -190 0 0 {name=Vgnd value=0 savecurrent=true}
C {lab_wire.sym} 1100 -560 0 0 {name=p7 sig_type=std_logic lab=on[63:0]}
C {lab_wire.sym} 1120 -480 0 0 {name=p8 sig_type=std_logic lab=on_n[63:0]}
C {complementary_driver.sym} 1000 -500 0 0 {name=xdigital[63:0]}
C {vsource.sym} 1070 -620 1 1 {name=Vpbleak value=0 savecurrent=true}
C {vsource.sym} 1050 -600 1 0 {name=Vpcleak value=0 savecurrent=true}
C {lab_wire.sym} 1130 -600 0 0 {name=p12 lab=Vpcleak}
C {lab_wire.sym} 1130 -620 0 0 {name=p13 lab=Vpbleak}
C {lab_wire.sym} 920 -500 0 0 {name=p14 sig_type=std_logic lab=(63*VDD,switch)}
