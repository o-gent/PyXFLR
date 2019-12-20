""" Uses ahk library, see https://pypi.org/project/ahk/ """

from ahk import AHK
import time
import logging

class WindowInteraction:
    """ low level key pressing interface with xflr windows """
    def __init__(self, app_load_time : int = 2):
        self.ahk = AHK(executable_path = r'C:\Users\olive\Documents\GitHub\pyxfl\ahk\AutoHotkeyU64.exe')
        self.ahk.run_script('Run, xflr/xflr5.exe')
        time.sleep(app_load_time)
        self.win = self.ahk.find_window(title=b'xflr')
    
    def field_selector(self, index : int):
        self.win.activate()
        for _ in range(index):
            self.win.send("{Tab}")
    
    def get_window(self, title : str):
        return self.ahk.find_window(title = title)
    
    def ctrl_press(self, key : str):
        self.win.activate()
        self.win.send(f"^{key}")
     
    def press(self, key : str):
        self.win.activate()
        self.win.send(f"{key}")
    
    def check_window_exists(self, name : str):
        return True if name in [window.title for window in self.ahk.windows()] else False