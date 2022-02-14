#################################################################################
# Author: Natinael Abebe
# Username: abeben
#
# Assignment: a03
# Purpose:
# Google Doc Link: https://docs.google.com/document/d/16lCjQwgEN9DpMXIOVi1iF42yxxbKww_ov-1BztKZfhU/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################
import turtle
import math
from turtle import *


def square (t, length, pensize, color,):
    #Setting the position, pensize, and color
    t.penup()
    t.setpos(30, -10)
    t.pensize(pensize)
    t.color(color)
    t.pendown()
    # To create the sides of the square
    for i in range(4):
        t.forward(length)
        t.right(90)

    ## To create the triangele

def triangle(t, length, color):

    t.fillcolor(color)
    t.setpos(90, -10)
    t.begin_fill()
    t.forward(length)
    t.left(135)
    t.forward(length / math.sqrt(2))
    t.left(90)
    t.forward(length / math.sqrt(2))
    t.left(135)
    t.end_fill()






















def main():

    wn =turtle.Screen()
    wn.bgcolor('black')
    square_turtle = turtle.Turtle()
    triangle_turtle = turtle.Turtle()
    triangle(triangle_turtle, 250,"red")

    square(square_turtle, 350, 25, "blue")


    wn.bgcolor('black')

    wn.exitonclick()

main()

