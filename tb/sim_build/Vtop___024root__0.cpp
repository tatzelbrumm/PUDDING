// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design implementation internals
// See Vtop.h for the primary calling header

#include "Vtop__pch.h"

#ifdef VL_DEBUG
VL_ATTR_COLD void Vtop___024root___dump_triggers__ico(const VlUnpacked<QData/*63:0*/, 1> &triggers, const std::string &tag);
#endif  // VL_DEBUG

void Vtop___024root___eval_triggers__ico(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_triggers__ico\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    vlSelfRef.__VicoTriggered[0U] = ((0xfffffffffffffffeULL 
                                      & vlSelfRef.__VicoTriggered
                                      [0U]) | (IData)((IData)(vlSelfRef.__VicoFirstIteration)));
    vlSelfRef.__VicoFirstIteration = 0U;
#ifdef VL_DEBUG
    if (VL_UNLIKELY(vlSymsp->_vm_contextp__->debug())) {
        Vtop___024root___dump_triggers__ico(vlSelfRef.__VicoTriggered, "ico"s);
    }
#endif
}

bool Vtop___024root___trigger_anySet__ico(const VlUnpacked<QData/*63:0*/, 1> &in) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___trigger_anySet__ico\n"); );
    // Locals
    IData/*31:0*/ n;
    // Body
    n = 0U;
    do {
        if (in[n]) {
            return (1U);
        }
        n = ((IData)(1U) + n);
    } while ((1U > n));
    return (0U);
}

