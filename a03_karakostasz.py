#################################################################################
# Author: karakostas Zacharias
# Username: karakostasz
#
# Assignment: A03
# Purpose: CSC 226 - This program creates the Greek war flag / banner with the main use of Turtle module.
# Google Doc Link: https://docs.google.com/document/d/1qw9MNUGLKzGOSEt-z-c50qLjH5rsSSm2Iqx_4XDDflg/edit?usp=sharing
#
#################################################################################
import turtle

#screen setup:
wn = turtle.Screen()


#turtle:
zach = turtle.Turtle()
re = turtle.Turtle()
ti = turtle.Turtle()
ax = turtle.Turtle()
we = turtle.Turtle()
writer = turtle.Turtle()


def backround(wn, zach):
    """
    A new backround!
    setting a gif file backround of dark wood!:

    """
    wn.register_shape("wood.gif")
    zach.penup()
    zach.pendown()
    zach.shape("wood.gif")
    zach.stamp()


def lavaro():
    '''
    This function make the base of the banner which will hold the flag.
    '''

    #put ax in place
    ax.pencolor("#753000")
    ax.fillcolor("#753000")
    ax.penup()
    ax.fd(-135)
    ax.right(90)
    ax.fd(280)
    ax.left(90)
    ax.fd(115)
    ax.pendown()

    # start shape
    ax.begin_fill()
    ax.left(90)
    ax.fd(510)
    ax.left(90)
    ax.fd(140)
    ax.right(90)
    ax.fd(20)
    ax.right(90)
    ax.fd(300)
    ax.right(90)
    ax.fd(20)
    ax.right(90)
    ax.fd(140)
    ax.left(90)
    ax.fd(510)
    ax.right(90)
    ax.fd(20)
    ax.end_fill()
    ax.hideturtle()


def golden():
    '''
    This function provides nice Goldern details on the base of the banner:
    '''

    we.pencolor("silver")
    we.fillcolor("gold")

    # set in location and create the left golder plate:
    we.penup()
    we.fd(-155)
    we.left(90)
    we.fd(250)
    we.begin_fill()
    we.pendown()
    for i in range (2):
        we.left(45)
        we.fd(10)
        we.left(90)
        we.fd(10)
        we.left(45)
        we.fd(20)
    we.end_fill()

    # creation of the right golden plate:
    we.right(90)
    we.fd(290)
    we.left(90)
    we.begin_fill()
    for i in range (2):
        we.right(45)
        we.fd(10)
        we.right(90)
        we.fd(10)
        we.right(45)
        we.fd(20)
    we.end_fill()
    we.hideturtle()


def perimeter():
    '''
    This function creates the perimeter of the war greek flag/banner:

    The color of the flag is a hexadecimal!
    '''

    zach.color("blue")
    zach.fillcolor('#2D63FA')
    zach.begin_fill()
    zach.penup()
    zach.forward(-130)
    zach.right(90)
    zach.pendown()
    zach.fd(250)
    zach.left(135)
    zach.fd(170)
    zach.left(-90)
    zach.fd(170)
    zach.left(135)
    zach.fd(460)

    for number in range(2):
        zach.fd(40)
        zach.left(90)
        zach.fd(48)
        zach.left(90)
        zach.fd(40)
        zach.right(90)
        zach.fd(48)
        zach.right(90)

    zach.fd(40)
    zach.left(90)
    zach.fd(48)
    zach.left(90)
    zach.fd(250)
    zach.end_fill()


def cross():
    '''
    This function makes the orthodox christian cross, which forms the Greek war flag.
    '''

    re.color("white")
    re.pencolor("white")
    re.penup()
    re.fillcolor("white")
    re.begin_fill()
    re.fd(-130)
    re.left(90)
    re.fd(84)
    re.pendown()
    re.begin_fill()

    #first part of cross
    re.right(90)
    re.fd(96)
    re.left(90)
    re.fd(166)
    re.right(90)
    re.fd(48)
    re.right(90)
    re.fd(166)
    re.left(90)
    re.fd(96)
    re.right(90)
    re.fd(48)

    #second part pf cross
    re.right(90)
    re.fd(96)
    re.left(90)

    re.fd(188)
    re.right(135)
    re.fd(34)
    re.left(90)
    re.fd(34)
    re.right(135)
    re.fd(188)

    re.left(90)
    re.fd(96)
    re.right(90)
    re.fd(48)

    re.end_fill()
    re.hideturtle()


def krosia():
    '''
    This function creates great detail in the flag.
    In greece they are refered to as "krosia" and make every flag really appealing.
    '''

    ti.pencolor("gold")
    ti.penup()
    ti.forward(-130)
    ti.right(90)
    ti.fd(250)
    ti.pendown()

    #first part going up:
    for i in range(30):
        ti.fd(5)
        ti.left(90)
        ti.forward(2)
        ti.left(90)
        ti.forward(9)
        ti.right(90)
        ti.forward(2)
        ti.right(90)

    ti.left(90)
    ti.fd(1)
    ti.right(90)

    #second part going down
    for i in range(30):
        ti.fd(9)
        ti.left(90)
        ti.forward(2)
        ti.left(90)
        ti.forward(5)
        ti.right(90)
        ti.forward(2)
        ti.right(90)

    ti.fd(5)
    ti.hideturtle()

def revolution():
    '''
    This function print the an important date for Greece that symbolises its revolution.

    Further the function print the name "Greece" twice in each side.
    '''

    #type an Important date for Greece
    writer.penup()
    writer.left(90)
    writer.fd(40)
    writer.right(90)
    writer.fd(-40)
    writer.color()
    writer.write("1821", font=("Arial", 20, 'normal', 'bold', 'italic'))
    writer.hideturtle()

    #type Greece in both sides

    writer.fd(40)
    writer.fd(140)
    writer.pencolor("white")
    writer.write("GREECE", font=("Arial", 20, 'normal', 'bold', 'italic'))
    writer.fd(-420)
    writer.write("GREECE", font=("Arial", 20, 'normal', 'bold', 'italic'))

def main():
    '''
    Gathering all function into one
    '''

    backround(wn, zach)
    lavaro()
    perimeter()
    cross()
    golden()
    revolution()
    krosia()

main()
wn.exitonclick()

