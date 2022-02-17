import turtle

def head0(head):
    'Draw head of person'
    head.penup()
    head.showturtle()
    head.setpos(0,150)
    head.fillcolor(255,160,122)
    head.begin_fill()
    head.circle(80)
    head.end_fill()
def body0(body):
     'Draw body of person'
     body.penup()
     body.setpos(70,0)
     body.pendown()
     body.begin_fill()
     body.fillcolor(125,0,125)
     for i in range(3):
         body.left(90)
         body.forward(150)
     body.end_fill()
def arms0(arm_1,arm_2):
    'Draw arms of person'

    arm_1.goto(-100,150)
    arm_1.fillcolor(225,160,122)
    arm_1.begin_fill()
    arm_1.left(220)
    arm_1.forward(200)
    arm_1.end_fill
    arm_2.goto(100, 150)
    arm_2.fillcolor(225, 160, 122)
    arm_2.begin_fill()
    arm_2.right(70)
    arm_2.forward(150)
    arm_2.end_fill

def legs0(leg_1,leg_2):
    'Draw legs of person'
    leg_1.setpos(70,0)
    for i in range(4):
        leg_1.begin_fill()
        leg_1.fillcolor(0, 0, 200)
        leg_1.right(90)
        leg_1.forward(200)
        leg_1.right(90)
        leg_1.forward(50)
        leg_1.end_fill()
    leg_2.setpos(-30,0)
    for i in range(4):
        leg_2.begin_fill()
        leg_2.fillcolor(0, 0, 0)
        leg_2.right(90)
        leg_2.forward(200)
        leg_2.right(90)
        leg_2.forward(50)
        leg_2.end_fill()
def feet0(foot_1, foot_2):
     "Draw feet of person"
     foot_1.setpos(-60, -250)
     foot_1.fillcolor(125,0,125)
     foot_1.begin_fill()
     foot_1.circle(30)
     foot_1.end_fill()
     foot_2.setpos(40, -250)
     foot_2.fillcolor(125, 0, 125)
     foot_2.begin_fill()
     foot_2.circle(30)
     foot_2.end_fill()
def hair0(hair):
    "Draw hair on person"
    hair.setpos(-10,150)
    for i in range(65):
        hair.begin_fill()
        hair.fillcolor(255, 255, 0)
        hair.forward(12.5)
        hair.left(6)
        hair.end_fill()

def main():
    wn = turtle.Screen()
    wn.bgcolor("green")
    wn.colormode(255)
    head = turtle.Turtle()
    arm_1 = turtle.Turtle()
    arm_2 = turtle.Turtle()
    body = turtle.Turtle()
    leg_1 = turtle.Turtle()
    leg_2 = turtle.Turtle()
    foot_1 = turtle.Turtle()
    foot_2 = turtle.Turtle()
    hair = turtle.Turtle()
    head.pensize(10)
    head.speed(10)
    arm_1.speed(10)
    arm_2.speed(10)
    body.speed(10)
    leg_1.speed(10)
    leg_2.speed(10)
    foot_1.speed(10)
    foot_2.speed(10)
    hair.speed(10)
    head0(head)
    arms0(arm_1,arm_2)
    body0(body)
    legs0(leg_1,leg_2)
    feet0(foot_1, foot_2)
    hair0(hair)
    wn.exitonclick()
main()
