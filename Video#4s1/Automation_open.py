'''
✨ Support My Work on YouTube! 🎥

Before using the code, I kindly request you to watch the complete video on YouTube. Your support helps me continue creating such content. It means a lot to me!

video Tutorial link :- https://youtu.be/SV20uBLGMqQ?si=4xXXc7BbpLUGpp56

'''
# first part code

import time
import pyautogui as ui


def open(text):
    time.sleep(0.5)
    ui.hotkey("win")
    time.sleep(0.2)
    ui.write(text)
    time.sleep(0.5)
    ui.press("enter")

# second part 

import random
import pyautogui as ui

def close():
    ui.hotkey("alt","f4")
