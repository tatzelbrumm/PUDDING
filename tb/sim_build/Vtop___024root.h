// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design internal header
// See Vtop.h for the primary calling header

#ifndef VERILATED_VTOP___024ROOT_H_
#define VERILATED_VTOP___024ROOT_H_  // guard

#include "verilated.h"


class Vtop__Syms;

class alignas(VL_CACHE_LINE_BYTES) Vtop___024root final : public VerilatedModule {
  public:

    // DESIGN SPECIFIC STATE
    // Anonymous structures to workaround compiler member-count bugs
    struct {
        VL_IN8(clk,0,0);
        VL_IN8(ui_in,7,0);
        VL_OUT8(uo_out,7,0);
        VL_IN8(uio_in,7,0);
        VL_OUT8(uio_out,7,0);
        VL_OUT8(uio_oe,7,0);
        VL_IN8(ena,0,0);
        VL_IN8(rst_n,0,0);
        VL_INOUT8(i_in,0,0);
        VL_INOUT8(i_out,0,0);
        VL_INOUT8(VPWR,0,0);
        VL_INOUT8(VGND,0,0);
        CData/*7:0*/ heichips25_pudding__DOT__ui_in;
        CData/*7:0*/ heichips25_pudding__DOT__uo_out;
        CData/*7:0*/ heichips25_pudding__DOT__uio_in;
        CData/*7:0*/ heichips25_pudding__DOT__uio_out;
        CData/*7:0*/ heichips25_pudding__DOT__uio_oe;
        CData/*0:0*/ heichips25_pudding__DOT__ena;
        CData/*0:0*/ heichips25_pudding__DOT__clk;
        CData/*0:0*/ heichips25_pudding__DOT__rst_n;
        CData/*0:0*/ heichips25_pudding__DOT__i_in;
        CData/*0:0*/ heichips25_pudding__DOT__i_out;
        CData/*0:0*/ heichips25_pudding__DOT__VPWR;
        CData/*0:0*/ heichips25_pudding__DOT__VGND;
        CData/*1:0*/ heichips25_pudding__DOT__iref;
        CData/*1:0*/ heichips25_pudding__DOT__bias;
        CData/*0:0*/ heichips25_pudding__DOT__dacout;
        CData/*1:0*/ heichips25_pudding__DOT__vdda;
        CData/*0:0*/ heichips25_pudding__DOT___unused;
        CData/*3:0*/ heichips25_pudding__DOT__stateen;
        CData/*3:0*/ heichips25_pudding__DOT__stateenp;
        CData/*3:0*/ heichips25_pudding__DOT__stateenn;
        CData/*0:0*/ heichips25_pudding__DOT__datum;
        CData/*0:0*/ heichips25_pudding__DOT__shift;
        CData/*0:0*/ heichips25_pudding__DOT__transfer;
        CData/*0:0*/ heichips25_pudding__DOT__dir;
        CData/*3:0*/ heichips25_pudding__DOT__digitalen__DOT__in;
        CData/*3:0*/ heichips25_pudding__DOT__digitalen__DOT__outn;
        CData/*3:0*/ heichips25_pudding__DOT__digitalen__DOT__outp;
        CData/*0:0*/ heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__IN;
        CData/*0:0*/ heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__OUTN;
        CData/*0:0*/ heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__OUTP;
        CData/*0:0*/ heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__inv1__DOT__Y;
        CData/*0:0*/ heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__inv1__DOT__A;
        CData/*0:0*/ heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__inv2__DOT__Y;
        CData/*0:0*/ heichips25_pudding__DOT__digitalen__DOT__g__BRA__0__KET____DOT__u__DOT__inv2__DOT__A;
        CData/*0:0*/ heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__IN;
        CData/*0:0*/ heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__OUTN;
        CData/*0:0*/ heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__OUTP;
        CData/*0:0*/ heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__inv1__DOT__Y;
        CData/*0:0*/ heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__inv1__DOT__A;
        CData/*0:0*/ heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__inv2__DOT__Y;
        CData/*0:0*/ heichips25_pudding__DOT__digitalen__DOT__g__BRA__1__KET____DOT__u__DOT__inv2__DOT__A;
        CData/*0:0*/ heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__IN;
        CData/*0:0*/ heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__OUTN;
        CData/*0:0*/ heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__OUTP;
        CData/*0:0*/ heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__inv1__DOT__Y;
        CData/*0:0*/ heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__inv1__DOT__A;
        CData/*0:0*/ heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__inv2__DOT__Y;
        CData/*0:0*/ heichips25_pudding__DOT__digitalen__DOT__g__BRA__2__KET____DOT__u__DOT__inv2__DOT__A;
        CData/*0:0*/ heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__IN;
        CData/*0:0*/ heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__OUTN;
        CData/*0:0*/ heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__OUTP;
        CData/*0:0*/ heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__inv1__DOT__Y;
    };
    struct {
        CData/*0:0*/ heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__inv1__DOT__A;
        CData/*0:0*/ heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__inv2__DOT__Y;
        CData/*0:0*/ heichips25_pudding__DOT__digitalen__DOT__g__BRA__3__KET____DOT__u__DOT__inv2__DOT__A;
        CData/*0:0*/ heichips25_pudding__DOT__dac__DOT__Iout;
        CData/*1:0*/ heichips25_pudding__DOT__dac__DOT__VcascP;
        CData/*1:0*/ heichips25_pudding__DOT__dac__DOT__VbiasP;
        CData/*3:0*/ heichips25_pudding__DOT__dac__DOT__EN;
        CData/*3:0*/ heichips25_pudding__DOT__dac__DOT__ENB;
        CData/*0:0*/ heichips25_pudding__DOT__dac__DOT__VDD;
        CData/*0:0*/ heichips25_pudding__DOT__dac__DOT__VSS;
        CData/*0:0*/ heichips25_pudding__DOT__wires__DOT__Iout;
        CData/*1:0*/ heichips25_pudding__DOT__wires__DOT__VcascP;
        CData/*1:0*/ heichips25_pudding__DOT__wires__DOT__VbiasP;
        CData/*0:0*/ heichips25_pudding__DOT__wires__DOT__i_in;
        CData/*0:0*/ heichips25_pudding__DOT__wires__DOT__i_out;
        CData/*1:0*/ heichips25_pudding__DOT__wires__DOT__VDDA;
        CData/*0:0*/ heichips25_pudding__DOT__wires__DOT__bias;
        CData/*0:0*/ heichips25_pudding__DOT__wires__DOT__casc;
        CData/*0:0*/ heichips25_pudding__DOT__wires__DOT__vdda;
        CData/*1:0*/ heichips25_pudding__DOT__wires__DOT__VcascP__out__strong__out1;
        CData/*1:0*/ heichips25_pudding__DOT__wires__DOT__VcascP__out__strong__out2;
        CData/*1:0*/ heichips25_pudding__DOT__wires__DOT__VbiasP__out__strong__out3;
        CData/*1:0*/ heichips25_pudding__DOT__wires__DOT__VbiasP__out__strong__out4;
        CData/*1:0*/ heichips25_pudding__DOT__wires__DOT__VDDA__out__strong__out7;
        CData/*1:0*/ heichips25_pudding__DOT__wires__DOT__VDDA__out__strong__out8;
        CData/*0:0*/ __VstlFirstIteration;
        CData/*0:0*/ __VicoFirstIteration;
        CData/*0:0*/ __Vtrigprevexpr___TOP__heichips25_pudding__DOT__clk__0;
        VlWide<4>/*127:0*/ heichips25_pudding__DOT__daisychain;
        VlWide<4>/*127:0*/ heichips25_pudding__DOT__state;
        VlWide<4>/*127:0*/ heichips25_pudding__DOT__dac__DOT__ON;
        VlWide<4>/*127:0*/ heichips25_pudding__DOT__dac__DOT__ONB;
        IData/*31:0*/ __VactIterCount;
        VlUnpacked<QData/*63:0*/, 1> __VstlTriggered;
        VlUnpacked<QData/*63:0*/, 1> __VicoTriggered;
        VlUnpacked<QData/*63:0*/, 1> __VactTriggered;
        VlUnpacked<QData/*63:0*/, 1> __VnbaTriggered;
    };

    // INTERNAL VARIABLES
    Vtop__Syms* const vlSymsp;

    // CONSTRUCTORS
    Vtop___024root(Vtop__Syms* symsp, const char* v__name);
    ~Vtop___024root();
    VL_UNCOPYABLE(Vtop___024root);

    // INTERNAL METHODS
    void __Vconfigure(bool first);
};


#endif  // guard
