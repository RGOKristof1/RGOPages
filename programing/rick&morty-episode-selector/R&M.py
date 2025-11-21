import webbrowser as web
import time
import pyautogui
import keyboard
import os


def wait(timetowait):
    time.sleep(timetowait)

linkStart = "https://play.hbomax.com/video/watch/"

file = open("C:\\Users\\rgokr\\Desktop\\RGOPages\\programing\\rick&morty-episode-selector\\R&M-data.txt")
lines = file.readlines()
newlines = ""
saved = False
cleared = False
linesToSkip = int(lines[81].strip())
for i in range(len(lines)-1):
    lastLine = i
    if linesToSkip == 0:
        tag = ""
        if saved == False:
            web.open(linkStart+lines[i].split(".")[3])
            if  len(lines[i].split(".")[0]) == 5:
                episodeNumber = lines[i].split(".")[0][3]+lines[i].split(".")[0][4]
            else:
                episodeNumber = lines[i].split(".")[0][3]
            seasonNumber = lines[i].split(".")[0][1]
            tag = str(input(f"Tag for s{seasonNumber}e{episodeNumber}:"))
            if i == len(lines)-1:
                tag = ""
                saved = True
            if tag == "save":
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