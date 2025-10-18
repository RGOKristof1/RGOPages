from turtle import Turtle
import time


file = open(".\\programing\\maze-solver\\map.txt")

lines = file.readlines()

strippedLines = []

for i in range(len(lines)):
    strippedLines.append(lines[i].strip())


gridx = int((strippedLines[0].split("x"))[0])
gridy = int((strippedLines[0].split('x'))[1])
gridSize = {
    "x" : gridx,
    "y" : gridy,
}

for i2 in range(gridSize["y"]):
    for i2 in range(gridSize["x"]):
        print(" · ",end="")
    print()

t = Turtle()
t.screen.title('Object-oriented turtle demo')
t.screen.bgcolor("black")
t.color("orange")
t.screen.mainloop()