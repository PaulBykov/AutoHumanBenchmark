import pyautogui
import keyboard
import time

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(500,350)[0] == 75:
        pyautogui.doubleClick()
        time.sleep(0.01)
        

