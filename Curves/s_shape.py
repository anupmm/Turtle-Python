#s shape without using radius or center or circumference
import turtle

# create a turtle object
t = turtle.Turtle()

# set the speed and pen color
t.speed(0)
t.pencolor("black")

iterations = 8
steps = 25
forwards_steps = 30
left_steps = 20

# draw an approximation of a circle using 36 line segments
for i in range(iterations):
    t.backward(steps)
    t.left(steps)    

for i in range(iterations):
    t.right(steps)    
    t.backward(steps)



# hide the turtle cursor
#t.hideturtle()

# wait for the user to close the window
turtle.done()
