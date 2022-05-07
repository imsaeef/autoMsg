import pyautogui
import time
msg = 10
while msg > 0:
    time.sleep(1)
    pyautogui.typewrite('python magic..!!!')
    pyautogui.press('enter')
    msg = msg - 1
