from ahk import AHK
import time

ahk = AHK(executable_path = r'C:\Users\olive\Documents\GitHub\PyXFLR\ahk\AutoHotkeyU64.exe')
ahk.run_script('Run, xflr/xflr5.exe')

time.sleep(2)
win = ahk.find_window(title=b'xflr')

win.activate()
win.send('^W')

for window in ahk.windows():
    print(window.title)

wing_edit = ahk.find_window(title=b'Wing Edition')
for i in range(8):
    time.sleep(0.01)
    wing_edit = ahk.find_window(title=b'Wing Edition')
    wing_edit.send("{Tab}")

wing_edit.send("60")
wing_edit = ahk.find_window(title=b'Wing Edition')
wing_edit.send("{Tab}")