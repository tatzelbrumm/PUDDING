import os
import sys
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb_tools.runner import get_runner
from cocotb.triggers import Timer, ClockCycles, RisingEdge


# -----------------------------
# Helpers: 128-bit shift/transfer reference model
# -----------------------------
def mask128(x: int) -> int:
    return x & ((1 << 128) - 1)


class RefModel:
    def __init__(self):
        self.daisy = 0
        self.state = 0

    def reset(self):
        self.daisy = 0
        self.state = 0

    def step(self, datum: int, shift: int, transfer: int, dir_: int):
        # Mirrors RTL priority: transfer > shift
        if transfer:
            if dir_:
                self.state = self.daisy
            else:
                self.daisy = self.state
        elif shift:
            self.daisy = mask128((self.daisy << 1) | (datum & 1))

    def uo_out(self) -> int:
        return (self.daisy >> 120) & 0xFF

    def uio_out(self) -> int:
        return (self.state >> 120) & 0xFF


# -----------------------------
# Cocotb test
# -----------------------------
@cocotb.test()
async def heichips25_pudding_smoke_and_random(dut):
    """Shift/transfer correctness + output mapping checks for heichips25_pudding."""

    # 100 MHz clock (10 ns period) like the template
    clock = Clock(dut.clk, 10, "ns")
    await cocotb.start(clock.start())

    # Drive always-on basics
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    # Optional power pins (exist in your RTL)
    if hasattr(dut, "VPWR"):
        dut.VPWR.value = 1
    if hasattr(dut, "VGND"):
        dut.VGND.value = 0

    # Optional analog-ish inouts: keep quiet
    if hasattr(dut, "i_in"):
        dut.i_in.value = 0

    ref = RefModel()

    # Reset
    dut.rst_n.value = 0
    await Timer(100, "ns")
    await RisingEdge(dut.clk)
    ref.reset()

    dut.rst_n.value = 1
    await Timer(50, "ns")
    await RisingEdge(dut.clk)

    # After reset, outputs should be 0
    assert int(dut.uo_out.value) == 0
    assert int(dut.uio_out.value) == 0
    assert int(dut.uio_oe.value) == 0xFF  # in RTL it's hardwired

    async def drive_ui(datum=0, shift=0, transfer=0, dir_=0, stateen=1):
        # ui_in mapping from your RTL:
        # [0]=datum, [1]=shift, [2]=transfer, [3]=dir, [4]=stateen
        v = (datum & 1) | ((shift & 1) << 1) | ((transfer & 1) << 2) | ((dir_ & 1) << 3) | ((stateen & 1) << 4)
        dut.ui_in.value = v

    async def pulse_shift(bitval: int):
        # assert shift for one clock edge
        await drive_ui(datum=bitval, shift=1, transfer=0, dir_=0, stateen=1)
        await RisingEdge(dut.clk)
        ref.step(datum=bitval, shift=1, transfer=0, dir_=0)
        await drive_ui(datum=bitval, shift=0, transfer=0, dir_=0, stateen=1)

    async def pulse_transfer(dirval: int):
        await drive_ui(datum=0, shift=0, transfer=1, dir_=dirval, stateen=1)
        await RisingEdge(dut.clk)
        ref.step(datum=0, shift=0, transfer=1, dir_=dirval)
        await drive_ui(datum=0, shift=0, transfer=0, dir_=dirval, stateen=1)

    def check_outputs():
        got_uo = int(dut.uo_out.value)
        got_uio = int(dut.uio_out.value)
        got_oe = int(dut.uio_oe.value)

        exp_uo = ref.uo_out()
        exp_uio = ref.uio_out()

        assert got_oe == 0xFF, f"uio_oe mismatch got=0x{got_oe:02x} exp=0xff"
        assert got_uo == exp_uo, f"uo_out mismatch got=0x{got_uo:02x} exp=0x{exp_uo:02x}"
        assert got_uio == exp_uio, f"uio_out mismatch got=0x{got_uio:02x} exp=0x{exp_uio:02x}"

    # Directed pattern load (LSB-first in the sense of successive datum bits)
    pattern = 0x0123456789ABCDEFFEDCBA9876543210
    for i in range(128):
        await pulse_shift((pattern >> i) & 1)
        check_outputs()

    # Transfer daisy -> state
    await pulse_transfer(1)
    check_outputs()

    # Dirty daisy a bit, then restore from state
    for _ in range(10):
        await pulse_shift((_ * 7) & 1)
    check_outputs()

    await pulse_transfer(0)
    check_outputs()

    # Randomized regression
    import random
    for _ in range(500):
        sel = random.randrange(10)
        if sel <= 5:
            b = random.getrandbits(1)
            await pulse_shift(b)
        elif sel <= 7:
            d = random.getrandbits(1)
            await pulse_transfer(d)
        else:
            # idle
            await drive_ui(datum=0, shift=0, transfer=0, dir_=0, stateen=1)
            await RisingEdge(dut.clk)
            # ref unchanged
        check_outputs()


# -----------------------------
# Runner
# -----------------------------
if __name__ == "__main__":
    sim = os.getenv("SIM", "verilator")
    gl = os.getenv("GL", "0") == "1"

    runner = get_runner(sim)

    # Verilator-only compile flags
    verilator_build_args = ["--trace", "--trace-fst", "--trace-structs"]
    build_args = verilator_build_args if sim == "verilator" else []

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
            build_args=build_args,
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
            build_args=build_args,
        )

    runner.test(
        hdl_toplevel="heichips25_pudding",
        test_module="testbench",
        waves=True,
    )

