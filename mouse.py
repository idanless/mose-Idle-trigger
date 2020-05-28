import win32api
import pyautogui
import random
import time
import datetime

idletime = 20

class GetIdleTime:
    def IdleTime():
        return (win32api.GetTickCount() - win32api.GetLastInputInfo()) / 1000.0


def movemosue():
    y = int(pyautogui.position()[1])
    x = int(pyautogui.position()[0])
    pyautogui.moveTo(x + int(random.randrange(20, 50, 3)), y + 10)
    pyautogui.hscroll(1)

while True:
    time.sleep(1)
    getIdleTime = GetIdleTime
    getIdleTime = int(getIdleTime.IdleTime())
    #print(getIdleTime)
    if getIdleTime > idletime:
        print(datetime.datetime.now(),"detected no move watchdog activate move mouse",getIdleTime)
        movemosue()
