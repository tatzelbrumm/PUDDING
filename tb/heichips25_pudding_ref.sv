// vibe coded reference model
// https://chatgpt.com/c/69991aec-4500-8384-9b56-c00368e7bbf9
`timescale 1ns/1ps
`default_nettype none

module heichips25_pudding_ref (
  input  logic [7:0] ui_in,
  output logic [7:0] uo_out,

  input  logic [7:0] uio_in,     // unused in your model, keep for interface match
  output logic [7:0] uio_out,
  output logic [7:0] uio_oe,

  input  logic       ena,        // unused in your model, keep for match
  input  logic       clk,
  input  logic       rst_n,
  inout  tri         i_in,        // unused
  inout  tri         i_out,       // unused
  input  logic       VPWR,        // unused
  input  logic       VGND         // unused
);

  logic [127:0] ref_daisychain;
  logic [127:0] ref_state;

  logic datum, shift, transfer, dir;

  always_comb begin
    datum    = ui_in[0];
    shift    = ui_in[1];
    transfer = ui_in[2];
    dir      = ui_in[3];
  end

  always_ff @(posedge clk) begin
    if (!rst_n) begin
      ref_daisychain <= '0;
      ref_state      <= '0;
    end else begin
      if (transfer) begin
        if (dir)
          ref_state <= ref_daisychain;
        else
          ref_daisychain <= ref_state;
      end else if (shift) begin
        ref_daisychain <= {ref_daisychain[126:0], datum};
      end
    end
  end

  always_comb begin
    // Match your comments/checks:
    uo_out  = ref_daisychain[127:120];
    uio_out = ref_state[127:120];
    uio_oe  = 8'hFF;
  end

endmodule

`default_nettype wire
