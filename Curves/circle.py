#circle without using radius or center or circumference
import turtle

# create a turtle object
t = turtle.Turtle()

# set the speed and pen color
t.speed(0)
t.pencolor("black")

iterations = 36
steps = 10

# draw an approximation of a circle using 36 line segments
for i in range(iterations):
    t.forward(steps)
    t.left(steps)

# hide the turtle cursor
t.hideturtle()

# wait for the user to close the window
turtle.done()