void Vtop___024root___ico_sequent__TOP__0(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___ico_sequent__TOP__0\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    vlSelfRef.heichips25_pudding__DOT__clk = vlSelfRef.clk;
    vlSelfRef.heichips25_pudding__DOT__dac__DOT__ON[0U] 
        = vlSelfRef.heichips25_pudding__DOT__state[0U];
    vlSelfRef.heichips25_pudding__DOT__dac__DOT__ON[1U] 
        = vlSelfRef.heichips25_pudding__DOT__state[1U];
    vlSelfRef.heichips25_pudding__DOT__dac__DOT__ON[2U] 
        = vlSelfRef.heichips25_pudding__DOT__state[2U];
    vlSelfRef.heichips25_pudding__DOT__dac__DOT__ON[3U] 
        = vlSelfRef.heichips25_pudding__DOT__state[3U];
    vlSelfRef.heichips25_pudding__DOT__dac__DOT__ONB[0U] 
        = (~ vlSelfRef.heichips25_pudding__DOT__state[0U]);
    vlSelfRef.heichips25_pudding__DOT__dac__DOT__ONB[1U] 
        = (~ vlSelfRef.heichips25_pudding__DOT__state[1U]);
    vlSelfRef.heichips25_pudding__DOT__dac__DOT__ONB[2U] 
        = (~ vlSelfRef.heichips25_pudding__DOT__state[2U]);
    vlSelfRef.heichips25_pudding__DOT__dac__DOT__ONB[3U] 
        = (~ vlSelfRef.heichips25_pudding__DOT__state[3U]);
    vlSelfRef.uio_oe = vlSelfRef.heichips25_pudding__DOT__uio_oe;
    vlSelfRef.heichips25_pudding__DOT__rst_n = vlSelfRef.rst_n;
    vlSelfRef.heichips25_pudding__DOT__dac__DOT__Iout 
        = vlSelfRef.heichips25_pudding__DOT__dacout;
    vlSelfRef.heichips25_pudding__DOT__wires__DOT__Iout 
        = vlSelfRef.heichips25_pudding__DOT__dacout;
    vlSelfRef.heichips25_pudding__DOT__i_in = vlSelfRef.i_in;
    vlSelfRef.heichips25_pudding__DOT__i_out = vlSelfRef.i_out;
    vlSelfRef.heichips25_pudding__DOT__VPWR = vlSelfRef.VPWR;
    vlSelfRef.heichips25_pudding__DOT__VGND = vlSelfRef.VGND;
    vlSelfRef.heichips25_pudding__DOT__uo_out = (vlSelfRef.heichips25_pudding__DOT__daisychain[3U] 
                                                 >> 0x00000018U);
    vlSelfRef.heichips25_pudding__DOT__uio_out = (vlSelfRef.heichips25_pudding__DOT__state[3U] 
                                                  >> 0x00000018U);
    vlSelfRef.heichips25_pudding__DOT__uio_in = vlSelfRef.uio_in;
    vlSelfRef.heichips25_pudding__DOT__ena = vlSelfRef.ena;
    vlSelfRef.heichips25_pudding__DOT__wires__DOT__VcascP__out__strong__out1 
        = ((2U & (IData)(vlSelfRef.heichips25_pudding__DOT__wires__DOT__VcascP__out__strong__out1)) 
           | (IData)(vlSelfRef.heichips25_pudding__DOT__wires__DOT__casc));
    vlSelfRef.heichips25_pudding__DOT__wires__DOT__VcascP__out__strong__out2 
        = ((1U & (IData)(vlSelfRef.heichips25_pudding__DOT__wires__DOT__VcascP__out__strong__out2)) 
           | ((IData)(vlSelfRef.heichips25_pudding__DOT__wires__DOT__casc) 
              << 1U));
    vlSelfRef.heichips25_pudding__DOT__wires__DOT__VbiasP__out__strong__out3 
        = ((2U & (IData)(vlSelfRef.heichips25_pudding__DOT__wires__DOT__VbiasP__out__strong__out3)) 
           | (IData)(vlSelfRef.heichips25_pudding__DOT__wires__DOT__bias));
    vlSelfRef.heichips25_pudding__DOT__wires__DOT__VbiasP__out__strong__out4 
        = ((1U & (IData)(vlSelfRef.heichips25_pudding__DOT__wires__DOT__VbiasP__out__strong__out4)) 
           | ((IData)(vlSelfRef.heichips25_pudding__DOT__wires__DOT__bias) 
              << 1U));
    vlSelfRef.heichips25_pudding__DOT__wires__DOT__VDDA__out__strong__out7 
        = ((1U & (IData)(vlSelfRef.heichips25_pudding__DOT__wires__DOT__VDDA__out__strong__out7)) 
           | ((IData)(vlSelfRef.heichips25_pudding__DOT__wires__DOT__vdda) 
              << 1U));
    vlSelfRef.heichips25_pudding__DOT__wires__DOT__VDDA__out__strong__out8 
        = ((2U & (IData)(vlSelfRef.heichips25_pudding__DOT__wires__DOT__VDDA__out__strong__out8)) 
           | (IData)(vlSelfRef.heichips25_pudding__DOT__wires__DOT__vdda));
    vlSelfRef.heichips25_pudding__DOT__ui_in = vlSelfRef.ui_in;
    vlSelfRef.heichips25_pudding__DOT__wires__DOT__i_in 
        = vlSelfRef.heichips25_pudding__DOT__i_in;
    vlSelfRef.heichips25_pudding__DOT__wires__DOT__i_out 
        = vlSelfRef.heichips25_pudding__DOT__i_out;
    vlSelfRef.heichips25_pudding__DOT__dac__DOT__VDD 
        = vlSelfRef.heichips25_pudding__DOT__VPWR;
    vlSelfRef.heichips25_pudding__DOT__dac__DOT__VSS 
        = vlSelfRef.heichips25_pudding__DOT__VGND;
    vlSelfRef.uo_out = vlSelfRef.heichips25_pudding__DOT__uo_out;
    vlSelfRef.uio_out = vlSelfRef.heichips25_pudding__DOT__uio_out;
    vlSelfRef.heichips25_pudding__DOT__iref = ((IData)(vlSelfRef.heichips25_pudding__DOT__wires__DOT__VcascP__out__strong__out1) 
                                               | (IData)(vlSelfRef.heichips25_pudding__DOT__wires__DOT__VcascP__out__strong__out2));
    vlSelfRef.heichips25_pudding__DOT__bias = ((IData)(vlSelfRef.heichips25_pudding__DOT__wires__DOT__VbiasP__out__strong__out3) 
                                               | (IData)(vlSelfRef.heichips25_pudding__DOT__wires__DOT__VbiasP__out__strong__out4));
    vlSelfRef.heichips25_pudding__DOT__vdda = ((IData)(vlSelfRef.heichips25_pudding__DOT__wires__DOT__VDDA__out__strong__out7) 
                                               | (IData)(vlSelfRef.heichips25_pudding__DOT__wires__DOT__VDDA__out__strong__out8));
    vlSelfRef.heichips25_pudding__DOT__datum = (1U 
                                                & (IData)(vlSelfRef.heichips25_pudding__DOT__ui_in));
    vlSelfRef.heichips25_pudding__DOT__shift = (1U 
                                                & ((IData)(vlSelfRef.heichips25_pudding__DOT__ui_in) 
                                                   >> 1U));
    vlSelfRef.heichips25_pudding__DOT__transfer = (1U 
                                                   & ((IData)(vlSelfRef.heichips25_pudding__DOT__ui_in) 
                                                      >> 2U));
    vlSelfRef.heichips25_pudding__DOT__dir = (1U & 
                                              ((IData)(vlSelfRef.heichips25_pudding__DOT__ui_in) 
                                               >> 3U));
    vlSelfRef.heichips25_pudding__DOT__stateen = (0x0000000fU 
                                                  & (- (IData)(
                                                               (1U 
                                                                & ((IData)(vlSelfRef.heichips25_pudding__DOT__ui_in) 
                                                                   >> 4U)))));
    vlSelfRef.heichips25_pudding__DOT__dac__DOT__VcascP 
        = vlSelfRef.heichips25_pudding__DOT__iref;
    vlSelfRef.heichips25_pudding__DOT__wires__DOT__VcascP 
        = vlSelfRef.heichips25_pudding__DOT__iref;
    vlSelfRef.heichips25_pudding__DOT__dac__DOT__VbiasP 
        = vlSelfRef.heichips25_pudding__DOT__bias;
    vlSelfRef.heichips25_pudding__DOT__wires__DOT__VbiasP 
        = vlSelfRef.heichips25_pudding__DOT__bias;
    vlSelfRef.heichips25_pudding__DOT__wires__DOT__VDDA 
        = vlSelfRef.heichips25_pudding__DOT__vdda;
    vlSelfRef.heichips25_pudding__DOT___unused = ((IData)(vlSelfRef.heichips25_pudding__DOT__ena) 
                                                  & ((0x000000ffU 
                                                      == (IData)(vlSelfRef.heichips25_pudding__DOT__uio_in)) 
                                                     & (IData)(
                                                               ((0xe0U 
                                                                 == 
                                                                 (0xe0U 
                                                                  & (IData)(vlSelfRef.heichips25_pudding__DOT__ui_in))) 
                                                                & (3U 
                                                                   == (IData)(vlSelfRef.heichips25_pudding__DOT__vdda))))));
    vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__in 
        = vlSelfRef.heichips25_pudding__DOT__stateen;
    vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__IN 
        = (1U & (IData)(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__in));
    vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__IN 
        = (1U & ((IData)(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__in) 
                 >> 1U));
    vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__IN 
        = (1U & ((IData)(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__in) 
                 >> 2U));
    vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__IN 
        = (1U & ((IData)(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__in) 
                 >> 3U));
    vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__inv1__DOT__A 
        = vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__IN;
    vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__inv1__DOT__A 
        = vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__IN;
    vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__inv1__DOT__A 
        = vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__IN;
    vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__inv1__DOT__A 
        = vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__IN;
    vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__inv1__DOT__Y 
        = (1U & (~ (IData)(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__inv1__DOT__A)));
    vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__inv1__DOT__Y 
        = (1U & (~ (IData)(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__inv1__DOT__A)));
    vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__inv1__DOT__Y 
        = (1U & (~ (IData)(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__inv1__DOT__A)));
    vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__inv1__DOT__Y 
        = (1U & (~ (IData)(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__inv1__DOT__A)));
    vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__OUTN 
        = vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__inv1__DOT__Y;
    vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__OUTN 
        = vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__inv1__DOT__Y;
    vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__OUTN 
        = vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__inv1__DOT__Y;
    vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__OUTN 
        = vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__inv1__DOT__Y;
    vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__inv2__DOT__A 
        = vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__OUTN;
    vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__inv2__DOT__A 
        = vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__OUTN;
    vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__inv2__DOT__A 
        = vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__OUTN;
    vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__outn 
        = ((((IData)(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__OUTN) 
             << 3U) | ((IData)(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__OUTN) 
                       << 2U)) | (((IData)(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__OUTN) 
                                   << 1U) | (IData)(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__OUTN)));
    vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__inv2__DOT__A 
        = vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__OUTN;
    vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__inv2__DOT__Y 
        = (1U & (~ (IData)(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__inv2__DOT__A)));
    vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__inv2__DOT__Y 
        = (1U & (~ (IData)(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__inv2__DOT__A)));
    vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__inv2__DOT__Y 
        = (1U & (~ (IData)(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__inv2__DOT__A)));
    vlSelfRef.heichips25_pudding__DOT__stateenn = vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__outn;
    vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__inv2__DOT__Y 
        = (1U & (~ (IData)(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__inv2__DOT__A)));
    vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__OUTP 
        = vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__inv2__DOT__Y;
    vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__OUTP 
        = vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__inv2__DOT__Y;
    vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__OUTP 
        = vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__inv2__DOT__Y;
    vlSelfRef.heichips25_pudding__DOT__dac__DOT__ENB 
        = vlSelfRef.heichips25_pudding__DOT__stateenn;
    vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__OUTP 
        = vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__inv2__DOT__Y;
    vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__outp 
        = ((((IData)(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__OUTP) 
             << 3U) | ((IData)(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__OUTP) 
                       << 2U)) | (((IData)(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__OUTP) 
                                   << 1U) | (IData)(vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__OUTP)));
    vlSelfRef.heichips25_pudding__DOT__stateenp = vlSelfRef.heichips25_pudding__DOT__digitalen__DOT__outp;
    vlSelfRef.heichips25_pudding__DOT__dac__DOT__EN 
        = vlSelfRef.heichips25_pudding__DOT__stateenp;
}

