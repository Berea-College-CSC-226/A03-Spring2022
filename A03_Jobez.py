######################################################################
# Author: Zak Jobe
# Username: jobez
# Google doc link: https://docs.google.com/document/d/1iD3XlN_utvlMyV4EwU8cg-IKovGhu7u9L05eKCRaKWU/edit?usp=sharing
# Assignment: A03: Functional Turtles
# Purpose: To draw a complex image using turtles
#####################################################################
import turtle


def landscape():            # Landscape creates the grass in front of the house
    sam = turtle.Turtle()
    sam.pensize(30)
    sam.pencolor(0, 80, 0)
    sam.penup()
    sam.setpos(-350, -175)
    sam.pendown()
    sam.fillcolor(0, 80, 0)
    sam.begin_fill()
    for i in range(2):
        sam.forward(700)
        sam.right(90)
        sam.forward(100)
        sam.right(90)
    sam.end_fill()


def mail():               # Creates a mailbox in the grass next to the house
    las = turtle.Turtle()
    las.penup()
    las.setpos(250, -170)
    las.pensize(5)
    las.pencolor("brown")
    las.pendown()
    las.left(90)
    las.forward(80)
    las.pencolor("white")
    las.fillcolor("white")
    las.begin_fill()
    las.left(90)
    las.forward(50)
    las.right(90)
    las.forward(50)
    las.right(90)
    las.forward(100)
    las.right(90)
    las.forward(50)
    las.right(90)
    las.forward(75)
    las.end_fill()
    las.pencolor("red")
    las.right(90)
    las.forward(100)
    las.right(90)
    las.forward(5)
    las.hideturtle()


def house():           # Creates the outline of the house and fills it in
    dan = turtle.Turtle()
    dan.penup()
    dan.setpos(-200, -150)
    dan.pendown()
    dan.pencolor("saddlebrown")
    dan.pensize(20)
    dan.fillcolor("peru")
    dan.begin_fill()
    for i in ("grey", "saddlebrown", "saddlebrown", "saddlebrown"):
        dan.pencolor(i)
        dan.forward(300)
        dan.left(90)
    dan.end_fill()
    dan.hideturtle()


def window():      # Draws the first of the 2 windows, this being the smaller one of the 2
    jess = turtle.Turtle()
    jess.penup()
    jess.setpos(-100, 30)
    jess.pencolor("maroon")
    jess.pendown()
    jess.pensize(5)
    jess.fillcolor("lightsteelblue")
    jess.begin_fill()
    for i in range(4):
        jess.left(90)
        jess.forward(50)
    jess.end_fill()
    jess.hideturtle()


def bay():          # Creates the long bay window that is beside the door
    ray = turtle.Turtle()
    ray.penup()
    ray.setpos(-25, -100)
    ray.pendown()
    ray.pencolor("maroon")
    ray.pensize(5)
    ray.fillcolor("lightsteelblue")
    ray.begin_fill()
    for i in range(2):
        ray.forward(100)
        ray.left(90)
        ray.forward(40)
        ray.left(90)
    ray.end_fill()
    ray.hideturtle()


def door():       # Creates the outline of the door and fills it in
    shon = turtle.Turtle()
    shon.penup()
    shon.setpos(-150, -150)
    shon.pendown()
    shon.pensize(7)
    shon.pencolor("saddlebrown")
    shon.fillcolor("sandybrown")
    shon.begin_fill()
    shon.hideturtle()
    for i in range(2):
        shon.forward(45)
        shon.left(90)
        shon.forward(100)
        shon.left(90)
    shon.end_fill()
    shon.hideturtle()


def doorhandle():           # Creates the gold door handle
    ann = turtle.Turtle()
    ann.pensize(1)
    ann.pencolor("gold")
    ann.fillcolor("gold")
    ann.penup()
    ann.setpos(-120, -100)
    ann.pendown()
    ann.shape("circle")
    ann.shapesize(.5)


def main():        # Calls all the functions to run
    wn = turtle.Screen()
    wn.colormode(255)
    wn.bgcolor("light blue")
    landscape()
    mail()
    house()
    window()
    bay()
    door()
    doorhandle()
    wn.exitonclick()


main()