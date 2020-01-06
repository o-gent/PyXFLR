from ahk import AHK
import time
import logging
from window_interaction import WindowInteraction

class WindowEdit:
    """ Interface to edit boxes """
    def __init__(self, window_interaction : WindowInteraction, parameters : dict):
        self.wi = window_interaction
        self.current_index = 0     
        self.parameters = parameters
    
    def __start(self):
        """ __Starts the window, must done at the beginning of every new interaction with the window """
        self.wi.ctrl_press(self.parameters['key'])
        self.edit = b'Wing Edition - xflr5 v6.47'
        self.current_index = 0
        time.sleep(0.1)
    
    def __end(self):
        """ Save and close the window """
        self.wi.press("{Esc}")
        # Check we have the save box
        
        self.wi.press("{Enter}")
    
    def __select_field(self, name : str, section : int):
        """ Select a field based on name and section number. See parameters """
        self.wi.field_selector(self.__section_index(name, section), self.edit)
    
    def __section_index(self, name : str, section : int):
        """ get the index for a given name and section, taking into accoutn current index """
        if name not in self.parameters.keys():
            raise FieldNotFound
        key_presses = self.parameters[name] + section*self.parameters['section_gap'] - self.current_index
        
        if key_presses < 0:
            # The 'cursor' has gone past the field. We gonna have to save and reopen..
            self.__end()
            self.__start()
            return self.__section_index(name, section)
        else:
            return key_presses 

    def __enter_number(self, value : float):
        """ Just wraps WI function for pressing a key """
        self.wi.press(f"{value}")

    def __edit_field(self, name : str, value : float, section : int):
        """ change the value of a field given: value, name, section """ 
        self.__select_field(name, section)
        self.__enter_number(value)
    
    def update_window(self, parmeter_entries):
        """ 
        update a window with specified values while keeping state 
        parameter entries {'name' : {'value' : 0, 'section' : 0}}
        """
        self.__start()
        # Go through given parameters and edit each field
        edit = lambda x, y : self.__edit_field(x, y[x]['value'], y[x]['value'])
        for key in parmeter_entries.keys():
            edit(key, parmeter_entries)
        self.__end()



# define Python user-defined exceptions
class Error(Exception):
   """Base class for other exceptions"""
   pass
class FieldNotFound(Error):
   """Raised when the input value is too small"""
   pass


def WingEdit(window_interaction):
        parameters = {
            'name'          : 'Wing Edit',
            'key'           : 'W',
            'section_gap'   : 10,
            'y'             : 7,
            'chord'         : 8,
            'offset'        : 9,
            'dihedral'      : 10,
            'twist'         : 11,
            'foil'          : 12,
            'x_panels'      : 13,
            'x_dist'        : 14,
            'y_panels'      : 15,
            'y_dist'        : 16
        }
        return WindowEdit(window_interaction, parameters)

class TailEdit(WindowEdit):
    def __init__(self, window_interaction):
        parameters = {
            'name'          : 'Tail Edit',
            'key'           : 'T',
            'section_gap'   : 10,
            'y'             : 7,
            'chord'         : 8,
            'offset'        : 9,
            'dihedral'      : 10,
            'twist'         : 11,
            'foil'          : 12,
            'x_panels'      : 13,
            'x_dist'        : 14,
            'y_panels'      : 15,
            'y_dist'        : 16
        }
        super().__init__(window_interaction, parameters)

class FinEdit(WindowEdit):
    def __init__(self, window_interaction):
        parameters = {
            'name'          : 'Fin Edit',
            'key'           : 'F',
            'section_gap'   : 10,
            'y'             : 7,
            'chord'         : 8,
            'offset'        : 9,
            'dihedral'      : 10,
            'twist'         : 11,
            'foil'          : 12,
            'x_panels'      : 13,
            'x_dist'        : 14,
            'y_panels'      : 15,
            'y_dist'        : 16
        }
        super().__init__(window_interaction, parameters)
