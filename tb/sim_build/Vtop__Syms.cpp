// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Symbol table implementation internals

#include "Vtop__pch.h"
#include "Vtop.h"
#include "Vtop___024root.h"

// FUNCTIONS
Vtop__Syms::~Vtop__Syms()
{

    // Tear down scope hierarchy
    __Vhier.remove(0, &__Vscope_heichips25_pudding);
    __Vhier.remove(&__Vscope_heichips25_pudding, &__Vscope_heichips25_pudding__dac);
    __Vhier.remove(&__Vscope_heichips25_pudding, &__Vscope_heichips25_pudding__digitalen);
    __Vhier.remove(&__Vscope_heichips25_pudding, &__Vscope_heichips25_pudding__wires);
    __Vhier.remove(&__Vscope_heichips25_pudding__digitalen, &__Vscope_heichips25_pudding__digitalen__g__BRA__0__KET__);
    __Vhier.remove(&__Vscope_heichips25_pudding__digitalen, &__Vscope_heichips25_pudding__digitalen__g__BRA__1__KET__);
    __Vhier.remove(&__Vscope_heichips25_pudding__digitalen, &__Vscope_heichips25_pudding__digitalen__g__BRA__2__KET__);
    __Vhier.remove(&__Vscope_heichips25_pudding__digitalen, &__Vscope_heichips25_pudding__digitalen__g__BRA__3__KET__);
    __Vhier.remove(&__Vscope_heichips25_pudding__digitalen__g__BRA__0__KET__, &__Vscope_heichips25_pudding__digitalen__g__BRA__0__KET____u);
    __Vhier.remove(&__Vscope_heichips25_pudding__digitalen__g__BRA__0__KET____u, &__Vscope_heichips25_pudding__digitalen__g__BRA__0__KET____u__inv1);
    __Vhier.remove(&__Vscope_heichips25_pudding__digitalen__g__BRA__0__KET____u, &__Vscope_heichips25_pudding__digitalen__g__BRA__0__KET____u__inv2);
    __Vhier.remove(&__Vscope_heichips25_pudding__digitalen__g__BRA__1__KET__, &__Vscope_heichips25_pudding__digitalen__g__BRA__1__KET____u);
    __Vhier.remove(&__Vscope_heichips25_pudding__digitalen__g__BRA__1__KET____u, &__Vscope_heichips25_pudding__digitalen__g__BRA__1__KET____u__inv1);
    __Vhier.remove(&__Vscope_heichips25_pudding__digitalen__g__BRA__1__KET____u, &__Vscope_heichips25_pudding__digitalen__g__BRA__1__KET____u__inv2);
    __Vhier.remove(&__Vscope_heichips25_pudding__digitalen__g__BRA__2__KET__, &__Vscope_heichips25_pudding__digitalen__g__BRA__2__KET____u);
    __Vhier.remove(&__Vscope_heichips25_pudding__digitalen__g__BRA__2__KET____u, &__Vscope_heichips25_pudding__digitalen__g__BRA__2__KET____u__inv1);
    __Vhier.remove(&__Vscope_heichips25_pudding__digitalen__g__BRA__2__KET____u, &__Vscope_heichips25_pudding__digitalen__g__BRA__2__KET____u__inv2);
    __Vhier.remove(&__Vscope_heichips25_pudding__digitalen__g__BRA__3__KET__, &__Vscope_heichips25_pudding__digitalen__g__BRA__3__KET____u);
    __Vhier.remove(&__Vscope_heichips25_pudding__digitalen__g__BRA__3__KET____u, &__Vscope_heichips25_pudding__digitalen__g__BRA__3__KET____u__inv1);
    __Vhier.remove(&__Vscope_heichips25_pudding__digitalen__g__BRA__3__KET____u, &__Vscope_heichips25_pudding__digitalen__g__BRA__3__KET____u__inv2);

}

