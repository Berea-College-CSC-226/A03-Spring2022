# Author: Bel Marquez
# Username: marquezi
# doc link: https://docs.google.com/document/d/1_EXnlOKNuuyA2cMfBd394FCZ9XTOVqiyUJnW-9D36Qg/edit?usp=sharing

import turtle

wn = turtle.Screen()
wn.bgcolor("#A5BF8B")

mount = turtle.Turtle()
house = turtle.Turtle()
roof = turtle.Turtle()
text = turtle.Turtle()
window = turtle.Turtle()

def main():
    def drawMount(turtle,length):
        mount.goto(-300,0)
        mount.fillcolor("#77905F")
        mount.begin_fill()
        for i in range(3):
            mount.fd(length)
            mount.left(120)

        mount.penup()
        mount.goto(-200, 0)
        mount.pendown()

        for i in range(3):
            mount.fd(length)
            mount.left(120)
        mount.penup()
        mount.goto(-150, 0)
        mount.pendown()

        for i in range(3):
            mount.fd(length)
            mount.left(120)
        mount.penup()
        mount.goto(0, 0)
        mount.pendown()
        mount.end_fill()

    drawMount(mount, 200)

    def drawhouse(t,length):
        house.penup()
        house.goto(100, 0)
        house.pendown()
        house.fillcolor("#D6E167")
        house.begin_fill()

        for i in range(4):
            house.fd(length)
            house.left(90)
        house.end_fill()
    drawhouse(house, 100)

    def drawroof(t,length):
        roof.penup()
        roof.goto(100, 100)
        roof.pendown()
        roof.fillcolor("#E1C967")
        roof.begin_fill()

        for i in range(3):
            roof.fd(length)
            roof.left(120)
        roof.end_fill()
    drawroof(roof, 100)

    def windows():
        window.penup()
        window.goto(110,20)
        window.pendown()
        for i in range(4):
            window.fd(15)
            window.left(90)
        window.penup()
        window.goto(175, 20)
        window.pendown()
        for i in range(4):
            window.fd(15)
            window.left(90)
        window.penup()
        window.goto(175, 50)
        window.pendown()
        for i in range(4):
            window.fd(15)
            window.left(90)
        window.penup()
        window.goto(110, 50)
        window.pendown()
        for i in range(4):
            window.fd(15)
            window.left(90)
    windows()

    text.penup()
    text.goto(120,110)
    text.pendown()
    text.write("Do not Enter")

main()





wn.exitonclick()