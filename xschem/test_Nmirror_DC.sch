v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 760 -500 760 -460 {lab=Vsub}
N 760 -400 760 -380 {lab=GND}
N 720 -380 760 -380 {lab=GND}
N 720 -500 720 -380 {lab=GND}
N 960 -540 960 -380 {lab=GND}
N 880 -380 960 -380 {lab=GND}
N 880 -540 880 -380 {lab=GND}
N 760 -380 880 -380 {lab=GND}
N 780 -640 780 -620 {lab=Vout2}
N 780 -640 880 -640 {lab=Vout2}
N 880 -640 880 -600 {lab=Vout2}
N 740 -660 740 -620 {lab=Vout1}
N 740 -660 960 -660 {lab=Vout1}
N 960 -660 960 -600 {lab=Vout1}
N 700 -660 700 -620 {lab=Vin}
N 700 -760 700 -720 {lab=probe}
N 680 -380 720 -380 {lab=GND}
N 680 -380 680 -360 {lab=GND}
N 620 -380 680 -380 {lab=GND}
N 620 -760 620 -600 {lab=probe}
N 620 -760 700 -760 {lab=probe}
N 620 -540 620 -380 {lab=GND}
N 540 -400 540 -380 {lab=GND}
N 540 -380 620 -380 {lab=GND}
N 540 -480 540 -460 {lab=logI}
C {title.sym} 160 0 0 0 {name=l1 author="Christoph Maier"}
C {Nmirror.sym} 740 -560 0 0 {name=xDUT}
C {vsource.sym} 960 -570 0 0 {name=V1 value=0.5 savecurrent=true}
C {vsource.sym} 880 -570 0 0 {name=V2 value=0.2 savecurrent=true}
C {vsource.sym} 760 -430 0 0 {name=VSUB value=0 savecurrent=true}
C {gnd.sym} 680 -360 0 0 {name=l2 lab=GND}
C {lab_wire.sym} 700 -630 0 0 {name=p1 lab=Vin}
C {lab_wire.sym} 880 -610 0 0 {name=p2 lab=Vout2}
C {lab_wire.sym} 960 -610 0 0 {name=p3 lab=Vout1}
C {lab_wire.sym} 760 -470 0 1 {name=p4 lab=Vsub}
C {devices/code_shown.sym} 40 -550 0 0 {name=NGSPICE only_toplevel=true 
value="
.include test_Nmirror_DC.save
.param temp=27
.options savecurrents
.control
save all 
op
write test_Nmirror_DC.raw
set appendwrite
dc V1 0 2 10m VlogI -8 -5 0.5
write test_Nmirror_DC.raw
plot vprobe#branch v1#branch v2#branch
plot xdut.vd_in xdut.vd_1 xdut.vd_2
plot @n.xdut.xm1.nsg13_lv_nmos[gm]/vprobe#branch @n.xdut.xm3.nsg13_lv_nmos[gm]/v1#branch @n.xdut.xm5.nsg13_lv_nmos[gm]/v2#branch
plot @n.xdut.xm2.nsg13_lv_nmos[gm]/vprobe#branch @n.xdut.xm4.nsg13_lv_nmos[gm]/v1#branch @n.xdut.xm6.nsg13_lv_nmos[gm]/v2#branch
plot @n.xdut.xm1.nsg13_lv_nmos[gm]/@n.xdut.xm1.nsg13_lv_nmos[gds] @n.xdut.xm3.nsg13_lv_nmos[gm]/@n.xdut.xm3.nsg13_lv_nmos[gds] @n.xdut.xm5.nsg13_lv_nmos[gm]/@n.xdut.xm5.nsg13_lv_nmos[gds]
plot @n.xdut.xm2.nsg13_lv_nmos[gm]/@n.xdut.xm2.nsg13_lv_nmos[gds] @n.xdut.xm4.nsg13_lv_nmos[gm]/@n.xdut.xm4.nsg13_lv_nmos[gds] @n.xdut.xm6.nsg13_lv_nmos[gm]/@n.xdut.xm6.nsg13_lv_nmos[gds]
.endc
"}
C {simulator_commands_shown.sym} 40 -160 0 0 {
name=Libs_Ngspice
simulator=ngspice
only_toplevel=false
value="
.lib cornerMOSlv.lib mos_tt
.lib cornerMOShv.lib mos_tt
.lib cornerHBT.lib hbt_typ
.lib cornerRES.lib res_typ
.lib cornerCAP.lib cap_typ
"
      }
C {launcher.sym} 420 -100 0 0 {name=h3
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
C {devices/launcher.sym} 420 -70 0 0 {name=h1
descr="OP annotate" 
tclcommand="xschem annotate_op"
}
C {devices/launcher.sym} 420 -40 0 0 {name=h2
descr="Load waves" 
tclcommand="
xschem raw_read $netlist_dir/[file rootname [file tail [xschem get current_name]]].raw dc
xschem setprop rect 2 0 fullxzoom
"
}
C {vsource.sym} 620 -570 0 1 {name=Vprobe value=0 savecurrent=true}
C {lab_wire.sym} 700 -730 0 0 {name=p5 lab=probe}
C {isource_arith.sym} 700 -690 0 0 {name=G1 CUR=10**V(logI)}
C {vsource.sym} 540 -430 0 1 {name=VlogI value=-7 savecurrent=true}
C {lab_pin.sym} 540 -480 0 0 {name=p6 lab=logI}
