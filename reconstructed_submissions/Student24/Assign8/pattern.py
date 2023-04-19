# @@@@@@@@@@@@
# CS1400 - MW1
# Assignment 8

# Import necessary modules
import turtle
import random

# Define the reset function with no parameters
def reset():
# Reset used parameters
	centerX = ""
	centerY = ""
	offset = ""
	height = ""
	width = ""
	count = ""
	rotation = ""
	radius = ""
# Reset the turtle
	turtle.clear()

# Define setup function with no parameters
def setup():
# Speedy turtle
	turtle.speed(0)
# Turtle window size
	turtle.setup(1000, 800)

# Define drawRectanglePattern function with appropriate parameters
def drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation):
	for i in range(count):
# Define parameters for use in drawRectangle function before calling
		centerX = centerX 
		centerY = centerY 
		offset = offset
		height = height
		width = width
		count = count
		rotation = rotation + (360 / count)
		drawRectangle(centerX, centerY, offset, width, height, rotation)

# Define drawRectangle function with appropriate parameters
def drawRectangle(centerX, centerY, offset, width, height, rotation):
	turtle.pu()
	turtle.color(setRandomColor())
	turtle.goto(centerX, centerY)
	turtle.setheading(360 - rotation)
	turtle.forward(offset)
	turtle.pd()
	turtle.forward(width)
	turtle.left(90)
	turtle.forward(height)
	turtle.left(90)
	turtle.forward(width)
	turtle.left(90)
	turtle.forward(height)
	turtle.left(90)
	turtle.pu()
	
def drawCirclePattern(centerX, centerY, offset, radius, count):
	for i in range(count):
		centerX = centerX
		centerY = centerY
		offset = offset
		radius = radius
		count = count
		turtle.color(setRandomColor())
		turtle.pu()
		turtle.goto(centerX, centerY)
		turtle.setheading(i * 360 / count)
		turtle.forward(offset)
		turtle.pd()
		turtle.circle(radius)
		turtle.pu()
		
def drawSuperPattern(count=random.randint(0,10)):
	for i in range(count):
		pattern = random.randint(0, 1)
		if pattern == 0:
			centerX = random.randint(-500, 500)
			centerY = random.randint(-400, 400)
			offset = random.randint(-100, 100)
			radius = random.randint(0, 100)
			drawCirclePattern(centerX, centerY, offset, radius, count)
		if pattern == 1:
			centerX = random.randint(-500, 500)
			centerY = random.randint(-400, 400)
			offset = random.randint(-100, 100)
			height = random.randint(0, 200)
			width = random.randint(0, 200)
			rotation = random.randint(-360, 360)
			drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation)

def setRandomColor():
	color = random.randint(1, 4)
	if color == 1:
		return "red"
	if color == 2:
		return "green"
	if color == 3:
		return "blue"
	if color == 4:
		return "black"

def done():
	turtle.done()
	turtle.hideturtle()
	
		
		
		
	 
