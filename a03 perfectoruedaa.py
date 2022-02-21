import turtle

wn = turtle.Screen()
wn.bgcolor("light blue")
wn.screensize(500, 500)

ax = turtle.Turtle()


def drawGrass(ax, y):
    for i in range(4):
        ax.forward(y)
        ax.right(90)


def drawSq(ax, t):
    for i in range(4):
        ax.forward(t)
        ax.left(90)


def drawTri(ax, b):
    for i in range(1):
        ax.forward(b)
        ax.left(125)
        ax.forward(b)
        ax.left(115)
        ax.forward(b)


def drawWin(ax, x):
    for i in range(4):
        ax.forward(x)
        ax.left(90)


def drawDoor(ax, g):
    for i in range(1):
        ax.forward(20)
        ax.left(90)
        ax.forward(60)
        ax.left(90)
        ax.forward(20)
        ax.left(90)
        ax.forward(60)


def main():
    ax.penup()
    ax.goto(-320, 20)
    ax.pendown()

    ax.color("green")
    ax.begin_fill()
    drawGrass(ax, 700)
    ax.end_fill()

    ax.color("red")
    ax.penup()
    ax.goto(0, 0)
    ax.pendown()

    ax.begin_fill()
    drawSq(ax, 100)
    ax.end_fill()

    ax.left(90)
    ax.forward(100)
    ax.right(90)
    ax.color("pink")

    ax.begin_fill()
    drawTri(ax, 100)
    ax.end_fill()

    ax.penup()
    ax.right(240)
    ax.goto(20, 70)
    ax.pendown()

    ax.begin_fill()
    drawWin(ax, 20)
    ax.end_fill()

    ax.penup()
    ax.goto(50, 0)
    ax.pendown()

    ax.begin_fill()
    drawDoor(ax, 0)
    ax.end_fill()


main()

wn.exitonclick()
