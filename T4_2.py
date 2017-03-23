import turtle
import numpy as np
# draw a poly line
# t is a turtle, n controls times of turning, length is distance of moving, dir is turning direction
def poly_line(t, n, length, angle):
    for i in range(n):
        t.forward(length)
        t.right(angle)
# draw a leaf
# t is a turtle, r is the radius of the arc, arcAngle is the center angle of arc, leafDir is direction of leaf
def draw_one_leaf(t, r, arcAngle):
    length = 2 * np.pi * r * arcAngle / 360
    n = int(length / 4) + 1
    step_length = length / n
    step_angle = arcAngle / n
    poly_line(t, n, step_length, step_angle)
    t.right(180.0 - arcAngle)
    poly_line(t, n, step_length, step_angle)
    t.right(180.0 - arcAngle)
'''draw one flower
t is a turtle
n is the number of flower leaf
'''
def draw_flower(t, r, arcAngle, n):
    for i in range(n):
        draw_one_leaf(t, r, arcAngle)
        t.right(360 / n)
