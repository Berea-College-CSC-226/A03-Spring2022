#Daniel Doh, dohd.
# Doc link: https://docs.google.com/document/d/1lRhFd3aTRC2WGJp3zaQuuSGvWdi5v5AJu8CkhqXgCH0/edit?usp=sharing
import turtle

def createhouse(x):
    "This function uses a for loop to create a house. On the 2nd iteration, it gets the position of the top corner of the house."
    "Once it gets the top corner, it proceeds to send the turtle to that location and begin creating the roof."
    for i in range(4):
        x.forward(200)
        x.left(90)
        if i == 1:
            j = x.pos()
    x.penup()
    x.goto(j)
    x.pendown()
    x.left(180)
    x.backward(70)
    x.right(45)
    x.forward(250)
    x.left(90)
    x.forward(250)
    x.left(135)
    x.forward(100)
def main():
    "Main function that initializes the turtle, its color, screen/screen color."
    "It also sets the turtle to a lower spot on the canvas and then calls the function 'createhouse' to begin."
    sam = turtle.Turtle()
    wn = turtle.Screen()
    wn.bgcolor("lightblue")
    wn.colormode(255)
    sam.pencolor(90,104,90)
    sam.penup()
    sam.goto(-100,-100)
    sam.pendown()
    sam.speed(3)
    sam.pensize(10)
    createhouse(sam)
    wn.exitonclick()

main()
