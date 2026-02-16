v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
B 2 840 -730 1400 -430 {flags=graph
y1=0
ypos1=0
ypos2=2
divy=5
subdivy=1
unity=1
x1=0.3
x2=1.5
divx=5
subdivx=1
node="xdut.vbias
xdut.cascode_sw[255]
xdut.cascode_sw[255]"
color="7 4 4"
dataset=-1
unitx=1
logx=0
logy=0
sim_type=dc
autoload=1
rawfile=$netlist_dir/dc_dac.raw
y2=2}
B 2 830 -400 1390 -100 {flags=graph
y2=3e-05
ypos1=0
ypos2=2
divy=5
subdivy=1
unity=1
x1=0.3
x2=1.5
divx=5
subdivx=1
node=i(vout)
color=4
dataset=-1
unitx=1
logx=0
logy=0
sim_type=dc
autoload=1
rawfile=$netlist_dir/dc_dac.raw
y1=0
rainbow=0
}
B 2 250 -730 810 -430 {flags=graph
y1=0
y2=1.5
ypos1=0
ypos2=2
divy=5
subdivy=1
unity=1
x1=0.3
x2=1.5
divx=5
subdivx=1
dataset=-1
unitx=1
logx=0
logy=0
sim_type=dc
autoload=1
color="12 4 13 15"
node="xdut.xsw_top.xsw[255].on_n
xdut.xsw_top.xsw[0].on_n
v_on
v_iref"}
N 40 -310 40 -290 {lab=GND}
N 40 -400 40 -370 {lab=VDD}
N 40 -400 180 -400 {lab=VDD}
N 180 -400 180 -260 {lab=VDD}
N 570 -200 570 -170 {lab=Vout}
N 570 -110 570 -30 {lab=GND}
N 30 -70 30 -30 {lab=GND}
N 30 -170 30 -130 {lab=V_iref}
N 30 -170 70 -170 {lab=V_iref}
N -230 -200 -230 -170 {lab=V_on}
N -230 -80 -230 -30 {lab=GND}
N 340 -200 570 -200 {lab=Vout}
N -110 -110 -110 -50 {lab=VDD}
N -110 -220 -110 -170 {lab=V_on_n}
N -110 -220 70 -220 {lab=V_on_n}
N -180 -200 70 -200 {lab=V_on}
N -180 -160 -150 -160 {lab=V_on}
N -180 -200 -180 -160 {lab=V_on}
N -230 -200 -180 -200 {lab=V_on}
N -180 -120 -150 -120 {lab=GND}
N -180 -120 -180 -80 {lab=GND}
N -230 -80 -180 -80 {lab=GND}
N -230 -110 -230 -80 {lab=GND}
C {DAC_TOP.sym} 220 -200 0 0 {name=Xdut}
C {vsource.sym} 40 -340 0 0 {name=V1 value=1.5 savecurrent=true}
C {gnd.sym} 40 -290 0 0 {name=l1 lab=GND}
C {vsource.sym} 570 -140 0 0 {name=Vout value=0.4 savecurrent=true}
C {gnd.sym} 570 -30 0 0 {name=l2 lab=GND}
C {lab_wire.sym} 570 -200 0 0 {name=p1 sig_type=std_logic lab=Vout}
C {isource.sym} 30 -100 0 0 {name=Iref value=100n}
C {gnd.sym} 30 -30 0 0 {name=l3 lab=GND}
C {vsource.sym} -230 -140 0 0 {name=VON value=0 savecurrent=true}
C {gnd.sym} -230 -30 0 0 {name=l5 lab=GND}
C {devices/code_shown.sym} -610 -330 0 0 {name=NGSPICE only_toplevel=true 
value="
.include DC_sim.save
.param temp=27
.options savecurrents
.control
save all 
op
write dc_dac.raw
set appendwrite
dc VON 0 1.5 0.1
write dc_dac.raw
.endc
"}
C {launcher.sym} 910 -70 0 0 {name=h3
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
C {simulator_commands_shown.sym} -660 -50 0 0 {
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
C {devices/launcher.sym} 910 -20 0 0 {name=h2
descr="Load waves" 
tclcommand="
xschem raw_read $netlist_dir/[file rootname [file tail [xschem get current_name]]].raw dc
xschem setprop rect 2 0 fullxzoom
"
}
C {lab_wire.sym} -10 -200 0 0 {name=p2 sig_type=std_logic lab=V_on}
C {lab_wire.sym} 30 -170 0 0 {name=p3 sig_type=std_logic lab=V_iref}
C {vcvs.sym} -110 -140 0 0 {name=E1 value=-1}
C {lab_wire.sym} 120 -400 0 0 {name=p5 sig_type=std_logic lab=VDD}
C {lab_wire.sym} -110 -80 3 0 {name=p6 sig_type=std_logic lab=VDD}
C {lab_wire.sym} -10 -220 0 0 {name=p7 sig_type=std_logic lab=V_on_n}
