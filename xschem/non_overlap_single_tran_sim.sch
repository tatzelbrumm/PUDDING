v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
B 2 530 -410 1330 -10 {flags=graph
y1=-0.36
y2=1.7
ypos1=0
ypos2=2
divy=5
subdivy=1
unity=1
x1=0
divx=5
subdivx=1
xlabmag=1.0
ylabmag=1.0

dataset=-1
unitx=1
logx=0
logy=0
color="7 8"
node="ON
ON_N"
x2=50n}
B 2 530 -820 1330 -420 {flags=graph
y1=-0.36
y2=1.7
ypos1=0
ypos2=2
divy=5
subdivy=1
unity=1
x1=10e-9
divx=5
subdivx=1
xlabmag=1.0
ylabmag=1.0

dataset=-1
unitx=1
logx=0
logy=0
color="6 10 12 15 6 20 7 8"
node="thermo
x1.thermon
x1.a1
x1.b1
x1.a2
x1.b2
on
on_n"
x2=11e-9}
N 410 -50 410 130 {
lab=GND}
N -270 40 -270 50 {
lab=GND}
N 410 -290 410 -110 {
lab=#net1}
N 80 -10 80 10 {lab=GND}
N 230 -100 270 -100 {lab=ON}
N 230 -60 270 -60 {lab=ON_N}
N 80 -290 80 -150 {lab=#net1}
N 80 -290 410 -290 {lab=#net1}
N -270 -80 -70 -80 {lab=thermo}
N -270 -80 -270 -20 {lab=thermo}
C {devices/code_shown.sym} -290 150 0 0 {name=MODEL only_toplevel=true
format="tcleval( @value )"
value="
.lib cornerMOSlv.lib mos_ff
.include sg13g2_stdcell.spice
"}
C {devices/code_shown.sym} -330 -540 0 0 {name=NGSPICE only_toplevel=true 
value="
.options gmin=1e-15 abstol=1p method=gear
.temp=-55
.control
save all 
tran 50p 200n
meas tran tdelay TRIG v(thermo) VAl=0.9 FALl=1 TARG v(ON) VAl=0.9 RISE=1
write non_overlap_single_tran_sim.raw
.endc
"}
C {devices/vsource.sym} 410 -80 0 0 {name=Vdd value=1.5}
C {devices/gnd.sym} 410 130 0 0 {name=l3 lab=GND}
C {devices/title.sym} -130 260 0 0 {name=l5 author="Luis Ardila"}
C {devices/launcher.sym} -270 -610 0 0 {name=h5
descr="load waves Ctrl + left click" 
tclcommand="xschem raw_read $netlist_dir/non_overlap_single_tran_sim.raw tran"
}
C {devices/gnd.sym} -270 50 0 0 {name=l7 lab=GND}
C {devices/vsource.sym} -270 10 0 0 {name=Vthermo value="dc 0 ac 0 pulse(0, 1.5, 0, 100p, 100p, 10n, 20n, 20) "}
C {devices/lab_pin.sym} -270 -80 0 0 {name=p3 sig_type=std_logic lab=thermo}
C {non_overlap.sym} 80 -80 0 0 {name=x1}
C {gnd.sym} 80 10 0 0 {name=l8 lab=GND}
C {lab_pin.sym} 270 -100 2 0 {name=p6 sig_type=std_logic lab=ON}
C {lab_pin.sym} 270 -60 2 0 {name=p7 sig_type=std_logic lab=ON_N}
C {launcher.sym} -270 -640 0 0 {name=h3
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
