#1

import turtle
bob = turtle.Turtle()
john = turtle.Turtle()
print(bob)
print(john)

def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)
        
square(bob)
square(john)
turtle.mainloop()

#2

import turtle
bob = turtle.Turtle()
john = turtle.Turtle()
print(bob)
print(john)

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
        
square(bob, 50)
square(john, 100)
turtle.mainloop()

#3

import turtle
bob = turtle.Turtle()
john = turtle.Turtle()
print(bob)
print(john)

# n-sided polygon
def polygon(t, n, length):
    for i in range(n):
        t.fd(length)
        t.lt(360 / n)
        
polygon(bob, 4, 50)
polygon(john, 5, 100)
turtle.mainloop()

# 4

import turtle
import math
bob = turtle.Turtle()
john = turtle.Turtle()
print(bob)
print(john)

# n-approximate polygon-circle
def polygon(t, r, n):
    for i in range(n):
        t.fd((2 * math.pi * r) / n)
        t.lt(360 / n)
        
polygon(bob, 100, 50)
polygon(john, 100, 100)
turtle.mainloop()
