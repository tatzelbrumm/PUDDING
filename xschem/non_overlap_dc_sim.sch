v {xschem version=3.4.8RC file_version=1.2}
G {}
K {}
V {}
S {}
F {}
E {}
B 2 540 -610 1100 -310 {flags=graph
y1=0
y2=1.5
ypos1=0
ypos2=2
divy=5
subdivy=1
unity=1
x1=0.52960382
x2=1.7296038
divx=5
subdivx=1
dataset=-1
unitx=1
logx=0
logy=0
sim_type=dc
autoload=1
color="12 4 13"
node="x_dut_noi.noi_top[255].ON_N
x_dut_noi.noi_top[255].ON
v_on"
hilight_wave=-1}
N 40 -310 40 -290 {lab=GND}
N 40 -400 40 -370 {lab=VDD}
N 40 -400 220 -400 {lab=VDD}
N -230 -200 -230 -170 {lab=V_on}
N -230 -200 70 -200 {lab=V_on}
N -230 -110 -230 -30 {lab=GND}
N 220 -400 220 -270 {lab=VDD}
N 370 -210 480 -210 {lab=ON[255:0]}
N 370 -190 480 -190 {lab=ON_N[255:0]}
C {vsource.sym} 40 -340 0 0 {name=V1 value=1.5 savecurrent=true}
C {gnd.sym} 40 -290 0 0 {name=l1 lab=GND}
C {vsource.sym} -230 -140 0 0 {name=VON value=0 savecurrent=true}
C {gnd.sym} -230 -30 0 0 {name=l5 lab=GND}
C {devices/code_shown.sym} -670 -410 0 0 {name=NGSPICE only_toplevel=true 
value="
.include non_overlap_dc_sim.save
.param temp=27
.options savecurrents
.control
save all 
op
write non_overlap_dc_dac.raw
set appendwrite
dc VON 0 1.5 0.1
write non_overlap_dc_dac.raw
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
C {lab_wire.sym} 120 -400 0 0 {name=p5 sig_type=std_logic lab=VDD}
C {non_overlap_top.sym} 220 -200 0 0 {name=x_dut_noi}
C {gnd.sym} 220 -130 0 0 {name=l2 lab=GND}
C {lab_wire.sym} 480 -210 0 0 {name=p1 sig_type=std_logic lab=ON[255:0]}
C {lab_wire.sym} 480 -190 0 0 {name=p3 sig_type=std_logic lab=ON_N[255:0]}
