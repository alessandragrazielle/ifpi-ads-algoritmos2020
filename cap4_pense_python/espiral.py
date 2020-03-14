import turtle
pen = turtle.Turtle()

from funcao_arc import arc


def posicao():
    pen.lt(90)
    pen.penup()
    pen.fd(50)
    pen.pendown() 
    pen.rt(90)


def circle():
    pen.circle(200)
    posicao()

    pen.circle(150)
    posicao()

    pen.circle(100)
    posicao()

    pen.circle(50)
    posicao()


def linha_1():
    pen.rt(90)
    pen.fd(200)
    pen.lt(180)
    pen.fd(400)
    pen.lt(180)
    pen.fd(200)


def linha_2():
    pen.rt(45)
    pen.fd(200)
    pen.lt(180)
    pen.fd(400)
    pen.lt(180)
    pen.fd(200)
    pen.rt(90)
    pen.fd(200)
    pen.lt(180)
    pen.fd(400)
    pen.lt(180)
    pen.fd(200)
    pen.rt(135)


def espiral():
    pen.color('orange')
    pen.pensize(3)
    arc(pen, 25, 180)
    arc(pen, 50, 90)
    arc(pen, 75, 180)
    arc(pen, 125, 180)
    arc(pen, 175, 180)


def main():
    circle()
    for i in range(2):
        linha_1()
    linha_2()
    espiral()
    


main()


turtle.mainloop()
