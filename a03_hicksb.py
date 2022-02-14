#################################################################################
# Author: Blade Hicks
# Username: hicksb
#
# Assignment:  A03: Functional Turtles
# Purpose: In this assignment, you will draw something complex, like a house, animal, or person.
# Google Doc: https://docs.google.com/document/d/1rKh-u9oseQdeVmg3RpVDxT3kmQQx_a31sUUaMfcW8Es/edit?usp=sharing
#
# Works Cited: https://youtu.be/mLUM2Gflf_c , csLab Sunday Night
#################################################################################

import turtle                                  # allows us to use the turtle library
from random import randint                     # import randit fucntion from random library

def first_flower(flower):
    """
    Move to a random location then makes a 5 pedal flower!
    :param flower: a Turtle object
    :return: None
    """
    flower.penup()
    flower.goto(randint(-400, 400), randint(-400, 400))  # goto random location
    flower.up()
    flower.down()
    flower.begin_fill()
    for i in range(5):                                   # loop for making 5 pedal flower
        flower.circle(30, 180)
        flower.right(108)
    flower.end_fill()
    flower.up()


def dot_flower(dotty):
    """
    Move to a random location then makes a Dot flower!
    :param dotty: a Turtle object
    :return: None
    """
    dotty.penup()
    dotty.goto(randint(-300, 300), randint(-300, 300))  # goto random location
    dotty.color("#CF1FF2")
    dotty.up()
    dotty.down()
    dotty.dot(120)
    # makes centre of flower
    dotty.color("#EBF21F")
    dotty.dot(50)
    dotty.up()


def main():
    """
    Draws dot_flower and first_flower at random locations in the window
    :return: None
    """

    wn = turtle.Screen()  # creates a graphics window
    wn.bgpic("This Ramen Is My Girlfriend.png")  # sets background to .png image
    wn.bgcolor("darksalmon")  # sets window background color
    wn.title("nam nam ramyun")  # sets window title

    flower = turtle.Turtle()  # creates a turtle named flower
    # flower.hideturtle()
    turtle.mode("logo")  # sets initial Turtle heading upward(north)
    flower.color("#F21F1F")  # sets flower color
    flower.speed(0)  # sets flower speed to instant

    dotty = turtle.Turtle()  # creates a turtle named dotty
    dotty.hideturtle()  # makes dotty invisible

    for i in range(20):  # loop to draw dot_flower
        dot_flower(dotty)
        for j in range(2):  # nested loop to draw first_flower, twice as many as dot_flower
            first_flower(flower)

    wn.exitonclick()


main()  # call main()
