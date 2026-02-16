# Minimal SDC for heichips25_pudding
create_clock -name clk -period 10 [get_ports clk]

# Simple defaults for IO timing
set_input_delay  0 [all_inputs]
set_output_delay 0 [all_outputs]