void Vtop___024root___eval_ico(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_ico\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    if ((1ULL & vlSelfRef.__VicoTriggered[0U])) {
        Vtop___024root___ico_sequent__TOP__0(vlSelf);
    }
}

bool Vtop___024root___eval_phase__ico(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_phase__ico\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Locals
    CData/*0:0*/ __VicoExecute;
    // Body
    Vtop___024root___eval_triggers__ico(vlSelf);
    __VicoExecute = Vtop___024root___trigger_anySet__ico(vlSelfRef.__VicoTriggered);
    if (__VicoExecute) {
        Vtop___024root___eval_ico(vlSelf);
    }
    return (__VicoExecute);
}

#ifdef VL_DEBUG
VL_ATTR_COLD void Vtop___024root___dump_triggers__act(const VlUnpacked<QData/*63:0*/, 1> &triggers, const std::string &tag);
#endif  // VL_DEBUG

void Vtop___024root___eval_triggers__act(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_triggers__act\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    vlSelfRef.__VactTriggered[0U] = (QData)((IData)(
                                                    ((IData)(vlSelfRef.heichips25_pudding__DOT__clk) 
                                                     & (~ (IData)(vlSelfRef.__Vtrigprevexpr___TOP__heichips25_pudding__DOT__clk__0)))));
    vlSelfRef.__Vtrigprevexpr___TOP__heichips25_pudding__DOT__clk__0 
        = vlSelfRef.heichips25_pudding__DOT__clk;
#ifdef VL_DEBUG
    if (VL_UNLIKELY(vlSymsp->_vm_contextp__->debug())) {
        Vtop___024root___dump_triggers__act(vlSelfRef.__VactTriggered, "act"s);
    }
#endif
}

