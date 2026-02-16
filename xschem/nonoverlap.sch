v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 420 -120 620 -120 {lab=VSS}
N 620 -520 620 -490 {lab=VDD}
N 600 -520 620 -520 {lab=VDD}
N 420 -520 420 -490 {lab=VDD}
N 80 -520 420 -520 {lab=VDD}
N 600 -460 620 -460 {lab=VDD}
N 600 -520 600 -460 {lab=VDD}
N 440 -520 600 -520 {lab=VDD}
N 420 -460 440 -460 {lab=VDD}
N 440 -520 440 -460 {lab=VDD}
N 420 -520 440 -520 {lab=VDD}
N 660 -460 680 -460 {lab=INN}
N 680 -460 680 -400 {lab=INN}
N 620 -150 620 -120 {lab=VSS}
N 620 -180 640 -180 {lab=VSS}
N 640 -180 640 -120 {lab=VSS}
N 620 -120 640 -120 {lab=VSS}
N 400 -180 420 -180 {lab=VSS}
N 400 -180 400 -120 {lab=VSS}
N 80 -120 400 -120 {lab=VSS}
N 420 -150 420 -120 {lab=VSS}
N 400 -120 420 -120 {lab=VSS}
N 420 -260 420 -210 {lab=OUTN}
N 620 -260 620 -210 {lab=OUTP}
N 420 -360 740 -360 {lab=OUTN}
N 420 -430 420 -360 {lab=OUTN}
N 620 -320 740 -320 {lab=OUTP}
N 620 -430 620 -320 {lab=OUTP}
N 460 -180 480 -180 {lab=OUTP}
N 480 -180 560 -260 {lab=OUTP}
N 560 -260 620 -260 {lab=OUTP}
N 620 -320 620 -260 {lab=OUTP}
N 560 -180 580 -180 {lab=OUTN}
N 480 -260 560 -180 {lab=OUTN}
N 420 -260 480 -260 {lab=OUTN}
N 420 -360 420 -260 {lab=OUTN}
N 80 -400 680 -400 {lab=INN}
N 80 -460 380 -460 {lab=INP}
C {iopin.sym} 80 -120 2 0 {name=p1 lab=VSS}
C {iopin.sym} 80 -520 2 0 {name=p2 lab=VDD}
C {ipin.sym} 80 -460 0 0 {name=p3 lab=INP}
C {ipin.sym} 80 -400 0 0 {name=p4 lab=INN}
C {opin.sym} 740 -320 0 0 {name=p5 lab=OUTP}
C {opin.sym} 740 -360 0 0 {name=p6 lab=OUTN}
C {title.sym} 160 0 0 0 {name=l1 author="Christoph Maier"}
C {sg13g2_pr/sg13_lv_pmos.sym} 400 -460 0 0 {name=M1
l=0.13u
w=0.3u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
C {sg13g2_pr/sg13_lv_pmos.sym} 640 -460 0 1 {name=M2
l=0.13u
w=0.3u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
C {sg13g2_pr/sg13_lv_nmos.sym} 440 -180 0 1 {name=M3
l=0.52u
w=0.15u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
C {sg13g2_pr/sg13_lv_nmos.sym} 600 -180 0 0 {name=M4
l=0.52u
w=0.15u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
