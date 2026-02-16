// File: inverterpair.sv
// SystemVerilog: simple ON - ON_N logic for the current mirrors

module inverterpair (
    input logic IN,
    output logic OUTN,
    output logic OUTP
);
(* keep *) sg13g2_inv_1 inv (.Y(OUTN), .A(IN));
(* keep *) sg13g2_buf_1 buff (.X(OUTP), .A(IN));
endmodule
