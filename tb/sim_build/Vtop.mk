# Verilated -*- Makefile -*-
# DESCRIPTION: Verilator output: Makefile for building Verilated archive or executable
#
# Execute this makefile from the object directory:
#    make -f Vtop.mk

default: heichips25_pudding

### Constants...
# Perl executable (from $PERL, defaults to 'perl' if not set)
PERL = perl
# Python3 executable (from $PYTHON3, defaults to 'python3' if not set)
PYTHON3 = python3
# Path to Verilator kit (from $VERILATOR_ROOT)
VERILATOR_ROOT = /nix/store/wc042p92sfn2pxyv3i8b86008f5j1kyc-verilator-5.042/share/verilator
# SystemC include directory with systemc.h (from $SYSTEMC_INCLUDE)
SYSTEMC_INCLUDE ?= /nix/store/adx3xvgndxyjrlz56ivg8hxbxm7qgs40-systemc-3.0.1/include
# SystemC library directory with libsystemc.a (from $SYSTEMC_LIBDIR)
SYSTEMC_LIBDIR ?= /nix/store/adx3xvgndxyjrlz56ivg8hxbxm7qgs40-systemc-3.0.1/lib

### Switches...
# C++ code coverage  0/1 (from --prof-c)
VM_PROFC = 0
# SystemC output mode?  0/1 (from --sc)
VM_SC = 0
# Legacy or SystemC output mode?  0/1 (from --sc)
VM_SP_OR_SC = $(VM_SC)
# Deprecated
VM_PCLI = 1
# Deprecated: SystemC architecture to find link library path (from $SYSTEMC_ARCH)
VM_SC_TARGET_ARCH = linux

### Vars...
# Design prefix (from --prefix)
VM_PREFIX = Vtop
# Module prefix (from --prefix)
VM_MODPREFIX = Vtop
# User CFLAGS (from -CFLAGS on Verilator command line)
VM_USER_CFLAGS = \

# User LDLIBS (from -LDFLAGS on Verilator command line)
VM_USER_LDLIBS = \
  -Wl,-rpath,/nix/store/yk336mn39lfjiawz9zq4qbgq29vhd694-python3.13-cocotb-2.0.0/lib/python3.13/site-packages/cocotb/libs -L/nix/store/yk336mn39lfjiawz9zq4qbgq29vhd694-python3.13-cocotb-2.0.0/lib/python3.13/site-packages/cocotb/libs -lcocotbvpi_verilator \

# User .cpp files (from .cpp's on Verilator command line)
VM_USER_CLASSES = \
  verilator \

# User .cpp directories (from .cpp's on Verilator command line)
VM_USER_DIR = \
  . \
  ../../../../../../nix/store/yk336mn39lfjiawz9zq4qbgq29vhd694-python3.13-cocotb-2.0.0/lib/python3.13/site-packages/cocotb/share/lib/verilator \

### Default rules...
# Include list of all generated classes
include Vtop_classes.mk
# Include global rules
include $(VERILATOR_ROOT)/include/verilated.mk

### Executable rules... (from --exe)
VPATH += $(VM_USER_DIR)

verilator.o: /nix/store/yk336mn39lfjiawz9zq4qbgq29vhd694-python3.13-cocotb-2.0.0/lib/python3.13/site-packages/cocotb/share/lib/verilator/verilator.cpp 
	$(OBJCACHE) $(CXX) $(CXXFLAGS) $(CPPFLAGS) $(OPT_FAST)  -c -o $@ $<

### Link rules... (from --exe)
heichips25_pudding: $(VK_USER_OBJS) $(VK_GLOBAL_OBJS) $(VM_PREFIX)__ALL.a
	$(LINK) $(LDFLAGS) $^ $(LOADLIBES) $(LDLIBS) $(LIBS) $(SC_LIBS) -o $@

# Verilated -*- Makefile -*-
