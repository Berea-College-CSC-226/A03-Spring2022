#===========================================================================================
#Name:Isaac Solomon Gray
#Username:IsaacSGray
#Purpose:To get the assignment done
#Acknowledgements:Doctor Shepard is awesome
#Use this for whatever whoever finds it. I'm a simple man trying to find his way through a CS degree.
#Google doc:https://docs.google.com/document/d/1RlYrT2DZDySsYA9f9pOAsjhPGdfmGWu_zj03pQKNnw8/edit?usp=sharing
#Don't use this code to harm anyone, anything, ect. Use it for whatever benevolent desire you have.
#====================================================================================================

import turtle

def turtleprep():
    Ike=turtle.Turtle()
    window=turtle.Screen()
    window.colormode(255)
    window.bgcolor("black")
    Ike.pencolor("red")
    Ike.penup()
    Ike.setposition(0,0)
    Ike.pensize(3)
    Ike.speed(20)
    return Ike,window

def DrawRoof():
    Ike , window=turtleprep()
    Ike.pendown()
    Ike.begin_fill()
    for i in range(3):
        Ike.right(60)
        Ike.forward(130)
        Ike.right(60)
    for i in range(3):
        Ike.right(180)
        Ike.forward(200)
    Ike.left(60)
    Ike.forward(110)
    Ike.left(115)
    Ike.forward(200)

    Ike.end_fill()

def DrawHouse():
    Ike, window = turtleprep()
    Ike.penup()
    Ike.setposition(-60,-113)
    Ike.pendown()
    for i in range(2):
        Ike.right(90)
        Ike.forward(140)
        Ike.right(10)
    Ike.forward(60)
    Ike.right(70)
    Ike.forward(120)
    Ike.penup()
    Ike.right(90)
    Ike.forward(305)
    Ike.right(60)
    Ike.forward(30)
    Ike.pendown()
    Ike.right(30)
    for i in range(2):
        Ike.forward(130)
        Ike.right(90)
    Ike.penup()
    Ike.setposition(-20,-245)
    Ike.pendown()
    for i in range (2):
        Ike.forward(60)
        Ike.right(90)
        Ike.forward(40)
        Ike.right(90)

def main():
    Ike, window = turtleprep()
    turtleprep()
    DrawRoof()
    DrawHouse()
    window.exitonclick()

main()




