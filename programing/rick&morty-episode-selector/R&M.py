import webbrowser as web
import time
import pyautogui
import keyboard

def wait(timetowait):
    time.sleep(timetowait)

linkStart = "https://play.hbomax.com/video/watch/"

file = open("./programing/rick&morty-episode-selector/R&M-data.txt")
lines = file.readlines()

stop = 0
for i in range(len(lines)):
    if stop == 0:
        link = lines[i].split(".")[3].strip()
        web.open(linkStart+link)
        wait(2)
        w = 1
        while w == 1:
            wait(1)
            if keyboard.is_pressed("control+alt+s"):
                stop = 1
                w = 0
            elif keyboard.is_pressed("control+alt+n"):
                w = 0
    else:
        print("stopped")
        break