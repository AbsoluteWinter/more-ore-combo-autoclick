# More Ore: Combo Autoclick
# Game link: https://syns.studio/more-ore/

# Code modified from: https://github.com/KianBrose/Image-Recognition-Botting-Tutorial


# SETTINGS
# dimension: 1920x1080 # Full HD screen
# white rgb(243, 243, 243)
# grey rgb(114, 114, 114)
# red rgb(255, 0, 0)
_TARGET1 = [243, 243, 243] # Target RGB
_TARGET2 = [255, 0, 0]
_SLEEP = 0.05 # Sleep X second each run
_EXIT_KEY = "q" # Press q to exit
_RAND_SLEEP = True # Toggle random sleep time - prevent detected
_DEBUG = False



# LIBRARIES
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

if _DEBUG: print("Libraries loaded")

time.sleep(2) # Initial sleep time



# FUNCTIONS
def click(x:int, y:int, sleep: float = 0.1):
    """
    Mouse click

    x : int
        x pos
    
    y : int
        y  pos

    sleep : float
        time sleep
    """
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(sleep)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def get_size(type: str = "normal", debug: bool = _DEBUG):
    """
    Get screen size and return relative combo postion

    Return: pyautogui's region
    """
    types = ["normal", "fullscreen"]
    if type not in types: type = "normal"
    if debug: print(type)

    x, y = pyautogui.size() # get size
    
    # region = (left, top, width, height)
    region_wh = int(round(x*0.15625, 0))
    # region = (region_x, region_y, region_wh, region_wh)
    region = {
        "normal": (
            int(round(x*0.3411, 0)), int(round(y*0.3472, 0)),
            region_wh, region_wh
        ), # (655,375,300,300)
        "fullscreen": (
            int(round(x*0.3406, 0)), int(round(y*0.2951, 0)),
            region_wh, region_wh
        ) # (654,319,300,300)
    }

    if debug: print(region)
    
    return region[type]

if _DEBUG: print("Functions loaded")



# MAIN
_REGION = get_size("fullscreen")
if _DEBUG:
    print("Location calculated")
    _savepic = True

while keyboard.is_pressed(_EXIT_KEY) == False:
    flag = 0
    
    # pic = pyautogui.screenshot(region=(655,375,300,300))
    pic = pyautogui.screenshot(region=_REGION)
    width, height = pic.size
    # _step = 3 # Check every X pixels
    _step = int(round(width/100, 0))
    if _DEBUG and _savepic:
        pic.save(r"./debugimage.png")
        print(f"Step check: {_step}")
        _savepic = False
    
    for x in range(0, width, _step):
        for y in range(0, height, _step):
            r, g, b = pic.getpixel((x, y))
            # if b == _TARGET1[2] and r == _TARGET1[0] and g == _TARGET1[1]:
            condition = [
                r == _TARGET1[0] and g == _TARGET1[1] and b == _TARGET1[2],
                r == _TARGET2[0] and g == _TARGET2[1] and b == _TARGET2[2],
            ]
            if any(condition):
                flag = 1
                # click(x+655, y+375, 0)
                click(x+_REGION[0], y+_REGION[1], 0)
                if _RAND_SLEEP:
                    rd_slp = round(random.uniform(_SLEEP, _SLEEP+0.03), 3)
                    time.sleep(rd_slp)
                else:
                    time.sleep(_SLEEP)
                break
        
        if flag == 1:
            break

# END
