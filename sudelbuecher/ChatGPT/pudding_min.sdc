# Minimal SDC for heichips25_pudding
create_clock -name clk -period 10 [get_ports clk]
set_input_delay  0 [all_inputs]
set_output_delay 0 [all_outputs]
# Prevent flattening away black-boxes (belt-and-suspenders; may be ignored by some steps)