bool Vtop___024root___trigger_anySet__act(const VlUnpacked<QData/*63:0*/, 1> &in) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___trigger_anySet__act\n"); );
    // Locals
    IData/*31:0*/ n;
    // Body
    n = 0U;
    do {
        if (in[n]) {
            return (1U);
        }
        n = ((IData)(1U) + n);
    } while ((1U > n));
    return (0U);
}

void Vtop___024root___nba_sequent__TOP__0(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___nba_sequent__TOP__0\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Locals
    VlWide<4>/*127:0*/ __Vdly__heichips25_pudding__DOT__state;
    VL_ZERO_W(128, __Vdly__heichips25_pudding__DOT__state);
    VlWide<4>/*127:0*/ __Vdly__heichips25_pudding__DOT__daisychain;
    VL_ZERO_W(128, __Vdly__heichips25_pudding__DOT__daisychain);
    // Body
    __Vdly__heichips25_pudding__DOT__daisychain[0U] 
        = vlSelfRef.heichips25_pudding__DOT__daisychain[0U];
    __Vdly__heichips25_pudding__DOT__daisychain[1U] 
        = vlSelfRef.heichips25_pudding__DOT__daisychain[1U];
    __Vdly__heichips25_pudding__DOT__daisychain[2U] 
        = vlSelfRef.heichips25_pudding__DOT__daisychain[2U];
    __Vdly__heichips25_pudding__DOT__daisychain[3U] 
        = vlSelfRef.heichips25_pudding__DOT__daisychain[3U];
    __Vdly__heichips25_pudding__DOT__state[0U] = vlSelfRef.heichips25_pudding__DOT__state[0U];
    __Vdly__heichips25_pudding__DOT__state[1U] = vlSelfRef.heichips25_pudding__DOT__state[1U];
    __Vdly__heichips25_pudding__DOT__state[2U] = vlSelfRef.heichips25_pudding__DOT__state[2U];
    __Vdly__heichips25_pudding__DOT__state[3U] = vlSelfRef.heichips25_pudding__DOT__state[3U];
    if (vlSelfRef.heichips25_pudding__DOT__rst_n) {
        if (vlSelfRef.heichips25_pudding__DOT__transfer) {
            if (vlSelfRef.heichips25_pudding__DOT__dir) {
                __Vdly__heichips25_pudding__DOT__state[0U] 
                    = vlSelfRef.heichips25_pudding__DOT__daisychain[0U];
                __Vdly__heichips25_pudding__DOT__state[1U] 
                    = vlSelfRef.heichips25_pudding__DOT__daisychain[1U];
                __Vdly__heichips25_pudding__DOT__state[2U] 
                    = vlSelfRef.heichips25_pudding__DOT__daisychain[2U];
                __Vdly__heichips25_pudding__DOT__state[3U] 
                    = vlSelfRef.heichips25_pudding__DOT__daisychain[3U];
            } else {
                __Vdly__heichips25_pudding__DOT__daisychain[0U] 
                    = vlSelfRef.heichips25_pudding__DOT__state[0U];
                __Vdly__heichips25_pudding__DOT__daisychain[1U] 
                    = vlSelfRef.heichips25_pudding__DOT__state[1U];
                __Vdly__heichips25_pudding__DOT__daisychain[2U] 
                    = vlSelfRef.heichips25_pudding__DOT__state[2U];
                __Vdly__heichips25_pudding__DOT__daisychain[3U] 
                    = vlSelfRef.heichips25_pudding__DOT__state[3U];
            }
        } else if (vlSelfRef.heichips25_pudding__DOT__shift) {
            __Vdly__heichips25_pudding__DOT__daisychain[0U] 
                = ((vlSelfRef.heichips25_pudding__DOT__daisychain[0U] 
                    << 1U) | (IData)(vlSelfRef.heichips25_pudding__DOT__datum));
            __Vdly__heichips25_pudding__DOT__daisychain[1U] 
                = ((vlSelfRef.heichips25_pudding__DOT__daisychain[0U] 
                    >> 0x0000001fU) | (vlSelfRef.heichips25_pudding__DOT__daisychain[1U] 
                                       << 1U));
            __Vdly__heichips25_pudding__DOT__daisychain[2U] 
                = ((vlSelfRef.heichips25_pudding__DOT__daisychain[1U] 
                    >> 0x0000001fU) | (vlSelfRef.heichips25_pudding__DOT__daisychain[2U] 
                                       << 1U));
            __Vdly__heichips25_pudding__DOT__daisychain[3U] 
                = ((vlSelfRef.heichips25_pudding__DOT__daisychain[2U] 
                    >> 0x0000001fU) | (vlSelfRef.heichips25_pudding__DOT__daisychain[3U] 
                                       << 1U));
        }
    } else {
        __Vdly__heichips25_pudding__DOT__daisychain[0U] = 0U;
        __Vdly__heichips25_pudding__DOT__daisychain[1U] = 0U;
        __Vdly__heichips25_pudding__DOT__daisychain[2U] = 0U;
        __Vdly__heichips25_pudding__DOT__daisychain[3U] = 0U;
        __Vdly__heichips25_pudding__DOT__state[0U] = 0U;
        __Vdly__heichips25_pudding__DOT__state[1U] = 0U;
        __Vdly__heichips25_pudding__DOT__state[2U] = 0U;
        __Vdly__heichips25_pudding__DOT__state[3U] = 0U;
    }
    vlSelfRef.heichips25_pudding__DOT__daisychain[0U] 
        = __Vdly__heichips25_pudding__DOT__daisychain[0U];
    vlSelfRef.heichips25_pudding__DOT__daisychain[1U] 
        = __Vdly__heichips25_pudding__DOT__daisychain[1U];
    vlSelfRef.heichips25_pudding__DOT__daisychain[2U] 
        = __Vdly__heichips25_pudding__DOT__daisychain[2U];
    vlSelfRef.heichips25_pudding__DOT__daisychain[3U] 
        = __Vdly__heichips25_pudding__DOT__daisychain[3U];
    vlSelfRef.heichips25_pudding__DOT__state[0U] = 
        __Vdly__heichips25_pudding__DOT__state[0U];
    vlSelfRef.heichips25_pudding__DOT__state[1U] = 
        __Vdly__heichips25_pudding__DOT__state[1U];
    vlSelfRef.heichips25_pudding__DOT__state[2U] = 
        __Vdly__heichips25_pudding__DOT__state[2U];
    vlSelfRef.heichips25_pudding__DOT__state[3U] = 
        __Vdly__heichips25_pudding__DOT__state[3U];
    vlSelfRef.heichips25_pudding__DOT__uo_out = (vlSelfRef.heichips25_pudding__DOT__daisychain[3U] 
                                                 >> 0x00000018U);
    vlSelfRef.heichips25_pudding__DOT__dac__DOT__ON[0U] 
        = vlSelfRef.heichips25_pudding__DOT__state[0U];
    vlSelfRef.heichips25_pudding__DOT__dac__DOT__ON[1U] 
        = vlSelfRef.heichips25_pudding__DOT__state[1U];
    vlSelfRef.heichips25_pudding__DOT__dac__DOT__ON[2U] 
        = vlSelfRef.heichips25_pudding__DOT__state[2U];
    vlSelfRef.heichips25_pudding__DOT__dac__DOT__ON[3U] 
        = vlSelfRef.heichips25_pudding__DOT__state[3U];
    vlSelfRef.heichips25_pudding__DOT__dac__DOT__ONB[0U] 
        = (~ vlSelfRef.heichips25_pudding__DOT__state[0U]);
    vlSelfRef.heichips25_pudding__DOT__dac__DOT__ONB[1U] 
        = (~ vlSelfRef.heichips25_pudding__DOT__state[1U]);
    vlSelfRef.heichips25_pudding__DOT__dac__DOT__ONB[2U] 
        = (~ vlSelfRef.heichips25_pudding__DOT__state[2U]);
    vlSelfRef.heichips25_pudding__DOT__dac__DOT__ONB[3U] 
        = (~ vlSelfRef.heichips25_pudding__DOT__state[3U]);
    vlSelfRef.heichips25_pudding__DOT__uio_out = (vlSelfRef.heichips25_pudding__DOT__state[3U] 
                                                  >> 0x00000018U);
    vlSelfRef.uo_out = vlSelfRef.heichips25_pudding__DOT__uo_out;
    vlSelfRef.uio_out = vlSelfRef.heichips25_pudding__DOT__uio_out;
}

