v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 600 -300 680 -300 {lab=GND}
N 680 -520 680 -500 {lab=Vpbias}
N 680 -440 680 -400 {lab=#net1}
N 680 -340 680 -300 {lab=GND}
N 540 -320 540 -300 {lab=GND}
N 540 -400 540 -380 {lab=logI}
N 620 -520 680 -520 {lab=Vpbias}
N 680 -550 680 -520 {lab=Vpbias}
N 620 -580 620 -520 {lab=Vpbias}
N 620 -580 640 -580 {lab=Vpbias}
N 600 -300 600 -280 {lab=GND}
N 540 -300 600 -300 {lab=GND}
N 680 -640 680 -610 {lab=GND}
N 680 -640 720 -640 {lab=GND}
N 720 -640 720 -580 {lab=GND}
N 680 -580 720 -580 {lab=GND}
N 720 -580 720 -300 {lab=GND}
N 680 -300 720 -300 {lab=GND}
C {title.sym} 160 0 0 0 {name=l1 author="Christoph Maier"}
C {gnd.sym} 600 -280 0 0 {name=l2 lab=GND}
C {devices/code_shown.sym} 40 -390 0 0 {name=NGSPICE only_toplevel=true 
value="
.include test_pmosdiode.save
.param temp=-100
.options savecurrents
.control
save all 
op
write test_pmosdiode.raw
set appendwrite
dc VlogI -12 -4 10m
write test_pmosdiode.raw
plot -vpbias
plot @n.xmdut.nsg13_lv_pmos[gm]/vprobe#branch
plot @n.xmdut.nsg13_lv_pmos[gm]/@n.xmdut.nsg13_lv_pmos[gds]
plot @n.xmdut.nsg13_lv_pmos[vth]
.endc
"}
C {simulator_commands_shown.sym} 40 -560 0 0 {
name=Libs_Ngspice
simulator=ngspice
only_toplevel=false
value="
.lib cornerMOSlv.lib mos_ff
"
      }
C {launcher.sym} 150 -700 0 0 {name=h3
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
C {devices/launcher.sym} 150 -670 0 0 {name=h1
descr="OP annotate" 
tclcommand="xschem annotate_op"
}
C {devices/launcher.sym} 150 -640 0 0 {name=h2
descr="Load waves" 
tclcommand="
xschem raw_read $netlist_dir/[file rootname [file tail [xschem get current_name]]].raw dc
xschem setprop rect 2 0 fullxzoom
"
}
C {vsource.sym} 680 -370 0 1 {name=Vprobe value=0 savecurrent=true}
C {isource_arith.sym} 680 -470 0 0 {name=G1 CUR=10**V(logI)}
C {vsource.sym} 540 -350 0 1 {name=VlogI value=-7 savecurrent=true}
C {lab_pin.sym} 540 -400 0 0 {name=p6 lab=logI}
C {lab_pin.sym} 620 -520 0 0 {name=p2 lab=Vpbias}
C {sg13g2_pr/sg13_lv_pmos.sym} 660 -580 0 0 {name=Mdut
l=0.15u
w=6u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
