# This program creates a turtle random pathing
# until it reaches out of bounds of the screen
import turtle, random

def create_window(colour="white"):
    wn = turtle.Screen()
    wn.bgcolor(colour)
    wn.colormode(255)
    return wn

def create_turtle(new_shape="turtle", colour="black", speed="normal"):
    new_turtle = turtle.Turtle()
    new_turtle.shape(new_shape)
    new_turtle.color(colour)
    new_turtle.speed(speed)
    return new_turtle

def random_colour():
    return (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))

def turtle_pathing(bounds, turt):
    inbound = True
    while inbound:
        if (turt.xcor() > bounds[0] or turt.xcor() < -bounds[0]) or (turt.ycor() > bounds[1] or turt.ycor() < -bounds[1]):
            inbound = False
        random_direction = random.randrange(0, 3)
        if random_direction == 1:
            turt.left(90)
        elif random_direction == 2:
            turt.right(90)
        turt.forward(random.randrange(0, 101))
    turt.hideturtle()

def turtle_loop(bounds, number):
    while number > 0:
        my_turtle = create_turtle(colour=random_colour())
        turtle_pathing(bounds, my_turtle)
        number -= 1

def main():
    display = create_window()
    turtle_number = int(input("Number of turtles: "))
    screen_bounds = (display.window_width()/2, display.window_height()/2)
    turtle_loop(screen_bounds, turtle_number)
    display.exitonclick()

main()
