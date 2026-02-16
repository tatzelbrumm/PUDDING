v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 460 -100 460 -80 {lab=GND}
N 540 -100 620 -100 {lab=GND}
N 1420 -700 1420 -580 {lab=VDD}
N 620 -700 620 -580 {lab=VDD}
N 700 -540 700 -440 {lab=Vpbias}
N 680 -540 700 -540 {lab=Vpbias}
N 620 -440 700 -440 {lab=Vpbias}
N 620 -460 620 -440 {lab=Vpbias}
N 1420 -460 1420 -280 {lab=Vout}
N 1420 -220 1420 -100 {lab=GND}
N 620 -220 620 -180 {lab=#net1}
N 620 -120 620 -100 {lab=GND}
N 540 -120 540 -100 {lab=GND}
N 540 -200 540 -180 {lab=logI}
N 620 -440 620 -390 {lab=Vpbias}
N 620 -300 620 -280 {lab=Vpcbias}
N 620 -300 740 -300 {lab=Vpcbias}
N 620 -330 620 -300 {lab=Vpcbias}
N 740 -360 740 -300 {lab=Vpcbias}
N 660 -360 740 -360 {lab=Vpcbias}
N 540 -700 620 -700 {lab=VDD}
N 540 -700 540 -360 {lab=VDD}
N 540 -360 620 -360 {lab=VDD}
N 740 -500 740 -360 {lab=Vpcbias}
N 680 -500 740 -500 {lab=Vpcbias}
N 1340 -500 1360 -500 {lab=Vpcasc}
N 740 -300 1160 -300 {lab=Vpcbias}
N 1220 -460 1340 -460 {lab=Vpcasc}
N 1340 -500 1340 -460 {lab=Vpcasc}
N 1160 -700 1420 -700 {lab=VDD}
N 460 -100 540 -100 {lab=GND}
N 460 -220 460 -100 {lab=GND}
N 460 -700 460 -280 {lab=VDD}
N 460 -700 540 -700 {lab=VDD}
N 920 -100 1420 -100 {lab=GND}
N 980 -480 1100 -480 {lab=off_n}
N 980 -440 1100 -440 {lab=on_n}
N 920 -400 920 -100 {lab=GND}
N 820 -100 920 -100 {lab=GND}
N 920 -700 1160 -700 {lab=VDD}
N 820 -220 820 -100 {lab=GND}
N 820 -460 820 -280 {lab=switch}
N 820 -460 860 -460 {lab=switch}
N 1160 -580 1160 -520 {lab=sw_p}
N 1160 -400 1160 -380 {lab=sw_n}
N 1160 -320 1160 -300 {lab=Vpcbias}
N 1160 -700 1160 -640 {lab=VDD}
N 920 -700 920 -520 {lab=VDD}
N 880 -700 920 -700 {lab=VDD}
N 740 -700 740 -660 {lab=VDD}
N 700 -700 740 -700 {lab=VDD}
N 770 -660 780 -660 {lab=VDD}
N 780 -700 780 -660 {lab=VDD}
N 740 -700 780 -700 {lab=VDD}
N 700 -660 710 -660 {lab=VDD}
N 700 -700 700 -660 {lab=VDD}
N 620 -700 700 -700 {lab=VDD}
N 840 -700 840 -660 {lab=VDD}
N 800 -700 840 -700 {lab=VDD}
N 870 -660 880 -660 {lab=VDD}
N 880 -700 880 -660 {lab=VDD}
N 840 -700 880 -700 {lab=VDD}
N 800 -660 810 -660 {lab=VDD}
N 800 -700 800 -660 {lab=VDD}
N 780 -700 800 -700 {lab=VDD}
N 840 -540 1360 -540 {lab=Vpbias}
N 840 -620 840 -540 {lab=Vpbias}
N 620 -100 820 -100 {lab=GND}
N 700 -540 840 -540 {lab=Vpbias}
N 740 -550 740 -500 {lab=Vpcbias}
N 740 -620 740 -610 {lab=#net2}
C {title.sym} 160 0 0 0 {name=l1 author="Christoph Maier"}
C {vsource.sym} 1420 -250 0 0 {name=Vout value=\{vdd-vout\} savecurrent=true}
C {gnd.sym} 460 -80 0 0 {name=l2 lab=GND}
C {devices/code_shown.sym} 1500 -670 0 0 {name=NGSPICE only_toplevel=true 
value="
.include test_switchedsources_tran.save
.temp=27
.options gmin=1e-15 abstol=1p method=gear
.options savecurrents
.control
save all 
op
write test_switchedsources_tran.raw
set appendwrite
*dc Vout 0 1.6 10m VlogI -8 -6 0.5
tran 10p 500n
write test_switchedsources_tran.raw
plot 2*(vout#branch-vprobe#branch)/(vprobe#branch+vout#branch)
plot vdd vpbias vpcbias switch on_n off_n vpcasc vout xref.drain xsrc.drain
plot vout#branch vprobe#branch
plot switch on_n off_n Vpcasc
*plot @n.xsw.xmbias.nsg13_lv_pmos[ids] @n.xsw.xmpullup.nsg13_lv_pmos[ids]
plot viswp#branch viswn#branch
plot 0.5*(viswp#branch+viswn#branch) viswp#branch-viswn#branch
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
C {vsource.sym} 620 -150 0 1 {name=Vprobe value=0 savecurrent=true}
C {isource_arith.sym} 620 -250 0 0 {name=G1 CUR=10**V(logI)}
C {vsource.sym} 540 -150 0 1 {name=VlogI value=\{logI\} savecurrent=true}
C {lab_pin.sym} 540 -200 0 0 {name=p6 lab=logI}
C {pcascsrc.sym} 620 -520 0 1 {name=xref w=\{w\} l=\{l\} wc=\{wc\} lc=\{lc\}}
C {pcascsrc.sym} 1420 -520 0 0 {name=xsrc w=\{w\} l=\{l\} wc=\{wc\} lc=\{lc\}}
C {vsource.sym} 460 -250 0 1 {name=VDDA value=\{vdd\} savecurrent=true}
C {lab_wire.sym} 720 -540 0 0 {name=p2 lab=Vpbias}
C {sg13g2_pr/sg13_lv_pmos.sym} 640 -360 0 1 {name=Mcbias
l=\{lb\}
w=\{wb\}
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
C {lab_wire.sym} 710 -300 0 0 {name=p3 lab=Vpcbias}
C {lab_wire.sym} 680 -700 0 0 {name=p1 lab=VDD}
C {lab_wire.sym} 1420 -450 3 0 {name=p4 lab=Vout}
C {cascodeswitch_pmos.sym} 1160 -460 0 0 {name=xsw}
C {lab_wire.sym} 1340 -500 0 0 {name=p5 lab=Vpcasc}
C {switch_logic_nonoverlap.sym} 920 -460 0 0 {name=xlogic}
C {lab_wire.sym} 1000 -480 0 0 {name=p7 sig_type=std_logic lab=off_n}
C {lab_wire.sym} 1000 -440 0 0 {name=p8 sig_type=std_logic lab=on_n}
C {vsource.sym} 820 -250 0 0 {name=VSW value="DC \{vdd\} PULSE(0 \{vdd\} \{td\} \{tr\} \{tf\} \{ton\} \{tcyc\})" savecurrent=true}
C {lab_wire.sym} 820 -460 0 0 {name=p9 sig_type=std_logic lab=switch}
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
.param vout=0.6
* simulation parameters
.param celsius = 25
.param td     = 10p
.param tr     = 10p
.param tf     = 10p
.param ton    = 50n
.param tcyc   = 100n
"}
C {vsource.sym} 1160 -610 0 0 {name=Viswp value=0 savecurrent=true}
C {vsource.sym} 1160 -350 0 0 {name=Viswn value=0 savecurrent=true}
C {lab_wire.sym} 1160 -380 0 0 {name=p10 lab=sw_n}
C {lab_wire.sym} 1160 -560 0 0 {name=p11 lab=sw_p}
C {sg13g2_pr/sg13_hv_pmos.sym} 740 -640 1 1 {name=Mcbuffer
l=6u
w=6u
ng=1
m=32
model=sg13_hv_pmos
spiceprefix=X
}
C {sg13g2_pr/sg13_hv_pmos.sym} 840 -640 1 1 {name=Mbbuffer
l=6u
w=6u
ng=1
m=32
model=sg13_hv_pmos
spiceprefix=X
}
C {vsource.sym} 740 -580 0 1 {name=Vleak value=0 savecurrent=true}
