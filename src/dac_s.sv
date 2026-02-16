//`define sim

`define G 10

`ifdef sim
`define TI input real
`define TO output real
`define TOx output real
`define TT real
`else
//`define TI inout
//`define TO inout
`define TI input
`define TO output
`define TOx input
`define TT wire
`endif

module mirror #(parameter w=1)(
`TI supply, 
`TI bias, 
`TO iout
);
`ifdef sim
assign iout=bias*w;
`endif
endmodule



module mirror_ref #(parameter w=1)(
`TI supply, 
`TI bias, 
`TI vout
);
endmodule


module switch
(input a, b, 
`TI iin, 
`TOx iout
);
`ifdef sim
assign iout = (a==1)? iin : 0.0;
`endif
endmodule


`ifdef sim
module sum #(parameter N=2)
(	
`TI  iin [N-1:0],
`TO iout
);
    
int ii[N], ss;

always@* begin
  //for (int i=0; i<N; i++) ii[i]=$realtobits(iin[i]);
  for (int i=0; i<N; i++) ii[i]=iin[i];
end

always@* begin
  //ss=$realtobits(0.0);
  ss=0;
  for (int i=0; i<N; i++) ss=ss+ii[i];
end

assign iout=ss;
endmodule
`endif


module dac #(parameter N=2)
(	
input logic [N-1:0] a, b,
`TI supply, bias, 
`TOx iout
);

//`TT w [N-1:0] ; //!!

mirror_ref m_0 ( .supply(supply), .bias(bias), .vout(bias) );
genvar i;

`ifdef sim
`TT r_io[N-1:0] ;
`endif
generate
for (i = 0; i < N; i = i + 1) begin
  `TT ww;
  mirror #(.w(1)) m_i ( .supply(supply), .bias(bias), .iout(ww) );

  switch s_i (.a(a[i]), .b(b[i]), .iin(ww), 
  `ifdef sim  
  .iout(r_io[i]) 
  `else
  .iout(iout)
  `endif
  );
end
endgenerate

`ifdef sim
sum #(.N(N)) sum_inst (.iin(r_io), .iout(iout));
`endif

endmodule



module dac_ctrl #(
parameter N=4, //no of steps
parameter nb=$clog2(N)
)
(
  input logic [nb-1:0] dacin,
  `TI supply, bias, 
  `TOx iout
);

logic [N-2:0] a,b;
always@* for(int i=0; i<(N-1); i++) begin a[i]=(i<dacin); b[i]=~a[i]; end 
dac #(.N(N-1)) dac_inst (.a(a), .b(b), .supply(supply), .bias(bias), .iout(iout));
endmodule


`ifdef do_not_use
module tb1 #(parameter N=4) ();
parameter nb=$clog2(N);

logic [nb-1:0] dacin ;
`TT supply, bias, iout;
  
dac_ctrl #(.N(N)) dc (
  .dacin(dacin),
  .supply(supply), 
  .bias(bias), 
  .iout(iout)
);

assign supply = 1.8;
assign bias = `G;

initial begin
  for (int i=0;i<N;i++) begin
    dacin=i;
    #10us;
  end
end

endmodule
`endif

module digtop #(parameter N=4)(
  input logic r_Clk,
  input logic r_Rst_L,

  input  logic w_SPI_Clk,
  input  logic w_SPI_CS_n,
  input  logic w_SPI_MOSI,
  output logic w_SPI_MISO,
  
  `TOx iout,
  
  
  output [7:0] uo_out,
  input  [7:3] ui_in,
  output [7:1] uio_out, 
  input  [7:0] uio_in,
  output [7:1] uio_oe,
  input        ena
);

  // List all unused inputs to prevent warnings
  wire _unused = &{ena, ui_in, uio_in};
  assign {uo_out, uio_out, uio_oe}='0;

  parameter SPI_MODE = 1; // CPOL = 0, CPHA = 1

  logic       w_Slave_RX_DV, r_Slave_TX_DV;
  logic [7:0] w_Slave_RX_Byte, w_Slave_TX_Byte;

  SPI_Slave #(.SPI_MODE(SPI_MODE)) SPI_Slave_UUT
  (
   // Control/Data Signals,
   .i_Rst_L(r_Rst_L),            // Reset
   .i_Clk(r_Clk),                // Clock
   .o_RX_DV(w_Slave_RX_DV),      // Data Valid pulse (1 clock cycle)
   .o_RX_Byte(w_Slave_RX_Byte),  // Byte received on MOSI
   .i_TX_DV(w_Slave_RX_DV),      // Data Valid pulse
   .i_TX_Byte(w_Slave_TX_Byte),  // Byte to serialize to MISO

   // SPI Interface
   .i_SPI_Clk(w_SPI_Clk),
   .o_SPI_MISO(w_SPI_MISO),
   .i_SPI_MOSI(w_SPI_MOSI),
   .i_SPI_CS_n(w_SPI_CS_n)
   );

