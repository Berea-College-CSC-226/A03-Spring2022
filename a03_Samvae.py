#################################################################################
# Author: Sam Villahermosa
# Username: Samvae
#
# Assignment: A03: Functional Turtles
# Purpose: Draw something complex
# Google Doc Link: https://docs.google.com/document/d/1u4-uRAqr_-e2bneJPlXUXUUkqMsGiZJtvCsiNWa0Xdg/edit?usp=sharing
#
#################################################################################

import turtle                                   # Allows us to use the turtles library

def sky(art):
    """
    Creates a blue rectangle which represents the sky.

    :param art: a Turtle object
    :return: None
    """

    art.color("#87CEFA")                        # Hex Code for a sky color blue
    art.penup()
    art.goto(-800, -100)
    art.pendown()
    art.begin_fill()
    for side in range(2):                       # Loop used for rectangle
        art.fd(1600)
        art.lt(90)
        art.fd(550)
        art.lt(90)
    art.end_fill()


def sun(art,x,y):
    """
    Creates the sun!

    :param art: a Turtle object
    :param x: the x coordinate of the sun
    :param y: the y coordinate of the sun
    :return: None
    """

    art.goto(x,y)
    art.color("#FFEB50")                           # Hex Code for a color yellow
    art.begin_fill()
    for i in range(18):                            # Loop used to create the sun
        art.right(90)
        art.forward(20)
        art.forward(-20)
        art.left(90)
        art.circle(100, 20)
    art.end_fill()

def clouds(art,x,y):
    """
    Creates circles to form clouds.

    :param art: a Turtle object
    :param x: the x coordinate for a cloud
    :param y: the y coordinate for a cloud
    :return:  None
    """

    art.color("white")
    art.penup()
    art.goto(x,y)
    art.pendown()
    art.begin_fill()
    art.circle(30)
    art.end_fill()
    art.begin_fill()
    art.goto(x+40,y+15)
    art.circle(30)
    art.end_fill()
    art.begin_fill()
    art.goto(x+40,y-15)
    art.circle(30)
    art.end_fill()

def house(build):
    """
    Draws the house base.

    :param build: a Turtle object
    :return: None
    """

    build.color("#E7BF8E")
    build.penup()
    build.goto(-150,-220)
    build.pendown()
    build.pensize(3)
    build.begin_fill()
    for i in range(2):                                  # For loop used to create rectangle
        build.fd(300)
        build.lt(90)
        build.fd(230)
        build.lt(90)
    build.end_fill()


def roof(build):
    """
    Creates the roof of the house!

    :param build: a Turtle object
    :return: None
    """

    build.color("#79301D")
    build.penup()
    build.goto(-175,10)
    build.pendown()
    build.begin_fill()
    build.fd(350)                                      # Triangle shape for roof
    build.lt(150)
    build.fd(220)
    build.lt(65)
    build.fd(185)
    build.end_fill()

def chimney(build):
    """
    Attaches the chimney onto the roof.

    :param build: a Turtle object
    :return: None
    """

    build.color("#79301D")
    build.rt(35)
    build.penup()
    build.goto(80, 130)
    build.pendown()
    build.begin_fill()
    for i in range(2):                                         # Rectangle shape for chimney
        build.fd(40)
        build.lt(90)
        build.fd(100)
        build.lt(90)
    build.end_fill()

def windows(build,x,y,z):
    """
    Creates the windows of the house.

    :param build: a Turtle object
    :param x: the x coordinates of a window
    :param y: the y coordinates of a window
    :param z: the angle of which the turtle is facing.
    :return: None
    """

    build.rt(z)
    build.penup()
    build.goto(x,y)
    build.pendown()
    build.color("black","lightblue")
    build.begin_fill()
    for i in range(4):                                      # Loop for the square
        build.fd(70)
        build.lt(90)
    build.end_fill()
    build.penup()
    build.goto(x,y-35)                                      # Creates the horizontal line of the window
    build.pendown()
    build.color("black")
    build.fd(70)
    build.end_fill()
    build.penup()
    build.goto(x-35,y)                                      # Creates the vertical line of the window
    build.pendown()
    build.lt(90)
    build.fd(70)

def door(build,x,y):
    """
    Makes the door of the house.

    :param build: a Turtle object
    :param x: the x coordinate of the door
    :param y: the y coordinate of the door
    :return: None
    """

    build.penup()
    build.goto(x,y)
    build.pendown()
    build.right(90)
    build.color("#79301D")
    build.begin_fill()
    for i in range(2):
        build.fd(50)
        build.lt(90)
        build.fd(80)
        build.lt(90)
    build.end_fill()

def circle(art,x,y,color,size):
    """
    Circles used for extra design like smoke and door handle.

    :param art: a Turtle object
    :param x: the x coordinate of the circle
    :param y: the y coordinate of the circle
    :param color: the color of the circle
    :param size: the size of the circle
    :return: None
    """

    art.color(color)
    art.penup()
    art.goto(x,y)
    art.pendown()
    art.begin_fill()
    art.circle(size)
    art.end_fill()

def tree(art,x,y,z):
    """
    Draws a tree.

    :param art: a Turtle object
    :param x: the x coordinate of the tree
    :param y: the y coordinate of the tree
    :param z: the angle the turtle is facing
    :return: None
    """
# Trunk
    art.rt(z)
    art.penup()
    art.goto(x,y)
    art.pendown()
    art.color("#725c42")
    art.begin_fill()
    for i in range(2):
        art.fd(140)
        art.lt(90)
        art.fd(40)
        art.lt(90)
    art.end_fill()
# Leaves
    art.fd(20)
    art.lt(90)
    art.fd(15)
    art.color("forestgreen")
    art.begin_fill()
    art.circle(75)
    art.end_fill()

def pavement(build,x,y):
    """
    Creates the pavement.

    :param build: a Turtle object
    :param x: the x coordinate of the pavement
    :param y: the y coordinate of the pavement
    :return: None
    """

    build.rt(90)
    build.penup()
    build.goto(x, y)
    build.pendown()
    build.right(90)
    build.color("lightgray")
    build.begin_fill()
    for i in range(2):
        build.fd(50)
        build.lt(90)
        build.fd(120)
        build.lt(90)
    build.end_fill()

def main():
    """
    Draws an image of a house with trees, clouds, sky, sun, etc.

    :return: None
    """

    wn = turtle.Screen()                            # Makes a new turtle screen
    wn.bgcolor("#348C31")                           # Sets the background color to green

    art = turtle.Turtle()
    art.hideturtle()
    art.speed(0)

    build = turtle.Turtle()
    build.hideturtle()
    build.speed(0)

    # Function calls for each part of the house and figures surrounding it.
    sky(art)
    sun(art,-250, 150)
    clouds(art,-120,150)
    clouds(art,-80,120)
    clouds(art,140,230)
    clouds(art,180,200)
    house(build)
    roof(build)
    chimney(build)
    circle(art, 75, 140, "gray", 15)
    circle(art, 65, 160, "gray", 15)
    circle(art, 75, 180, "gray", 15)
    windows(build,-60,-10,0)
    windows(build,115,-10,90)
    windows(build,-60,-110,90)
    windows(build,115,-110,90)
    door(build,20,-140)
    circle(art,10,-185,"yellow",5)
    tree(art,250,0,90)
    tree(art,-250,-10,90)
    pavement(build,-30,-345)

    wn.exitonclick()                    # Exits window when user clicks on the canvas

main()          # Call main()

