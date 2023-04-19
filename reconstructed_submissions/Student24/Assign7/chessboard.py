# @@@@@@@@@@@@
# CS1400 - MW1
# Assignment 7

# Set up the turtle
import turtle

def drawRectangles(startRecX, startRecY, width, height):
	turtle.fillcolor("black")
	turtle.goto(startRecX, startRecY)
	turtle.setheading(0)
	turtle.pd()
	turtle.begin_fill()
	turtle.forward(width / 8)
	turtle.left(90)
	turtle.forward(height / 8)
	turtle.left(90)
	turtle.forward(width / 8)
	turtle.left(90)
	turtle.forward(height / 8)
	turtle.end_fill()
	turtle.pu()

def drawAllRectangles(startX, startY, width, height):
	startX -= width / 4
	for i in range(4):
		for j in range(4):
			startX += width / 4
			drawRectangles(startX, startY, width, height)
		startX -= width
		startY += height / 4
	
def drawChessboard(startX, startY, width=250, height=250):
	turtle.speed(0)
	turtle.pu()
	turtle.fillcolor("white")
	turtle.goto(startX, startY)
	turtle.pd()
	turtle.goto(startX + width, startY)
	turtle.goto(startX + width, startY + height)
	turtle.goto(startX, startY + height)
	turtle.goto(startX, startY)
	drawAllRectangles(startX, startY, width, height)
	drawAllRectangles(startX + width / 8, startY + height / 8, width, height)
	turtle.hideturtle()
	turtle.done()



