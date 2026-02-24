# Design integration flow

Notes for   
* verifying the synthesized digital part of the design  
* writing, synthesizing, and verifying the eFPGA part of the design    

## Links to information

* [HeiChips25 workshop repository](https://github.com/FPGA-Research/heichips25-workshop)  
* [https://github.com/FPGA-Research/heichips25-tapeout/blob/main/ip/fabric/user_designs/top_wrapper.v](https://github.com/FPGA-Research/heichips25-tapeout/blob/main/ip/fabric/user_designs/top_wrapper.v)  
* [https://github.com/FPGA-Research/heichips25-tapeout/tree/main/ip/fabric](https://github.com/FPGA-Research/heichips25-tapeout/tree/main/ip/fabric)    

### cocotb "documentation"  

* [refcard](https://docs.cocotb.org/en/stable/refcard.html)  

### Open Padrings  
  
* [Open Pad rings](https://github.com/KrzysztofHerman/Open-Padrings)  
* [IHP-Open-PDK xschemIO](https://github.com/KrzysztofHerman/IHP-Open-PDK/tree/xschemIO-prabhat)  
* [Example FLDO design](https://github.com/rjordans/TO_Sep2025/tree/main/FLDO)  

## Debugging the Debugger

### In an environment driven by software engineers' discussion forums, debugging the debugger is orders of magnitude harder than debugging the DUT itself

#### [Installation and configuration hell](https://chatgpt.com/c/6998bf81-a078-838d-a8ad-1b67493cf8e9)  
* [Mine laid in the abstraction stack: ciel update not documented.](https://github.com/FPGA-Research/heichips25-template/issues/10)  
* [Mine laid in abstraction layer stack: cocotb version updated, tb/testbench.py that accesses cocotb not updated accordingly.](https://github.com/FPGA-Research/heichips25-template/issues/11)  
* [Mine laid in abstraction layer stack: https://github.com/FPGA-Research/heichips25-template/blob/main/tb/testbench.py#L92 syntax error](https://github.com/FPGA-Research/heichips25-template/issues/12)  
* [nix dependency hell: pytest missing in https://github.com/FPGA-Research/heichips25-template/blob/main/flake.nix#L61](https://github.com/FPGA-Research/heichips25-template/issues/13)  

### Sifting through a stack of duplicate, subtly inconsistent verification tools (SystemVerilog, cocotb)  

A [vibe coded](https://chatgpt.com/c/6990cdd9-6788-8397-990b-999bf1d28013) cocotb [test base](https://github.com/tatzelbrumm/PUDDING/blob/tatzelbranch/tb/testbench.py), after [lots of iterative minesweeping](https://github.com/tatzelbrumm/PUDDING/commits/tatzelbranch/tb), executes `make sim` without crashing outright.    
But some assertions fail.  
  
* Assertion `assert got_oe == 0xFF, f"uio_oe mismatch got=0x{got_oe:02x} exp=0xff` passes.  
* Assertion `assert got_uo == exp_uo, f"uo_out mismatch got=0x{got_uo:02x} exp=0x{exp_uo:02x}"`  fails at 133 us.  
* Assertion `assert got_uio == exp_uio, f"uio_out mismatch got=0x{got_uio:02x} exp=0x{exp_uio:02x}"` fails at 137 us.  

[Replaced stopping assertions by a non-stopping `check_equal` function](https://github.com/tatzelbrumm/PUDDING/commit/eb236d945c1ccde94e002c2d6044383d3bc44274).
  
It is difficult to get `cocotb` to show the reference waveforms, which are more likely than the Verilog to be wrong.  

#### [Stand-alone SystemVerilog test base](https://github.com/tatzelbrumm/PUDDING/blob/tatzelbranch/tb/tb_heichips25_pudding.sv)  
  
works with  
```
iverilog -g2012 -o simv tb/tb_heichips25_pudding.sv src/heichips25_pudding.sv src/dac128module.v src/analog_wires.v tb/sg13g2_inv_1.v > >(tee iverilog.out) 2> >(tee iverilog.err >&2)  
```
and returns empty `iverilog.out` and `iverilog.err` files.

`simv` outputs
```
[TB] Loading daisychain pattern A via shift...
[TB] Transfer daisychain -> state (dir=1)...
[TB] Clear daisychain by reset-like behavior? No reset used; transfer back should restore it anyway.
[TB] Transfer state -> daisychain (dir=0)...
[TB] Random stimulus phase...
[TB] PASS
tb/tb_heichips25_pudding.sv:209: $finish called at 11870000 (1ps)
```

GTKviewer doesn't allow displaying subsets of data vectors, like `state[127:120]` out of `state[127:0]`.  

#### Gate level simulation

`make sim-gl > >(tee make_sim.out) 2> >(tee make_sim.err >&2)` starts a new nightmare.  
Default `SIM=verilator` crashes with errors.

`SIM=icarus make sim-gl > >(tee make_sim.out) 2> >(tee make_sim.err >&2)`  
After lots of ChatGPT vibe coding, as of [https://github.com/tatzelbrumm/PUDDING/commit/b254a1ddd64bb234509f675fca174a70c727c5ec](https://github.com/tatzelbrumm/PUDDING/commit/b254a1ddd64bb234509f675fca174a70c727c5ec),  
[`tb/testbench.py`](https://github.com/tatzelbrumm/PUDDING/blob/tatzelbranch/tb/testbench.py) produces the same errors as RTL verification.

The `sg13g2_dfrbpq_1` DFFs should get an asynchronous `RESET_B` input.  
  
[Gate level simulation](https://github.com/tatzelbrumm/PUDDING/blob/tatzelbranch/tb/gatelevel_sim.20260224_0313.pdf) passes, but with signal discrepancies.  





