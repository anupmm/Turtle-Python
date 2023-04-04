import turtle
import math
import random

putani = turtle.Turtle()
turtle.colormode(255)
putani.speed(10)

for i in range(2000):
	putani.forward(10)
	putani.left(math.sin(i/10)*25)
	putani.left(20)

turtle.done()

