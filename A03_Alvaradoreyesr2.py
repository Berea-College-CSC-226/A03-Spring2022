# Name: Rodolfo Alvarado
# Username: Alvaradoreyesr2
import turtle
from threading import Thread

wn = turtle.Screen()
house = turtle.Turtle()
door = turtle.Turtle()
wn.bgcolor("light blue")


def border(width,height):
    house.penup()
    house.left(180)
    house.forward(230)
    house.left(90)
    house.forward(100)
    house.left(90)
    house.pendown()
    house.pensize(30)
    for i in range(4):
        house.forward(width)
        house.left(90)
        house.forward(height)
        house.left(90)

def front():
    door.penup()
    door.left(180)
    door.forward(80)
    door.left(90)
    door.forward(100)
    door.left(180)
    door.pendown()
    for i in range(2):
        door.forward(100)
        door.right(90)
        door.forward(30)
        door.right(90)



long = True

while long:
    width = int(input("What width do you want the house to have"))
    if width < 250:
        print("this is too short")
    elif width >700:
        print("house is too long")
    else:
        long = False

tall = True
while tall:
    height = int(input("What height do you want the house to have"))
    if height <250:
        print("house is too short")
    elif height >300:
        print("house is too tall")
    else:
        tall = False




w = border(width,height)
front()


wn.exitonclick()