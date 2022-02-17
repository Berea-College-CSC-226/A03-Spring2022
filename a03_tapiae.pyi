# Name: Eduardo Tapia
# Google Doc Link: https://docs.google.com/document/d/15Q76GVT4pYPm6n2wNGQj0YFcG_CQbO7HkYzoZI39kx0/edit?usp=sharing

# Importing the turtles and set it up
import turtle
wn = turtle.Screen()
turtle1 = turtle.Turtle()
turtle.bgcolor("light blue")
turtle.colormode(255)
turtle1.penup()
turtle1.setpos(-300, -250)
turtle1.pendown()
print(turtle.screensize())
print(turtle.pos())
turtle1.left(90)


# Making the square
def drawsquare():
    turtle1.fillcolor("red")
    turtle1.begin_fill()
    for i in (range(4)):
        turtle1.forward(250)
        turtle1.right(90)
    turtle1.end_fill()


# Making the triangle
def drawtriangle():
    turtle1.fillcolor(196, 164, 132)
    turtle1.begin_fill()
    turtle1.forward(250)
    turtle1.right(45)
    turtle1.forward(178)
    turtle1.right(90)
    turtle1.forward(176)
    turtle1.right(135)
    turtle1.forward(250)
    turtle1.end_fill()

# Moving the turtle
def moveturtle():
    turtle1.right(180)
    turtle1.forward(250)
    turtle1.right(90)
    turtle1.forward(251)
    turtle1.right(90)
    turtle1.forward(125)
    turtle1.forward(50)

# Making the door
def drawdoor():
    turtle1.fillcolor(115, 134, 120)
    turtle1.begin_fill()
    for i in range(4):
        turtle1.right(90)
        turtle1.forward(100)
    turtle1.end_fill()
    turtle1.penup()
    turtle1.setpos(150, 250)
    turtle1.pendown()

# Start of making a circle
def drawcircle():
    turtle1.fillcolor('yellow')
    turtle1.begin_fill()
    turtle1.circle(100)
    turtle1.end_fill()

def main():
    drawsquare()
    drawtriangle()
    moveturtle()
    drawdoor()
    drawcircle()

main()

turtle.exitonclick()
