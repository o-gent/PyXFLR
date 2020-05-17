""" Uses ahk library, see https://pypi.org/project/ahk/ """

from ahk import AHK
import time
import logging

class WindowInteraction:
    """ low level key pressing interface with xflr windows """

    def __init__(self, app_load_time : int = 2):
        self.ahk = AHK(executable_path = r'ahk\AutoHotkeyU64.exe')
        self.ahk.run_script('Run, xflr/xflr5.exe')
        time.sleep(app_load_time)
        self.win = self.ahk.find_window(title=b'xflr')

    """
    Public methods
    """

    def reset_window(self):
        self.win = self.ahk.find_window(title=b'xflr')
    

    def field_selector(self, index : int, window = None):
        logging.info(f"selecting index: {index}")
        wing_edit = self.ahk.find_window_by_title(b'Wing Edition - xflr5 v6.47')
        if window == None:
            window = self.win
        for _ in range(index):
            time.sleep(0.01)
            #wing_edit.send("{Tab}")
            self.press(r'{Tab}', wing_edit)


    def get_window(self, title : str):
        return self.ahk.find_window_by_title(title)
    

    def list_windows(self):
        return [window.title for window in self.ahk.windows()]
    

    def ctrl_press(self, key : str):
        self.press(f"^{key}")


    def press(self, key : str, window = None):
        
        self.list_windows()

        if window == None:
            window = self.win
        window.activate()
        logging.info(key)
        window.send(f"{key}")
    

    def check_window_exists(self, name : str):
        return True if name in [window.title for window in self.ahk.windows()] else False