`ifdef sim
initial begin
w_Slave_TX_Byte=8'h00;
r_Slave_TX_DV=1'b0;
repeat(10) @(posedge w_SPI_Clk);

repeat(10) @(posedge r_Clk);
w_Slave_TX_Byte=8'h55;
r_Slave_TX_DV=1'b1;
repeat(1) @(posedge r_Clk);
r_Slave_TX_DV=1'b0;
repeat(100) @(posedge w_SPI_Clk);

repeat(10) @(posedge r_Clk);
w_Slave_TX_Byte=8'hAA;
r_Slave_TX_DV=1'b1;
repeat(1) @(posedge r_Clk);
r_Slave_TX_DV=1'b0;

end
`else
assign w_Slave_TX_Byte=8'h00;
assign r_Slave_TX_DV=1'b0;
`endif

parameter nb=$clog2(N);
logic [23:0] datain;
logic [23:6] datain_;

always @(posedge r_Clk or negedge r_Rst_L) begin
  if (~r_Rst_L) begin
    datain_ <= '0;
    datain <= '0;
  end else if (w_Slave_RX_DV) begin
    case (w_Slave_RX_Byte[7:6])
    'd0:     datain<={datain_, w_Slave_RX_Byte[5:0]};
    'd1:     datain_[11: 6] <= w_Slave_RX_Byte[5:0];
    'd2:     datain_[17:12] <= w_Slave_RX_Byte[5:0];
    default: datain_[23:18] <= w_Slave_RX_Byte[5:0];
    endcase
  end
end


//`TT supply, bias, iout;
`TT supply, bias;

`ifdef sim
assign supply = 1.8;
assign bias = `G;
`else
assign supply = 1; //!!
assign bias = 1;
`endif


dac_ctrl #(.N(N)) dc (
  .dacin(datain[nb-1:0]),
  .supply(supply), 
  .bias(bias), 
  .iout(iout)
);

endmodule




//500x200um, 500X415um
module heichips25_pudding #(parameter N=256)(
input  [7:0] ui_in,
output [7:0] uo_out,
input  [7:0] uio_in,
output [7:0] uio_out,
output [7:0] uio_oe,
input  ena,
input  clk,
input  rst_n

// Dedicated pins
//,`TOx iout

);

`ifdef sim
`TT iout;
`endif

digtop #(.N(N)) dut(
  /* input logic */ .r_Clk        (clk),
  /* input logic */ .r_Rst_L      (rst_n),

  /* input  logic */ .w_SPI_CS_n  (ui_in[0]),
  /* input  logic */ .w_SPI_Clk   (ui_in[1]),
  /* input  logic */ .w_SPI_MOSI  (ui_in[2]),
  /* output logic */ .w_SPI_MISO  (uio_out[0]),

`ifdef sim
  /* `TOx */         .iout        (iout),
