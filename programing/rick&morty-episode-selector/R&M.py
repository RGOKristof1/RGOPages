import webbrowser as web
import time
import pyautogui
import keyboard

def wait(timetowait):
    time.sleep(timetowait)

linkStart = "https://play.hbomax.com/video/watch/"

file = open("./programing/rick&morty-episode-selector/R&M-data.txt")
lines = file.readlines()
newlines = ""
saved = False
cleared = False
linesToSkip = int(lines[81].strip())
for i in range(len(lines)-1):
    if linesToSkip == 0:
        tag = ""
        if saved == False:
            tag = str(input(f"Tag for episode{lines[i].split(".")[0][3]}:"))
            if tag == "save":
                lastLine = i
                tag = ""
                saved = True
            elif tag == "clear":
                newlines = ""
                lastLine = 0
                for i in range(len(lines)-1):
                    section = lines[i].strip().split(".")
                    newlines += str(f"{section[0]}.{section[1]}.{section[2]}.{section[3]}.\n")
                newlines += str(lastLine)
                newfile = open("./programing/rick&morty-episode-selector/R&M-data.txt", "w")
                newfile.write(newlines)
                exit()
        if i == len(lines)-1:
            newlines += (lines[i].strip()+tag)
        else:
            newlines += (lines[i].strip()+tag+"\n")
    else:
        if i == len(lines)-1:
            newlines += (lines[i].strip())
        else:
            newlines += (lines[i].strip()+"\n")
        linesToSkip -= 1

      
newlines += str(lastLine)
newfile = open("./programing/rick&morty-episode-selector/R&M-data.txt", "w")
newfile.write(newlines)