
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

#draw eyes

def function_eye1():
    for i in range(36):
        akan.right(10)
        akan.forward(4)


def function_eye2():
    for i in range(36):
        akan.right(10)
        akan.forward(4)

#drawing nose

def function_nose():
    for n in range(3):
        akan.forward(30)
        akan.left(120)

#drawing mouth

def function_mouth1():
    for b in range (4):
        akan.right(16)
        akan.forward(10)


def function_mouth2():
    for i in range(4):
        akan.left(16)
        akan.forward(10)

#drawing tongue
def function_tongue():
    for i in range(9):
        akan.forward(8)
        akan.left(21)

#drawing whiskers

def function_whisker1():
    for i in range(5):
        akan.forward(101)
        akan.backward(101)
        akan.right(15)

def function_whisker2():
    for i in range(5):
        akan.forward(101)
        akan.back(101)
        akan.left(15)

def main():
    function_1()
    akan.penup()
    akan.goto(-80, 90)
    akan.pendown()
    akan.left(90)
    #drawing eyes
    function_eye1()

    akan.penup()
    akan.goto(100, 90)
    akan.pendown()
    akan.left(180)

    function_eye2()

    akan.penup()
    akan.goto(25, 50)
    akan.pendown()

    akan.right(90)
    #drawing nose
    function_nose()

    akan.left(60)
    akan.forward(30)

    #draw mouth
    function_mouth1()

    akan.penup()
    akan.goto(25, 50)
    akan.pendown()
    akan.left(60)
    akan.forward(30)
    akan.left(72)
    function_mouth2()

    akan.penup()
    akan.goto(-10, 10)
    akan.right(90)
    akan.pendown()

    function_tongue()

    # drawing ears
    akan.penup()
    akan.goto(114, 212)
    akan.pendown()
    akan.right(21)
    akan.forward(80)
    akan.left(120)
    akan.forward(95)

    akan.penup()
    akan.goto(-115, 195)
    akan.pendown()

    akan.setheading(90)
    akan.forward(95)
    akan.right(120)
    akan.forward(95)

    akan.penup()
    akan.goto(50, 25)
    akan.pendown()

    akan.setheading(30)

    # drawing whisker
    function_whisker1()

    akan.penup()
    akan.goto(-30, 25)
    akan.pendown()
    akan.setheading(150)

    function_whisker2()
    akan.hideturtle()

main()

wn.exitonclick()
