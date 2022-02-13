
#################################################################################
# Author: Josahn Oginga
# Username: ogingaj@berea.edu
#
# Assignment: A03 - Functional Turtles
# Purpose: Fully functional gitty psychedelic robotic turtles
# Google Doc Link: https://docs.google.com/document/d/1wd3B9vDGKYxIQli4bwXiheFc9BGSxO3Y0y0me2Ye-dY/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle
import math
wn = turtle.Screen() #setting up the turtle and the screen
wn.colormode(255)
wn.bgcolor(120,0,120)
akan = turtle.Turtle()
akan.color(255,255,255)
akan.speed(0)
akan.pensize(5)
akan.penup()
akan.goto(0,-100)
akan.pendown()

#draw a circle - head of cat
def function_1():
    for i in range(72):
        akan.forward(15)
        akan.left(5)
    #pass
    # ....
function_1()

akan.penup()
akan.goto(-80,90)
akan.pendown()

#draw eyes
akan.left(90)
def function_eye1():
    for i in range(36):
        akan.right(10)
        akan.forward(4)

function_eye1()

akan.penup()
akan.goto(100,90)
akan.pendown()
akan.left(180)

def function_eye2():
    for i in range(36):
        akan.right(10)
        akan.forward(4)

function_eye2()


akan.penup()
akan.goto(25,50)
akan.pendown()

akan.right(90)

#drawing nose

def function_nose():
    for n in range(3):
        akan.forward(30)
        akan.left(120)

function_nose()

akan.left(60)
akan.forward(30)

#drawing mouth

def function_mouth1():
    for b in range (4):
        akan.right(16)
        akan.forward(10)
function_mouth1()

akan.penup()
akan.goto(25,50)
akan.pendown()
akan.left(60)
akan.forward(30)
akan.left(72)
def function_mouth2():
    for i in range(4):
        akan.left(16)
        akan.forward(10)

function_mouth2()

akan.penup()
akan.goto(-10,10)
akan.right(90)
akan.pendown()
#drawing tongue
def function_t():
    for i in range(9):
        akan.forward(8)
        akan.left(21)

function_t()

#drawing ears
akan.penup()
akan.goto(114,212)
akan.pendown()
akan.right(21)
akan.forward(80)
akan.left(120)
akan.forward(95)

akan.penup()
akan.goto(-115,195)
akan.pendown()

akan.setheading(90)
akan.forward(95)
akan.right(120)
akan.forward(95)


akan.penup()
akan.goto(50,25)
akan.pendown()

akan.setheading(30)

#drawing whiskers

def function_whisker1():
    for i in range(5):
        akan.forward(100)
        akan.backward(100)
        akan.right(15)

function_whisker1()

akan.penup()
akan.goto(-30,25)
akan.pendown()
akan.setheading(150)
#akan.left(135)

def function_whisker2():
    for i in range(5):
        akan.forward(100)
        akan.back(100)
        akan.left(15)

function_whisker2()


def function_3():
    """
    Docstring for function_2
    """
    pass
    # ...


#def main():
    """
    Docstring for main
    """
    # ...
    function_1()            # Function call to function_1
    function_2()            # Function call to function_2


#main()

wn.exitonclick()
