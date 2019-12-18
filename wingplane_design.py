from ahk import AHK
import time
import logging
from window_interaction import WindowInteraction

class WingEdit:
    """ Interface to wing edit box """
    def __init__(self, window_interaction : WindowInteraction):
        self.wi = window_interaction
        self.current_index = 0
        self.section_gap = 10
        self.interface_map = {
            'y'         : 7,
            'chord'     : 8,
            'offset'    : 9,
            'dihedral'  : 10,
            'twist'     : 11,
            'foil'      : 12,
            'x_panels'  : 13,
            'x_dist'    : 14,
            'y_panels'  : 15,
            'y_dist'    : 16
        }
    
    def start(self):
        """ Starts the window, must done at the beginning of every new interaction with the window """
        self.wi.ctrl_press("W")
        self.wi.get_window("Wing Edit")
        self.current_index = 0
    
    def end(self):
        """ Save and close the window """
        self.wi.press("{Esc}")
        # Check we have the save box
        
        self.wi.press("{Enter}")
    
    def select_field(self, name : str, section : int):
        """ Select a field based on name and section number. See interface_map """
        self.wi.get_window("Wing Edit")
        self.wi.field_selector(self.section_index(name, section))
    
    def section_index(self, name : str, section : int):
        """ get the index for a given name and section, taking into accoutn current index """
        if name not in self.interface_map.keys():
            raise FieldNotFound
        
        key_presses = self.interface_map[name] + section*self.section_gap - self.current_index
        
        if key_presses < 0:
            # The 'cursor' has gone past the field. We gonna have to save and reopen..
            self.end()
            self.start()
            return self.section_index(name, section)
        else:
            return key_presses 

    def enter_number(self, value : float):
        """ Just wraps WI function for pressing a key """
        self.wi.press(f"{value}")

    def edit_field(self, value : float, name : str, section : int):
        """ change the value of a field given: value, name, section """
        self.select_field(name, section)
        self.enter_number(value)


# define Python user-defined exceptions
class Error(Exception):
   """Base class for other exceptions"""
   pass
class FieldNotFound(Error):
   """Raised when the input value is too small"""
   pass