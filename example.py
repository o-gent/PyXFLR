from ahk import AHK
import time

from window_interaction import WindowInteraction
from main_interaction import OverallNav
from window_edit import WingEdit

wi = WindowInteraction()
on = OverallNav(wi)
we = WingEdit(wi)

on.default_start()

parameters = {
    'chord' : {'value' : 300, 'section' : 1},
    'twist' : {'value' : 1, 'section' : 1}
    #'chord' : {'value' : 200, 'section' : 2}
}

we.update_window(parameters)
