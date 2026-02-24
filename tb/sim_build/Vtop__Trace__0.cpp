// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Tracing implementation internals
#include "verilated_fst_c.h"
#include "Vtop__Syms.h"


void Vtop___024root__trace_chg_0_sub_0(Vtop___024root* vlSelf, VerilatedFst::Buffer* bufp);

void Vtop___024root__trace_chg_0(void* voidSelf, VerilatedFst::Buffer* bufp) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root__trace_chg_0\n"); );
    // Body
    Vtop___024root* const __restrict vlSelf VL_ATTR_UNUSED = static_cast<Vtop___024root*>(voidSelf);
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    if (VL_UNLIKELY(!vlSymsp->__Vm_activity)) return;
    Vtop___024root__trace_chg_0_sub_0((&vlSymsp->TOP), bufp);
}

void Vtop___024root__trace_chg_0_sub_0(Vtop___024root* vlSelf, VerilatedFst::Buffer* bufp) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root__trace_chg_0_sub_0\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    uint32_t* const oldp VL_ATTR_UNUSED = bufp->oldp(vlSymsp->__Vm_baseCode + 1);
    bufp->chgCData(oldp+0,(vlSelfRef.ui_in),8);
    bufp->chgCData(oldp+1,(vlSelfRef.uo_out),8);
    bufp->chgCData(oldp+2,(vlSelfRef.uio_in),8);
    bufp->chgCData(oldp+3,(vlSelfRef.uio_out),8);
    bufp->chgCData(oldp+4,(vlSelfRef.uio_oe),8);
    bufp->chgBit(oldp+5,(vlSelfRef.ena));
    bufp->chgBit(oldp+6,(vlSelfRef.clk));
    bufp->chgBit(oldp+7,(vlSelfRef.rst_n));
    bufp->chgBit(oldp+8,(vlSelfRef.i_in));
    bufp->chgBit(oldp+9,(vlSelfRef.i_out));
    bufp->chgBit(oldp+10,(vlSelfRef.VPWR));
    bufp->chgBit(oldp+11,(vlSelfRef.VGND));
    bufp->chgCData(oldp+12,(vlSelfRef.heichips25_pudding__DOT__ui_in),8);
    bufp->chgCData(oldp+13,(vlSelfRef.heichips25_pudding__DOT__uo_out),8);
    bufp->chgCData(oldp+14,(vlSelfRef.heichips25_pudding__DOT__uio_in),8);
    bufp->chgCData(oldp+15,(vlSelfRef.heichips25_pudding__DOT__uio_out),8);
    bufp->chgCData(oldp+16,(vlSelfRef.heichips25_pudding__DOT__uio_oe),8);
    bufp->chgBit(oldp+17,(vlSelfRef.heichips25_pudding__DOT__ena));
    bufp->chgBit(oldp+18,(vlSelfRef.heichips25_pudding__DOT__clk));
    bufp->chgBit(oldp+19,(vlSelfRef.heichips25_pudding__DOT__rst_n));
    bufp->chgBit(oldp+20,(vlSelfRef.heichips25_pudding__DOT__i_in));
    bufp->chgBit(oldp+21,(vlSelfRef.heichips25_pudding__DOT__i_out));
    bufp->chgBit(oldp+22,(vlSelfRef.heichips25_pudding__DOT__VPWR));
    bufp->chgBit(oldp+23,(vlSelfRef.heichips25_pudding__DOT__VGND));
    bufp->chgCData(oldp+24,(vlSelfRef.heichips25_pudding__DOT__iref),2);
    bufp->chgCData(oldp+25,(vlSelfRef.heichips25_pudding__DOT__bias),2);
    bufp->chgBit(oldp+26,(vlSelfRef.heichips25_pudding__DOT__dacout));
    bufp->chgCData(oldp+27,(vlSelfRef.heichips25_pudding__DOT__vdda),2);
    bufp->chgCData(oldp+28,(vlSelfRef.heichips25_pudding__DOT__stateen),4);
    bufp->chgCData(oldp+29,(vlSelfRef.heichips25_pudding__DOT__stateenp),4);
    bufp->chgCData(oldp+30,(vlSelfRef.heichips25_pudding__DOT__stateenn),4);
    bufp->chgBit(oldp+31,(vlSelfRef.heichips25_pudding__DOT__datum));
    bufp->chgBit(oldp+32,(vlSelfRef.heichips25_pudding__DOT__shift));
    bufp->chgBit(oldp+33,(vlSelfRef.heichips25_pudding__DOT__transfer));
    bufp->chgBit(oldp+34,(vlSelfRef.heichips25_pudding__DOT__dir));
    bufp->chgWData(oldp+35,(vlSelfRef.heichips25_pudding__DOT__daisychain),128);
    bufp->chgWData(oldp+39,(vlSelfRef.heichips25_pudding__DOT__state),128);
    bufp->chgBit(oldp+43,(vlSelfRef.heichips25_pudding__DOT__dac__DOT__Iout));
    bufp->chgCData(oldp+44,(vlSelfRef.heichips25_pudding__DOT__dac__DOT__VcascP),2);
    bufp->chgCData(oldp+45,(vlSelfRef.heichips25_pudding__DOT__dac__DOT__VbiasP),2);
    bufp->chgWData(oldp+46,(vlSelfRef.heichips25_pudding__DOT__dac__DOT__ON),128);
    bufp->chgWData(oldp+50,(vlSelfRef.heichips25_pudding__DOT__dac__DOT__ONB),128);
    bufp->chgCData(oldp+54,(vlSelfRef.heichips25_pudding__DOT__dac__DOT__EN),4);
    bufp->chgCData(oldp+55,(vlSelfRef.heichips25_pudding__DOT__dac__DOT__ENB),4);
    bufp->chgBit(oldp+56,(vlSelfRef.heichips25_pudding__DOT__dac__DOT__VDD));
    bufp->chgBit(oldp+57,(vlSelfRef.heichips25_pudding__DOT__dac__DOT__VSS));
    bufp->chgCData(oldp+58,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__in),4);
    bufp->chgCData(oldp+59,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__outn),4);
    bufp->chgCData(oldp+60,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__outp),4);
    bufp->chgBit(oldp+61,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__IN));
    bufp->chgBit(oldp+62,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__OUTN));
    bufp->chgBit(oldp+63,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__OUTP));
    bufp->chgBit(oldp+64,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__inv1__DOT__Y));
    bufp->chgBit(oldp+65,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__inv1__DOT__A));
    bufp->chgBit(oldp+66,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__inv2__DOT__Y));
    bufp->chgBit(oldp+67,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__inv2__DOT__A));
    bufp->chgBit(oldp+68,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__IN));
    bufp->chgBit(oldp+69,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__OUTN));
    bufp->chgBit(oldp+70,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__OUTP));
    bufp->chgBit(oldp+71,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__inv1__DOT__Y));
    bufp->chgBit(oldp+72,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__inv1__DOT__A));
    bufp->chgBit(oldp+73,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__inv2__DOT__Y));
    bufp->chgBit(oldp+74,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__inv2__DOT__A));
    bufp->chgBit(oldp+75,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__IN));
    bufp->chgBit(oldp+76,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__OUTN));
    bufp->chgBit(oldp+77,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__OUTP));
    bufp->chgBit(oldp+78,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__inv1__DOT__Y));
    bufp->chgBit(oldp+79,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__inv1__DOT__A));
    bufp->chgBit(oldp+80,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__inv2__DOT__Y));
    bufp->chgBit(oldp+81,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__inv2__DOT__A));
    bufp->chgBit(oldp+82,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__IN));
    bufp->chgBit(oldp+83,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__OUTN));
    bufp->chgBit(oldp+84,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__OUTP));
    bufp->chgBit(oldp+85,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__inv1__DOT__Y));
    bufp->chgBit(oldp+86,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__inv1__DOT__A));
    bufp->chgBit(oldp+87,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__inv2__DOT__Y));
    bufp->chgBit(oldp+88,(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__inv2__DOT__A));
    bufp->chgBit(oldp+89,(vlSelfRef.heichips25_pudding__DOT__wires__DOT__Iout));
    bufp->chgCData(oldp+90,(vlSelfRef.heichips25_pudding__DOT__wires__DOT__VcascP),2);
    bufp->chgCData(oldp+91,(vlSelfRef.heichips25_pudding__DOT__wires__DOT__VbiasP),2);
    bufp->chgBit(oldp+92,(vlSelfRef.heichips25_pudding__DOT__wires__DOT__i_in));
    bufp->chgBit(oldp+93,(vlSelfRef.heichips25_pudding__DOT__wires__DOT__i_out));
    bufp->chgCData(oldp+94,(vlSelfRef.heichips25_pudding__DOT__wires__DOT__VDDA),2);
    bufp->chgBit(oldp+95,(vlSelfRef.heichips25_pudding__DOT__wires__DOT__bias));
    bufp->chgBit(oldp+96,(vlSelfRef.heichips25_pudding__DOT__wires__DOT__casc));
    bufp->chgBit(oldp+97,(vlSelfRef.heichips25_pudding__DOT__wires__DOT__vdda));
}

void Vtop___024root__trace_cleanup(void* voidSelf, VerilatedFst* /*unused*/) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root__trace_cleanup\n"); );
    // Locals
    VlUnpacked<CData/*0:0*/, 1> __Vm_traceActivity;
    for (int __Vi0 = 0; __Vi0 < 1; ++__Vi0) {
        __Vm_traceActivity[__Vi0] = 0;
    }
    // Body
    Vtop___024root* const __restrict vlSelf VL_ATTR_UNUSED = static_cast<Vtop___024root*>(voidSelf);
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    vlSymsp->__Vm_activity = false;
    __Vm_traceActivity[0U] = 0U;
}
