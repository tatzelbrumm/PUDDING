`default_nettype none
module sg13g2_inv_1 (
  output Y,
  input  A
);
  assign Y = ~A;
endmodule
`default_nettype wire