`else
  /* `TOx */         .iout        (ena),
`endif
  
  /* output [7:0] */ .uo_out      (uo_out[7:0]),
  /* input [7:3]  */ .ui_in       (ui_in[7:3]),
  /* output [7:1] */ .uio_out     (uio_out[7:1]), 
  /* input  [7:0] */ .uio_in      (uio_in[7:0]),
  /* output [7:1] */ .uio_oe      (uio_oe[7:1]),
  /* input        */ .ena         (ena)
);

assign uio_oe[0] = ~ui_in[0]; //tristate MISO when w_SPI_CS_n=1

// List all unused inputs to prevent warnings
//wire _unused = &{ena, ui_in[7:3], uio_in[7:0]};
//assign { uo_out[7:1] , uio_out[7:0], uio_oe[7:0]}='0;

endmodule




`ifdef sim
module tb ();
  parameter N = 256;
  parameter SPI_MODE = 1; // CPOL = 0, CPHA = 1
  parameter SPI_CLK_DELAY = 20;  // 2.5 MHz
  parameter MAIN_CLK_DELAY = 2;  // 25 MHz

  logic [7:0] dataPayload[0:255]; 
  logic [7:0] dataLength;
  
  logic r_Rst_L= 1'b0;
  logic r_Clk=1'b0;
  always #(MAIN_CLK_DELAY) r_Clk = ~r_Clk;

  logic w_SPI_MISO;
  logic [7:0] r_Master_RX_Byte;
  logic       w_Slave_RX_DV, r_Slave_TX_DV;
  logic [7:0] w_Slave_RX_Byte, r_Slave_TX_Byte;
  logic [7:0] r_Master_TX_Byte = 0;
  logic r_Master_TX_DV = 1'b0;
  logic r_Master_CS_n;

