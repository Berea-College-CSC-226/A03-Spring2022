import turtle
wn = turtle.Screen()

#changes background color
wn.bgcolor("lightblue")

#turtle name


#starting code picture
def turtle_grass():
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.forward(350)
    t.right(90)
    t.forward(150)
    t.right(90)

    #makes the grass
    t.pendown()
    t.pensize(200)
    t.pencolor("green")
    for i in [0, 1,]:
        t.forward(700)
        t.left(90)
        t.forward(150)
        t.left(90)
    t.goto(500, -500)

#new turtle to build house
def turtle_house():
    tu = turtle.Turtle()
    tu.speed(0)
    tu.penup()
    tu.goto(-100,100)
    tu.pendown()
    #house
    tu.fillcolor("red")
    tu.begin_fill()
    for x in [0, 1, 2 ,3]:
        tu.right(90)
        tu.forward(200)
    tu.end_fill()
    tu.forward(5)

    # roof
    tu.fillcolor("brown")
    tu.begin_fill()
    tu.left(135)
    for t in range(2):
        tu.forward(150)
        tu.left(90)
    tu.left(45)
    tu.forward(150)
    tu.end_fill()

    #door
    tu.penup()
    tu.goto(-230,0)
    tu.pendown()
    tu.fillcolor()
    tu.begin_fill()
    for d in [0, 1]:
        tu.forward(50)
        tu.right(90)
        tu.forward(100)
        tu.right(90)
    tu.end_fill()
    tu.penup()

    #left side window
    tu.left(90)
    tu.forward(30)

    tu.fillcolor("lightgray")
    tu.begin_fill()
    for w in range(4):
        tu.forward(50)
        tu.left(90)

    tu.penup()
    tu.right(90)
    tu.forward(55)
    #right side window
    for w in range(4):
        tu.forward(50)
        tu.left(90)
    tu.end_fill()

    #window lines
    tu.pendown()
    tu.pencolor("black")
    for i in range(4):
        tu.forward(50)
        tu.left(90)
    tu.forward(25)
    tu.left(90)
    tu.forward(50)
    tu.left(90)
    tu.forward(25)
    tu.left(90)
    tu.forward(25)
    tu.left(90)
    tu.forward(50)

    #window lines on left side

    tu.penup()
    tu.forward(-155)
    tu.right(90)
    tu.forward(25)
    tu.left(90)
    tu.pendown()
    for i in range(4):
        tu.forward(50)
        tu.left(90)
    tu.forward(25)
    tu.left(90)
    tu.forward(50)
    tu.left(90)
    tu.forward(25)
    tu.left(90)
    tu.forward(25)
    tu.left(90)
    tu.forward(50)

    #door knob
    tu.penup()
    tu.right(90)
    tu.forward(105)
    tu.left(90)
    tu.forward(37)
    tu.pensize(7)
    tu.pendown()
    tu.forward(1)
    tu.penup()
    tu.goto(-500, -500)


#making the dog
def turtle_dog():
    dog = turtle.Turtle()
    dog.speed(0)
    dog.pencolor("brown")
    dog.penup()
    #head
    dog.goto(0,-100)
    dog.pendown()
    dog.pensize(25)
    dog.forward(15)
    dog.left(90)
    dog.forward(5)
    dog.right(90)
    dog.pensize(35)
    dog.forward(5)

    #body
    dog.penup()
    dog.right(90)
    dog.forward(25)
    dog.left(90)
    dog.forward(5)
    dog.pendown()
    dog.forward(70)

    #tail
    dog.pensize(13)
    dog.left(45)
    dog.forward(40)

    #ear
    dog.penup()
    dog.goto(20,-85)
    dog.pendown()
    dog.pencolor("black")
    dog.right(115)
    dog.forward(20)

    #nose
    dog.penup()
    dog.goto(-8,-93)
    dog.pendown()
    dog.pensize(7)
    dog.forward(1)
    dog.penup()
    dog.forward(40)

    #legs
    dog.left(70)
    dog.pencolor("brown")
    dog.pensize(13)
    dog.forward(15)
    dog.pendown()

    for d in [0, 1]: #front legs
        dog.right(90)
        dog.forward(40) #leg down
        dog.right(180)
        dog.forward(40)#leg up
        dog.right(90)
        dog.forward(15)

        #back legs
    dog.forward(35)
    dog.right(90)
    dog.forward(40) #leg down
    dog.right(180)
    dog.forward(40)#leg up
    dog.right(90)
    dog.forward(15)

    dog.right(90)
    dog.forward(40) #leg down
    dog.right(180)
    dog.forward(40)#leg up

    dog.penup()
    dog.goto(0,-500)

#dog house
def turtle_doghouse():
    dh = turtle.Turtle()
    dh.penup()
    dh.speed(0)
    dh.goto(200, -175)
    dh.pendown()

    dh.fillcolor("navyblue")
    dh.begin_fill()
    for d in range(2):
        dh.forward(150)
        dh.left(90)
        dh.forward(100)
        dh.left(90)
    dh.end_fill()
    dh.penup()

    #dog house roof
    dh.left(90)
    dh.forward(100)
    dh.pendown()


    dh.fillcolor("saddlebrown")
    dh.begin_fill()
    dh.left(90)
    dh.forward(15)
    dh.right(125)
    dh.forward(70)
    dh.right(55)
    dh.forward(100)
    dh.right(55)
    dh.forward(70)
    dh.right(125)
    dh.forward(160)
    dh.end_fill()

    #ball
    dh.penup()
    dh.pencolor("yellow")
    dh.left(90)
    dh.forward(105)
    dh.right(90)
    dh.forward(30)
    dh.pensize(20)
    dh.pendown()
    dh.forward(1)

    dh.pencolor("lime")
    dh.pensize(5)
    dh.forward(8)
    dh.forward(-17)
    dh.penup()
    dh.goto(-500, -500)

#sun
def turtle_sun():
    sun = turtle.Turtle()
    sun.penup()
    sun.speed(0)
    sun.goto(330, 300)
    sun.pendown()
    sun.pencolor("yellow")
    sun.pensize(150)
    sun.forward(1)

    #sun rays
    sun.pensize(25)
    sun.penup()
    sun.forward(15)
    sun.right(90)
    sun.forward(90)
    sun.pendown()
    sun.forward(30)
    sun.penup()
    sun.forward(-50)

    for s in range(3):
        sun.right(90)
        sun.forward(50)
        sun.left(60)
        sun.forward(15)
        sun.pendown()
        sun.forward(30)
        sun.penup()
        sun.forward(-50)
    sun.penup()
    sun.goto(500,500)



def main():
    turtle_grass()
    turtle_house()
    turtle_dog()
    turtle_doghouse()
    turtle_sun()

    wn.exitonclick()

main() #done