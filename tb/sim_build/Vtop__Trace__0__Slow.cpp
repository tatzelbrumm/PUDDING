// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Tracing implementation internals
#include "verilated_vcd_c.h"
#include "Vtop__Syms.h"


VL_ATTR_COLD void Vtop___024root__trace_init_sub__TOP__0(Vtop___024root* vlSelf, VerilatedVcd* tracep) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root__trace_init_sub__TOP__0\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    const int c = vlSymsp->__Vm_baseCode;
    tracep->pushPrefix("$rootio", VerilatedTracePrefixType::SCOPE_MODULE);
    tracep->declBus(c+1,0,"ui_in",-1, VerilatedTraceSigDirection::INPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1, 7,0);
    tracep->declBus(c+2,0,"uo_out",-1, VerilatedTraceSigDirection::OUTPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1, 7,0);
    tracep->declBus(c+3,0,"uio_in",-1, VerilatedTraceSigDirection::INPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1, 7,0);
    tracep->declBus(c+4,0,"uio_out",-1, VerilatedTraceSigDirection::OUTPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1, 7,0);
    tracep->declBus(c+5,0,"uio_oe",-1, VerilatedTraceSigDirection::OUTPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1, 7,0);
    tracep->declBit(c+6,0,"ena",-1, VerilatedTraceSigDirection::INPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declBit(c+7,0,"clk",-1, VerilatedTraceSigDirection::INPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declBit(c+8,0,"rst_n",-1, VerilatedTraceSigDirection::INPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declBit(c+9,0,"i_in",-1, VerilatedTraceSigDirection::INOUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declBit(c+10,0,"i_out",-1, VerilatedTraceSigDirection::INOUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declBit(c+11,0,"VPWR",-1, VerilatedTraceSigDirection::INOUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declBit(c+12,0,"VGND",-1, VerilatedTraceSigDirection::INOUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->popPrefix();
    tracep->pushPrefix("heichips25_pudding", VerilatedTracePrefixType::SCOPE_MODULE);
    tracep->declBus(c+13,0,"ui_in",-1, VerilatedTraceSigDirection::INPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1, 7,0);
    tracep->declBus(c+14,0,"uo_out",-1, VerilatedTraceSigDirection::OUTPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1, 7,0);
    tracep->declBus(c+15,0,"uio_in",-1, VerilatedTraceSigDirection::INPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1, 7,0);
    tracep->declBus(c+16,0,"uio_out",-1, VerilatedTraceSigDirection::OUTPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1, 7,0);
    tracep->declBus(c+17,0,"uio_oe",-1, VerilatedTraceSigDirection::OUTPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1, 7,0);
    tracep->declBit(c+18,0,"ena",-1, VerilatedTraceSigDirection::INPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declBit(c+19,0,"clk",-1, VerilatedTraceSigDirection::INPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declBit(c+20,0,"rst_n",-1, VerilatedTraceSigDirection::INPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declBit(c+21,0,"i_in",-1, VerilatedTraceSigDirection::INOUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declBit(c+22,0,"i_out",-1, VerilatedTraceSigDirection::INOUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declBit(c+23,0,"VPWR",-1, VerilatedTraceSigDirection::INOUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declBit(c+24,0,"VGND",-1, VerilatedTraceSigDirection::INOUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declBus(c+25,0,"iref",-1, VerilatedTraceSigDirection::NONE, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1, 1,0);
    tracep->declBus(c+26,0,"bias",-1, VerilatedTraceSigDirection::NONE, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1, 1,0);
    tracep->declBit(c+27,0,"dacout",-1, VerilatedTraceSigDirection::NONE, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declBus(c+28,0,"vdda",-1, VerilatedTraceSigDirection::NONE, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1, 1,0);
    tracep->declBus(c+29,0,"stateen",-1, VerilatedTraceSigDirection::NONE, VerilatedTraceSigKind::VAR, VerilatedTraceSigType::LOGIC, false,-1, 3,0);
    tracep->declBus(c+30,0,"stateenp",-1, VerilatedTraceSigDirection::NONE, VerilatedTraceSigKind::VAR, VerilatedTraceSigType::LOGIC, false,-1, 3,0);
    tracep->declBus(c+31,0,"stateenn",-1, VerilatedTraceSigDirection::NONE, VerilatedTraceSigKind::VAR, VerilatedTraceSigType::LOGIC, false,-1, 3,0);
    tracep->declBit(c+32,0,"datum",-1, VerilatedTraceSigDirection::NONE, VerilatedTraceSigKind::VAR, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declBit(c+33,0,"shift",-1, VerilatedTraceSigDirection::NONE, VerilatedTraceSigKind::VAR, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declBit(c+34,0,"transfer",-1, VerilatedTraceSigDirection::NONE, VerilatedTraceSigKind::VAR, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declBit(c+35,0,"dir",-1, VerilatedTraceSigDirection::NONE, VerilatedTraceSigKind::VAR, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declArray(c+36,0,"daisychain",-1, VerilatedTraceSigDirection::NONE, VerilatedTraceSigKind::VAR, VerilatedTraceSigType::LOGIC, false,-1, 127,0);
    tracep->declArray(c+40,0,"state",-1, VerilatedTraceSigDirection::NONE, VerilatedTraceSigKind::VAR, VerilatedTraceSigType::LOGIC, false,-1, 127,0);
    tracep->pushPrefix("dac", VerilatedTracePrefixType::SCOPE_MODULE);
    tracep->declBit(c+44,0,"Iout",-1, VerilatedTraceSigDirection::INOUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declBus(c+45,0,"VcascP",-1, VerilatedTraceSigDirection::INOUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1, 1,0);
    tracep->declBus(c+46,0,"VbiasP",-1, VerilatedTraceSigDirection::INOUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1, 1,0);
    tracep->declArray(c+47,0,"ON",-1, VerilatedTraceSigDirection::INPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1, 127,0);
    tracep->declArray(c+51,0,"ONB",-1, VerilatedTraceSigDirection::INPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1, 127,0);
    tracep->declBus(c+55,0,"EN",-1, VerilatedTraceSigDirection::INPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1, 3,0);
    tracep->declBus(c+56,0,"ENB",-1, VerilatedTraceSigDirection::INPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1, 3,0);
    tracep->declBit(c+57,0,"VDD",-1, VerilatedTraceSigDirection::INOUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declBit(c+58,0,"VSS",-1, VerilatedTraceSigDirection::INOUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->popPrefix();
    tracep->pushPrefix("digitalen", VerilatedTracePrefixType::SCOPE_MODULE);
    tracep->declBus(c+59,0,"in",-1, VerilatedTraceSigDirection::INPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1, 3,0);
    tracep->declBus(c+60,0,"outn",-1, VerilatedTraceSigDirection::OUTPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1, 3,0);
    tracep->declBus(c+61,0,"outp",-1, VerilatedTraceSigDirection::OUTPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1, 3,0);
    tracep->pushPrefix("g[0]", VerilatedTracePrefixType::SCOPE_MODULE);
    tracep->pushPrefix("u", VerilatedTracePrefixType::SCOPE_MODULE);
    tracep->declBit(c+62,0,"IN",-1, VerilatedTraceSigDirection::INPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declBit(c+63,0,"OUTN",-1, VerilatedTraceSigDirection::OUTPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declBit(c+64,0,"OUTP",-1, VerilatedTraceSigDirection::OUTPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->pushPrefix("inv1", VerilatedTracePrefixType::SCOPE_MODULE);
    tracep->declBit(c+65,0,"Y",-1, VerilatedTraceSigDirection::OUTPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declBit(c+66,0,"A",-1, VerilatedTraceSigDirection::INPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->popPrefix();
    tracep->pushPrefix("inv2", VerilatedTracePrefixType::SCOPE_MODULE);
    tracep->declBit(c+67,0,"Y",-1, VerilatedTraceSigDirection::OUTPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declBit(c+68,0,"A",-1, VerilatedTraceSigDirection::INPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->popPrefix();
    tracep->popPrefix();
    tracep->popPrefix();
    tracep->pushPrefix("g[1]", VerilatedTracePrefixType::SCOPE_MODULE);
    tracep->pushPrefix("u", VerilatedTracePrefixType::SCOPE_MODULE);
    tracep->declBit(c+69,0,"IN",-1, VerilatedTraceSigDirection::INPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declBit(c+70,0,"OUTN",-1, VerilatedTraceSigDirection::OUTPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declBit(c+71,0,"OUTP",-1, VerilatedTraceSigDirection::OUTPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->pushPrefix("inv1", VerilatedTracePrefixType::SCOPE_MODULE);
    tracep->declBit(c+72,0,"Y",-1, VerilatedTraceSigDirection::OUTPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declBit(c+73,0,"A",-1, VerilatedTraceSigDirection::INPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->popPrefix();
    tracep->pushPrefix("inv2", VerilatedTracePrefixType::SCOPE_MODULE);
    tracep->declBit(c+74,0,"Y",-1, VerilatedTraceSigDirection::OUTPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declBit(c+75,0,"A",-1, VerilatedTraceSigDirection::INPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->popPrefix();
    tracep->popPrefix();
    tracep->popPrefix();
    tracep->pushPrefix("g[2]", VerilatedTracePrefixType::SCOPE_MODULE);
    tracep->pushPrefix("u", VerilatedTracePrefixType::SCOPE_MODULE);
    tracep->declBit(c+76,0,"IN",-1, VerilatedTraceSigDirection::INPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declBit(c+77,0,"OUTN",-1, VerilatedTraceSigDirection::OUTPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declBit(c+78,0,"OUTP",-1, VerilatedTraceSigDirection::OUTPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->pushPrefix("inv1", VerilatedTracePrefixType::SCOPE_MODULE);
    tracep->declBit(c+79,0,"Y",-1, VerilatedTraceSigDirection::OUTPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declBit(c+80,0,"A",-1, VerilatedTraceSigDirection::INPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->popPrefix();
    tracep->pushPrefix("inv2", VerilatedTracePrefixType::SCOPE_MODULE);
    tracep->declBit(c+81,0,"Y",-1, VerilatedTraceSigDirection::OUTPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declBit(c+82,0,"A",-1, VerilatedTraceSigDirection::INPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->popPrefix();
    tracep->popPrefix();
    tracep->popPrefix();
    tracep->pushPrefix("g[3]", VerilatedTracePrefixType::SCOPE_MODULE);
    tracep->pushPrefix("u", VerilatedTracePrefixType::SCOPE_MODULE);
    tracep->declBit(c+83,0,"IN",-1, VerilatedTraceSigDirection::INPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declBit(c+84,0,"OUTN",-1, VerilatedTraceSigDirection::OUTPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declBit(c+85,0,"OUTP",-1, VerilatedTraceSigDirection::OUTPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->pushPrefix("inv1", VerilatedTracePrefixType::SCOPE_MODULE);
    tracep->declBit(c+86,0,"Y",-1, VerilatedTraceSigDirection::OUTPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declBit(c+87,0,"A",-1, VerilatedTraceSigDirection::INPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->popPrefix();
    tracep->pushPrefix("inv2", VerilatedTracePrefixType::SCOPE_MODULE);
    tracep->declBit(c+88,0,"Y",-1, VerilatedTraceSigDirection::OUTPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declBit(c+89,0,"A",-1, VerilatedTraceSigDirection::INPUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->popPrefix();
    tracep->popPrefix();
    tracep->popPrefix();
    tracep->popPrefix();
    tracep->pushPrefix("wires", VerilatedTracePrefixType::SCOPE_MODULE);
    tracep->declBit(c+90,0,"Iout",-1, VerilatedTraceSigDirection::INOUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declBus(c+91,0,"VcascP",-1, VerilatedTraceSigDirection::INOUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1, 1,0);
    tracep->declBus(c+92,0,"VbiasP",-1, VerilatedTraceSigDirection::INOUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1, 1,0);
    tracep->declBit(c+93,0,"i_in",-1, VerilatedTraceSigDirection::INOUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declBit(c+94,0,"i_out",-1, VerilatedTraceSigDirection::INOUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declBus(c+95,0,"VDDA",-1, VerilatedTraceSigDirection::INOUT, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1, 1,0);
    tracep->declBit(c+96,0,"bias",-1, VerilatedTraceSigDirection::NONE, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declBit(c+97,0,"casc",-1, VerilatedTraceSigDirection::NONE, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->declBit(c+98,0,"vdda",-1, VerilatedTraceSigDirection::NONE, VerilatedTraceSigKind::WIRE, VerilatedTraceSigType::LOGIC, false,-1);
    tracep->popPrefix();
    tracep->popPrefix();
}

VL_ATTR_COLD void Vtop___024root__trace_init_top(Vtop___024root* vlSelf, VerilatedVcd* tracep) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root__trace_init_top\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    Vtop___024root__trace_init_sub__TOP__0(vlSelf, tracep);
}

VL_ATTR_COLD void Vtop___024root__trace_const_0(void* voidSelf, VerilatedVcd::Buffer* bufp);
VL_ATTR_COLD void Vtop___024root__trace_full_0(void* voidSelf, VerilatedVcd::Buffer* bufp);
void Vtop___024root__trace_chg_0(void* voidSelf, VerilatedVcd::Buffer* bufp);
void Vtop___024root__trace_cleanup(void* voidSelf, VerilatedVcd* /*unused*/);

VL_ATTR_COLD void Vtop___024root__trace_register(Vtop___024root* vlSelf, VerilatedVcd* tracep) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root__trace_register\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    tracep->addConstCb(&Vtop___024root__trace_const_0, 0, vlSelf);
    tracep->addFullCb(&Vtop___024root__trace_full_0, 0, vlSelf);
    tracep->addChgCb(&Vtop___024root__trace_chg_0, 0, vlSelf);
    tracep->addCleanupCb(&Vtop___024root__trace_cleanup, vlSelf);
}

VL_ATTR_COLD void Vtop___024root__trace_const_0(void* voidSelf, VerilatedVcd::Buffer* bufp) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root__trace_const_0\n"); );
    // Body
    Vtop___024root* const __restrict vlSelf VL_ATTR_UNUSED = static_cast<Vtop___024root*>(voidSelf);
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
}

VL_ATTR_COLD void Vtop___024root__trace_full_0_sub_0(Vtop___024root* vlSelf, VerilatedVcd::Buffer* bufp);

VL_ATTR_COLD void Vtop___024root__trace_full_0(void* voidSelf, VerilatedVcd::Buffer* bufp) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root__trace_full_0\n"); );
    // Body
    Vtop___024root* const __restrict vlSelf VL_ATTR_UNUSED = static_cast<Vtop___024root*>(voidSelf);
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    Vtop___024root__trace_full_0_sub_0((&vlSymsp->TOP), bufp);
}

VL_ATTR_COLD void Vtop___024root__trace_full_0_sub_0(Vtop___024root* vlSelf, VerilatedVcd::Buffer* bufp) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root__trace_full_0_sub_0\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    uint32_t* const oldp VL_ATTR_UNUSED = bufp->oldp(vlSymsp->__Vm_baseCode);
    bufp->fullCData(oldp+1,(vlSelfRef.ui_in),8);
    bufp->fullCData(oldp+2,(vlSelfRef.uo_out),8);
    bufp->fullCData(oldp+3,(vlSelfRef.uio_in),8);
    bufp->fullCData(oldp+4,(vlSelfRef.uio_out),8);
    bufp->fullCData(oldp+5,(vlSelfRef.uio_oe),8);
    bufp->fullBit(oldp+6,(vlSelfRef.ena));
    bufp->fullBit(oldp+7,(vlSelfRef.clk));
    bufp->fullBit(oldp+8,(vlSelfRef.rst_n));
    bufp->fullBit(oldp+9,(vlSelfRef.i_in));
    bufp->fullBit(oldp+10,(vlSelfRef.i_out));
    bufp->fullBit(oldp+11,(vlSelfRef.VPWR));
    bufp->fullBit(oldp+12,(vlSelfRef.VGND));
    bufp->fullCData(oldp+13,(vlSelfRef.heichips25_pudding__DOT__ui_in),8);
    bufp->fullCData(oldp+14,(vlSelfRef.heichips25_pudding__DOT__uo_out),8);
    bufp->fullCData(oldp+15,(vlSelfRef.heichips25_pudding__DOT__uio_in),8);
    bufp->fullCData(oldp+16,(vlSelfRef.heichips25_pudding__DOT__uio_out),8);
    bufp->fullCData(oldp+17,(vlSelfRef.heichips25_pudding__DOT__uio_oe),8);
    bufp->fullBit(oldp+18,(vlSelfRef.heichips25_pudding__DOT__ena));
    bufp->fullBit(oldp+19,(vlSelfRef.heichips25_pudding__DOT__clk));
    bufp->fullBit(oldp+20,(vlSelfRef.heichips25_pudding__DOT__rst_n));
    bufp->fullBit(oldp+21,(vlSelfRef.heichips25_pudding__DOT__i_in));
    bufp->fullBit(oldp+22,(vlSelfRef.heichips25_pudding__DOT__i_out));
    bufp->fullBit(oldp+23,(vlSelfRef.heichips25_pudding__DOT__VPWR));
    bufp->fullBit(oldp+24,(vlSelfRef.heichips25_pudding__DOT__VGND));
    bufp->fullCData(oldp+25,(vlSelfRef.heichips25_pudding__DOT__iref),2);
    bufp->fullCData(oldp+26,(vlSelfRef.heichips25_pudding__DOT__bias),2);
    bufp->fullBit(oldp+27,(vlSelfRef.heichips25_pudding__DOT__dacout));
    bufp->fullCData(oldp+28,(vlSelfRef.heichips25_pudding__DOT__vdda),2);
    bufp->fullCData(oldp+29,(vlSelfRef.heichips25_pudding__DOT__stateen),4);
    bufp->fullCData(oldp+30,(vlSelfRef.heichips25_pudding__DOT__stateenp),4);
    bufp->fullCData(oldp+31,(vlSelfRef.heichips25_pudding__DOT__stateenn),4);
    bufp->fullBit(oldp+32,(vlSelfRef.heichips25_pudding__DOT__datum));
    bufp->fullBit(oldp+33,(vlSelfRef.heichips25_pudding__DOT__shift));
    bufp->fullBit(oldp+34,(vlSelfRef.heichips25_pudding__DOT__transfer));
    bufp->fullBit(oldp+35,(vlSelfRef.heichips25_pudding__DOT__dir));
    bufp->fullWData(oldp+36,(vlSelfRef.heichips25_pudding__DOT__daisychain),128);
    bufp->fullWData(oldp+40,(vlSelfRef.heichips25_pudding__DOT__state),128);
    bufp->fullBit(oldp+44,(vlSelfRef.heichips25_pudding__DOT__dac__DOT__Iout));
    bufp->fullCData(oldp+45,(vlSelfRef.heichips25_pudding__DOT__dac__DOT__VcascP),2);
    bufp->fullCData(oldp+46,(vlSelfRef.heichips25_pudding__DOT__dac__DOT__VbiasP),2);
    bufp->fullWData(oldp+47,(vlSelfRef.heichips25_pudding__DOT__dac__DOT__ON),128);
    bufp->fullWData(oldp+51,(vlSelfRef.heichips25_pudding__DOT__dac__DOT__ONB),128);
    bufp->fullCData(oldp+55,(vlSelfRef.heichips25_pudding__DOT__dac__DOT__EN),4);
    bufp->fullCData(oldp+56,(vlSelfRef.heichips25_pudding__DOT__dac__DOT__ENB),4);
    bufp->fullBit(oldp+57,(vlSelfRef.heichips25_pudding__DOT__dac__DOT__VDD));
    bufp->fullBit(oldp+58,(vlSelfRef.heichips25_pudding__DOT__dac__DOT__VSS));
    bufp->fullCData(oldp+59,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__in),4);
    bufp->fullCData(oldp+60,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__outn),4);
    bufp->fullCData(oldp+61,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__outp),4);
    bufp->fullBit(oldp+62,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__IN));
    bufp->fullBit(oldp+63,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__OUTN));
    bufp->fullBit(oldp+64,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__OUTP));
    bufp->fullBit(oldp+65,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__inv1__DOT__Y));
    bufp->fullBit(oldp+66,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__inv1__DOT__A));
    bufp->fullBit(oldp+67,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__inv2__DOT__Y));
    bufp->fullBit(oldp+68,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__inv2__DOT__A));
    bufp->fullBit(oldp+69,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__IN));
    bufp->fullBit(oldp+70,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__OUTN));
    bufp->fullBit(oldp+71,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__OUTP));
    bufp->fullBit(oldp+72,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__inv1__DOT__Y));
    bufp->fullBit(oldp+73,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__inv1__DOT__A));
    bufp->fullBit(oldp+74,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__inv2__DOT__Y));
    bufp->fullBit(oldp+75,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__inv2__DOT__A));
    bufp->fullBit(oldp+76,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__IN));
    bufp->fullBit(oldp+77,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__OUTN));
    bufp->fullBit(oldp+78,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__OUTP));
    bufp->fullBit(oldp+79,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__inv1__DOT__Y));
    bufp->fullBit(oldp+80,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__inv1__DOT__A));
    bufp->fullBit(oldp+81,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__inv2__DOT__Y));
    bufp->fullBit(oldp+82,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__inv2__DOT__A));
    bufp->fullBit(oldp+83,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__IN));
    bufp->fullBit(oldp+84,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__OUTN));
    bufp->fullBit(oldp+85,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__OUTP));
    bufp->fullBit(oldp+86,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__inv1__DOT__Y));
    bufp->fullBit(oldp+87,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__inv1__DOT__A));
    bufp->fullBit(oldp+88,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__inv2__DOT__Y));
    bufp->fullBit(oldp+89,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__inv2__DOT__A));
    bufp->fullBit(oldp+90,(vlSelfRef.heichips25_pudding__DOT__wires__DOT__Iout));
    bufp->fullCData(oldp+91,(vlSelfRef.heichips25_pudding__DOT__wires__DOT__VcascP),2);
    bufp->fullCData(oldp+92,(vlSelfRef.heichips25_pudding__DOT__wires__DOT__VbiasP),2);
    bufp->fullBit(oldp+93,(vlSelfRef.heichips25_pudding__DOT__wires__DOT__i_in));
    bufp->fullBit(oldp+94,(vlSelfRef.heichips25_pudding__DOT__wires__DOT__i_out));
    bufp->fullCData(oldp+95,(vlSelfRef.heichips25_pudding__DOT__wires__DOT__VDDA),2);
    bufp->fullBit(oldp+96,(vlSelfRef.heichips25_pudding__DOT__wires__DOT__bias));
    bufp->fullBit(oldp+97,(vlSelfRef.heichips25_pudding__DOT__wires__DOT__casc));
    bufp->fullBit(oldp+98,(vlSelfRef.heichips25_pudding__DOT__wires__DOT__vdda));
}
