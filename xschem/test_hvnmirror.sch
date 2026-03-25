v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 740 -140 800 -140 {lab=GND}
N 420 -160 420 -140 {lab=GND}
N 420 -240 420 -220 {lab=logI}
N 480 -480 480 -440 {lab=vss}
N 340 -140 420 -140 {lab=GND}
N 340 -580 480 -580 {lab=GND}
N 480 -580 480 -540 {lab=GND}
N 340 -140 340 -120 {lab=GND}
N 680 -320 800 -320 {lab=Vd[7:0]}
N 420 -140 620 -140 {lab=GND}
N 620 -140 700 -140 {lab=GND}
N 700 -280 760 -280 {lab=Vd}
N 340 -580 340 -140 {lab=GND}
N 480 -320 560 -320 {lab=Vg}
N 480 -380 480 -320 {lab=Vg}
N 740 -240 760 -240 {lab=GND}
N 740 -240 740 -140 {lab=GND}
N 700 -140 740 -140 {lab=GND}
N 700 -280 700 -260 {lab=Vd}
N 700 -220 700 -140 {lab=GND}
N 620 -260 620 -140 {lab=GND}
N 800 -320 800 -290 {lab=Vd[7:0]}
N 800 -230 800 -200 {lab=sense[7:0]}
C {title.sym} 160 0 0 0 {name=l1 author="Christoph Maier"}
C {simulator_commands_shown.sym} 20 -250 0 0 {
name=Libs_Ngspice
simulator=ngspice
only_toplevel=false
value=".include sg13g2_stdcell.spice
.lib cornerMOSlv.lib mos_tt
.lib cornerMOShv.lib mos_tt"
      }
C {launcher.sym} 90 -150 0 0 {name=h3
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
C {devices/launcher.sym} 90 -120 0 0 {name=h1
descr="OP annotate" 
tclcommand="xschem annotate_op"
}
C {devices/launcher.sym} 90 -90 0 0 {name=h2
descr="Load waves" 
tclcommand="
xschem raw_read $netlist_dir/[file rootname [file tail [xschem get current_name]]].raw dc
xschem setprop rect 2 0 fullxzoom
"
}
C {devices/code_shown.sym} 20 -490 0 0 {name=params only_toplevel=false value="* device parameters
.param l      = 10u
.param lc     = 5u
.param w      = 2u
* instrumentation parameters
.param logI=-7
.param vout=0.6
* simulation parameters
"}
C {vsource.sym} 480 -510 0 1 {name=Vprobe value=0 savecurrent=true}
C {isource_arith.sym} 480 -410 0 0 {name=G1 CUR=10**V(logI)}
C {vsource.sym} 420 -190 0 1 {name=VlogI value=\{logI\} savecurrent=true}
C {lab_pin.sym} 420 -240 0 0 {name=p1 lab=logI}
C {gnd.sym} 340 -120 0 0 {name=l2 lab=GND}
C {lab_wire.sym} 520 -320 0 1 {name=p2 lab=Vg}
C {lab_wire.sym} 720 -320 0 1 {name=p3 lab=Vd[7:0]}
C {devices/code_shown.sym} 840 -490 0 0 {name=NGSPICE only_toplevel=true 
value="
.include test_hvnmirror.save
.temp=27
.options gmin=1e-15 abstol=1p method=gear
.options savecurrents
.control
save all 
op
write test_hvnmirror.raw
set appendwrite
foreach l_val 10u
  foreach lc_val 5u
    alterparam l = $l_val
    alterparam lc = $lc_val
    reset
    save all
    dc Vd 0 1.2 10m VlogI -8 -5 0.5
    write test_hvnmirror.raw
    plot Vg Vd
    plot vprobe#branch 0-\\"vsense[0]#branch\\"
    plot 2*(vprobe#branch+8*\\"vsense[0]#branch\\")/(vprobe#branch-8*\\"vsense[0]#branch\\")
  end
end
.endc
"}
C {lab_wire.sym} 480 -450 0 1 {name=p6 lab=vss}
C {hvnmirror.sym} 620 -320 0 0 {name=xDUT}
C {vsource.sym} 700 -230 0 1 {name=Vd value=\{vout\} savecurrent=true}
C {lab_wire.sym} 710 -280 0 1 {name=p4 lab=Vd}
C {vcvs.sym} 800 -260 0 0 {name=E[7:0] value=1}
C {vsource.sym} 800 -170 0 0 {name=Vsense[7:0] value=0 savecurrent=true}
C {lab_wire.sym} 800 -210 0 1 {name=p5 lab=sense[7:0]}
