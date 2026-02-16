###############################################################################
# Created by write_sdc
###############################################################################
current_design heichips25_pudding
###############################################################################
# Timing Constraints
###############################################################################
create_clock -name clk -period 10.0000 [get_ports {clk}]
set_propagated_clock [get_clocks {clk}]
set_input_delay 0.0000 -add_delay [get_ports {clk}]
set_input_delay 0.0000 -add_delay [get_ports {ena}]
set_input_delay 0.0000 -add_delay [get_ports {i_in}]
set_input_delay 0.0000 -add_delay [get_ports {i_out}]
set_input_delay 0.0000 -add_delay [get_ports {rst_n}]
set_input_delay 0.0000 -add_delay [get_ports {ui_in[0]}]
set_input_delay 0.0000 -add_delay [get_ports {ui_in[1]}]
set_input_delay 0.0000 -add_delay [get_ports {ui_in[2]}]
set_input_delay 0.0000 -add_delay [get_ports {ui_in[3]}]
set_input_delay 0.0000 -add_delay [get_ports {ui_in[4]}]
set_input_delay 0.0000 -add_delay [get_ports {ui_in[5]}]
set_input_delay 0.0000 -add_delay [get_ports {ui_in[6]}]
set_input_delay 0.0000 -add_delay [get_ports {ui_in[7]}]
set_input_delay 0.0000 -add_delay [get_ports {uio_in[0]}]
set_input_delay 0.0000 -add_delay [get_ports {uio_in[1]}]
set_input_delay 0.0000 -add_delay [get_ports {uio_in[2]}]
set_input_delay 0.0000 -add_delay [get_ports {uio_in[3]}]
set_input_delay 0.0000 -add_delay [get_ports {uio_in[4]}]
set_input_delay 0.0000 -add_delay [get_ports {uio_in[5]}]
set_input_delay 0.0000 -add_delay [get_ports {uio_in[6]}]
set_input_delay 0.0000 -add_delay [get_ports {uio_in[7]}]
set_output_delay 0.0000 -add_delay [get_ports {i_in}]
set_output_delay 0.0000 -add_delay [get_ports {i_out}]
set_output_delay 0.0000 -add_delay [get_ports {uio_oe[0]}]
set_output_delay 0.0000 -add_delay [get_ports {uio_oe[1]}]
set_output_delay 0.0000 -add_delay [get_ports {uio_oe[2]}]
set_output_delay 0.0000 -add_delay [get_ports {uio_oe[3]}]
set_output_delay 0.0000 -add_delay [get_ports {uio_oe[4]}]
set_output_delay 0.0000 -add_delay [get_ports {uio_oe[5]}]
set_output_delay 0.0000 -add_delay [get_ports {uio_oe[6]}]
set_output_delay 0.0000 -add_delay [get_ports {uio_oe[7]}]
set_output_delay 0.0000 -add_delay [get_ports {uio_out[0]}]
set_output_delay 0.0000 -add_delay [get_ports {uio_out[1]}]
set_output_delay 0.0000 -add_delay [get_ports {uio_out[2]}]
set_output_delay 0.0000 -add_delay [get_ports {uio_out[3]}]
set_output_delay 0.0000 -add_delay [get_ports {uio_out[4]}]
set_output_delay 0.0000 -add_delay [get_ports {uio_out[5]}]
set_output_delay 0.0000 -add_delay [get_ports {uio_out[6]}]
set_output_delay 0.0000 -add_delay [get_ports {uio_out[7]}]
set_output_delay 0.0000 -add_delay [get_ports {uo_out[0]}]
set_output_delay 0.0000 -add_delay [get_ports {uo_out[1]}]
set_output_delay 0.0000 -add_delay [get_ports {uo_out[2]}]
set_output_delay 0.0000 -add_delay [get_ports {uo_out[3]}]
set_output_delay 0.0000 -add_delay [get_ports {uo_out[4]}]
set_output_delay 0.0000 -add_delay [get_ports {uo_out[5]}]
set_output_delay 0.0000 -add_delay [get_ports {uo_out[6]}]
set_output_delay 0.0000 -add_delay [get_ports {uo_out[7]}]
###############################################################################
# Environment
###############################################################################
###############################################################################
# Design Rules
###############################################################################
