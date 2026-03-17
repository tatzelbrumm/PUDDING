// File: input_mirror.v
// input current mirror (etc.) digital placeholder
// Yosys hints: blackbox + keep_hierarchy.
(* blackbox *)
module input_mirror (
    inout [7:0] VbiasP,
    inout       i_in,
    inout       i_out,
    inout [1:0] VSSA
);

//  wire bias;
//  wire casc;
//  wire vdda;
    wire vssa;

//  assign VbiasP[0] = bias;
//  assign VbiasP[1] = bias;
//  assign VcascP[0] = casc;
//  assign VcascP[1] = casc;
//  assign VDDA[3] = vdda;
//  assign VDDA[2] = vdda;
//  assign VDDA[1] = vdda;
//  assign VDDA[0] = vdda;
    assign VSSA[1] = vssa;
    assign VSSA[0] = vssa;
endmodule
