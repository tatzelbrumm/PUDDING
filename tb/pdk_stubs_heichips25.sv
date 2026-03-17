// Simple simulation stubs for missing analog/PDK cells.
// These are NOT physically accurate; they exist only to let digital simulation elaborate.
`default_nettype none

// Sky130 / SG13G2 inverter cell stub
module sg13g2_inv_1(
    output wire Y,
    input  wire A
);
    assign Y = ~A;
endmodule

// 128-bit DAC macro stub
module dac128module(
    output wire       Iout,
    inout  wire [1:0] VcascP,
    inout  wire [1:0] VbiasP,
    input  wire [127:0] ON,
    input  wire [127:0] ONB,
    input  wire [3:0]   EN,
    input  wire [3:0]   ENB,
    input  wire         VDD,
    input  wire         VSS
);
    // Crude digital placeholder: drive Iout high if any ON bit is set and any EN bit is high.
    // (The real macro is analog/current-mode.)
    wire en_any  = |EN;
    wire on_any  = |ON;
    assign Iout  = en_any & on_any;
endmodule

// Analog wiring/bias network stub
module analog_wires(
    input  wire       Iout,
    inout  wire [1:0] VcascP,
    inout  wire [1:0] VbiasP,
    inout  wire       i_out,
    inout  wire       i_in,
    output wire [1:0] VDDA
);
    // Provide a stable value for VDDA so 'unused' reduction doesn't go X.
    assign VDDA = 2'b00;

    // Leave i_in/i_out/VcascP/VbiasP undriven (high-Z) in this stub.
    // If your TB checks these, replace with a more detailed behavioral model.
endmodule

`default_nettype wire
