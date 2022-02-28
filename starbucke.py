
# Ethan Starbuck     starbucke

# https://docs.google.com/document/d/1DhKQbC95RNKwi08EpyYeFsqpdeKcI5szkpRHfpXhmxk/edit?usp=sharing


import turtle
wn = turtle.Screen()
Bruce = turtle.Turtle()
Bruce.speed(0)
turtle.Screen().bgcolor("royal blue")
Bruce.penup()
Bruce.width(300)
Bruce.color("dark green")
Bruce.goto(-390,-200)
Bruce.pendown()
Bruce.forward(900)
Bruce.penup()
Bruce.width(15)
Bruce.color("gray")
# First Building Begin
Bruce.goto(-360, 170)
Bruce.pendown()
Bruce.fillcolor()
def greyBuilding():
    Bruce.color('gray')
    Bruce.begin_fill()
    for greybuilding in range(2):
        Bruce.forward(90)
        Bruce.right(90)
        Bruce.forward(300)
        Bruce.right(90)
    Bruce.end_fill()
Bruce.penup()


greyBuilding()

# Second Building begin
Bruce.goto(-50, 200)
Bruce.pendown()
Bruce.fillcolor()
def blackBuilding():
    Bruce.color('black')
    Bruce.begin_fill()
    for blackBuilding in range(2):
        Bruce.forward(90)
        Bruce.right(90)
        Bruce.forward(300)
        Bruce.right(90)
    Bruce.end_fill()
blackBuilding()

# Third Building begin
Bruce.penup()
Bruce.goto(-230,50)
Bruce.pendown()
Bruce.fillcolor()
def brownBuilding():
    Bruce.color('brown4')
    Bruce.begin_fill()
    for brownbuilding in range (2):
        Bruce.forward(250)
        Bruce.right(90)
        Bruce.forward(150)
        Bruce.right(90)
    Bruce.end_fill()
brownBuilding()

#Third Building end


#Road begin
Bruce.penup()
Bruce.color('black')
Bruce.goto(-400, -200)
Bruce.pendown()
Bruce.begin_fill()
Bruce.forward(800)
Bruce.right(90)
Bruce.forward(80)
Bruce.right(90)
Bruce.forward(800)
Bruce.right(90)
Bruce.forward(80)
Bruce.end_fill()
Bruce.penup()
Bruce.goto(-325, -230)
Bruce.color('yellow')
Bruce.pendown()
Bruce.right(90)
Bruce.forward(50)
Bruce.penup()
Bruce.goto(-200, -230)
Bruce.pendown()
Bruce.forward(50)
Bruce.penup()
Bruce.goto(-75, -230)
Bruce.pendown()
Bruce.forward(50)
Bruce.penup()
Bruce.goto(50, -230)
Bruce.pendown()
Bruce.forward(50)
Bruce.penup()
Bruce.goto(170, -230)
Bruce.pendown()
Bruce.forward(50)
Bruce.penup()
Bruce.goto(280, -230)
Bruce.pendown()
Bruce.forward(50)
Bruce.penup()
#Road end

# Sun
Bruce.goto(350, 300)
Bruce.pendown()
Bruce.dot(110)
Bruce.penup()

# Windows (building 1)
Bruce.width(5)
Bruce.pencolor('white')
Bruce.goto(-345, 150)
Bruce.pendown()
Bruce.right(90)
Bruce.forward(15)
Bruce.left(90)
Bruce.forward(15)
Bruce.left(90)
Bruce.forward(15)
Bruce.left(90)
Bruce.forward(15)
Bruce.penup()


Bruce.goto(-290, 135)
Bruce.pendown()
Bruce.right(90)
Bruce.forward(15)
Bruce.left(90)
Bruce.forward(15)
Bruce.left(90)
Bruce.forward(15)
Bruce.left(90)
Bruce.forward(15)
Bruce.penup()

Bruce.goto(-345, 100)
Bruce.pendown()
Bruce.right(90)
Bruce.forward(15)
Bruce.left(90)
Bruce.forward(15)
Bruce.left(90)
Bruce.forward(15)
Bruce.left(90)
Bruce.forward(15)
Bruce.penup()

Bruce.goto(-305, 85)
Bruce.pendown()
def windowSquare4():
    for windows4 in range(4):
        Bruce.right(90)
        Bruce.forward(15)

windowSquare4()

Bruce.penup()
Bruce.goto (-345, 35)
Bruce.pendown()
windowSquare4()
Bruce.penup()

Bruce.goto(-305, 35)
Bruce.pendown()
windowSquare4()
Bruce.penup()

Bruce.goto(-345, -15)
Bruce.pendown()
windowSquare4()
Bruce.penup()

Bruce.goto(-305, -15)
Bruce.pendown()
windowSquare4()
Bruce.penup()

# Door
Bruce.goto(-325, -130)
Bruce.pencolor('black')
Bruce.width(3)
Bruce.pendown()
Bruce.fillcolor('black')
def drawDoor():
    Bruce.begin_fill()
    for blackdoor in range (2):
        Bruce.right(90)
        Bruce.forward(23)
        Bruce.right(90)
        Bruce.forward(15)
    Bruce.end_fill()
drawDoor()
Bruce.penup()

#Building 2 windows
Bruce.goto(-200, 30)
Bruce.pencolor('white')
Bruce.pendown()
windowSquare4()
Bruce.penup()

Bruce.goto(-150, 30)
Bruce.pendown()
windowSquare4()
Bruce.penup()

Bruce.goto(-200, -15)
Bruce.pendown()
windowSquare4()
Bruce.penup()

Bruce.goto(-150, -15)
Bruce.pendown()
windowSquare4()
Bruce.penup()

Bruce.goto(-200, -65)
Bruce.pendown()
windowSquare4()
Bruce.penup()

Bruce.goto(-150, -65)
Bruce.pendown()
windowSquare4()
Bruce.penup()

# Door 2
Bruce.goto(-20,- 107)
Bruce.pencolor('black')
Bruce.width(2)
Bruce.pendown()
Bruce.fillcolor('gray')
drawDoor()

Bruce.penup()


wn.exitonclick()

