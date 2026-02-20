import os
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb_tools.runner import get_runner
from cocotb.triggers import RisingEdge, Timer


# -----------------------------
# Cocotb test
# -----------------------------
@cocotb.test()
async def smoke(dut):
    clock = Clock(dut.clk, 10, "ns")
    await cocotb.start_soon(clock.start())

    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    if hasattr(dut, "VPWR"):
        dut.VPWR.value = 1
    if hasattr(dut, "VGND"):
        dut.VGND.value = 0

    dut.rst_n.value = 0
    await Timer(100, "ns")
    await RisingEdge(dut.clk)

    dut.rst_n.value = 1
    await RisingEdge(dut.clk)

    # simple sanity
    for _ in range(10):
        await RisingEdge(dut.clk)


# -----------------------------
# Runner
# -----------------------------
if __name__ == "__main__":
    sim = os.getenv("SIM", "verilator")
    gl = os.getenv("GL", "0") == "1"

    runner = get_runner(sim)

    if gl:
        # Gate level
        runner.build(
            sources=[
                Path("../macro/nl/heichips25_pudding.nl.v"),
                Path("~/.ciel/ihp-sg13g2/libs.ref/sg13g2_stdcell/verilog/sg13g2_stdcell.v").expanduser(),
            ],
            hdl_toplevel="heichips25_pudding",
            defines={"FUNCTIONAL": True, "UNIT_DELAY": "#0"},
            timescale=["1ns", "1ps"],
            waves=True,
            build_args=["--trace", "--trace-fst", "--trace-structs"],
        )
    else:
        # RTL — ONLY modules instantiated by heichips25_pudding.sv
        runner.build(
            sources=[
                Path("../src/heichips25_pudding.sv"),
                Path("../src/dac128module.v"),
                Path("../src/analog_wires.v"),
                Path("sg13g2_inv_1.v"),
            ],
            hdl_toplevel="heichips25_pudding",
            defines={"RTL": True},
            timescale=["1ns", "1ps"],
            waves=True,
            build_args=["--trace", "--trace-structs"],
        )

    runner.test(
        hdl_toplevel="heichips25_pudding",
        test_module="testbench",
        waves=True,
    )

