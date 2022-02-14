# A03-CSC 226
# Aaron Meadows
# -https://docs.google.com/document/d/1aAQ04LTdyc0C6Ml8-dFdsBNZwKhWySfWZkDeYK-NgO4/edit#
# -https://github.com/Berea-College-CSC-226/a03-functional-turtles-meadowsa2.git

import turtle

def hay():
    #draws haybail outline
    haybail =turtle.Turtle()
    haybail.color("brown")
    haybail.pensize(10)
    haybail.fillcolor("#FAD02C")
    haybail.goto(300,0)
    haybail.begin_fill()
    for i in range(4):
        haybail.left(90)
        haybail.fd(600)
    haybail.end_fill()

    #draws haybail ties
    haybail.penup()
    haybail.goto(180,0)
    haybail.pendown()
    haybail.left(90)
    haybail.pensize(50)
    haybail.fd(600)

    haybail.penup()
    haybail.goto(-180, 0)
    haybail.pendown()
    haybail.pensize(50)
    haybail.fd(600)



def bill():
    # draws head of piggy
    bill = turtle.Turtle()
    bill.shape("turtle")
    bill.color("green")
    bill.pencolor("black")
    bill.fillcolor("pink")
    bill.pensize(15)

    bill.penup()
    bill.goto(0, -100)
    bill.pendown()
    bill.begin_fill()
    bill.circle(200)
    bill.end_fill()

    # draws eyes of piggy
    bill.fillcolor("black")
    bill.penup()
    bill.goto(80, 150)
    bill.pendown()
    bill.begin_fill()
    bill.circle(40)
    bill.end_fill()

    bill.penup()
    bill.goto(-80, 150)
    bill.pendown()
    bill.begin_fill()
    bill.circle(40)
    bill.end_fill()

    # draws nose of piggy
    bill.fillcolor('#e75480')
    bill.begin_fill()
    bill.penup()
    bill.goto(15, -10)
    bill.pendown()
    bill.fd(50)
    for i in range(5):
        bill.left(36)
        bill.forward(30)
    bill.fd(100)
    for i in range(5):
        bill.left(36)
        bill.forward(30)
    bill.fd(50)
    bill.end_fill()

    # draws ears of piggy
    # right side ear
    bill.fillcolor("pink")
    bill.penup()
    bill.goto(110, 280)
    bill.pendown()
    bill.begin_fill()
    bill.left(45)
    bill.fd(80)
    bill.right(30)
    bill.fd(40)
    bill.right(30)
    bill.fd(40)
    bill.right(90)
    bill.fd(175)
    bill.goto(110, 280)
    bill.end_fill()
    #left side ear
    bill.penup()
    bill.goto(-110, 280)
    bill.pendown()
    bill.goto(-110, 280)
    bill.pendown()
    bill.begin_fill()
    bill.right(115)
    bill.fd(80)
    bill.left(30)
    bill.fd(40)
    bill.left(30)
    bill.fd(40)
    bill.left(90)
    bill.fd(175)
    bill.goto(-110, 280)
    bill.end_fill()
def rick():
    # draws nostrils
    rick = turtle.Turtle()
    rick.shape("circle")
    rick.color("black")
    rick.fillcolor("black")
    rick.penup()
    rick.goto(50, 20)
    rick.pendown()
    rick.begin_fill()
    rick.circle(20)
    rick.end_fill()

    rick.penup()
    rick.goto(-50, 20)
    rick.pendown()
    rick.begin_fill()
    rick.circle(20)
    rick.end_fill()

    # eye-glare
    rick.pencolor("white")
    rick.fillcolor("white")
    rick.penup()
    rick.goto(100, 200)
    rick.pendown()
    rick.begin_fill()
    rick.circle(10)
    rick.end_fill()

    rick.penup()
    rick.goto(-60, 200)
    rick.pendown()
    rick.begin_fill()
    rick.circle(10)
    rick.end_fill()


def main():
    wn = turtle.Screen()
    wn.bgcolor('lightblue')
    hay()
    bill()
    rick()

    wn.exitonclick()
main()