void Vtop___024root___eval_nba(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_nba\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    if ((1ULL & vlSelfRef.__VnbaTriggered[0U])) {
        Vtop___024root___nba_sequent__TOP__0(vlSelf);
    }
}

void Vtop___024root___trigger_orInto__act(VlUnpacked<QData/*63:0*/, 1> &out, const VlUnpacked<QData/*63:0*/, 1> &in) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___trigger_orInto__act\n"); );
    // Locals
    IData/*31:0*/ n;
    // Body
    n = 0U;
    do {
        out[n] = (out[n] | in[n]);
        n = ((IData)(1U) + n);
    } while ((1U > n));
}

bool Vtop___024root___eval_phase__act(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_phase__act\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    Vtop___024root___eval_triggers__act(vlSelf);
    Vtop___024root___trigger_orInto__act(vlSelfRef.__VnbaTriggered, vlSelfRef.__VactTriggered);
    return (0U);
}

void Vtop___024root___trigger_clear__act(VlUnpacked<QData/*63:0*/, 1> &out) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___trigger_clear__act\n"); );
    // Locals
    IData/*31:0*/ n;
    // Body
    n = 0U;
    do {
        out[n] = 0ULL;
        n = ((IData)(1U) + n);
    } while ((1U > n));
}

bool Vtop___024root___eval_phase__nba(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_phase__nba\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Locals
    CData/*0:0*/ __VnbaExecute;
    // Body
    __VnbaExecute = Vtop___024root___trigger_anySet__act(vlSelfRef.__VnbaTriggered);
    if (__VnbaExecute) {
        Vtop___024root___eval_nba(vlSelf);
        Vtop___024root___trigger_clear__act(vlSelfRef.__VnbaTriggered);
    }
    return (__VnbaExecute);
}

