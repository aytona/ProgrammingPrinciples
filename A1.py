# This program will draw a sine wave using
# user inputed amplitude and frequency amount
# Programming Principles: Assignment 1
# By: Christopher Aytona

import turtle
import math

# Amplitude and frequency inputs
amp = int(input('Amplitude amount: '))
fre = int(input('Frequency amount: '))

# Screen object
wn = turtle.Screen()
wn.bgcolor("lightyellow")
# Setting the window coordinates to make things look better
# Using the amplitude as the min and max coord
wn.setworldcoordinates(0, -amp, 361, amp)

# Turtle object
a_turtle = turtle.Turtle(shape='turtle')

# Iterates through all 360 degrees
for x in range(361):
    # Finding the y-coordinates using the y = sin(x)
    y = amp * math.sin(math.radians(x * fre))
    # Move the turtle along the x with the new y
    a_turtle.goto(x, y)

# Exit the program
wn.exitonclick()
