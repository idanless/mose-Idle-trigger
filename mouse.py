import win32api
import pyautogui
import time
import datetime
import random

idletime = 20
pyautogui.FAILSAFE = False

class GetIdleTime:
    def IdleTime():
        return (win32api.GetTickCount() - win32api.GetLastInputInfo()) / 1000.0


def movemosue(x,y):
    x1=int(random.randint(100, 1000))
    y1=int(random.randint(100, 1000))
    pyautogui.moveTo(x1,y1)
    time.sleep(1)
    pyautogui.moveTo(x1,y1)
    time.sleep(1)
    pyautogui.hscroll(1)

while True:
    time.sleep(1)
    y = int(pyautogui.position()[1])
    x = int(pyautogui.position()[0])
    getIdleTime = GetIdleTime
    getIdleTime = int(getIdleTime.IdleTime())
    #print(getIdleTime)
    if getIdleTime > idletime:
        print(datetime.datetime.now(),"detected no move watchdog activate move mouse","move to" ,pyautogui.position())
        movemosue(x,y)