void Vtop___024root___eval(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Locals
    IData/*31:0*/ __VicoIterCount;
    IData/*31:0*/ __VnbaIterCount;
    // Body
    __VicoIterCount = 0U;
    vlSelfRef.__VicoFirstIteration = 1U;
    do {
        if (VL_UNLIKELY(((0x00000064U < __VicoIterCount)))) {
#ifdef VL_DEBUG
            Vtop___024root___dump_triggers__ico(vlSelfRef.__VicoTriggered, "ico"s);
#endif
            VL_FATAL_MT("/home/cmaier/EDA/PUDDING/src/heichips25_pudding.sv", 9, "", "Input combinational region did not converge after 100 tries");
        }
        __VicoIterCount = ((IData)(1U) + __VicoIterCount);
    } while (Vtop___024root___eval_phase__ico(vlSelf));
    __VnbaIterCount = 0U;
    do {
        if (VL_UNLIKELY(((0x00000064U < __VnbaIterCount)))) {
#ifdef VL_DEBUG
            Vtop___024root___dump_triggers__act(vlSelfRef.__VnbaTriggered, "nba"s);
#endif
            VL_FATAL_MT("/home/cmaier/EDA/PUDDING/src/heichips25_pudding.sv", 9, "", "NBA region did not converge after 100 tries");
        }
        __VnbaIterCount = ((IData)(1U) + __VnbaIterCount);
        vlSelfRef.__VactIterCount = 0U;
        do {
            if (VL_UNLIKELY(((0x00000064U < vlSelfRef.__VactIterCount)))) {
#ifdef VL_DEBUG
                Vtop___024root___dump_triggers__act(vlSelfRef.__VactTriggered, "act"s);
#endif
                VL_FATAL_MT("/home/cmaier/EDA/PUDDING/src/heichips25_pudding.sv", 9, "", "Active region did not converge after 100 tries");
            }
            vlSelfRef.__VactIterCount = ((IData)(1U) 
                                         + vlSelfRef.__VactIterCount);
        } while (Vtop___024root___eval_phase__act(vlSelf));
    } while (Vtop___024root___eval_phase__nba(vlSelf));
}

#ifdef VL_DEBUG
void Vtop___024root___eval_debug_assertions(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_debug_assertions\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    if (VL_UNLIKELY(((vlSelfRef.ena & 0xfeU)))) {
        Verilated::overWidthError("ena");
    }
    if (VL_UNLIKELY(((vlSelfRef.clk & 0xfeU)))) {
        Verilated::overWidthError("clk");
    }
    if (VL_UNLIKELY(((vlSelfRef.rst_n & 0xfeU)))) {
        Verilated::overWidthError("rst_n");
    }
    if (VL_UNLIKELY(((vlSelfRef.i_in & 0xfeU)))) {
        Verilated::overWidthError("i_in");
    }
    if (VL_UNLIKELY(((vlSelfRef.i_out & 0xfeU)))) {
        Verilated::overWidthError("i_out");
    }
    if (VL_UNLIKELY(((vlSelfRef.VPWR & 0xfeU)))) {
        Verilated::overWidthError("VPWR");
    }
    if (VL_UNLIKELY(((vlSelfRef.VGND & 0xfeU)))) {
        Verilated::overWidthError("VGND");
    }
}
#endif  // VL_DEBUG