`ifdef use_digtop
digtop #(.N(N)) dut(
  /* input logic */ .r_Clk        (r_Clk),
  /* input logic */ .r_Rst_L      (r_Rst_L),

  /* input  logic */ .w_SPI_Clk   (w_SPI_Clk),
  /* input  logic */ .w_SPI_CS_n  (r_Master_CS_n),
  /* input  logic */ .w_SPI_MOSI  (w_SPI_MOSI),
  /* output logic */ .w_SPI_MISO  (w_SPI_MISO)
);
`else
wire [7:0] uo_out, uio_out, uio_oe;
wire ena;
assign ena=1'b0;
assign w_SPI_MISO=uio_oe[0]?uio_out[0] :  1'bZ;
heicips25_template #(.N(N))  dut(
/* input  [7:0] */ .ui_in   ({5'd0, w_SPI_MOSI, w_SPI_Clk, r_Master_CS_n}),
/* output [7:0] */ .uo_out  (uo_out),
/* input  [7:0] */ .uio_in  (8'b0),
/* output [7:0] */ .uio_out (uio_out),
/* output [7:0] */ .uio_oe  (uio_oe),
/* input        */ .ena     (ena),
/* input        */ .clk     (r_Clk),
/* input        */ .rst_n   (r_Rst_L)
);
`endif

// Instantiate Master to drive Slave
  SPI_Master 
  #(.SPI_MODE(SPI_MODE),
    .CLKS_PER_HALF_BIT(2)) SPI_Master_UUT
  (
   // Control/Data Signals,
   .i_Rst_L(r_Rst_L),     // FPGA Reset
   .i_Clk(r_Clk),         // FPGA Clock
   
   // TX (MOSI) Signals
   .i_TX_Byte(r_Master_TX_Byte),     // Byte to transmit on MOSI
   .i_TX_DV(r_Master_TX_DV),         // Data Valid Pulse with i_TX_Byte
   .o_TX_Ready(w_Master_TX_Ready),   // Transmit Ready for Byte
   
   // RX (MISO) Signals
   .o_RX_DV(r_Master_RX_DV),       // Data Valid pulse (1 clock cycle)
   .o_RX_Byte(r_Master_RX_Byte),   // Byte received on MISO

   // SPI Interface
   .o_SPI_Clk(w_SPI_Clk),
   .i_SPI_MISO(w_SPI_MISO),
   .o_SPI_MOSI(w_SPI_MOSI)
   );

  // Sends a single byte from master to slave.  Will drive CS on its own.
  task SendSingleByte(input [7:0] data);
    @(posedge r_Clk);
    r_Master_CS_n    <= 1'b0;
    @(posedge r_Clk);
    r_Master_TX_Byte <= data;
    r_Master_TX_DV   <= 1'b1;
    //r_Master_CS_n    <= 1'b0;
    @(posedge r_Clk);
    r_Master_TX_DV <= 1'b0;
    @(posedge w_Master_TX_Ready);
    @(posedge r_Clk);
    r_Master_CS_n    <= 1'b1;    
  endtask // SendSingleByte

  // Sends a multi-byte transfer from master to slave.  Drives CS on its own.  
  task SendMultiByte(input [7:0] data[0:255], input [7:0] length);
    integer ii;
    @(posedge r_Clk);
    r_Master_CS_n    <= 1'b0;
    for (ii=0; ii<length; ii++)
    begin
      @(posedge r_Clk);
      r_Master_TX_Byte <= data[ii];
      r_Master_TX_DV   <= 1'b1;
      @(posedge r_Clk);
      r_Master_TX_DV <= 1'b0;
      @(posedge w_Master_TX_Ready);
      @(posedge r_Clk);
    end
    r_Master_CS_n <= 1'b1;
  endtask // SendMultiByte

  task SendDacValue(input [23:0] datain);
    //for (logic [3:0] i=0; i<4; i++) dataPayload[i]  = {i[1:0], datain[ 6*(i+1)-1 : 6*i]};
    dataPayload[0]  = {2'd0, datain[ 5: 0]};
    dataPayload[1]  = {2'd1, datain[11: 6]};
    dataPayload[2]  = {2'd2, datain[17:12]};
    dataPayload[3]  = {2'd3, datain[23:18]};
    if(0) begin
      dataLength      = 4;
      SendMultiByte(dataPayload, dataLength);
      repeat(10) @(posedge r_Clk);
    end else begin
      for (int i=3;i>=0;i--) begin 
        SendSingleByte(dataPayload[i]);
        repeat(10) @(posedge r_Clk);
      end
    end
  endtask
   
  int errors; 
    
  initial
    begin
      r_Master_CS_n=1'b1;
      repeat(10) @(posedge r_Clk);
      r_Rst_L  = 1'b0;
      repeat(10) @(posedge r_Clk);
      r_Rst_L          = 1'b1;
      
      errors=0;
      for (int i=0; i<N; i++) begin
        SendDacValue(i);
        if (tb.dut.iout  != `G * i) 
        //if(tb.dut.dut.iout != `G * i) 
          errors++;
      end
      
      //r_Slave_TX_Byte <= 8'h5A;
      //r_Slave_TX_DV   <= 1'b1;
      //repeat(10) @(posedge r_Clk);
      //r_Slave_TX_DV   <= 1'b0;
      /*
      SendSingleByte(8'hC1);
      repeat(100) @(posedge r_Clk);
      dataPayload[0]  = 8'h00;
      dataPayload[1]  = 8'h01;
      dataPayload[2]  = 8'h80;
      dataPayload[3]  = 8'hFF;
      dataPayload[4]  = 8'h55;
      dataPayload[5]  = 8'hAA;
      dataLength      = 6;
      SendMultiByte(dataPayload, dataLength);
      */
      repeat(100) @(posedge r_Clk);
      
      $display("======== %1d errors ======== \n", errors);
      assert(errors==0);
      
      $finish();      
    end // initial begin

endmodule
`endif








