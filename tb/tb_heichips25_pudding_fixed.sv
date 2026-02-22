`timescale 1ns/1ps
`default_nettype none

module tb_heichips25_pudding;

  // ----------------------------
  // Clk / reset
  // ----------------------------
  logic clk = 1'b0;
  always #5 clk = ~clk; // 100 MHz

  logic rst_n;

  // ----------------------------
  // DUT ports
  // ----------------------------
  logic  [7:0] ui_in;
  wire   [7:0] uo_out;

  logic  [7:0] uio_in;
  wire   [7:0] uio_out;
  wire   [7:0] uio_oe;

  logic ena;

  // inouts (analog-ish)
  tri i_in;
  tri i_out;

  // power pins
  logic VPWR;
  logic VGND;

  // ----------------------------
  // Instantiate DUT
  // ----------------------------
  heichips25_pudding dut (
    .ui_in  (ui_in),
    .uo_out (uo_out),
    .uio_in (uio_in),
    .uio_out(uio_out),
    .uio_oe (uio_oe),
    .ena    (ena),
    .clk    (clk),
    .rst_n  (rst_n),
    .i_in   (i_in),
    .i_out  (i_out),
    .VPWR   (VPWR),
    .VGND   (VGND)
  );

  // ----------------------------
  // Reference model (mirrors DUT always_ff)
  // ----------------------------
  logic [127:0] ref_daisychain;
  logic [127:0] ref_state;

  // Convenience aliases for ui_in bits
  logic datum, shift, transfer, dir;
  logic stateen;

  always_comb begin
    datum    = ui_in[0];
    shift    = ui_in[1];
    transfer = ui_in[2];
    dir      = ui_in[3];
    stateen  = ui_in[4];
  end

  // Reference model update at posedge
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

  // ----------------------------
  // Checks
  // ----------------------------
  // Dedicated outputs: uo_out = daisychain[127:120]
  // IO outputs:       uio_out = state[127:120]
  // IO enable:        uio_oe = 8'hFF
  always_ff @(posedge clk) begin
    if (rst_n) begin
      // uio_oe should always be driven
      assert (uio_oe === 8'hFF)
        else $fatal(1, "[TB] uio_oe mismatch: got %02h exp FF @%0t", uio_oe, $time);

      assert (uo_out === ref_daisychain[127:120])
        else $fatal(1, "[TB] uo_out mismatch: got %02h exp %02h @%0t",
                    uo_out, ref_daisychain[127:120], $time);

      assert (uio_out === ref_state[127:120])
        else $fatal(1, "[TB] uio_out mismatch: got %02h exp %02h @%0t",
                    uio_out, ref_state[127:120], $time);
    end
  end

  // ----------------------------
  // Stimulus tasks
  // ----------------------------
  task automatic apply_idle();
    ui_in   <= '0;
    uio_in  <= '0;
    ena     <= 1'b1;
  endtask

  task automatic pulse_shift(input logic bitval);
    // shift is sampled at posedge; transfer has priority over shift in DUT
    @(negedge clk);
    ui_in[0] <= bitval; // datum
    ui_in[1] <= 1'b1;   // shift
    ui_in[2] <= 1'b0;   // transfer
    ui_in[3] <= 1'b0;   // dir don't care
    ui_in[4] <= 1'b1;   // stateen (doesn't affect the shift/state regs, but keep it asserted)
    @(negedge clk);
    ui_in[1] <= 1'b0;   // deassert shift
  endtask

  task automatic pulse_transfer(input logic dirval);
    @(negedge clk);
    ui_in[1] <= 1'b0;   // shift
    ui_in[2] <= 1'b1;   // transfer
    ui_in[3] <= dirval; // dir
    ui_in[4] <= 1'b1;   // stateen
    @(negedge clk);
    ui_in[2] <= 1'b0;   // deassert transfer
  endtask

  task automatic load_daisychain_lsb_first(input logic [127:0] payload);
    // Because DUT shifts: daisychain <= {daisychain[126:0], datum}
    // the first bit you send ends up at bit 0 after 1 shift, and eventually walks up.
    // This task sends payload[127] last; i.e., bit order is payload[0], payload[1], ...
    for (int i = 0; i < 128; i++) begin
      pulse_shift(payload[i]);
    end
  endtask

  // ----------------------------
  // Main test sequence
  // ----------------------------
  initial begin
    logic [127:0] pattern_a;
    int sel;

    // init
    ui_in  = '0;
    uio_in = '0;
    ena    = 1'b1;

    // power
    VPWR = 1'b1;
    VGND = 1'b0;

    // reset
    rst_n = 1'b0;
    repeat (3) @(posedge clk);
    rst_n = 1'b1;
    @(posedge clk);

    // 1) Directed test: shift in a known pattern, transfer to state, transfer back
    pattern_a = 128'h0123_4567_89ab_cdef_fedc_ba98_7654_3210;

    $display("[TB] Loading daisychain pattern A via shift...");
    load_daisychain_lsb_first(pattern_a);

    $display("[TB] Transfer daisychain -> state (dir=1)...");
    pulse_transfer(1'b1);

    $display("[TB] Clear daisychain by reset-like behavior? No reset used; transfer back should restore it anyway.");
    // Change daisychain contents by shifting a few bits, then restore from state:
    repeat (10) pulse_shift($urandom_range(0,1));

    $display("[TB] Transfer state -> daisychain (dir=0)...");
    pulse_transfer(1'b0);

    // 2) Randomized regress: random mix of shift/transfer/idle
    $display("[TB] Random stimulus phase...");
    for (int k = 0; k < 500; k++) begin
      sel = $urandom_range(0, 9);
      case (sel)
        0,1,2,3,4,5: begin
          pulse_shift($urandom_range(0,1));
        end
        6,7: begin
          pulse_transfer($urandom_range(0,1));
        end
        default: begin
          // idle cycle(s)
          @(negedge clk);
          ui_in[1] <= 1'b0;
          ui_in[2] <= 1'b0;
          ui_in[4] <= 1'b1;
        end
      endcase
    end

    $display("[TB] PASS");
    $finish;
  end

endmodule

`default_nettype wire

