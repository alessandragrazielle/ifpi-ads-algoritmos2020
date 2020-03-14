import turtle
pen = turtle.Turtle()


def polygon(t, length, n):
    for i in range(n):
        pen.fd(length)
        pen.lt(360/n)

def circle(t, r):
    circumference = 2 * 3.14 * r
    n = int(circumference/3)
    length = circumference / n
    polygon(pen, length, n)

circle(pen, 100)