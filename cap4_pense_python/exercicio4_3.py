import turtle
pen = turtle.Turtle()

def polygon(t, length, n):
    for i in range(n):
        pen.fd(length)
        pen.lt(360/n)

polygon(pen, 100, 6)