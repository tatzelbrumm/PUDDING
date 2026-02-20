module cocotb_iverilog_dump();
initial begin
    string dumpfile_path;    if ($value$plusargs("dumpfile_path=%s", dumpfile_path)) begin
        $dumpfile(dumpfile_path);
    end else begin
        $dumpfile("/home/cmaier/EDA/PUDDING/tb/sim_build/heichips25_pudding.fst");
    end
    $dumpvars(0, heichips25_pudding);
end
endmodule
