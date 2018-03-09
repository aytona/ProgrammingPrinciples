# This program draws patterns using Turtle
import turtle

def makeScreen():
    m_wn = turtle.Screen()
    return m_wn

def makeTurtle(n_colour, n_shape='turtle', n_size=1, n_initPos=(0,0)):
    m_turtle = turtle.Turtle(shape=n_shape)
    m_turtle.color(n_colour)
    m_turtle.pensize(n_size)
    m_turtle.penup()
    m_turtle.goto(n_initPos[0], n_initPos[1])
    m_turtle.pendown()
    return m_turtle

def flowerPattern(turt):
    for i in range(24):
        turt.right(15)
        for x in range(36):
            turt.left(10)
            turt.forward(15)

def spiralPattern(turt):
    for distance in range(100):
        turt.forward(distance)
        turt.left(20)

def spiralSticksPattern(turt):
    turt.begin_fill()
    for n in range(8):
        for i in range(2):
            turt.forward(100)
            turt.left(90)
            turt.forward(10)
            turt.left(90)
        turt.left(45)
    turt.end_fill()

def main():
    wn = makeScreen()
    flowerTurt = makeTurtle('blue', n_initPos=(-250, 250))
    flowerPattern(flowerTurt)
    spiralTurt = makeTurtle('red', n_initPos=(250, 250))
    spiralPattern(spiralTurt)
    stickTurt = makeTurtle('green', n_initPos=(0, -100))
    spiralSticksPattern(stickTurt)
    wn.exitonclick()

main()