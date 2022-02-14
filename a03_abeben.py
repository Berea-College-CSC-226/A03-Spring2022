#################################################################################
# Author: Natinael Abebe
# Username: abeben
#
# Assignment: a03
# Purpose:
# Google Doc Link: https://docs.google.com/document/d/16lCjQwgEN9DpMXIOVi1iF42yxxbKww_ov-1BztKZfhU/edit?usp=sharing
#
#################################################################################
# Acknowledgements: Stackflow- refer the loop to create the triangle
#
#
#################################################################################
import turtle
import math
from turtle import *


def square (t, length, pensize, color,):
    #Setting the position, pensize, and color
    t.penup()
    t.setpos(210, 110)
    t.pensize(pensize)
    t.color(color)
    t.pendown()
    # To create the sides of the square
    for i in range(4):
        t.forward(length)
        t.right(90)

        t.penup()
        t.setpos(210, 110)
        t.pensize(pensize)
        t.color(color)
        t.pendown()

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

    for i in range(4):   #### loop fpr triangle
        t.forward(length)
        t.right(90)
        t.color("green")
        t.pensize(5)
    #### Creates the illusion circle
def circle(t,length, color):
    circle = turtle.Turtle()
    circle.penup()
    circle.pencolor("blue")
    circle.setpos(100, 110)
    circle.left(43)
    circle.shapesize(40)

    # Creates the Circle
    for i in range(100):
        circle.stamp()
        circle.forward(13.6)
        circle.right(3.6)

def main():

    wn =turtle.Screen()
    wn.bgcolor('black')
    square_turtle = turtle.Turtle()
    triangle_turtle = turtle.Turtle()
    triangle(triangle_turtle, 250,"#e51212")
    square(square_turtle, 20, 25, "#dee9e1")
    circle_turtle = turtle.Turtle()
    circle(circle_turtle, 2, "red" )
    wn.bgcolor('black')

    wn.exitonclick()

main()

