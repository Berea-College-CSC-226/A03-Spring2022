#################################################################################
# Author: Josh Heigley
# Username: heigleyj
#
# Assignment: a03
# Purpose: learn about branches and work more with turtles and function definitions
# Google Doc Link:https://docs.google.com/document/d/1ReHYb_4BsqqU_xZHgrw8dVmx586dybLVKxJevAvM0uo/edit#
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle
wn = turtle.Screen()

def function_1():
    """
    sets up the background
    """
    wn.bgcolor("lightblue")
    grass = turtle.Turtle()
    grass.fillcolor("green")
    grass.penup()
    grass.speed(0)
    grass.setposition(-385, -200)
    grass.pendown()
    grass.begin_fill()
    for g in range(4):
        grass.forward(800)
        grass.right(90)
    grass.end_fill()

    pass
    # ....


def function_2():
    """
    Makes the turtles draw a house
    """
    pass
    house1 = turtle.Turtle()
    house1.setposition(0, -200)
    house1.fillcolor("tan")
    house1.begin_fill()
    for h1 in range(3):
        house1.forward(200)
        house1.left(90)
    house1.end_fill()

    # roof
    house2 = turtle.Turtle()
    house2.fillcolor(.8, .1, .1)
    house2.begin_fill()
    house2.left(180)
    house2.forward(30)
    for h2 in range(2):
        house2.right(150)
        house2.forward(150)
        house2.left(90)
    house2.left(120)
    house2.forward(230)
    house2.end_fill()
    # ...

def function_3():
    """
    Makes the sun and its rays
    """
    # properties
    sun = turtle.Turtle()
    sunbeam = turtle.Turtle()
    sun.penup()
    sunbeam.penup()
    sun.fillcolor("yellow")
    sunbeam.color("yellow")
    sunbeam.pensize(3)

    # sun
    sun.setposition(-250, 200)
    sun.begin_fill()
    for s in range(40):
        sun.forward(s)
        sun.right(s)

    sun.end_fill()

    # sun rays
    for beam in range(0, 361, 10):
        sunbeam.setposition(-250, 150)
        sunbeam.forward(60)
        sunbeam.pendown()
        sunbeam.forward(45)
        sunbeam.penup()
        sunbeam.left(beam)


def main():
    """
    Docstring for main
    """
    # ...
    function_1()            # Function call to function_1
    function_2()            # Function call to function_2
    function_3()
main()
wn.exitonclick()