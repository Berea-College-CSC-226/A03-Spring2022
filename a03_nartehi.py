##########################################################################################################
#Author: IsaacNarteh
#Username:nartehi
# Assignment: A03: Fully Functional Gitty Psychedelic Robotic Turtles

# Purpose : Applying functions to draw something complex using turtle module.

#Google Doc url:https://docs.google.com/document/d/1XFO3_puWOUFOabHbE6mhNC1OCdDmkEVry6ZY5i_NJRg/edit?usp=sharing

##########################################################################################################

import turtle
wn=turtle.Screen()
ike=turtle.Turtle()
wn.bgcolor("lightblue")
turtle.colormode(255)
ike.pensize(2)
ike.pencolor("brown")
ike.hideturtle()
ike.speed(2)
ike.penup()
ike.goto(-200,-200)
ike.pendown()

def drawRectangle(l,w):
    ike.color("#4275f5")
    ike.begin_fill()
    ike.pencolor((250, 0, 200))
    for base in range(2):
        ike.forward(300)
        ike.left(90)
        ike.forward(320)
        ike.left(90)
    ike.end_fill()
# code to move pen to the a new location
def movepen_1(a,b):
    ike.penup()
    ike.setpos(-40,-200)
    ike.pendown()

#code to draw the front door

def DrawDoor(l,w):
    ike.color("red")
    ike.begin_fill()
    for x in range(2):
        ike.forward(10)
        ike.left(90)
        ike.forward(200)
        ike.left(90)
        ike.forward(50)
    ike.end_fill()
#code to draw first window

def movepen_2(h,c):
    ike.penup()
    ike.setpos(-170,-80)
    ike.pendown()

def DrawWindow_1(s,h):
    ike.color("white")
    ike.begin_fill()
    for g in range(4):
       ike.forward(40)
       ike.left(90)
    ike.end_fill()


def movepen_3(j,y):
    ike.penup()
    ike.setpos(30,-80)
    ike.pendown()

def DrawWindow_2(s,h):
    ike.color("white")
    ike.begin_fill()
    for g in range(4):
        ike.forward(40)
        ike.left(90)
    ike.end_fill()


def movepen_4(r,k):
     ike.penup()
     ike.setpos(-240,120)
     ike.pendown()


 #code to draw roof

def DrawRoof(g,h):
    ike.color("black")
    ike.begin_fill()
    ike.forward(360)
    ike.left(135)
    ike.forward(250)
    ike.left(90)
    ike.forward(250)
    ike.end_fill()



drawRectangle(300,320)
movepen_1(-40,150)
DrawDoor(10,200)
movepen_2(-170,-80)
DrawWindow_1(40,90)
movepen_3(30,-80)
DrawWindow_2(40,90)
movepen_4(-240,120)
DrawRoof(360,120)


wn.exitonclick()
