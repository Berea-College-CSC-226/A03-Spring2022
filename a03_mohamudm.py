#################################################################################
# Author: Mostaphe Mohamud
# Username: mohamudm
# Assignment: AO3 - Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: The purpose is to create a house that has a roof, two windows and a door with a grass planted infront of it.

# Google Doc Link: https://bereacollege-my.sharepoint.com/:w:/g/personal/mohamudm_berea_edu/EaHp-zuFy8BFkZEAzQJBCDUBGGSOeNZPkmL1v2YEID5cLw?e=HMno0l


import turtle

wn = turtle.Screen()
wn.bgcolor('Aqua')
fish = turtle.Turtle()
fish.speed(6)

# Grass
fish.penup()
fish.goto(-382, -70)
fish.pendown()
fish.color("green")
fish.begin_fill()

def drawGrass():
    """Draw a grass in front of the house"""

    for i in range(2):
        fish.forward(762)
        fish.right(90)
        fish.forward(246)
        fish.right(90)

print(drawGrass())
fish.end_fill()

# Sun
fish.penup()
fish.goto(-320, 225)
fish.pendown()
fish.fillcolor("yellow")
fish.begin_fill()
fish.circle(35)
fish.end_fill()

# House
fish.penup()
fish.goto(-80, -70)
fish.pendown()
fish.color("orange")
fish.begin_fill()

def drawHouse():
    """Draw a House that has a roof, two windows and a door"""

    for i in range(4):
        fish.forward(200)
        fish.left(90)
print(drawHouse())
fish.end_fill()

# Roof
fish.penup()
fish.goto(-94, 125)
fish.pendown()
fish.color("brown")
fish.begin_fill()

for i in range(3):
    fish.forward(225)
    fish.left(120)
fish.end_fill()

# Door
def drawDoor():
    """Make a door in the lower central part of the front of the house"""

fish.penup()
fish.goto(-5, -50)
fish.pendown()
fish.begin_fill()
fish.color("Red")

for i in range(2):
    fish.forward(50)
    fish.left(90)
    fish.forward(80)
    fish.left(90)
fish.end_fill()

drawDoor()

# Door Handle
fish.penup()
fish.goto(2, -15)
fish.pendown()
fish.fillcolor("Black")
fish.begin_fill()
fish.circle(5)
fish.end_fill()


# Windows 1
fish.penup()
fish.goto(70, 40)
fish.pendown()
fish.begin_fill()
fish.color("White")

for i in range(2):
    fish.forward(40)
    fish.left(90)
    fish.forward(40)
    fish.left(90)
fish.end_fill()

# Window 2
fish.penup()
fish.goto(-70, 40)
fish.pendown()
fish.begin_fill()
fish.color("White")

for i in range(2):
    fish.forward(40)
    fish.left(90)
    fish.forward(40)
    fish.left(90)
fish.end_fill()

# Trees

def tree():
    fish.color("brown")
    fish.begin_fill()
    for i in range(2):
        fish.left(90)
        fish.forward(40)
        fish.left(90)
        fish.forward(10)
    fish.end_fill()

    fish.forward(10)
    fish.left(90)
    fish.forward(5)

    fish.penup()
    fish.goto(-5, -140)
    fish.pendown()
    fish.color("forestgreen")
    fish.begin_fill()

    fish.circle(25)
    fish.end_fill()


fish.penup()
fish.goto(-25, -200)
fish.pendown()
tree()


def main():
    wn = turtle.Screen()
    wn.bgcolor('Aqua')
    fish = turtle.Turtle()
    fish.speed(6)

main()

wn.exitonclick()