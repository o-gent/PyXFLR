from window_interaction import WindowInteraction
from window_edit import WingEdit, ElevatorEdit, FinEdit
from main_interaction import OverallNav

import logging
logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d:%H:%M:%S',
                    level=logging.INFO)

class PyXFLR:
    """ Orchestrates XFLR """
    def __init__(self):
        self.window_interaction = WindowInteraction()
        self.overall_nav = OverallNav(self.window_interaction)
        
        # Init plane parts
        self.wing_edit = WingEdit(self.window_interaction)
        self.fin_edit = FinEdit(self.window_interaction)
        self.elevator_edit = ElevatorEdit(self.window_interaction)
        
        # Go to the 
        self.overall_nav.default_start()