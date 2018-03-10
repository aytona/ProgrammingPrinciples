# By: Christopher Aytona
# Programming Principles Midterm
import turtle, random

def makeScreen(screen_colour):
    """This function creates the window using a string param for colour"""
    _wn = turtle.Screen()
    _wn.bgcolor(screen_colour)
    return _wn

def makeTurtle(turtle_colour, turtle_shape='turtle'):
    """This function creates the turtle object using the turtle shape as default shape"""
    new_turtle = turtle.Turtle(shape=turtle_shape)
    new_turtle.color(turtle_colour)
    return new_turtle

def makeShape(turt, side_amount):
    """This function creates a shape that has a certain amount of sides"""
    side_counter = side_amount
    while side_counter > 0:
        turt.forward(100)
        turt.left(360/side_amount)
        side_counter -= 1

def main():
    a_turtle = makeTurtle(input("Turtle colour: "))  # Creating the turtle
    wn = makeScreen(input("Colour of the screen: "))  # Creating the window
    shapes_drawn = [0, 1, 2, 3]  # Checker to see if all shapes has been drawn
    cont = "y"  # Checker to see if the user wants to continue
    while len(shapes_drawn) > 0 or cont == "y":
        # Random number generation between 0 and 3
        randNum = random.randrange(0, 4)
        # If the random number is in the shape checker, remove it (check it off)
        if randNum in shapes_drawn:
            shapes_drawn.remove(randNum)
        # Uses the random number generated to draw certain shapes
        if randNum == 0:
            makeShape(a_turtle, 3)
        elif randNum == 1:
            makeShape(a_turtle, 4)
        elif randNum == 2:
            makeShape(a_turtle, 5)
        else:
            makeShape(a_turtle, 8)
        # If all shapes has been drawn, ask the user if they still want to continue
        if len(shapes_drawn) == 0:
            print("Congratulations! All shapes has been drawn!")
            cont = input("Would you still like to continue? (Y/N): ").lower()
    print('Click on the screen to close')
    wn.exitonclick()

main()