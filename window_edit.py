from ahk import AHK
import logging
from window_interaction import WindowInteraction
import time 

class WindowEdit:
    """ Interface to edit boxes """

    def __init__(self, window_interaction : WindowInteraction, parameters : dict):
        self.wi = window_interaction
        self.current_index = 0
        self.parameters = parameters
    
    """ 
    Public methods
    """
    def get_window(self):
        return self.wi.get_window(self.parameters['name'])
    

    def get_question(self):
        return self.wi.get_window(b'Question - xflr5 v6.47')

    
    def update_window(self, parmeter_entries: dict) -> None:
        """ 
        update a window with specified values while keeping state 
        parameter entries {section: {'name' : 0, 'value' : 0}}
        """
        self.__start()
        # Go through given parameters and edit each field
        for section in parmeter_entries.keys():
            for name in parmeter_entries[section]:
                value = parmeter_entries[section][name]
                self.__edit_field(section, name, value)
        self.wi.press("{Enter}") # finish last field
        self.wi.press("{Esc}") # stop editing the fields
        self.__end()


    """
    Private methods
    """

    def __start(self):
        """ __Starts the window, must done at the beginning of every new interaction with the window """
        self.wi.ctrl_press(self.parameters['key'])
        # check the new window exits

        self.current_index = 0
        time.sleep(0.1)
    

    def __end(self):
        """ Save and close the window """
        self.wi.press("{Esc}", self.get_question())
        self.wi.press("{Enter}", self.get_question())
    

    def __select_field(self, name : str, section : int):
        """ Select a field based on name and section number. See parameters """
        index = self.__section_index(name, section)
        self.current_index += index
        self.wi.field_selector(index, self.get_window())


    def __section_index(self, name : str, section : int) -> int:
        """ get the index for a given name and section, taking into account current index """
        if name not in self.parameters.keys():
            raise FieldNotFound
        key_presses = self.parameters[name] + (section - 1 ) * self.parameters['section_gap'] - self.current_index
        
        if key_presses < 0:
            # The 'cursor' has gone past the field. We gonna have to save and reopen..
            self.__end()
            self.__start()
            return self.__section_index(name, section)
        else:
            return key_presses 


    def __enter_number(self, value : float):
        """ Just wraps WI function for pressing a key """
        self.wi.press(f"{value}", self.get_window())


    def __edit_field(self, section : int, name : str, value : float):
        """ change the value of a field given: value, name, section """ 
        self.__select_field(name, section)
        self.__enter_number(value)


# define Python user-defined exceptions
class Error(Exception):
   """Base class for other exceptions"""
   pass
class FieldNotFound(Error):
   """Raised when the input value is too small"""
   pass

class WingEdit(WindowEdit):
    """ Wrapper for window edit for Wing edit """
    def __init__(self, window_interaction):
        parameters = {
            'name'          : b'Wing Edition - xflr5 v6.47',
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
        super().__init__(window_interaction, parameters)


class ElevatorEdit(WindowEdit):
    def __init__(self, window_interaction):
        parameters = {
            'name'          : b'Wing Edition - xflr5 v6.47',
            'key'           : 'E',
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
            'name'          : b'Wing Edition - xflr5 v6.47',
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
