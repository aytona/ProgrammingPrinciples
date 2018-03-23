# Programming Principles Quiz 3
# By: Christopher Aytona
# This program exercises the while, if, and else operators
# And knowledge of the turtle and random module
import turtle, random

def create_turtle(m_colour="black", m_shape="turtle", m_speed="normal", m_loc=(0.0, 0.0)):
    """Returns a turtle object using default param values"""
    new_turtle = turtle.Turtle(shape=m_shape)
    new_turtle.color(m_colour)
    new_turtle.speed(m_speed)
    new_turtle.penup()
    new_turtle.goto(m_loc)
    new_turtle.pendown()
    return new_turtle

def create_screen(m_colour="lightyellow"):
    """Returns the screen using default param value"""
    m_wn = turtle.Screen()
    m_wn.bgcolor(m_colour)
    return m_wn

def random_sizing(m_turtle, m_coord):
    """Randomly resizes the turtle from size 1 to 6,
    until it reaches the target y-coordination"""
    while m_turtle.ycor() != m_coord:
        m_turtle.sety(m_turtle.ycor() - 1)
        m_turtle.shapesize(random.randrange(1, 7))
    write_evaluation(m_turtle)

def size_evaluation(m_turtle, m_target_size):
    """Evaluates the turtle's size,
    if it's greater than the target size it'll return True, else it returns False"""
    if m_turtle.shapesize() > m_target_size:
        return True
    return False

def write_evaluation(m_turtle):
    """Writes out the turtle size at the moment of evaluation"""
    m_turtle.write("Turtle size: {}".format(m_turtle.shapesize()), align="right", font=("Arial", 10, "normal"))

def triangle_evaluation(m_turtle):
    """Draws a triangle until the desired size is achieved"""
    while size_evaluation(m_turtle, (3,3)):
        sides = 3
        while sides > 0:
            m_turtle.forward(50)
            m_turtle.right(360/3)
            sides -= 1
        m_turtle.shapesize(random.randrange(1, 7))

def main():
    # Initializing the screen and turtle
    wn = create_screen()
    # First screenshot
    a_turtle = create_turtle(m_loc=(-300, 240))
    # Second screenshot
    a_turtle.goto(0, 240)
    a_turtle.color("blue")
    # Third screenshot
    a_turtle.goto(290, 240)
    a_turtle.right(90)
    # Fourth screenshot
    random_sizing(a_turtle, 0)
    a_turtle.color("red" if size_evaluation(a_turtle, (3,3)) else "green")
    # Fifth screenshot
    random_sizing(a_turtle, -240)
    a_turtle.right(90)
    # Sixth screenshot
    triangle_evaluation(a_turtle)
    # Seventh screenshot
    a_turtle.goto(-300, -240)
    wn.exitonclick()
    
main()