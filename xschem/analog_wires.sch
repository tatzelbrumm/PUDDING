v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 360 -320 400 -320 {lab=vdda}
N 440 -320 440 -280 {lab=vdda}
N 400 -320 440 -320 {lab=vdda}
N 470 -280 480 -280 {lab=vdda}
N 480 -320 480 -280 {lab=vdda}
N 440 -320 480 -320 {lab=vdda}
N 400 -280 410 -280 {lab=vdda}
N 400 -320 400 -280 {lab=vdda}
N 320 -320 320 -280 {lab=vdda}
N 280 -320 320 -320 {lab=vdda}
N 350 -280 360 -280 {lab=vdda}
N 360 -320 360 -280 {lab=vdda}
N 320 -320 360 -320 {lab=vdda}
N 280 -280 290 -280 {lab=vdda}
N 280 -320 280 -280 {lab=vdda}
N 220 -220 320 -220 {lab=pbias}
N 320 -240 320 -220 {lab=pbias}
N 220 -320 280 -320 {lab=vdda}
N 220 -120 440 -120 {lab=pcbias}
N 440 -260 440 -120 {lab=pcbias}
C {title.sym} 160 0 0 0 {name=l1 author="Christoph Maier"}
C {sg13g2_pr/sg13_hv_pmos.sym} 440 -260 1 1 {name=Mcbuffer
l=8u
w=8u
ng=1
m=19
model=sg13_hv_pmos
spiceprefix=X
}
C {sg13g2_pr/sg13_hv_pmos.sym} 320 -260 1 1 {name=Mbbuffer
l=8u
w=8u
ng=1
m=19
model=sg13_hv_pmos
spiceprefix=X
}
C {iopin.sym} 220 -320 0 1 {name=p3 lab=vdda}
C {iopin.sym} 220 -120 0 1 {name=p6 lab=pcbias}
C {iopin.sym} 220 -220 0 1 {name=p8 lab=pbias}
C {lab_wire.sym} 380 -320 0 0 {name=p10 sig_type=std_logic lab=vdda}
