// File: thermometer_encoder.sv
// SystemVerilog: 8 bit to thermometer code encoder 
// Default: OUT_WIDTH = (2^IN_WIDTH) = 256 bit for IN_WIDTH = 8

module thermometer_encoder #(
	parameter int IN_WIDTH = 8,
	parameter int OUT_WIDTH = (1 << IN_WIDTH)
) (
	input logic [IN_WIDTH-1:0] din,
	output logic [OUT_WIDTH-1:0] thermo
);
	initial  thermo = 0;
	// Combinatorial generation of thermometer bits
	always_comb begin 
		for (int i = 0; i < OUT_WIDTH; i++) begin
			thermo[i] = (din >= i);	
		end
	end
endmodule
