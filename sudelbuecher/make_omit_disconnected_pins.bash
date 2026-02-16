cd ../librelane/
librelane --pdk ihp-sg13g2 config.yaml -S OpenROAD.IRDropReport -S Checker.DisconnectedPins > >(tee make.out) 2> >(tee make.err >&2)

