import turtle
pen = turtle.Turtle()
import math


def triangulo(t, length, angle):
    x = length * math.sin(angle/2 * math.pi / 180) * 2

    t.rt(angle/2)
    t.fd(length)
    t.lt(90+angle/2)
    t.fd(x)      
    t.lt(90+angle/2)
    t.fd(length)
    t.lt(180-angle/2)


def torta(t, n, length):
    angle = 360/n
    for i in range(n):
        triangulo(t, length, angle)
        t.lt(angle)


torta(pen, 5, 100)