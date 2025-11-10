import webbrowser
import time
import pyautogui
import keyboard

linkStart = "https://play.hbomax.com/video/watch/"

file = open("./programing/rick&morty-episode-selector/R&M-data.txt")
lines = file.readlines()

season = str(input("Season: "))
episode = str(input("Episode: "))

for i in range(len(lines)):
    if lines[i].split(".")[0] == season+episode:
        print(f"Epizode name:{lines[i].split(".")[1]}Epizode length:{lines[i].split(".")[2]}")
        print("Episode starts in...")
        for i2 in range(3):
            print(str(i2+1))
            time.sleep(1)
        webbrowser.open(linkStart+lines[i].split(".")[3].strip())
time.sleep(10)