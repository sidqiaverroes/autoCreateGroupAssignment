import pyautogui
import time

# Get the current mouse cursor position
x, y = pyautogui.position()

while True:
    time.sleep(2)
    x, y = pyautogui.position()
    print(f"Mouse cursor position: ({x}, {y})")
