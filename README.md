# more-ore-combo-autoclick
Combo Autoclicker for the game More Ore by Syns Studio

- [Game Link](https://syns.studio/more-ore/)

Code - Short ver
```python
_TARGET1 = [243, 243, 243]
_TARGET2 = [255, 0, 0]
_SLEEP = 0.05
_EXIT_KEY = "q" # Press q to exit

from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
time.sleep(2)

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def get_size():
    x, y = pyautogui.size()
    return (int(round(x*0.3411, 0)), int(round(y*0.3472, 0)), 300, 300)

_REGION = get_size()
while keyboard.is_pressed(_EXIT_KEY) == False:
    flag = 0
    pic = pyautogui.screenshot(region=_REGION)
    width, height = pic.size
    for x in range(0, width, 3):
        for y in range(0, height, 3):
            r, g, b = pic.getpixel((x, y))
            condition = [
                r == _TARGET1[0] and g == _TARGET1[1] and b == _TARGET1[2],
                r == _TARGET2[0] and g == _TARGET2[1] and b == _TARGET2[2],
            ]
            if any(condition):
                flag = 1
                click(x+_REGION[0], y+_REGION[1])
                time.sleep(_SLEEP)
                break
        if flag == 1: break
```
