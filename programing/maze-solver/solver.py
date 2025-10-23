from turtle import Turtle

t = Turtle()
t.screen.colormode(255)
t.screen.bgcolor("black")
t.color("white")
t.pencolor(136, 0, 21)
u = 100

file = open(".\\programing\\maze-solver\\map.txt")
unstrippedFileLines = file.readlines()
fileLines = []
for i in range(len(unstrippedFileLines)):
    fileLines.append(unstrippedFileLines[i].strip())

for i in range(len(fileLines)):
    if i == 0:
        gridx = fileLines[i].split("x")[0]
        gridy = fileLines[i].split("x")[1]
    elif fileLines[i] == "r":
        if fileLines[i+1] == "c":
            makingColoumn = fileLines[i+1].split()