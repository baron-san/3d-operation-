import win32api
import time 

while (True):
    if win32api.GetAsyncKeyState(0x02) != 0 :
        win32api.mouse_event(0x01,int(75),int(0))
        time.sleep(float(0.05))
    elif win32api.GetAsyncKeyState(0x01) != 0 :
        win32api.mouse_event(0x01,int(0),int(75))
        time.sleep(float(0.05))