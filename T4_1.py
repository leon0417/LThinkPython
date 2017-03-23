import turtle
import numpy as np

def square(t, length):
    t.showturtle()
    for i in range(4):
        t.forward(length)
        t.right(90)

def polygon(t, length, n, angle):
    t.showturtle()
    for i in range(n):
        t.forward(length)
        t.delay = 0.01
        t.right(360 / n)
        if i > angle:
            break;

def circle(t, r, angle):
    t.showturtle()
    length = 2 * np.pi * r
    polygon(t, length / 360, 360, angle)

def arc(t, r, angle):
    t.showturtle()
    length = 2 * np.pi * r
    circle(t, r, angle)