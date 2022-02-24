######################################################################
# Author: Paulina Conder
# Username: conderp
#
# Assignment: A03 Functional Turtles
#
# Purpose: Gain practice in using the turtle library, colors, source
# control, and git
#
# Google Doc: https://docs.google.com/document/d/1dbJYNbF1AAt_ZdRHUC3Fk6xZ9fRMYqNkvu6aLG4bHR4/edit#
######################################################################

import turtle
from random import randint

wn = turtle.Screen()
wn.bgcolor("#150030")
wn.colormode(255)

meg = turtle.Turtle()
meg.penup()
meg.ht()

tim = turtle.Turtle()
tim.penup()
tim.ht()

pat = turtle.Turtle()
pat.penup()
pat.ht()

bob = turtle.Turtle()
bob.penup()
bob.ht()


def moon():
    """Draws a crescent moon"""
    tim.color(255, 255, 255)
    tim.setposition(-180, 200)
    tim.left(-15)
    tim.pendown()
    tim.begin_fill()
    for i in range(210):
        tim.forward(1)
        tim.right(1)
    tim.right(140)
    for i in range(140):
        tim.forward(1)
        tim.left(1)
    tim.end_fill()
    tim.penup()
    tim.right(115)
    # pass?


def big_star():
    """Draws a shooting star"""
    meg.color('gold')
    meg.setposition(153, 97)
    meg.pendown()
    meg.begin_fill()
    for i in range(5):                  # main star
        meg.right(-80)
        meg.forward(20)
        meg.right(150)
        meg.forward(20)
    meg.end_fill()
    meg.penup()
    meg.setposition(120, 90)             # light beam 1
    meg.pendown()
    meg.left(10)
    meg.backward(150)
    meg.penup()
    meg.setposition(-10, 0)           # light beam 1
    meg.left(7)
    meg.pendown()
    meg.forward(150)
    meg.penup()
    meg.setposition(140, 55)            # light beam 3
    meg.pendown()
    meg.right(165)
    meg.forward(150)
    meg.penup()


def planet():
    """Draws a planet"""
    pat.color('lightcyan')
    pat.setposition(-50, -100)
    pat.pendown()
    pat.pensize(20)
    pat.shape('circle')
    pat.begin_fill()                     # main planet
    for i in range(360):
        pat.forward(1)
        pat.right(1)
    pat.end_fill()
    pat.pensize(3)
    pat.color('mediumslateblue')         # colors on planet
    for i in range(100):
        pat.forward(1)
        pat.right(1)
    pat.penup()
    pat.setposition(-105, -150)
    pat.pendown()
    for i in range(75):
        pat.forward(1)
        pat.left(1)
    pat.penup()
    pat.setposition(-115, -175)          # ring around planet
    pat.pendown()
    pat.pensize(9)
    pat.color(255, 160, 0)
    pat.right(120)
    for i in range(20):
        pat.forward(1)
        pat.left(1)
    for i in range(12):
        pat.left(10)
        pat.forward(1)
    for i in range(37):
        pat.forward(5)
        pat.left(2)
    for i in range(12):
        pat.left(10)
        pat.forward(1)
    for i in range(20):
        pat.forward(1)
        pat.left(1)
    pat.penup()


def stars():
    """Adds stars to background"""
    bob.color('white')
    bob.pensize(1)
    for i in range(100):
        bob.goto((randint(-350,350), randint(-350, 350)))
        bob.pendown()
        bob.forward(1)
        bob.penup()


def main():
    stars()
    moon()
    big_star()
    planet()


main()

wn.exitonclick()
