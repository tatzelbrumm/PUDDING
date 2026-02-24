// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design implementation internals
// See Vtop.h for the primary calling header

#include "Vtop__pch.h"

VL_ATTR_COLD void Vtop___024root___eval_static(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_static\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    vlSelfRef.__Vtrigprevexpr___TOP__heichips25_pudding__DOT__clk__0 
        = vlSelfRef.heichips25_pudding__DOT__clk;
    vlSelfRef.__Vtrigprevexpr___TOP__heichips25_pudding__DOT__rst_n__0 
        = vlSelfRef.heichips25_pudding__DOT__rst_n;
}

VL_ATTR_COLD void Vtop___024root___eval_initial__TOP(Vtop___024root* vlSelf);

VL_ATTR_COLD void Vtop___024root___eval_initial(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_initial\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    Vtop___024root___eval_initial__TOP(vlSelf);
}

VL_ATTR_COLD void Vtop___024root___eval_initial__TOP(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_initial__TOP\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    vlSelfRef.heichips25_pudding__DOT__uio_oe = 0xffU;
    vlSelfRef.i_in = 0U;
    vlSelfRef.i_out = 0U;
    vlSelfRef.VPWR = 0U;
    vlSelfRef.VGND = 0U;
    vlSelfRef.heichips25_pudding__DOT__dacout = 0U;
}

VL_ATTR_COLD void Vtop___024root___eval_final(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_final\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
}

#ifdef VL_DEBUG
VL_ATTR_COLD void Vtop___024root___dump_triggers__stl(const VlUnpacked<QData/*63:0*/, 1> &triggers, const std::string &tag);
#endif  // VL_DEBUG
VL_ATTR_COLD bool Vtop___024root___eval_phase__stl(Vtop___024root* vlSelf);

VL_ATTR_COLD void Vtop___024root___eval_settle(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_settle\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Locals
    IData/*31:0*/ __VstlIterCount;
    // Body
    __VstlIterCount = 0U;
    vlSelfRef.__VstlFirstIteration = 1U;
    do {
        if (VL_UNLIKELY(((0x00000064U < __VstlIterCount)))) {
#ifdef VL_DEBUG
            Vtop___024root___dump_triggers__stl(vlSelfRef.__VstlTriggered, "stl"s);
#endif
            VL_FATAL_MT("/home/cmaier/EDA/PUDDING/src/heichips25_pudding.sv", 9, "", "Settle region did not converge after 100 tries");
        }
        __VstlIterCount = ((IData)(1U) + __VstlIterCount);
    } while (Vtop___024root___eval_phase__stl(vlSelf));
}

VL_ATTR_COLD void Vtop___024root___eval_triggers__stl(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_triggers__stl\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    vlSelfRef.__VstlTriggered[0U] = ((0xfffffffffffffffeULL 
                                      & vlSelfRef.__VstlTriggered
                                      [0U]) | (IData)((IData)(vlSelfRef.__VstlFirstIteration)));
    vlSelfRef.__VstlFirstIteration = 0U;
#ifdef VL_DEBUG
    if (VL_UNLIKELY(vlSymsp->_vm_contextp__->debug())) {
        Vtop___024root___dump_triggers__stl(vlSelfRef.__VstlTriggered, "stl"s);
    }
#endif
}

VL_ATTR_COLD bool Vtop___024root___trigger_anySet__stl(const VlUnpacked<QData/*63:0*/, 1> &in);

#ifdef VL_DEBUG
VL_ATTR_COLD void Vtop___024root___dump_triggers__stl(const VlUnpacked<QData/*63:0*/, 1> &triggers, const std::string &tag) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___dump_triggers__stl\n"); );
    // Body
    if ((1U & (~ (IData)(Vtop___024root___trigger_anySet__stl(triggers))))) {
        VL_DBG_MSGS("         No '" + tag + "' region triggers active\n");
    }
    if ((1U & (IData)(triggers[0U]))) {
        VL_DBG_MSGS("         '" + tag + "' region trigger index 0 is active: Internal 'stl' trigger - first iteration\n");
    }
}
#endif  // VL_DEBUG

VL_ATTR_COLD bool Vtop___024root___trigger_anySet__stl(const VlUnpacked<QData/*63:0*/, 1> &in) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___trigger_anySet__stl\n"); );
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

