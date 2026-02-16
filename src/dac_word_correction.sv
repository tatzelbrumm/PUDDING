
module dac_cal #(
  parameter int RAW_WIDTH   = 8,
  parameter int SEGMENTS    = 8,
  parameter int FRACT_BITS  = 8,
  parameter int signed A0_Counts [0:SEGMENTS-1] = '{0,1,-1,2,-2,0,0,0},
  parameter int signed A1_Q8_8   [0:SEGMENTS-1] = '{256,250,256,262,248,264,256,256}
) (
  input  logic                     clk,
  input  logic                     reset,
  input  logic                     enable,   // 1=calibrate, 0=bypass
  input  logic [RAW_WIDTH-1:0]     raw_code,
  output logic [RAW_WIDTH-1:0]     out_code
);

  localparam int MAX_CD = (1<<RAW_WIDTH) - 1;
  localparam int SEG_W  = (MAX_CD + 1) / SEGMENTS;

  logic signed [31:0]   line_v;
  logic signed [31:0]   result_i;
  int                    D;
  int                    seg;

  always_ff @(posedge clk or posedge reset) begin
    if (reset) begin
      out_code <= '0;
    end else begin
      if (!enable) begin
        out_code <= raw_code;
      end else begin
        D   = raw_code;
        seg = D / SEG_W;
        if (seg >= SEGMENTS) seg = SEGMENTS - 1;

        // affine: offset + (gain * D) >> FRACT_BITS
        line_v = A0_Counts[seg] + ((A1_Q8_8[seg] * D) >>> FRACT_BITS);
        result_i = line_v;

        // clamp
        if (result_i < 0)
          result_i = 0;
        else if (result_i > MAX_CD)
          result_i = MAX_CD;

        out_code <= result_i;
      end
    end
  end

endmodule