from pyxflr import PyXFLR

xflr = PyXFLR()

parameters = {
    1: {'chord' : 300, 'twist' : 1, 'foil': 0},
    2: {'chord' : 200, 'twist' : 0, 'foil': 0},
}

xflr.wing_edit.update_window(parameters)
