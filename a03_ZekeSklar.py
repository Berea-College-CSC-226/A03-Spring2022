######################################################################


# Author: Zechariah Sklar
# Username: ZekeSklar

######################################################################

import turtle, math


def roadf():   #makes the road in front of the house with the yellow lines

    road = turtle.Turtle()
    road.hideturtle()
    road.penup()
    road.pensize(5)
    road.setpos(-250, -250)
    road.pendown()
    road.pencolor("gray")
    road.fillcolor("gray")

    yline = turtle.Turtle()
    yline.hideturtle()
    yline.pencolor("yellow")
    yline.pensize(5)
    yline.penup()
    yline.setpos(-250, -250)

    road.begin_fill()
    for i in range(2):
        road.forward(500)
        road.left(90)
        road.forward(50)
        road.left(90)
    road.end_fill()

    for i in range(5):
        yline.pendown()
        yline.forward(50)
        yline.penup()
        yline.fd(50)


def grassf():   #makes the grass in front of the house literally just a box of green
    grass = turtle.Turtle()
    grass.pencolor("green")
    grass.penup()
    grass.setpos(-250, -200)
    grass.hideturtle()
    grass.pensize(5)
    grass.fillcolor("green")
    grass.pendown()

    grass.begin_fill()
    for i in range(2):
        grass.forward(500)
        grass.left(90)
        grass.forward(50)
        grass.left(90)
    grass.end_fill()


def houseb():   #makes the base of the house
    box = turtle.Turtle()
    box.pensize(5)
    box.hideturtle()
    box.penup()
    box.setpos(-125, -150)
    box.pencolor(225, 225, 225)
    box.fillcolor(225, 225, 225)
    box.pendown()

    box.begin_fill()
    for i in range(2):
        box.fd(250)
        box.left(90)
        box.fd(175)
        box.left(90)
    box.end_fill()


def houser():   #makes the roof of the house
    roof = turtle.Turtle()
    roof.hideturtle()
    roof.penup()
    roof.setpos(-150, 25)
    roof.pencolor(150, 75, 0)
    roof.fillcolor(150, 75, 0)
    roof.pensize(5)
    roof.pendown()

    roof.begin_fill()
    roof.fd(300)
    roof.left(135)
    roof.fd(math.sqrt(45000))
    roof.left(90)
    roof.fd(math.sqrt(45000))
    roof.left(45)
    roof.end_fill()

def windows(x,y):   #makes the window of the house had planned on putting more than one but did not have enough space but the code is there for it

    window = turtle.Turtle()
    window.hideturtle()
    window.penup()
    window.setpos(x, y)
    window.pendown()
    window.pensize(3)
    window.pencolor("saddlebrown")
    window.fillcolor(0, 0, 139)

    window.begin_fill()
    for i in range(2):
        window.fd(50)
        window.left(90)
        window.forward(75)
        window.left(90)
    window.end_fill()

    window.fd(25)
    window.left(90)
    window.fd(75)
    window.left(90)
    window.fd(25)
    window.left(90)
    window.fd(75/2)
    window.left(90)
    window.fd(50)

def door():   #makes the door to the house with a door handle

    door = turtle.Turtle()
    door.hideturtle()
    door.pensize(5)
    door.penup()
    door.setpos(50, -150)
    door.pendown()
    door.fillcolor("saddlebrown")
    door.begin_fill()
    for i in range(2):
        door.fd(50)
        door.left(90)
        door.fd(100)
        door.left(90)
    door.end_fill()

    doorh = turtle.Turtle()
    doorh.shape("circle")
    doorh.shapesize(1)
    doorh.color("yellow")
    doorh.penup()
    doorh.hideturtle()
    doorh.setpos(90, -100)
    doorh.stamp()

def chimneyf():   #makes the chimney to the house

    chimney = turtle.Turtle()
    chimney.hideturtle()
    chimney.penup()
    chimney.setpos(25, 25)
    chimney.pensize(5)
    chimney.pendown()
    chimney.pencolor("brown")
    chimney.fillcolor("brown")

    chimney.begin_fill()
    for i in range(2):
        chimney.fd(25)
        chimney.left(90)
        chimney.fd(150)
        chimney.left(90)
    chimney.end_fill()

def house():  #the order in which the house should be built in order to reduce confusion
    houseb()
    windows(-100, -100)
    door()
    chimneyf()
    houser()

def fencef(x, y):   # makes the fence around the house
    fence = turtle.Turtle()
    fence.penup()
    fence.setpos(x, y)
    fence.pensize(3)
    fence.hideturtle()
    fence.left(90)
    fence.pendown()
    fence.fillcolor("saddlebrown")

    for i in range(13):
        fence.begin_fill()
        fence.fd(75)
        fence.right(45)
        fence.fd(math.sqrt(50))
        fence.right(90)
        fence.fd(math.sqrt(50))
        fence.right(45)
        fence.fd(75)
        fence.right(180)
        fence.end_fill()

def sunf():   #puts a sun up in the corner of the screen
    sun = turtle.Turtle()
    sun.hideturtle()
    sun.shape("circle")
    sun.shapesize(8)
    sun.pencolor("yellow")
    sun.fillcolor("yellow")
    sun.penup()
    sun.setpos(-250, 250)
    sun.stamp()
    sun.hideturtle()

def main():   #main function in which everything is ran through

    wn = turtle.Screen()
    wn.bgcolor("lightblue")
    wn.colormode(255)

    fencef(-250, -150)
    fencef(120, -150)
    roadf()
    grassf()
    house()
    sunf()

    wn.exitonclick()


main()
