v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 600 -200 640 -200 {lab=Vg}
N 520 -170 520 -140 {lab=GND}
N 520 -140 680 -140 {lab=GND}
N 680 -170 680 -140 {lab=GND}
N 680 -200 700 -200 {lab=GND}
N 700 -200 700 -140 {lab=GND}
N 680 -140 700 -140 {lab=GND}
N 500 -200 520 -200 {lab=GND}
N 500 -200 500 -140 {lab=GND}
N 500 -140 520 -140 {lab=GND}
N 600 -260 600 -200 {lab=Vg}
N 560 -200 600 -200 {lab=Vg}
N 520 -260 600 -260 {lab=Vg}
N 520 -260 520 -230 {lab=Vg}
N 420 -140 500 -140 {lab=GND}
N 420 -160 420 -140 {lab=GND}
N 420 -240 420 -220 {lab=logI}
N 520 -400 520 -360 {lab=#net1}
N 340 -140 420 -140 {lab=GND}
N 340 -500 340 -140 {lab=GND}
N 340 -500 520 -500 {lab=GND}
N 520 -500 520 -460 {lab=GND}
N 520 -300 520 -260 {lab=Vg}
N 340 -140 340 -120 {lab=GND}
N 680 -260 680 -230 {lab=Vd}
N 680 -260 780 -260 {lab=Vd}
N 780 -260 780 -220 {lab=Vd}
N 780 -160 780 -140 {lab=GND}
N 700 -140 780 -140 {lab=GND}
C {title.sym} 160 0 0 0 {name=l1 author="Christoph Maier"}
C {sg13g2_pr/sg13_hv_nmos.sym} 660 -200 0 0 {name=Msrc
l=l
w=w
ng=1
m=1
model=sg13_hv_nmos
spiceprefix=X
}
C {sg13g2_pr/sg13_hv_nmos.sym} 540 -200 0 1 {name=Mref
l=l
w=w
ng=1
m=1
model=sg13_hv_nmos
spiceprefix=X
}
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
.param l      = 5u
.param w      = 1u
* instrumentation parameters
.param logI=-7
.param vout=0.6
* simulation parameters
"}
C {vsource.sym} 520 -430 0 1 {name=Vprobe value=0 savecurrent=true}
C {isource_arith.sym} 520 -330 0 0 {name=G1 CUR=10**V(logI)}
C {vsource.sym} 420 -190 0 1 {name=VlogI value=\{logI\} savecurrent=true}
C {lab_pin.sym} 420 -240 0 0 {name=p1 lab=logI}
C {vsource.sym} 780 -190 0 0 {name=Vd value=\{vout\} savecurrent=true}
C {gnd.sym} 340 -120 0 0 {name=l2 lab=GND}
C {lab_wire.sym} 560 -260 0 1 {name=p2 lab=Vg}
C {lab_wire.sym} 720 -260 0 1 {name=p3 lab=Vd}
C {devices/code_shown.sym} 840 -490 0 0 {name=NGSPICE only_toplevel=true 
value="
.include test_nmirror.save
.temp=27
.options gmin=1e-15 abstol=1p method=gear
.options savecurrents
.control
save all 
op
write test_nmirror.raw
set appendwrite
foreach l_val 5u
  foreach w_val 1u 2u
    alterparam l = $l_val
    alterparam w = $w_val
    reset
    save all
    dc Vd 0 1.2 10m VlogI -8 -6 0.5
    write test_nmirror.raw
    plot Vg Vd
    plot vprobe#branch 0-vd#branch
    plot 2*(vprobe#branch+vd#branch)/(vprobe#branch-vd#branch)
  end
end
.endc
"}
