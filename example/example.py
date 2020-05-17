from pyxflr import PyXFLR

xflr = PyXFLR()

wing_parameters = {
    1: {'chord': 300, 'twist': 1, 'foil': 0},
    2: {'chord': 200, 'twist': 0, 'foil': 0},
}

elevator_parameters = {
    1: {'chord': 100, 'twist': 0, 'foil': 0},
    2: {'chord' : 80, 'twist': 0, 'foil': 0},
}

fin_parameters = {
    1: {'chord': 100, 'twist': 0, 'foil': 0},
    2: {'chord': 60, 'twist': 0, 'foil': 0},
}

xflr.wing_edit.update_window(wing_parameters)
xflr.elevator_edit.update_window(elevator_parameters)
xflr.fin_edit.update_window(fin_parameters)
