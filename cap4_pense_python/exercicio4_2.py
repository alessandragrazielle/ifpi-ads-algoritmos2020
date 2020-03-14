import turtle
pen = turtle.Turtle()

def square(t, length):
    for i in range(4):
        pen.fd(length)
        pen.lt(90)

square(pen, 100)