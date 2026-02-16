v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
B 2 80 -520 640 -220 {flags=graph
y1=-0.4
ypos1=0
ypos2=2
divy=5
subdivy=1
unity=1
x1=0
divx=5
subdivx=1
node="xdut.vbias
v_on[0]
v_on[1]
v_on[2]
v_on_n[0]
v_on_n[1]
v_on_n[2]"
color="7 4 5 6 7 8 10"
dataset=-1
unitx=1
logx=0
logy=0
sim_type=tran
autoload=1
rawfile=$netlist_dir/tran_sim.raw
y2=1.6
x2=0.0001}
B 2 670 -190 1230 110 {flags=graph
y2=3.4834199e-05
ypos1=0
ypos2=2
divy=5
subdivy=1
unity=1
x1=0
x2=0.0001
divx=5
subdivx=1
dataset=-1
unitx=1
logx=0
logy=0
sim_type=tran
autoload=1
rawfile=$netlist_dir/tran_sim.raw
y1=1.1926534e-05
rainbow=0
color="9 16"
node="i(vout)
i(@iref[current])"}
B 2 670 -520 1230 -220 {flags=graph
y1=-0.3
y2=2
ypos1=0
ypos2=2
divy=5
subdivy=1
unity=1
x1=0
x2=0.0001
divx=5
subdivx=1
dataset=-1
unitx=1
logx=0
logy=0
sim_type=tran
autoload=1
color="12 4 13 15"
node="xdut.xsw_top.xsw[255].on_n
xdut.xsw_top.xsw[0].on_n
v_on
v_iref"
rawfile=$netlist_dir/tran_sim.raw}
B 2 80 -870 640 -570 {flags=graph
y1=-0.4
ypos1=0
ypos2=2
divy=5
subdivy=1
unity=1
x1=0
divx=5
subdivx=1
node="v_on[0]
v_on_n[0]"
color="5 4"
dataset=-1
unitx=1
logx=0
logy=0
sim_type=tran
autoload=1
rawfile=$netlist_dir/tran_sim.raw
y2=1.6
x2=0.0001}
B 2 670 -870 1230 -570 {flags=graph
y1=-0.4
ypos1=0
ypos2=2
divy=5
subdivy=1
unity=1
x1=0
divx=5
subdivx=1
node="v_on[1]
v_on_n[1]"
color="7 4"
dataset=-1
unitx=1
logx=0
logy=0
sim_type=tran
autoload=1
rawfile=$netlist_dir/tran_sim.raw
y2=1.6
x2=0.0001}
B 2 1260 -870 1820 -570 {flags=graph
y1=-0.4
ypos1=0
ypos2=2
divy=5
subdivy=1
unity=1
x1=0
divx=5
subdivx=1
node="v_on[2]
v_on_n[2]"
color="7 4"
dataset=-1
unitx=1
logx=0
logy=0
sim_type=tran
autoload=1
rawfile=$netlist_dir/tran_sim.raw
y2=1.6
x2=0.0001}
N -120 -100 -120 -80 {lab=GND}
N -120 -190 -120 -160 {lab=#net1}
N 20 -190 20 -50 {lab=#net2}
N 410 10 410 40 {lab=V_out}
N -130 140 -130 180 {lab=GND}
N -130 40 -130 80 {lab=V_iref}
N -130 40 -90 40 {lab=V_iref}
N 20 70 20 180 {lab=GND}
N -300 10 -90 10 {lab=(100*V_on[0],100*V_on[1],56*V_on[2])}
N 410 100 410 180 {lab=GND}
N -120 -190 -90 -190 {lab=#net1}
N -30 -190 20 -190 {lab=#net2}
N 180 10 220 10 {lab=#net3}
N 280 10 410 10 {lab=V_out}
N -560 550 -560 580 {lab=GND}
N -290 560 -290 580 {lab=GND}
N -20 550 -20 580 {lab=GND}
N -560 230 -560 370 {lab=V_on[0]}
N -290 230 -290 380 {lab=V_on[1]}
N -20 230 -20 380 {lab=V_on[2]}
N -20 440 -20 490 {lab=#net4}
N -290 440 -290 500 {lab=#net5}
N -560 430 -560 490 {lab=#net6}
N -300 -10 -90 -10 {lab=(100*V_on_N[0],100*V_on_N[1],56*V_on_N[2])}
N -560 960 -560 990 {lab=GND}
N -290 970 -290 990 {lab=GND}
N -20 960 -20 990 {lab=GND}
N -560 640 -560 780 {lab=V_on_N[0]}
N -290 640 -290 790 {lab=V_on_N[1]}
N -20 640 -20 790 {lab=V_on_N[2]}
N -20 850 -20 900 {lab=#net7}
N -290 850 -290 910 {lab=#net8}
N -560 840 -560 900 {lab=#net9}
C {DAC_TOP.sym} 60 10 0 0 {name=Xdut}
C {vsource.sym} -120 -130 0 0 {name=V1 value=1.5 savecurrent=true}
C {gnd.sym} -120 -80 0 0 {name=l1 lab=GND}
C {vsource.sym} 410 70 0 0 {name=Vout value=0.4 savecurrent=true}
C {gnd.sym} 410 180 0 0 {name=l2 lab=GND}
C {lab_wire.sym} 410 10 0 0 {name=p1 sig_type=std_logic lab=V_out}
C {isource.sym} -130 110 0 0 {name=Iref value=100n}
C {gnd.sym} -130 180 0 0 {name=l3 lab=GND}
C {gnd.sym} 20 180 0 0 {name=l4 lab=GND}
C {devices/code_shown.sym} -920 -70 0 0 {name=NGSPICE only_toplevel=true 
value="
.include tran_sim.save
.param temp=27
.options savecurrents
.control
save all 
tran 1n 5u
write tran_sim.raw
.endc
"}
C {launcher.sym} 750 140 0 0 {name=h3
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
mkdir -p $netlist_dir
write_data [save_params] $netlist_dir/[file rootname [file tail [xschem get current_name]]].save

# run netlist and simulation
xschem netlist
simulate
"}
C {simulator_commands_shown.sym} -940 200 0 0 {
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
C {devices/launcher.sym} 750 190 0 0 {name=h2
descr="Load waves" 
tclcommand="
xschem raw_read $netlist_dir/[file rootname [file tail [xschem get current_name]]].raw tran
xschem setprop rect 2 0 fullxzoom
"
}
C {lab_wire.sym} -140 10 0 0 {name=p2 sig_type=std_logic lab=(100*V_on[0],100*V_on[1],56*V_on[2])}
C {lab_wire.sym} -130 40 0 0 {name=p3 sig_type=std_logic lab=V_iref}
C {gnd.sym} -20 580 0 0 {name=l6 lab=GND}
C {gnd.sym} -290 580 0 0 {name=l7 lab=GND}
C {vsource.sym} -560 520 0 0 {name=VON3 value="dc 0 ac 0 PULSE(0 1.5 0 100p 100p 5000n 10u)" savecurrent=true}
C {gnd.sym} -560 580 0 0 {name=l8 lab=GND}
C {vsource.sym} -290 530 0 0 {name=VON1 value="dc 0 ac 0 PULSE(0 1.5 0 100p 100p 10u 20u)" savecurrent=true}
C {vsource.sym} -20 520 0 0 {name=VON2 value="dc 0 ac 0 PULSE(0 1.5 0 100p 100p 20u 30u)" savecurrent=true}
C {lab_wire.sym} -560 230 3 0 {name=p4 sig_type=std_logic lab=V_on[0]}
C {lab_wire.sym} -290 230 3 0 {name=p5 sig_type=std_logic lab=V_on[1]}
C {lab_wire.sym} -20 230 3 0 {name=p6 sig_type=std_logic lab=V_on[2]}
C {res.sym} -60 -190 1 0 {name=R1
value=10
footprint=1206
device=resistor
m=1}
C {res.sym} 250 10 1 0 {name=R2
value=10
footprint=1206
device=resistor
m=1}
C {res.sym} -560 400 2 0 {name=R3
value=10
footprint=1206
device=resistor
m=1}
C {res.sym} -290 410 2 0 {name=R4
value=10
footprint=1206
device=resistor
m=1}
C {res.sym} -20 410 2 0 {name=R5
value=10
footprint=1206
device=resistor
m=1}
C {capa.sym} -530 310 1 0 {name=C2
m=1
value=500f
footprint=1206
device="ceramic capacitor"}
C {gnd.sym} -500 310 3 0 {name=l5 lab=GND}
C {capa.sym} -260 310 1 0 {name=C3
m=1
value=500f
footprint=1206
device="ceramic capacitor"}
C {gnd.sym} -230 310 3 0 {name=l9 lab=GND}
C {capa.sym} 10 310 1 0 {name=C4
m=1
value=500f
footprint=1206
device="ceramic capacitor"}
C {gnd.sym} 40 310 3 0 {name=l10 lab=GND}
C {capa.sym} 50 -190 1 0 {name=C5
m=1
value=500f
footprint=1206
device="ceramic capacitor"}
C {gnd.sym} 80 -190 3 0 {name=l11 lab=GND}
C {lab_wire.sym} -140 -10 0 0 {name=p7 sig_type=std_logic lab=(100*V_on_N[0],100*V_on_N[1],56*V_on_N[2])}
C {gnd.sym} -20 990 0 0 {name=l12 lab=GND}
C {gnd.sym} -290 990 0 0 {name=l13 lab=GND}
C {vsource.sym} -560 930 0 0 {name=VON4 value="dc 0 ac 0 PULSE(1.5 0 1n 100p 100p 4998n 10u)" savecurrent=true}
C {gnd.sym} -560 990 0 0 {name=l14 lab=GND}
C {vsource.sym} -290 940 0 0 {name=VON5 value="dc 0 ac 0 PULSE(1.5 0 1n 100p 100p 9.998u 20u)" savecurrent=true}
C {vsource.sym} -20 930 0 0 {name=VON6 value="dc 0 ac 0 PULSE(1.5 0 1n 10p 100p 100p 19.998u 30u)" savecurrent=true}
C {lab_wire.sym} -560 640 3 0 {name=p8 sig_type=std_logic lab=V_on_N[0]}
C {lab_wire.sym} -290 640 3 0 {name=p9 sig_type=std_logic lab=V_on_N[1]}
C {lab_wire.sym} -20 640 3 0 {name=p10 sig_type=std_logic lab=V_on_N[2]}
C {res.sym} -560 810 2 0 {name=R6
value=10
footprint=1206
device=resistor
m=1}
C {res.sym} -290 820 2 0 {name=R7
value=10
footprint=1206
device=resistor
m=1}
C {res.sym} -20 820 2 0 {name=R8
value=10
footprint=1206
device=resistor
m=1}
C {capa.sym} -530 720 1 0 {name=C1
m=1
value=500f
footprint=1206
device="ceramic capacitor"}
C {gnd.sym} -500 720 3 0 {name=l15 lab=GND}
C {capa.sym} -260 720 1 0 {name=C6
m=1
value=500f
footprint=1206
device="ceramic capacitor"}
C {gnd.sym} -230 720 3 0 {name=l16 lab=GND}
C {capa.sym} 10 720 1 0 {name=C7
m=1
value=500f
footprint=1206
device="ceramic capacitor"}
C {gnd.sym} 40 720 3 0 {name=l17 lab=GND}
