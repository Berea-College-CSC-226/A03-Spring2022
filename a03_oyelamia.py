# Header Information
# Eni Oyelami, Oyelamia, https://docs.google.com/document/d/1ou5qrWVva4eKnLW2-lGcrM5cBxoDHfnN7Dwx9cRjsdw/edit?usp=sharing

import turtle
wn = turtle.Screen()

eye = turtle.Turtle()
nose = turtle.Turtle()
face = turtle.Turtle()
tongue = turtle.Turtle()
tonguebk = turtle.Turtle()

leftear = turtle.Turtle()
rightear = turtle.Turtle()

leftear.color('brown')
leftear.begin_fill()
leftear.penup()
leftear.goto(-138,-50)
leftear.pendown()
leftear.forward(90)
leftear.left(90)
leftear.forward(90)
leftear.left(90)
leftear.forward(50)
leftear.left(90)
leftear.forward(50)
leftear.right(90)
leftear.forward(40)
leftear.left(90)
leftear.forward(40)
leftear.end_fill()
leftear.hideturtle()

rightear.color('brown')
rightear.begin_fill()
rightear.penup()
rightear.goto(150,-50)
rightear.pendown()
rightear.forward(90)
rightear.left(90)
rightear.forward(40)
rightear.left(90)
rightear.forward(50)
rightear.right(90)
rightear.forward(50)
rightear.left(90)
rightear.forward(50)
rightear.left(90)
rightear.forward(90)
rightear.left(90)
rightear.forward(30)
rightear.end_fill()
rightear.hideturtle()


def eyes():
    eye.begin_fill()
    eye.pensize(2)
    eye.circle(5)
    eye.end_fill()
    eye.hideturtle()

def nariz(rad):
    for i in range(2):
        nose.begin_fill()
        nose.circle(rad,90)
        nose.circle(rad//10,90)
        nose.end_fill()
nose.seth(-45)
nose.hideturtle()

def head():
    '''
        Create the rectangle head
    '''

    face.pensize(2)
    face.forward(130)
    face.left(90)
    face.forward(130)
    face.left(90)
    face.forward(185)
    face.left(90)
    face.forward(130)
    face.left(90)
    face.forward(70)

#Tongue Background
tonguebk.color("pink")
tonguebk.begin_fill()
tonguebk.pensize(2)
tonguebk.penup()
tonguebk.goto(36, -100)
tonguebk.pendown()
for i in range(2):
    tonguebk.forward(30)
    tonguebk.left(90)
    tonguebk.forward(30)
    tonguebk.left(90)
tonguebk.end_fill()
tonguebk.hideturtle()

#Actual Tongue
tongue.pensize(2)
tongue.penup()
tongue.goto(36, -100)
tongue.pendown()
for i in range(2):
    tongue.forward(30)
    tongue.left(90)
    tongue.forward(30)
    tongue.left(90)
tongue.penup()
tongue.goto(51, -70)
tongue.pendown()
tongue.right(90)
tongue.forward(23)
tongue.hideturtle()

def main():

    '''
    Call all the functions and put them in the correct positions
    '''

    wn.bgcolor('#A1CAF1')

    face.color("#F5F5DC")
    face.begin_fill()
    face.penup()
    face.goto(10, -70)
    face.pendown()

    head()
    face.end_fill()
    face.hideturtle()



    """
     Creating Eyes
    """
    eyes()
    eye.penup()
    eye.goto(95,0)
    eye.pendown()
    eyes()

    nose.penup()
    nose.goto(36,-25)
    nose.pendown()
    nariz(20)

    turtle.exitonclick()

main()