Vtop__Syms::Vtop__Syms(VerilatedContext* contextp, const char* namep, Vtop* modelp)
    : VerilatedSyms{contextp}
    // Setup internal state of the Syms class
    , __Vm_modelp{modelp}
    // Setup module instances
    , TOP{this, namep}
{
    // Check resources
    Verilated::stackCheck(314);
    // Configure time unit / time precision
    _vm_contextp__->timeunit(-9);
    _vm_contextp__->timeprecision(-12);
    // Setup each module's pointers to their submodules
    // Setup each module's pointer back to symbol table (for public functions)
    TOP.__Vconfigure(true);
    // Setup scopes
    __Vscope_TOP.configure(this, name(), "TOP", "TOP", "<null>", 0, VerilatedScope::SCOPE_OTHER);
    __Vscope_heichips25_pudding.configure(this, name(), "heichips25_pudding", "heichips25_pudding", "heichips25_pudding", -9, VerilatedScope::SCOPE_MODULE);
    __Vscope_heichips25_pudding__dac.configure(this, name(), "heichips25_pudding.dac", "dac", "dac128module", -9, VerilatedScope::SCOPE_MODULE);
    __Vscope_heichips25_pudding__digitalen.configure(this, name(), "heichips25_pudding.digitalen", "digitalen", "digital4", -9, VerilatedScope::SCOPE_MODULE);
    __Vscope_heichips25_pudding__digitalen__g__BRA__0__KET__.configure(this, name(), "heichips25_pudding.digitalen.g[0]", "g[0]", "<null>", -9, VerilatedScope::SCOPE_OTHER);
    __Vscope_heichips25_pudding__digitalen__g__BRA__0__KET____u.configure(this, name(), "heichips25_pudding.digitalen.g[0].u", "u", "inverterpair", -9, VerilatedScope::SCOPE_MODULE);
    __Vscope_heichips25_pudding__digitalen__g__BRA__0__KET____u__inv1.configure(this, name(), "heichips25_pudding.digitalen.g[0].u.inv1", "inv1", "sg13g2_inv_1", -9, VerilatedScope::SCOPE_MODULE);
    __Vscope_heichips25_pudding__digitalen__g__BRA__0__KET____u__inv2.configure(this, name(), "heichips25_pudding.digitalen.g[0].u.inv2", "inv2", "sg13g2_inv_1", -9, VerilatedScope::SCOPE_MODULE);
    __Vscope_heichips25_pudding__digitalen__g__BRA__1__KET__.configure(this, name(), "heichips25_pudding.digitalen.g[1]", "g[1]", "<null>", -9, VerilatedScope::SCOPE_OTHER);
    __Vscope_heichips25_pudding__digitalen__g__BRA__1__KET____u.configure(this, name(), "heichips25_pudding.digitalen.g[1].u", "u", "inverterpair", -9, VerilatedScope::SCOPE_MODULE);
    __Vscope_heichips25_pudding__digitalen__g__BRA__1__KET____u__inv1.configure(this, name(), "heichips25_pudding.digitalen.g[1].u.inv1", "inv1", "sg13g2_inv_1", -9, VerilatedScope::SCOPE_MODULE);
    __Vscope_heichips25_pudding__digitalen__g__BRA__1__KET____u__inv2.configure(this, name(), "heichips25_pudding.digitalen.g[1].u.inv2", "inv2", "sg13g2_inv_1", -9, VerilatedScope::SCOPE_MODULE);
    __Vscope_heichips25_pudding__digitalen__g__BRA__2__KET__.configure(this, name(), "heichips25_pudding.digitalen.g[2]", "g[2]", "<null>", -9, VerilatedScope::SCOPE_OTHER);
    __Vscope_heichips25_pudding__digitalen__g__BRA__2__KET____u.configure(this, name(), "heichips25_pudding.digitalen.g[2].u", "u", "inverterpair", -9, VerilatedScope::SCOPE_MODULE);
    __Vscope_heichips25_pudding__digitalen__g__BRA__2__KET____u__inv1.configure(this, name(), "heichips25_pudding.digitalen.g[2].u.inv1", "inv1", "sg13g2_inv_1", -9, VerilatedScope::SCOPE_MODULE);
    __Vscope_heichips25_pudding__digitalen__g__BRA__2__KET____u__inv2.configure(this, name(), "heichips25_pudding.digitalen.g[2].u.inv2", "inv2", "sg13g2_inv_1", -9, VerilatedScope::SCOPE_MODULE);
    __Vscope_heichips25_pudding__digitalen__g__BRA__3__KET__.configure(this, name(), "heichips25_pudding.digitalen.g[3]", "g[3]", "<null>", -9, VerilatedScope::SCOPE_OTHER);
    __Vscope_heichips25_pudding__digitalen__g__BRA__3__KET____u.configure(this, name(), "heichips25_pudding.digitalen.g[3].u", "u", "inverterpair", -9, VerilatedScope::SCOPE_MODULE);
    __Vscope_heichips25_pudding__digitalen__g__BRA__3__KET____u__inv1.configure(this, name(), "heichips25_pudding.digitalen.g[3].u.inv1", "inv1", "sg13g2_inv_1", -9, VerilatedScope::SCOPE_MODULE);
    __Vscope_heichips25_pudding__digitalen__g__BRA__3__KET____u__inv2.configure(this, name(), "heichips25_pudding.digitalen.g[3].u.inv2", "inv2", "sg13g2_inv_1", -9, VerilatedScope::SCOPE_MODULE);
    __Vscope_heichips25_pudding__wires.configure(this, name(), "heichips25_pudding.wires", "wires", "analog_wires", -9, VerilatedScope::SCOPE_MODULE);

    // Set up scope hierarchy
    __Vhier.add(0, &__Vscope_heichips25_pudding);
    __Vhier.add(&__Vscope_heichips25_pudding, &__Vscope_heichips25_pudding__dac);
    __Vhier.add(&__Vscope_heichips25_pudding, &__Vscope_heichips25_pudding__digitalen);
    __Vhier.add(&__Vscope_heichips25_pudding, &__Vscope_heichips25_pudding__wires);
    __Vhier.add(&__Vscope_heichips25_pudding__digitalen, &__Vscope_heichips25_pudding__digitalen__g__BRA__0__KET__);
    __Vhier.add(&__Vscope_heichips25_pudding__digitalen, &__Vscope_heichips25_pudding__digitalen__g__BRA__1__KET__);
    __Vhier.add(&__Vscope_heichips25_pudding__digitalen, &__Vscope_heichips25_pudding__digitalen__g__BRA__2__KET__);
    __Vhier.add(&__Vscope_heichips25_pudding__digitalen, &__Vscope_heichips25_pudding__digitalen__g__BRA__3__KET__);
    __Vhier.add(&__Vscope_heichips25_pudding__digitalen__g__BRA__0__KET__, &__Vscope_heichips25_pudding__digitalen__g__BRA__0__KET____u);
    __Vhier.add(&__Vscope_heichips25_pudding__digitalen__g__BRA__0__KET____u, &__Vscope_heichips25_pudding__digitalen__g__BRA__0__KET____u__inv1);
    __Vhier.add(&__Vscope_heichips25_pudding__digitalen__g__BRA__0__KET____u, &__Vscope_heichips25_pudding__digitalen__g__BRA__0__KET____u__inv2);
    __Vhier.add(&__Vscope_heichips25_pudding__digitalen__g__BRA__1__KET__, &__Vscope_heichips25_pudding__digitalen__g__BRA__1__KET____u);
    __Vhier.add(&__Vscope_heichips25_pudding__digitalen__g__BRA__1__KET____u, &__Vscope_heichips25_pudding__digitalen__g__BRA__1__KET____u__inv1);
    __Vhier.add(&__Vscope_heichips25_pudding__digitalen__g__BRA__1__KET____u, &__Vscope_heichips25_pudding__digitalen__g__BRA__1__KET____u__inv2);
    __Vhier.add(&__Vscope_heichips25_pudding__digitalen__g__BRA__2__KET__, &__Vscope_heichips25_pudding__digitalen__g__BRA__2__KET____u);
    __Vhier.add(&__Vscope_heichips25_pudding__digitalen__g__BRA__2__KET____u, &__Vscope_heichips25_pudding__digitalen__g__BRA__2__KET____u__inv1);
    __Vhier.add(&__Vscope_heichips25_pudding__digitalen__g__BRA__2__KET____u, &__Vscope_heichips25_pudding__digitalen__g__BRA__2__KET____u__inv2);
    __Vhier.add(&__Vscope_heichips25_pudding__digitalen__g__BRA__3__KET__, &__Vscope_heichips25_pudding__digitalen__g__BRA__3__KET____u);
    __Vhier.add(&__Vscope_heichips25_pudding__digitalen__g__BRA__3__KET____u, &__Vscope_heichips25_pudding__digitalen__g__BRA__3__KET____u__inv1);
    __Vhier.add(&__Vscope_heichips25_pudding__digitalen__g__BRA__3__KET____u, &__Vscope_heichips25_pudding__digitalen__g__BRA__3__KET____u__inv2);

    // Setup export functions
    for (int __Vfinal = 0; __Vfinal < 2; ++__Vfinal) {
        __Vscope_TOP.varInsert(__Vfinal,"VGND", &(TOP.VGND), false, VLVT_UINT8,VLVD_INOUT|VLVF_PUB_RW,0,0);
        __Vscope_TOP.varInsert(__Vfinal,"VPWR", &(TOP.VPWR), false, VLVT_UINT8,VLVD_INOUT|VLVF_PUB_RW,0,0);
        __Vscope_TOP.varInsert(__Vfinal,"clk", &(TOP.clk), false, VLVT_UINT8,VLVD_IN|VLVF_PUB_RW,0,0);
        __Vscope_TOP.varInsert(__Vfinal,"ena", &(TOP.ena), false, VLVT_UINT8,VLVD_IN|VLVF_PUB_RW,0,0);
        __Vscope_TOP.varInsert(__Vfinal,"i_in", &(TOP.i_in), false, VLVT_UINT8,VLVD_INOUT|VLVF_PUB_RW,0,0);
        __Vscope_TOP.varInsert(__Vfinal,"i_out", &(TOP.i_out), false, VLVT_UINT8,VLVD_INOUT|VLVF_PUB_RW,0,0);
        __Vscope_TOP.varInsert(__Vfinal,"rst_n", &(TOP.rst_n), false, VLVT_UINT8,VLVD_IN|VLVF_PUB_RW,0,0);
        __Vscope_TOP.varInsert(__Vfinal,"ui_in", &(TOP.ui_in), false, VLVT_UINT8,VLVD_IN|VLVF_PUB_RW,0,1 ,7,0);
        __Vscope_TOP.varInsert(__Vfinal,"uio_in", &(TOP.uio_in), false, VLVT_UINT8,VLVD_IN|VLVF_PUB_RW,0,1 ,7,0);
        __Vscope_TOP.varInsert(__Vfinal,"uio_oe", &(TOP.uio_oe), false, VLVT_UINT8,VLVD_OUT|VLVF_PUB_RW,0,1 ,7,0);
        __Vscope_TOP.varInsert(__Vfinal,"uio_out", &(TOP.uio_out), false, VLVT_UINT8,VLVD_OUT|VLVF_PUB_RW,0,1 ,7,0);
        __Vscope_TOP.varInsert(__Vfinal,"uo_out", &(TOP.uo_out), false, VLVT_UINT8,VLVD_OUT|VLVF_PUB_RW,0,1 ,7,0);
        __Vscope_heichips25_pudding.varInsert(__Vfinal,"VGND", &(TOP.heichips25_pudding__DOT__VGND), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding.varInsert(__Vfinal,"VPWR", &(TOP.heichips25_pudding__DOT__VPWR), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding.varInsert(__Vfinal,"_unused", &(TOP.heichips25_pudding__DOT___unused), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding.varInsert(__Vfinal,"bias", &(TOP.heichips25_pudding__DOT__bias), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,1 ,1,0);
        __Vscope_heichips25_pudding.varInsert(__Vfinal,"clk", &(TOP.heichips25_pudding__DOT__clk), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding.varInsert(__Vfinal,"dacout", &(TOP.heichips25_pudding__DOT__dacout), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding.varInsert(__Vfinal,"daisychain", &(TOP.heichips25_pudding__DOT__daisychain), false, VLVT_WDATA,VLVD_NODIR|VLVF_PUB_RW,0,1 ,127,0);
        __Vscope_heichips25_pudding.varInsert(__Vfinal,"datum", &(TOP.heichips25_pudding__DOT__datum), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding.varInsert(__Vfinal,"dir", &(TOP.heichips25_pudding__DOT__dir), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding.varInsert(__Vfinal,"ena", &(TOP.heichips25_pudding__DOT__ena), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding.varInsert(__Vfinal,"i_in", &(TOP.heichips25_pudding__DOT__i_in), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding.varInsert(__Vfinal,"i_out", &(TOP.heichips25_pudding__DOT__i_out), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding.varInsert(__Vfinal,"iref", &(TOP.heichips25_pudding__DOT__iref), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,1 ,1,0);
        __Vscope_heichips25_pudding.varInsert(__Vfinal,"rst_n", &(TOP.heichips25_pudding__DOT__rst_n), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding.varInsert(__Vfinal,"shift", &(TOP.heichips25_pudding__DOT__shift), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding.varInsert(__Vfinal,"state", &(TOP.heichips25_pudding__DOT__state), false, VLVT_WDATA,VLVD_NODIR|VLVF_PUB_RW,0,1 ,127,0);
        __Vscope_heichips25_pudding.varInsert(__Vfinal,"stateen", &(TOP.heichips25_pudding__DOT__stateen), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,1 ,3,0);
        __Vscope_heichips25_pudding.varInsert(__Vfinal,"stateenn", &(TOP.heichips25_pudding__DOT__stateenn), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,1 ,3,0);
        __Vscope_heichips25_pudding.varInsert(__Vfinal,"stateenp", &(TOP.heichips25_pudding__DOT__stateenp), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,1 ,3,0);
        __Vscope_heichips25_pudding.varInsert(__Vfinal,"transfer", &(TOP.heichips25_pudding__DOT__transfer), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding.varInsert(__Vfinal,"ui_in", &(TOP.heichips25_pudding__DOT__ui_in), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,1 ,7,0);
        __Vscope_heichips25_pudding.varInsert(__Vfinal,"uio_in", &(TOP.heichips25_pudding__DOT__uio_in), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,1 ,7,0);
        __Vscope_heichips25_pudding.varInsert(__Vfinal,"uio_oe", &(TOP.heichips25_pudding__DOT__uio_oe), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,1 ,7,0);
        __Vscope_heichips25_pudding.varInsert(__Vfinal,"uio_out", &(TOP.heichips25_pudding__DOT__uio_out), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,1 ,7,0);
        __Vscope_heichips25_pudding.varInsert(__Vfinal,"uo_out", &(TOP.heichips25_pudding__DOT__uo_out), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,1 ,7,0);
        __Vscope_heichips25_pudding.varInsert(__Vfinal,"vdda", &(TOP.heichips25_pudding__DOT__vdda), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,1 ,1,0);
        __Vscope_heichips25_pudding__dac.varInsert(__Vfinal,"EN", &(TOP.heichips25_pudding__DOT__dac__DOT__EN), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,1 ,3,0);
        __Vscope_heichips25_pudding__dac.varInsert(__Vfinal,"ENB", &(TOP.heichips25_pudding__DOT__dac__DOT__ENB), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,1 ,3,0);
        __Vscope_heichips25_pudding__dac.varInsert(__Vfinal,"Iout", &(TOP.heichips25_pudding__DOT__dac__DOT__Iout), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding__dac.varInsert(__Vfinal,"ON", &(TOP.heichips25_pudding__DOT__dac__DOT__ON), false, VLVT_WDATA,VLVD_NODIR|VLVF_PUB_RW,0,1 ,127,0);
        __Vscope_heichips25_pudding__dac.varInsert(__Vfinal,"ONB", &(TOP.heichips25_pudding__DOT__dac__DOT__ONB), false, VLVT_WDATA,VLVD_NODIR|VLVF_PUB_RW,0,1 ,127,0);
        __Vscope_heichips25_pudding__dac.varInsert(__Vfinal,"VDD", &(TOP.heichips25_pudding__DOT__dac__DOT__VDD), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding__dac.varInsert(__Vfinal,"VSS", &(TOP.heichips25_pudding__DOT__dac__DOT__VSS), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding__dac.varInsert(__Vfinal,"VbiasP", &(TOP.heichips25_pudding__DOT__dac__DOT__VbiasP), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,1 ,1,0);
        __Vscope_heichips25_pudding__dac.varInsert(__Vfinal,"VcascP", &(TOP.heichips25_pudding__DOT__dac__DOT__VcascP), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,1 ,1,0);
        __Vscope_heichips25_pudding__digitalen.varInsert(__Vfinal,"in", &(TOP.heichips25_pudding__DOT__digitalen__DOT__in), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,1 ,3,0);
        __Vscope_heichips25_pudding__digitalen.varInsert(__Vfinal,"outn", &(TOP.heichips25_pudding__DOT__digitalen__DOT__outn), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,1 ,3,0);
        __Vscope_heichips25_pudding__digitalen.varInsert(__Vfinal,"outp", &(TOP.heichips25_pudding__DOT__digitalen__DOT__outp), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,1 ,3,0);
        __Vscope_heichips25_pudding__digitalen__g__BRA__0__KET____u.varInsert(__Vfinal,"IN", &(TOP.heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__IN), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding__digitalen__g__BRA__0__KET____u.varInsert(__Vfinal,"OUTN", &(TOP.heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__OUTN), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding__digitalen__g__BRA__0__KET____u.varInsert(__Vfinal,"OUTP", &(TOP.heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__OUTP), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding__digitalen__g__BRA__0__KET____u__inv1.varInsert(__Vfinal,"A", &(TOP.heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__inv1__DOT__A), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding__digitalen__g__BRA__0__KET____u__inv1.varInsert(__Vfinal,"Y", &(TOP.heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__inv1__DOT__Y), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding__digitalen__g__BRA__0__KET____u__inv2.varInsert(__Vfinal,"A", &(TOP.heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__inv2__DOT__A), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding__digitalen__g__BRA__0__KET____u__inv2.varInsert(__Vfinal,"Y", &(TOP.heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__inv2__DOT__Y), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding__digitalen__g__BRA__1__KET____u.varInsert(__Vfinal,"IN", &(TOP.heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__IN), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding__digitalen__g__BRA__1__KET____u.varInsert(__Vfinal,"OUTN", &(TOP.heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__OUTN), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding__digitalen__g__BRA__1__KET____u.varInsert(__Vfinal,"OUTP", &(TOP.heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__OUTP), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding__digitalen__g__BRA__1__KET____u__inv1.varInsert(__Vfinal,"A", &(TOP.heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__inv1__DOT__A), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding__digitalen__g__BRA__1__KET____u__inv1.varInsert(__Vfinal,"Y", &(TOP.heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__inv1__DOT__Y), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding__digitalen__g__BRA__1__KET____u__inv2.varInsert(__Vfinal,"A", &(TOP.heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__inv2__DOT__A), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding__digitalen__g__BRA__1__KET____u__inv2.varInsert(__Vfinal,"Y", &(TOP.heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__inv2__DOT__Y), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding__digitalen__g__BRA__2__KET____u.varInsert(__Vfinal,"IN", &(TOP.heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__IN), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding__digitalen__g__BRA__2__KET____u.varInsert(__Vfinal,"OUTN", &(TOP.heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__OUTN), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding__digitalen__g__BRA__2__KET____u.varInsert(__Vfinal,"OUTP", &(TOP.heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__OUTP), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding__digitalen__g__BRA__2__KET____u__inv1.varInsert(__Vfinal,"A", &(TOP.heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__inv1__DOT__A), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding__digitalen__g__BRA__2__KET____u__inv1.varInsert(__Vfinal,"Y", &(TOP.heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__inv1__DOT__Y), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding__digitalen__g__BRA__2__KET____u__inv2.varInsert(__Vfinal,"A", &(TOP.heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__inv2__DOT__A), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding__digitalen__g__BRA__2__KET____u__inv2.varInsert(__Vfinal,"Y", &(TOP.heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__inv2__DOT__Y), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding__digitalen__g__BRA__3__KET____u.varInsert(__Vfinal,"IN", &(TOP.heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__IN), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding__digitalen__g__BRA__3__KET____u.varInsert(__Vfinal,"OUTN", &(TOP.heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__OUTN), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding__digitalen__g__BRA__3__KET____u.varInsert(__Vfinal,"OUTP", &(TOP.heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__OUTP), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding__digitalen__g__BRA__3__KET____u__inv1.varInsert(__Vfinal,"A", &(TOP.heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__inv1__DOT__A), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding__digitalen__g__BRA__3__KET____u__inv1.varInsert(__Vfinal,"Y", &(TOP.heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__inv1__DOT__Y), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding__digitalen__g__BRA__3__KET____u__inv2.varInsert(__Vfinal,"A", &(TOP.heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__inv2__DOT__A), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding__digitalen__g__BRA__3__KET____u__inv2.varInsert(__Vfinal,"Y", &(TOP.heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__inv2__DOT__Y), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding__wires.varInsert(__Vfinal,"Iout", &(TOP.heichips25_pudding__DOT__wires__DOT__Iout), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding__wires.varInsert(__Vfinal,"VDDA", &(TOP.heichips25_pudding__DOT__wires__DOT__VDDA), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,1 ,1,0);
        __Vscope_heichips25_pudding__wires.varInsert(__Vfinal,"VbiasP", &(TOP.heichips25_pudding__DOT__wires__DOT__VbiasP), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,1 ,1,0);
        __Vscope_heichips25_pudding__wires.varInsert(__Vfinal,"VcascP", &(TOP.heichips25_pudding__DOT__wires__DOT__VcascP), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,1 ,1,0);
        __Vscope_heichips25_pudding__wires.varInsert(__Vfinal,"bias", &(TOP.heichips25_pudding__DOT__wires__DOT__bias), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding__wires.varInsert(__Vfinal,"casc", &(TOP.heichips25_pudding__DOT__wires__DOT__casc), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding__wires.varInsert(__Vfinal,"i_in", &(TOP.heichips25_pudding__DOT__wires__DOT__i_in), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding__wires.varInsert(__Vfinal,"i_out", &(TOP.heichips25_pudding__DOT__wires__DOT__i_out), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
        __Vscope_heichips25_pudding__wires.varInsert(__Vfinal,"vdda", &(TOP.heichips25_pudding__DOT__wires__DOT__vdda), false, VLVT_UINT8,VLVD_NODIR|VLVF_PUB_RW,0,0);
    }
}
