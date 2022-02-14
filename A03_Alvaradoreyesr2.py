# Name: Rodolfo Alvarado
# Username: Alvaradoreyesr2
import turtle
from threading import Thread
import time

wn = turtle.Screen()
house = turtle.Turtle()
door = turtle.Turtle()
nob = turtle.Turtle()
newin = turtle.Turtle()
wn.bgcolor("#3776ab")
wn.bgpic("background.gif")




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
    door.forward(85)
    door.left(180)
    door.pendown()
    door.fillcolor("brown")
    door.begin_fill()
    for i in range(2):
        door.forward(100)
        door.right(90)
        door.forward(30)
        door.right(90)
    door.end_fill()
    frontnob()

def frontnob():
    nob.penup()
    nob.color("grey")
    nob.left(180)
    nob.forward(70)
    nob.left(90)
    nob.forward(40)

def createwindow():
    newin.penup()
    newin.left(180)
    newin.forward(150)
    newin.right(90)
    newin.forward(50)
    newin.right(90)
    newin.pendown()
    for i in range(2):
        newin.left(90)
        newin.forward(50)
        newin.left(90)
        newin.forward(50)
    for i in range(2):
        newin.right(-135)
        newin.forward(71)
        newin.left(135)
        newin.forward(50)







def main():
    long = True

    while long:
        width = int(input("What width do you want the house to have"))
        if width < 250:
            print("this is too short")
        elif width > 700:
            print("house is too long")
        else:
            long = False

    tall = True
    while tall:
        height = int(input("What height do you want the house to have"))
        if height < 250:
            print("house is too short")
        elif height > 300:
            print("house is too tall")
        else:
            tall = False
    Thread(target=border(width, height)).start()
    Thread(target= front).start()
    Thread(target = createwindow).start()

if __name__ == '__main__':
    main()



wn.exitonclick()