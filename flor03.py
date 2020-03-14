import turtle
pen = turtle.Turtle()

from funcao_arco import arc

def petala(t, n, angle):
    for i in range(2):
        arc(t, n, angle)
        t.lt(180-angle)

def flor(t, n, r, angle):
    for i in range(n):
        petala(t, r, angle)
        t.lt(360/n)

flor(pen, 20, 150, 20)