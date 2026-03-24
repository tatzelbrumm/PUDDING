v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 460 -100 460 -80 {lab=GND}
N 1420 -220 1420 -100 {lab=GND}
N 540 -680 540 -640 {lab=inprobe}
N 540 -120 540 -100 {lab=GND}
N 540 -200 540 -180 {lab=logI}
N 460 -100 540 -100 {lab=GND}
N 460 -220 460 -100 {lab=GND}
N 960 -380 1000 -380 {lab=switch}
N 540 -780 840 -780 {lab=VDD}
N 1380 -480 1420 -480 {lab=Vout}
N 1420 -480 1420 -280 {lab=Vout}
N 1320 -100 1420 -100 {lab=GND}
N 1180 -420 1260 -420 {lab=onb[127:0]}
N 1180 -420 1180 -360 {lab=onb[127:0]}
N 1120 -360 1180 -360 {lab=onb[127:0]}
N 1160 -440 1260 -440 {lab=on[127:0]}
N 1160 -440 1160 -380 {lab=on[127:0]}
N 1120 -380 1160 -380 {lab=on[127:0]}
N 1060 -320 1060 -100 {lab=GND}
N 840 -420 840 -100 {lab=GND}
N 840 -780 1060 -780 {lab=VDD}
N 900 -480 1260 -480 {lab=en[15:0]}
N 900 -460 1260 -460 {lab=enb[15:0]}
N 740 -100 840 -100 {lab=GND}
N 960 -100 1060 -100 {lab=GND}
N 740 -220 740 -100 {lab=GND}
N 740 -480 780 -480 {lab=enable}
N 740 -480 740 -280 {lab=enable}
N 840 -100 960 -100 {lab=GND}
N 960 -140 960 -100 {lab=GND}
N 960 -380 960 -200 {lab=switch}
N 1320 -680 1320 -580 {lab=dac_p}
N 1320 -380 1320 -180 {lab=dac_n}
N 1320 -120 1320 -100 {lab=GND}
N 1060 -100 1320 -100 {lab=GND}
N 460 -780 460 -280 {lab=VDD}
N 840 -780 840 -520 {lab=VDD}
N 1060 -780 1060 -420 {lab=VDD}
N 640 -480 640 -100 {lab=GND}
N 640 -100 740 -100 {lab=GND}
N 540 -100 640 -100 {lab=GND}
N 540 -540 580 -540 {lab=vgate}
N 540 -580 540 -540 {lab=vgate}
N 540 -780 540 -740 {lab=VDD}
N 460 -780 540 -780 {lab=VDD}
N 1320 -780 1320 -740 {lab=VDD}
N 1060 -780 1320 -780 {lab=VDD}
N 700 -540 940 -540 {lab=drain[7:0]}
N 1000 -540 1260 -540 {lab=vbiasp[7:0]}
C {title.sym} 160 0 0 0 {name=l1 author="Christoph Maier"}
C {vsource.sym} 1420 -250 0 0 {name=Vout value=\{vout\} savecurrent=true}
C {gnd.sym} 460 -80 0 0 {name=l2 lab=GND}
C {devices/code_shown.sym} 60 -1210 0 0 {name=NGSPICE only_toplevel=true 
value="
.include test_dac4x32_dc.save
.temp=27
.options gmin=1e-15 abstol=1p method=gear
.options savecurrents
.control
save all 
op
write test_dac4x32_dc.raw
set appendwrite
dc Vout 0 1.2 10m VlogI -8 -6 0.5
*tran 10n 500u
write test_dac4x32_dc.raw
plot title \\"output/reference current asymmetry\\" 2*(vout#branch-8*vprobe#branch)/(8*vprobe#branch+vout#branch)
plot ylimit -40m 5m title \\"output/reference current asymmetry\\" 2*(vout#branch-8*vprobe#branch)/(8*vprobe#branch+vout#branch)
plot vdd enable switch v(\\"en[0]\\") v(\\"enb[0]\\") v(\\"on[0]\\") v(\\"onb[0]\\") Vout
plot vgate \\"vbiasp[0]\\" Vout
plot vout#branch vprobe#branch
plot vidacp#branch vidacn#branch
plot 8*\\"viin[0]#branch\\" vprobe#branch
plot 2*(8*\\"viin[0]#branch\\"-vprobe#branch)/(8*\\"viin[0]#branch\\"+vprobe#branch)
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
C {vsource.sym} 540 -610 0 1 {name=Vprobe value=0 savecurrent=true}
C {isource_arith.sym} 540 -710 0 0 {name=G1 CUR=10**V(logI)}
C {vsource.sym} 540 -150 0 1 {name=VlogI value=\{logI\} savecurrent=true}
C {lab_pin.sym} 540 -200 0 0 {name=p6 lab=logI}
C {vsource.sym} 460 -250 0 1 {name=VDDA value=\{vdd\} savecurrent=true}
C {lab_wire.sym} 680 -780 0 0 {name=p1 lab=VDD}
C {lab_wire.sym} 1420 -370 3 0 {name=p4 lab=Vout}
C {lab_wire.sym} 1240 -420 0 0 {name=p7 sig_type=std_logic lab=onb[127:0]}
C {lab_wire.sym} 1240 -440 0 0 {name=p8 sig_type=std_logic lab=on[127:0]}
C {vsource.sym} 960 -170 0 0 {name=VSW value="DC \{vdd\} PULSE(0 \{vdd\} \{td\} \{tr\} \{tf\} \{ton\} \{tcyc\})" savecurrent=true}
C {lab_wire.sym} 960 -380 0 0 {name=p9 sig_type=std_logic lab=switch}
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
.param vdd=1.2
.param vout=0.6
* simulation parameters
.param celsius = 25
.param td     = 25u
.param tr     = 10p
.param tf     = 10p
.param ton    = 50u
.param tcyc   = 100u
"}
C {vsource.sym} 1320 -710 0 0 {name=Vidacp value=0 savecurrent=true}
C {vsource.sym} 1320 -150 0 0 {name=Vidacn value=0 savecurrent=true}
C {lab_wire.sym} 1320 -200 0 0 {name=p10 lab=dac_n}
C {lab_wire.sym} 540 -540 0 0 {name=p11 lab=vgate}
C {dac4x32module.sym} 1320 -480 0 0 {name=xdac}
C {inverterpair.sym} 840 -480 0 0 {name=xen[15:0]}
C {inverterpair.sym} 1060 -380 0 0 {name=xdrv[127:0]}
C {vsource.sym} 740 -250 0 0 {name=VEN value="DC \{vdd\} PULSE(\{vdd\} \{vdd\} \{td\} \{tr\} \{tf\} \{ton\} \{tcyc\})" savecurrent=true}
C {lab_wire.sym} 740 -480 0 0 {name=p13 sig_type=std_logic lab=enable}
C {lab_wire.sym} 920 -460 0 1 {name=p14 sig_type=std_logic lab=enb[15:0]}
C {lab_wire.sym} 920 -480 0 1 {name=p15 sig_type=std_logic lab=en[15:0]}
C {hvnmirror.sym} 640 -540 0 0 {name=xfeed}
C {vsource.sym} 970 -540 1 1 {name=Viin[7:0] value=0 savecurrent=true}
C {lab_wire.sym} 720 -540 0 1 {name=p2 sig_type=std_logic lab=drain[7:0]}
C {lab_wire.sym} 1240 -540 0 0 {name=p3 lab=vbiasp[7:0]}
C {lab_wire.sym} 540 -660 0 0 {name=p5 lab=inprobe}
C {lab_wire.sym} 1320 -620 0 0 {name=p12 lab=dac_p}
