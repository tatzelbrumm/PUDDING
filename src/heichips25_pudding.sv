// SPDX-FileCopyrightText: © 2025 Luis Ardila, Jonas Buehler, Christoph Maier
// SPDX-License-Identifier: Apache-2.0

// Adapted from the Tiny Tapeout template
// 64 DAC sources only

`default_nettype none

module heichips25_pudding(
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (active high: 0=input, 1=output)
    input  wire       ena,      // always 1 when the design is powered, so you can ignore it
    input  wire       clk,      // clock
    input  wire       rst_n,    // reset_n - low to reset
    inout  wire       i_in,     // input (reference) current
    inout  wire       i_out,    // output (DAC) current
    inout VPWR,
    inout VGND
);

//(* keep = "yes" *) wire VPWR;
//(* keep = "yes" *) wire VGND;
   
    wire [7:0] iref;
    wire       dacout;
    wire       vssa;
    // List all unused inputs to prevent warnings
    wire _unused = &{uio_in[7:0], vssa, iref[7:0]};

    logic[3:0] dacen0, dacenp0, dacenn0;
    logic[3:0] dacen1, dacenp1, dacenn1;
    logic[3:0] dacen2, dacenp2, dacenn2;
    logic[3:0] dacen3, dacenp3, dacenn3;

    logic datum, shift, transfer, dir;

    logic[127:0] daisychain;
    logic[127:0] state;

    assign datum    = ui_in[0];
    assign shift    = ui_in[1];
    assign transfer = ui_in[2];
    assign dir      = ui_in[3];

    assign dacen0 = {4{ui_in[4]}};
    assign dacen1 = {4{ui_in[5]}};
    assign dacen2 = {4{ui_in[6]}};
    assign dacen3 = {4{ui_in[7]}};

    always_ff @(posedge clk or negedge rst_n) 
    begin
        if (!rst_n) 
        begin
            daisychain <= '0;
            state <= '0;
        end 
        else 
        begin
            if (transfer) 
            begin
                if (dir)
                    state <= daisychain;
                else
                    daisychain <= state;
            end
            else if (shift)
            begin
                daisychain <= {daisychain[126:0],datum};
            end
        end
    end

    
assign uo_out  = daisychain[127:120];
assign uio_out = state[127:120];
assign uio_oe  = {8{ena}};

    digital4 digitalen0 (
    .in(dacen0[3:0]),
    .outp(dacenp0[3:0]),
    .outn(dacenn0[3:0])
    );

    digital4 digitalen1 (
    .in(dacen1[3:0]),
    .outp(dacenp1[3:0]),
    .outn(dacenn1[3:0])
    );

    digital4 digitalen2 (
    .in(dacen2[3:0]),
    .outp(dacenp2[3:0]),
    .outn(dacenn2[3:0])
    );

    digital4 digitalen3 (
    .in(dacen3[3:0]),
    .outp(dacenp3[3:0]),
    .outn(dacenn3[3:0])
    );


(* keep_hierarchy = "yes", keep = "yes" *) dac4x32module dac (
    .Iout(i_out),
    .VbiasP(iref[7:0]),
    .ON(state[127:0]),
    .ONB(~state[127:0]),
    .EN({dacenp3[3:0],dacenp2[3:0],dacenp1[3:0],dacenp0[3:0]}),
    .ENB({dacenn3[3:0],dacenn2[3:0],dacenn1[3:0],dacenn0[3:0]}),
    .VDD(VPWR),
    .VSS(VGND)
    );

(* keep_hierarchy = "yes", keep = "yes" *) input_mirror wires (
    .VbiasP(iref),
    .i_out(i_out),
    .i_in(i_in),
    .VSSA(vssa)
    );
endmodule

module digital4(
    input  logic [3:0] in,
    output logic [3:0] outn,
    output logic [3:0] outp
);
    // 16 instances, each bit wired to one instance
  genvar i;
      for (i = 0; i < 4; i++) begin : g
          inverterpair u (
              .IN   (in[i]),
              .OUTN (outn[i]),
              .OUTP (outp[i])
          );
  end
endmodule

// File: inverterpair.sv
// SystemVerilog: simple ON - ON_N logic for the current mirrors

module inverterpair (
    input logic IN,
    output logic OUTN,
    output logic OUTP
);
(* keep *) sg13g2_inv_1 inv1 (.Y(OUTN), .A(IN));
(* keep *) sg13g2_inv_1 inv2 (.Y(OUTP), .A(OUTN));
endmodule
