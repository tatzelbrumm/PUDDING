// File: analog_wires.v
// analog wires (etc.) digital placeholder
// Yosys hints: blackbox + keep_hierarchy.
(* blackbox *)
module analog_wires (
    inout Iout,
    inout [1:0] VcascP,
    inout [1:0] VbiasP,
    inout i_in,
    inout i_out,
    inout [1:0] VDDA
);

    wire bias;
    wire casc;
    wire vdda;

    assign VbiasP[0] = bias;
    assign VbiasP[1] = bias;
    assign VcascP[0] = casc;
    assign VcascP[1] = casc;
    assign VDDA[1] = vdda;
    assign VDDA[0] = vdda;
endmodule
