import klayout.db as pya

# 1) Read the GDS
layout = pya.Layout()
layout.read("dac2u128out4in.gds")

# 2) Get top cell
top_cell = layout.top_cell()

# 3) Layer info
layer_idxs = layout.layer_indexes()
layer_infos = layout.layer_infos()

# 4) Recursively iterate shapes in all cells
def process_cell(cell):
    print(f"\n>> Cell: {cell.name}")
    for idx, info in zip(layer_idxs, layer_infos):
        layer_no, datatype = info.layer, info.datatype
        shapes = cell.shapes(idx)
        for i, shape in enumerate(shapes.each()):
            if shape.is_box():
                box = shape.box
                pts = [(box.p1.x, box.p1.y), (box.p2.x, box.p1.y), (box.p2.x, box.p2.y), (box.p1.x, box.p2.y)]
                print(f"Layer {layer_no}, DType {datatype}, Box #{i}: 4 points → {pts}")
            elif shape.is_polygon():
                poly = shape.polygon
                pts = [(pt.x, pt.y) for pt in poly.each_point()]
                print(f"Layer {layer_no}, DType {datatype}, Polygon #{i}: {len(pts)} points → {pts}")
            elif shape.is_path():
                path = shape.path
                pts = [(pt.x, pt.y) for pt in path.each_point()]
                print(f"Layer {layer_no}, DType {datatype}, Path #{i}: Width = {path.width}, Points → {pts}")
            elif shape.is_text():
                text = shape.text
                print(f"Layer {layer_no}, DType {datatype}, Text #{i}: Text = '{text.string}', at ({text.trans.disp.x}, {text.trans.disp.y})")
            else:
                print(f"Layer {layer_no}, DType {datatype}, Shape #{i}: Unhandled type {shape.shape_type}")
    
    # Recurse into child cells
    for child_index in cell.each_child_cell():
        child_cell = layout.cell(child_index)
        process_cell(child_cell)

# Run on top cell
process_cell(top_cell)

