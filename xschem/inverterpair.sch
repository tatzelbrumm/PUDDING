v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 120 -200 180 -200 {lab=IN}
N 120 -80 170 -80 {lab=VSS}
N 120 -120 170 -120 {lab=VDD}
N 300 -200 340 -200 {lab=OUTN}
N 420 -200 480 -200 {lab=OUTP}
N 300 -200 300 -120 {lab=OUTN}
N 260 -200 300 -200 {lab=OUTN}
N 300 -120 480 -120 {lab=OUTN}
C {iopin.sym} 120 -80 2 0 {name=p1 lab=VSS}
C {ipin.sym} 120 -200 0 0 {name=p3 lab=IN}
C {opin.sym} 480 -120 0 0 {name=p4 lab=OUTN}
C {opin.sym} 480 -200 0 0 {name=p5 lab=OUTP}
C {iopin.sym} 120 -120 2 0 {name=p2 lab=VDD}
C {title.sym} 160 0 0 0 {name=l1 author="Christoph Maier"}
C {lab_wire.sym} 170 -80 0 0 {name=p8 sig_type=std_logic lab=VSS}
C {lab_wire.sym} 170 -120 0 0 {name=p9 sig_type=std_logic lab=VDD}
C {devices/code_shown.sym} 240 -70 0 0 {name=MODEL only_toplevel=true
format="tcleval( @value )"
value=".lib cornerMOSlv.lib mos_tt
"}
C {sg13g2_stdcells/sg13g2_inv_1.sym} 380 -200 0 0 {name=xinv2 VDD=VDD VSS=VSS prefix=sg13g2_ }
C {sg13g2_stdcells/sg13g2_inv_1.sym} 220 -200 0 0 {name=xinv1 VDD=VDD VSS=VSS prefix=sg13g2_ }
