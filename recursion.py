import turtle

putani = turtle.Turtle()
putani.getscreen().bgcolor("#994444")
putani.penup()
putani.goto((-200,100))
putani.pendown()

def star(turtle, size):
	if size <= 10:
		return
	else:
		turtle.begin_fill()
		for i in range(5):

			turtle.forward(size)
			star(turtle, size/3)
			turtle.left(216)
		turtle.end_fill()

star(putani, 360)

turtle.done()

