v {xschem version=3.4.7 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 300 -480 320 -480 {lab=VDD}
N 320 -400 320 -280 {lab=VDD}
N 300 -280 320 -280 {lab=VDD}
N 300 -400 320 -400 {lab=VDD}
N 320 -480 320 -400 {lab=VDD}
N 300 -480 300 -430 {lab=VDD}
N 160 -480 300 -480 {lab=VDD}
N 300 -250 300 -200 {lab=Vbpcasc}
N 160 -200 300 -200 {lab=Vbpcasc}
N 300 -340 300 -310 {lab=Vcasc}
N 300 -340 420 -340 {lab=Vcasc}
N 300 -370 300 -340 {lab=Vcasc}
N 160 -400 260 -400 {lab=off_n}
N 160 -280 260 -280 {lab=on_n}
C {sg13g2_pr/sg13_lv_pmos.sym} 280 -400 0 0 {name=Mpullup
l=0.13u
w=0.3u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
C {sg13g2_pr/sg13_lv_pmos.sym} 280 -280 0 0 {name=Mbias
l=0.13u
w=0.3u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
C {ipin.sym} 160 -400 0 0 {name=p1 lab=off_n}
C {ipin.sym} 160 -200 0 0 {name=p2 lab=Vbpcasc}
C {opin.sym} 420 -340 0 0 {name=p6 lab=Vcasc}
C {ipin.sym} 160 -280 0 0 {name=p5 lab=on_n}
C {ipin.sym} 160 -480 0 0 {name=p3 lab=VDD}
C {title.sym} 160 0 0 0 {name=l1 author="Christoph Maier"}