VL_ATTR_COLD void Vtop___024root___stl_sequent__TOP__0(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___stl_sequent__TOP__0\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
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
    vlSelfRef.heichips25_pudding__DOT__clk = vlSelfRef.clk;
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

VL_ATTR_COLD void Vtop___024root___eval_stl(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_stl\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    if ((1ULL & vlSelfRef.__VstlTriggered[0U])) {
        Vtop___024root___stl_sequent__TOP__0(vlSelf);
    }
}

VL_ATTR_COLD bool Vtop___024root___eval_phase__stl(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_phase__stl\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Locals
    CData/*0:0*/ __VstlExecute;
    // Body
    Vtop___024root___eval_triggers__stl(vlSelf);
    __VstlExecute = Vtop___024root___trigger_anySet__stl(vlSelfRef.__VstlTriggered);
    if (__VstlExecute) {
        Vtop___024root___eval_stl(vlSelf);
    }
    return (__VstlExecute);
}

bool Vtop___024root___trigger_anySet__ico(const VlUnpacked<QData/*63:0*/, 1> &in);

#ifdef VL_DEBUG
VL_ATTR_COLD void Vtop___024root___dump_triggers__ico(const VlUnpacked<QData/*63:0*/, 1> &triggers, const std::string &tag) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___dump_triggers__ico\n"); );
    // Body
    if ((1U & (~ (IData)(Vtop___024root___trigger_anySet__ico(triggers))))) {
        VL_DBG_MSGS("         No '" + tag + "' region triggers active\n");
    }
    if ((1U & (IData)(triggers[0U]))) {
        VL_DBG_MSGS("         '" + tag + "' region trigger index 0 is active: Internal 'ico' trigger - first iteration\n");
    }
}
#endif  // VL_DEBUG

bool Vtop___024root___trigger_anySet__act(const VlUnpacked<QData/*63:0*/, 1> &in);

#ifdef VL_DEBUG
VL_ATTR_COLD void Vtop___024root___dump_triggers__act(const VlUnpacked<QData/*63:0*/, 1> &triggers, const std::string &tag) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___dump_triggers__act\n"); );
    // Body
    if ((1U & (~ (IData)(Vtop___024root___trigger_anySet__act(triggers))))) {
        VL_DBG_MSGS("         No '" + tag + "' region triggers active\n");
    }
    if ((1U & (IData)(triggers[0U]))) {
        VL_DBG_MSGS("         '" + tag + "' region trigger index 0 is active: @(posedge heichips25_pudding.clk)\n");
    }
    if ((1U & (IData)((triggers[0U] >> 1U)))) {
        VL_DBG_MSGS("         '" + tag + "' region trigger index 1 is active: @(negedge heichips25_pudding.rst_n)\n");
    }
}
#endif  // VL_DEBUG

