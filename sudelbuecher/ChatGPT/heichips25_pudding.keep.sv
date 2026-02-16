// SPDX-FileCopyrightText: © 2025 Luis Ardila, Jonas Buehler, Christoph Maier
// SPDX-License-Identifier: Apache-2.0

// Adapted from the Tiny Tapeout template

`default_nettype none

module heichips25_pudding(
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (active high: 0=input, 1=output)
    input  wire       ena,      // always 1 when the design is powered, so you can ignore it
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);

    // List all unused inputs to prevent warnings
    wire _unused = &{ena, uio_in[7:0], ui_in[7:4]};

    logic datum, shift, transfer, dir;

    logic[127:0] daisychain;
    logic[127:0] state;

    assign datum    = ui_in[0];
    assign shift    = ui_in[1];
    assign transfer = ui_in[2];
    assign dir      = ui_in[3];

    always_ff @(posedge clk) 
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
assign uio_oe  = 8'hFF;

(* keep_hierarchy = "yes", keep = "yes" *) dac2u128out4in dacL (
    .ON(state[127:0]),
    .ON_N(~state[127:0]),
    .EN(ena),
    .EN_N(~ena)
);

(* keep_hierarchy = "yes", keep = "yes" *) dac2u128out4in dacH (
    .ON(daisychain[127:0]),
    .ON_N(~daisychain[127:0]),
    .EN(ena),
    .EN_N(~ena)
);

endmodule
