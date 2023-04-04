import turtle
from turtle import *
import sys

#turtle.bye()

def draw_curve(curve_type, iterations, steps):
    curve_type = turtle.textinput(None, "Enter the type of curve (c: circle, s: s shape or a: arc): ")
    iterations = int(turtle.numinput(None, "Enter the number of iterations: "))
    steps = int(turtle.numinput(None, "Enter the step size: "))

    # create a turtle object
    t = turtle.Turtle()

    # set the speed and pen color
    t.speed(0)
    t.pencolor("black")

    # draw the curve based on the input type
    if curve_type == "c":
        # draw an approximation of a circle using 36 line segments
        for i in range(36):
            t.forward(steps)
            t.left(steps)

    elif curve_type == "s":
        # draw an approximation of an S shape using 16 line segments
        for i in range(iterations):
            t.backward(steps)
            t.left(steps)

        for i in range(iterations):
            t.right(steps)
            t.backward(steps)
    elif curve_type == 'a':
        # draw an approximation of an using steps line segments
        for i in range(iterations):
            t.backward(steps)
            t.left(steps)    

    else:
        print("Invalid curve type.")

    # hide the turtle cursor
    #t.hideturtle()

    # wait for the user to close the window
    turtle.done()


draw_curve(None, None, None)