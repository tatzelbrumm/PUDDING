// Hard macro stub for OpenROAD/LibreLane
// Ensures instances 'dacL' and 'dacH' remain as macro instances.
// Yosys hints: blackbox + keep_hierarchy.
(* blackbox *)
module dac2u128out4in (
    input  [127:0] ON,
    input  [127:0] ON_N,
    input          EN,
    input          EN_N
);
    // no RTL — implemented by GDS/LEF
endmodule