VL_ATTR_COLD void Vtop___024root___ctor_var_reset(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___ctor_var_reset\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    const uint64_t __VscopeHash = VL_MURMUR64_HASH(vlSelf->name());
    vlSelf->ui_in = VL_SCOPED_RAND_RESET_I(8, __VscopeHash, 9967284984545053805ull);
    vlSelf->uo_out = VL_SCOPED_RAND_RESET_I(8, __VscopeHash, 4898547878985855477ull);
    vlSelf->uio_in = VL_SCOPED_RAND_RESET_I(8, __VscopeHash, 1424820951596298123ull);
    vlSelf->uio_out = VL_SCOPED_RAND_RESET_I(8, __VscopeHash, 16185529977779244833ull);
    vlSelf->uio_oe = VL_SCOPED_RAND_RESET_I(8, __VscopeHash, 3840965624738958755ull);
    vlSelf->ena = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 4194194277674688301ull);
    vlSelf->clk = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 16707436170211756652ull);
    vlSelf->rst_n = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 1638864771569018232ull);
    vlSelf->i_in = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 5478634717024035798ull);
    vlSelf->i_out = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 1585470361475204052ull);
    vlSelf->VPWR = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 3289325325852222735ull);
    vlSelf->VGND = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 7470078799392243463ull);
    vlSelf->heichips25_pudding__DOT__ui_in = VL_SCOPED_RAND_RESET_I(8, __VscopeHash, 14127009779563225248ull);
    vlSelf->heichips25_pudding__DOT__uo_out = VL_SCOPED_RAND_RESET_I(8, __VscopeHash, 2685519478111167104ull);
    vlSelf->heichips25_pudding__DOT__uio_in = VL_SCOPED_RAND_RESET_I(8, __VscopeHash, 7900606652158528080ull);
    vlSelf->heichips25_pudding__DOT__uio_out = VL_SCOPED_RAND_RESET_I(8, __VscopeHash, 343827758024575352ull);
    vlSelf->heichips25_pudding__DOT__uio_oe = VL_SCOPED_RAND_RESET_I(8, __VscopeHash, 13928594957565549437ull);
    vlSelf->heichips25_pudding__DOT__ena = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 14872008717009262370ull);
    vlSelf->heichips25_pudding__DOT__clk = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 12957507503777167718ull);
    vlSelf->heichips25_pudding__DOT__rst_n = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 4194375120223618160ull);
    vlSelf->heichips25_pudding__DOT__i_in = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 18421874000406163155ull);
    vlSelf->heichips25_pudding__DOT__i_out = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 15517674585884538006ull);
    vlSelf->heichips25_pudding__DOT__VPWR = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 3890978665197121340ull);
    vlSelf->heichips25_pudding__DOT__VGND = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 16186154859853037807ull);
    vlSelf->heichips25_pudding__DOT__iref = VL_SCOPED_RAND_RESET_I(2, __VscopeHash, 7345983892469260105ull);
    vlSelf->heichips25_pudding__DOT__bias = VL_SCOPED_RAND_RESET_I(2, __VscopeHash, 6038060446761372236ull);
    vlSelf->heichips25_pudding__DOT__dacout = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 14175434198741098519ull);
    vlSelf->heichips25_pudding__DOT__vdda = VL_SCOPED_RAND_RESET_I(2, __VscopeHash, 16712989643670217611ull);
    vlSelf->heichips25_pudding__DOT___unused = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 15866512830493819582ull);
    vlSelf->heichips25_pudding__DOT__stateen = VL_SCOPED_RAND_RESET_I(4, __VscopeHash, 14218846249229921513ull);
    vlSelf->heichips25_pudding__DOT__stateenp = VL_SCOPED_RAND_RESET_I(4, __VscopeHash, 14122195893584597327ull);
    vlSelf->heichips25_pudding__DOT__stateenn = VL_SCOPED_RAND_RESET_I(4, __VscopeHash, 15251612755766360013ull);
    vlSelf->heichips25_pudding__DOT__datum = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 14311915519720759671ull);
    vlSelf->heichips25_pudding__DOT__shift = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 2693848471323213957ull);
    vlSelf->heichips25_pudding__DOT__transfer = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 2151987800783696565ull);
    vlSelf->heichips25_pudding__DOT__dir = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 9491284313702628262ull);
    VL_SCOPED_RAND_RESET_W(128, vlSelf->heichips25_pudding__DOT__daisychain, __VscopeHash, 4734782965310073885ull);
    VL_SCOPED_RAND_RESET_W(128, vlSelf->heichips25_pudding__DOT__state, __VscopeHash, 14315148644247807151ull);
    vlSelf->heichips25_pudding__DOT__digitalen__DOT__in = VL_SCOPED_RAND_RESET_I(4, __VscopeHash, 8735478816695391587ull);
    vlSelf->heichips25_pudding__DOT__digitalen__DOT__outn = VL_SCOPED_RAND_RESET_I(4, __VscopeHash, 3660079329091059667ull);
    vlSelf->heichips25_pudding__DOT__digitalen__DOT__outp = VL_SCOPED_RAND_RESET_I(4, __VscopeHash, 1826110858821782138ull);
    vlSelf->heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__IN = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 5747760707001566801ull);
    vlSelf->heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__OUTN = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 917197159715359261ull);
    vlSelf->heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__OUTP = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 13016774005879788902ull);
    vlSelf->heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__inv1__DOT__Y = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 11437812773969235785ull);
    vlSelf->heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__inv1__DOT__A = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 9605395941681441794ull);
    vlSelf->heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__inv2__DOT__Y = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 2978746889898253991ull);
    vlSelf->heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__inv2__DOT__A = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 4898876460958196321ull);
    vlSelf->heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__IN = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 6395630187550909720ull);
    vlSelf->heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__OUTN = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 1007805169078976052ull);
    vlSelf->heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__OUTP = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 6354505803804149707ull);
    vlSelf->heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__inv1__DOT__Y = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 9118259392382284034ull);
    vlSelf->heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__inv1__DOT__A = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 16874643124557643323ull);
    vlSelf->heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__inv2__DOT__Y = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 6131066206281926217ull);
    vlSelf->heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__inv2__DOT__A = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 9162359159806085773ull);
    vlSelf->heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__IN = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 6206118775761891546ull);
    vlSelf->heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__OUTN = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 17050081092423402557ull);
    vlSelf->heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__OUTP = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 6054544853615184842ull);
    vlSelf->heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__inv1__DOT__Y = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 13685529809781142422ull);
    vlSelf->heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__inv1__DOT__A = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 12050631399482331802ull);
    vlSelf->heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__inv2__DOT__Y = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 5758155999877302432ull);
    vlSelf->heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__inv2__DOT__A = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 6863550219263285310ull);
    vlSelf->heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__IN = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 4483558632601856458ull);
    vlSelf->heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__OUTN = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 16333999455535715288ull);
    vlSelf->heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__OUTP = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 14911574875262382746ull);
    vlSelf->heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__inv1__DOT__Y = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 259921455445495270ull);
    vlSelf->heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__inv1__DOT__A = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 10119743729535556348ull);
    vlSelf->heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__inv2__DOT__Y = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 12201066587525309840ull);
    vlSelf->heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__inv2__DOT__A = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 12166531117059717097ull);
    vlSelf->heichips25_pudding__DOT__dac__DOT__Iout = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 7294574632252799150ull);
    vlSelf->heichips25_pudding__DOT__dac__DOT__VcascP = VL_SCOPED_RAND_RESET_I(2, __VscopeHash, 6921057376811212024ull);
    vlSelf->heichips25_pudding__DOT__dac__DOT__VbiasP = VL_SCOPED_RAND_RESET_I(2, __VscopeHash, 4010677639917319577ull);
    VL_SCOPED_RAND_RESET_W(128, vlSelf->heichips25_pudding__DOT__dac__DOT__ON, __VscopeHash, 3726738740964005662ull);
    VL_SCOPED_RAND_RESET_W(128, vlSelf->heichips25_pudding__DOT__dac__DOT__ONB, __VscopeHash, 14857999654027155034ull);
    vlSelf->heichips25_pudding__DOT__dac__DOT__EN = VL_SCOPED_RAND_RESET_I(4, __VscopeHash, 5309515232952745451ull);
    vlSelf->heichips25_pudding__DOT__dac__DOT__ENB = VL_SCOPED_RAND_RESET_I(4, __VscopeHash, 11236643099566287869ull);
    vlSelf->heichips25_pudding__DOT__dac__DOT__VDD = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 7384193178519717224ull);
    vlSelf->heichips25_pudding__DOT__dac__DOT__VSS = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 17486486826300266354ull);
    vlSelf->heichips25_pudding__DOT__wires__DOT__Iout = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 10194241005637133062ull);
    vlSelf->heichips25_pudding__DOT__wires__DOT__VcascP = VL_SCOPED_RAND_RESET_I(2, __VscopeHash, 12615460886871750553ull);
    vlSelf->heichips25_pudding__DOT__wires__DOT__VbiasP = VL_SCOPED_RAND_RESET_I(2, __VscopeHash, 10751464247886067211ull);
    vlSelf->heichips25_pudding__DOT__wires__DOT__i_in = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 8613852613002626567ull);
    vlSelf->heichips25_pudding__DOT__wires__DOT__i_out = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 14597791234091602706ull);
    vlSelf->heichips25_pudding__DOT__wires__DOT__VDDA = VL_SCOPED_RAND_RESET_I(2, __VscopeHash, 535246582839616054ull);
    vlSelf->heichips25_pudding__DOT__wires__DOT__bias = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 17999127345045362773ull);
    vlSelf->heichips25_pudding__DOT__wires__DOT__casc = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 4687973086697758332ull);
    vlSelf->heichips25_pudding__DOT__wires__DOT__vdda = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 1800036576802221107ull);
    vlSelf->heichips25_pudding__DOT__wires__DOT__VcascP__out__strong__out1 = VL_SCOPED_RAND_RESET_I(2, __VscopeHash, 11397420063546275275ull);
    vlSelf->heichips25_pudding__DOT__wires__DOT__VcascP__out__strong__out2 = VL_SCOPED_RAND_RESET_I(2, __VscopeHash, 12490334042254509408ull);
    vlSelf->heichips25_pudding__DOT__wires__DOT__VbiasP__out__strong__out3 = VL_SCOPED_RAND_RESET_I(2, __VscopeHash, 2183540693673489903ull);
    vlSelf->heichips25_pudding__DOT__wires__DOT__VbiasP__out__strong__out4 = VL_SCOPED_RAND_RESET_I(2, __VscopeHash, 11107364028830092890ull);
    vlSelf->heichips25_pudding__DOT__wires__DOT__VDDA__out__strong__out7 = VL_SCOPED_RAND_RESET_I(2, __VscopeHash, 1369124030123130111ull);
    vlSelf->heichips25_pudding__DOT__wires__DOT__VDDA__out__strong__out8 = VL_SCOPED_RAND_RESET_I(2, __VscopeHash, 9932688818155722088ull);
    for (int __Vi0 = 0; __Vi0 < 1; ++__Vi0) {
        vlSelf->__VstlTriggered[__Vi0] = 0;
    }
    for (int __Vi0 = 0; __Vi0 < 1; ++__Vi0) {
        vlSelf->__VicoTriggered[__Vi0] = 0;
    }
    for (int __Vi0 = 0; __Vi0 < 1; ++__Vi0) {
        vlSelf->__VactTriggered[__Vi0] = 0;
    }
    vlSelf->__Vtrigprevexpr___TOP__heichips25_pudding__DOT__clk__0 = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 7098216593267175069ull);
    vlSelf->__Vtrigprevexpr___TOP__heichips25_pudding__DOT__rst_n__0 = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 12485115792721925510ull);
    for (int __Vi0 = 0; __Vi0 < 1; ++__Vi0) {
        vlSelf->__VnbaTriggered[__Vi0] = 0;
    }
}
