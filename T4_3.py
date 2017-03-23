import turtle
import numpy as np

def draw_isosceles_triangle(t, slength, sangle):
    oangle = (180 - sangle) / 2
    olength = slength / np.sin( oangle * np.pi / 180 ) * np.sin( sangle * np.pi / 180 )
    t.forward(slength)
    t.speed(0.01)
    t.right(180 - oangle)
    t.forward(olength)
    t.right(180 - oangle)
    t.forward(slength)

def draw_poly(t, slength, n):
    step_angle = 360 / n
    for i in range(n):
        draw_isosceles_triangle(t, slength, step_angle)
        t.right(180)
