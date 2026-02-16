# KLayout 0.30.2‑compatible PCell: PMOSSwitchArray (simplified, integer params)
# ----------------------------------------------------------------------
# PMOS switch array, side‑by‑side. Bottom diffusion gets CO→M1 drains.
# Top diffusion left clean for abutment. No substrate tap in this
# simplified version. All geometry parameters are **integers in nm**
# (no TypeDouble anywhere).
# ----------------------------------------------------------------------

import pya

class PMOSSwitchArray(pya.PCellDeclarationHelper):
    def __init__(self):
        super(PMOSSwitchArray, self).__init__()

        # ------------- Parameters (all nm, integers) -------------
        self.param("n", self.TypeInt, "Number of devices", default=2)
        self.param("w_nm", self.TypeInt, "Gate width (nm)", default=300)          # 0.30 um
        self.param("l_nm", self.TypeInt, "Gate length (nm)", default=400)          # 0.4 um
        self.param("sd_ext_nm", self.TypeInt, "S/D OD extension (nm)", default=100)
        self.param("bot_gap_nm", self.TypeInt, "Bottom OD gap (nm)", default=200)

        self.param("cont_size_nm", self.TypeInt, "Contact size (nm)", default=140)
        self.param("cont_pitch_nm", self.TypeInt, "Contact pitch (nm)", default=240)
        self.param("cont_enc_od_nm", self.TypeInt, "OD enclosure of CO (nm)", default=30)
        self.param("cont_enc_m1_nm", self.TypeInt, "M1 enclosure of CO (nm)", default=30)

        self.param("po_ovl_od_nm", self.TypeInt, "Poly over OD (nm)", default=50)
        self.param("po_space_nm", self.TypeInt, "Poly to poly spacing (nm)", default=280)

        self.param("m1_lbl_prefix", self.TypeString, "M1 drain label prefix", default="D")
        self.param("add_gate_strap", self.TypeBoolean, "Add shared gate strap (M1)", default=True)

        # ---------- Layers (map to SG13G2) ----------
        self.param("ly_od", self.TypeLayer, "Diffusion (OD)", default=pya.LayerInfo(1, 0))
        self.param("ly_pimp", self.TypeLayer, "P+ implant", default=pya.LayerInfo(14, 0))
        self.param("ly_nwell", self.TypeLayer, "N-Well", default=pya.LayerInfo(31, 0))
        self.param("ly_po", self.TypeLayer, "Poly (Gate)", default=pya.LayerInfo(5, 0))
        self.param("ly_co", self.TypeLayer, "Contact (CO)", default=pya.LayerInfo(6, 0))
        self.param("ly_m1", self.TypeLayer, "Metal1 (M1)", default=pya.LayerInfo(8, 0))
        self.param("ly_lbl", self.TypeLayer, "Text Labels", default=pya.LayerInfo(63, 0))
        self.param("ly_pr", self.TypeLayer, "Placement boundary", default=pya.LayerInfo(63, 0))

    def display_text_impl(self):
        return f"PMOSSwitchArray_n{self.n}_W{self.w_nm}nm_L{self.l_nm}nm"

    # ---------- Helpers (integer nm → DBU; 0.30.2 safe) ----------
    def _to_dbu_nm(self, nm, dbu):
        # nm → um → dbu
        return int(round((nm * 1e-3) / dbu))

    def _ibox_nm(self, x0, y0, x1, y1, dbu):
        return pya.Box(self._to_dbu_nm(x0, dbu), self._to_dbu_nm(y0, dbu),
                       self._to_dbu_nm(x1, dbu), self._to_dbu_nm(y1, dbu))

    def _ico_nm(self, xc, yc, size_nm, dbu):
        s = size_nm // 2
        return self._ibox_nm(xc - s, yc - s, xc + s, yc + s, dbu)

    def _text_nm(self, shapes, layer, txt, x_nm, y_nm, dbu):
        t = pya.Trans(self._to_dbu_nm(x_nm, dbu), self._to_dbu_nm(y_nm, dbu))
        shapes(layer).insert(pya.Text(txt, t))

    def produce_impl(self):
        dbu = self.layout.dbu

        # Layers
        ly_od = self.layout.layer(self.ly_od)
        ly_pimp = self.layout.layer(self.ly_pimp)
        ly_nwell = self.layout.layer(self.ly_nwell)
        ly_po = self.layout.layer(self.ly_po)
        ly_co = self.layout.layer(self.ly_co)
        ly_m1 = self.layout.layer(self.ly_m1)
        ly_lbl = self.layout.layer(self.ly_lbl)
        ly_pr = self.layout.layer(self.ly_pr)

        shapes = self.cell.shapes

        # --------- Derived layout (all nm) ---------
        gate_pitch = self.l_nm + 2*self.sd_ext_nm + self.po_space_nm
        array_width = self.n * gate_pitch - self.po_space_nm

        bottom_y = 0  # drain CO centerline is at bottom + enc + size/2
        drain_co_y = bottom_y + self.cont_enc_od_nm + self.cont_size_nm // 2
        od_bottom = bottom_y
        od_height = self.w_nm + 2*self.sd_ext_nm + self.bot_gap_nm
        od_top = od_bottom + od_height
        gate_y0 = od_bottom + self.sd_ext_nm
        gate_y1 = gate_y0 + self.w_nm

        # OD and PIMP regions with bottom notches between devices
        od_reg = pya.Region(self._ibox_nm(0, od_bottom, array_width, od_top, dbu))
        pim_reg = pya.Region(self._ibox_nm(0, od_bottom, array_width, od_top, dbu))

        gate_boxes = []
        x0 = 0
        for i in range(self.n):
            g_x0 = x0 + self.sd_ext_nm
            g_x1 = g_x0 + self.l_nm
            gate_boxes.append(self._ibox_nm(g_x0, gate_y0 - self.po_ovl_od_nm, g_x1, gate_y1 + self.po_ovl_od_nm, dbu))

            if i < self.n - 1:
                notch_x0 = x0 + gate_pitch - self.po_space_nm // 2
                notch_x1 = notch_x0 + self.po_space_nm
                notch_box = self._ibox_nm(notch_x0, od_bottom, notch_x1, od_bottom + self.bot_gap_nm, dbu)
                od_reg -= pya.Region(notch_box)
                pim_reg -= pya.Region(notch_box)

            x0 += gate_pitch

        shapes(ly_od).insert(od_reg)
        shapes(ly_pimp).insert(pim_reg)

        for bx in gate_boxes:
            shapes(ly_po).insert(bx)

        # Bottom drain contacts + M1 bars + labels
        x0 = 0
        for i in range(self.n):
            od_left = x0
            od_right = x0 + (self.l_nm + 2*self.sd_ext_nm)
            usable_w = (od_right - od_left) - 2*self.cont_enc_od_nm
            n_cuts = max(1, (usable_w + (self.cont_pitch_nm - self.cont_size_nm)) // self.cont_pitch_nm)
            total_cuts_w = n_cuts * self.cont_pitch_nm - (self.cont_pitch_nm - self.cont_size_nm)
            start_x = od_left + self.cont_enc_od_nm + ((usable_w - total_cuts_w) // 2) + self.cont_size_nm // 2

            # Contacts
            for k in range(n_cuts):
                cx = start_x + k * self.cont_pitch_nm
                shapes(ly_co).insert(self._ico_nm(cx, drain_co_y, self.cont_size_nm, dbu))

            # M1 landing
            m1_y0 = drain_co_y - (self.cont_size_nm // 2 + self.cont_enc_m1_nm)
            m1_y1 = drain_co_y + (self.cont_size_nm // 2 + self.cont_enc_m1_nm)
            m1_x0 = start_x - self.cont_size_nm // 2 - self.cont_enc_m1_nm
            m1_x1 = start_x + (n_cuts - 1) * self.cont_pitch_nm + self.cont_size_nm // 2 + self.cont_enc_m1_nm
            shapes(ly_m1).insert(self._ibox_nm(m1_x0, m1_y0, m1_x1, m1_y1, dbu))

            # Label
            self._text_nm(shapes, ly_lbl, f"{self.m1_lbl_prefix}{i}", (m1_x0 + m1_x1) // 2, m1_y1 + 50, dbu)

            x0 += gate_pitch

        # Optional shared gate strap in M1 on the left (placeholder)
        if self.add_gate_strap:
            gs_x0 = - self.po_space_nm - 100
            gs_x1 = - self.po_space_nm + 100
            shapes(ly_m1).insert(self._ibox_nm(gs_x0, gate_y0 - 100, gs_x1, gate_y1 + 100, dbu))

        # N-Well keep (no tap)
        shapes(ly_nwell).insert(self._ibox_nm(-500, od_bottom - 500, array_width + 500, od_top + 500, dbu))

        # Placement boundary
        shapes(ly_pr).insert(self._ibox_nm(-1200, od_bottom - 800, array_width + 800, od_top + 800, dbu))

# Register library
class PMOSSwitchArrayLib(pya.Library):
    def __init__(self):
        super(PMOSSwitchArrayLib, self).__init__()
        self.description = "Simplified PMOS array (integer nm params)"
        self.layout().register_pcell("PMOSSwitchArray", PMOSSwitchArray())
        self.register("PMOSSwitchArrayLib")

def load_libraries():
    PMOSSwitchArrayLib()

load_libraries()

