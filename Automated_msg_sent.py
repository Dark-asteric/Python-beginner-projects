import pyautogui as pg
import time
time.sleep(4)
count = 0
while count <= 10:
    pg.typewrite("Cameraman Jaldi focus karo.")
    pg.press("enter")
    count = count +1
