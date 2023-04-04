import turtle

putani = turtle.Turtle()

putani.color("blue", "cyan")

# Square
putani.begin_fill()
putani.forward(100)
putani.setheading(90)
putani.forward(100)
putani.setheading(180)
putani.forward(100)
putani.setheading(270)
putani.forward(100)
putani.end_fill()

putani.penup()
putani.setheading(270)
putani.forward(120)
putani.pendown()

putani.begin_fill()
putani.setheading(0)
putani.forward(100)
putani.setheading(90)
putani.forward(100)
putani.setheading(180)
putani.forward(100)
putani.setheading(270)
putani.forward(100)
putani.end_fill()

turtle.done()