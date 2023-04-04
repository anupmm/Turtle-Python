import turtle
import math
import random

putani = turtle.Turtle()
turtle.colormode(255)
putani.speed(10)

for i in range(2000):
	putani.forward(math.sqrt(i))
	putani.left(i%180)

turtle.done()