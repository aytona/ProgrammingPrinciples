# Programming Principles: Quiz 1
# By: Christopher Aytona
import turtle

# Create the screen object
wn = turtle.Screen()
wn.bgcolor("green")

# Initialize the turtle shape and color
a_turtle = turtle.Turtle(shape='turtle')
a_turtle.color("lightyellow")

# Initialize the first side distance
step_amount = 50

# Set the angle of each side of the shape
angle = 360/8

# Number of shapes
for x in range(3):
    # Number of sides per shape
    for i in range(8):
        # Move the turtle using the set amount of distance
        a_turtle.forward(step_amount)
        # Turn the turtle to face the next side
        a_turtle.left(angle)
        # Increment the distance for the next side
        step_amount = step_amount + 5

# Exit the program
wn.exitonclick()
