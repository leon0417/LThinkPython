import numpy as np


def check_fermat(a, b, c, n):
    if int(a) ** int(n) + int(b) ** int(n) == int(c) ** int(n):
        print('God, Fema is wrong!')
    else:
        print('Fema is right!')

def check_func():
    a = input('please input the first positive integer!\n')
    b = input('please input the second positive integer!\n')
    c = input('please input the third positive integer!\n')
    n = input('please input a positive integer which is larger than 2!\n')
    check_fermat(a, b, c, n)

def is_triangle(a, b, c):
    if a.isdigit() and b.isdigit() and c.isdigit():
        if int(a) + int(b) > int(c) and int(c) + int(b) > int(a) and int(c) + int(a) > int(b):
          print("Yes")
        else:
            print("No")
    else:
        print("one side is not a digit!\n")

def input_triangle():
    a = input("please input the first side!\n")
    b = input("please input the second side!\n")
    c = input("please input the third side!\n")
    is_triangle(a, b, c)

'''Please input a integer larger than 0
'''
def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n - 1, n + s)

import turtle
def draw(t, length, n):
    if n == 0:
        return
    angle = 20
    t.forward(length * n)
    t.left(angle)
    draw(t, length - 1, n - 1)
    t.right(2 * angle)
    draw(t, length - 1, n - 1)
    t.left(angle)
    t.back(length * n)

def draw_koch(t, length):
    if length < 3:
        t.forward( length )
    else:
        t.forward(length / 3)
        t.left(60)
        t.forward(length / 3)
        t.right(120)
        t.forward(length / 3)
        t.left(60)
        t.forward(length / 3)

def snowflake(t, length, n):
    if 0 == n:
        return
    else:
        draw_koch(t, length)
        t.right(120)
        draw_koch(t, length)
        t.left(60)
        draw_koch(t, length)
        t.left(120)
        n = n - 1
        snowflake(t, length, n)
