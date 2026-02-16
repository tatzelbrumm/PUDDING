// File: non_overlap.sv
// SystemVerilog: non overlaping ON - ON_N logic for the current mirrors

module non_overlap #(
	parameter int IN_WIDTH = 256
) (
	input logic [IN_WIDTH-1:0] thermo,
	output logic [IN_WIDTH-1:0] ON,
	output logic [IN_WIDTH-1:0] ON_N
);
	
	// Combinatorial generation of non overlaping inverted logic
	for (genvar i = 0; i < IN_WIDTH; i++) begin : comb_logic
		(* keep *) wire inv_in;
		
		(* keep *) wire xnor_outa;
		(* keep *) wire inv0a; 
		(* keep *) wire inv1a; 
		(* keep *) wire inv2a; 
		(* keep *) wire inv3a; 
		(* keep *) wire inv4a;
		(* keep *) wire inv5a; 
			
		(* keep *) wire xnor_outb;
		(* keep *) wire inv0b; 
		(* keep *) wire inv1b; 
		(* keep *) wire inv2b; 
		(* keep *) wire inv3b; 
		(* keep *) wire inv4b;
		(* keep *) wire inv5b; 
		
		(* keep *) not u_inv_in (inv_in, thermo[i]);
		
		(* keep *) xnor u_xnor_outa (xnor_outa, thermo[i], inv4b);
		(* keep *) not u_inv0a (inv0a, xnor_outa);
		(* keep *) not u_inv1a (inv1a, inv0a);
		(* keep *) not u_inv2a (inv2a, inv1a);
		(* keep *) not u_inv3a (inv3a, inv2a);
		(* keep *) not u_inv4a (inv4a, inv3a);
		(* keep *) not u_inv5a (inv5a, inv4a);
		
		(* keep *) xnor u_xnor_outb (xnor_outb, inv_in, inv4a);
		(* keep *) not u_inv0b (inv0b, xnor_outb);
		(* keep *) not u_inv1b (inv1b, inv0b);
		(* keep *) not u_inv2b (inv2b, inv1b);
		(* keep *) not u_inv3b (inv3b, inv2b);
		(* keep *) not u_inv4b (inv4b, inv3b);
		(* keep *) not u_inv5b (inv5b, inv4b);
		
		assign ON[i] = inv5a;
		assign ON_N[i] = inv5b;
	end
	
endmodule