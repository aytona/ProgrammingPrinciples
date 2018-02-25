# Q2 version (100%) Christopher Aytona
# This program will create a number of filled in flags using user specified amount
# and have the flags be in a user specified colour
import turtle

def createScreen(colour):
    """This fruitful function takes in a string parameter
    for the background colour of the screen
    then returns the screen object"""
    wn = turtle.Screen()
    wn.bgcolor(colour)
    return wn

def createFlags(turtle, amount):
    """This procedure takes in the turtle object being used to draw,
    and the amount of flags to be created"""
    angle = 360 / amount      
    for i in range(amount):
        turtle.forward(100)
        createSquare(turtle, 50)
        turtle.goto(0,0)
        turtle.left(angle)

def createSquare(turtle, distance):
    """This procedure takes in the turtle object used to draw,
    and the distance on how big the flag is.
    It is used to create the filled in flag"""
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(distance)
        turtle.left(90)
    turtle.end_fill()

def createTurtle(colour):
    """This fruitful function takes in the colour used to change the colour of the turtle,
    and returns the turtle object"""
    a_turtle = turtle.Turtle(shape='turtle')
    a_turtle.color(colour)
    return a_turtle

def main():
    screenColour = input('Colour of the screen: ')
    turtleColour = input('Colour of the turtle: ')
    flagAmount = int(input('Number of flags: '))
    wn = createScreen(screenColour)
    a_turtle = createTurtle(turtleColour)
    createFlags(a_turtle, flagAmount)
    wn.exitonclick()

main()
