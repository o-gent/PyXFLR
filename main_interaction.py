""" Interacts with non sub windows """

# startup 
# - Select wing and plane design ctrl + 6
# - Create a new plane F3
# - Save new plane, Enter * 2

from window_edit import WindowInteraction
import logging 

class OverallNav:
    """ Need a better name for this """
    def __init__(self, window_interaction : WindowInteraction):
        self.wi = window_interaction
    
    def __plane_design(self):
        self.wi.ctrl_press('6')

    def __new_plane(self):
        self.wi.press('{F3}')
        self.wi.list_windows()
        win = self.wi.get_window(b'Plane Editor - xflr5 v6.47')
        win.send('{Enter}')
        win.send('{Enter}')
    
    def default_start(self):
        logging.info("Overall nav default start")
        self.__plane_design()
        self.__new_plane()