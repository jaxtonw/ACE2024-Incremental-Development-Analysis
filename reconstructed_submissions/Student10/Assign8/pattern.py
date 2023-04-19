# @@@@@@@@@@
# CS 1400 - 14 week
# Assignment 8

# import statements
import turtle
from random import randint

# function to erase all patterns and start over
def reset():
    turtle.reset()
    turtle.speed(0)

# function to set up 1000 by 800 screen
def setup():
    turtle.setup(1000, 800)
    turtle.speed(0)

# function to draw the rectangle pattern
def drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation):
    # find angle
    angle = 360 / count
    # loop to draw actual pattern
    for i in range(1, count + 1):
        turtle.pu()
        turtle.goto(centerX, centerY)
        turtle.setheading(angle * (i - 1))
        turtle.forward(offset)
        turtle.right(rotation)
        setRandomColor()
        drawRectangle(height, width)

# function to draw a single rectangle
def drawRectangle(height, width):
    turtle.pd()
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)

# function to draw circle pattern
def drawCirclePattern(centerX, centerY, offset, radius, count):
    # find angle
    angle = 360 / count
    # loop to draw actual pattern
    for i in range(1, count + 1):
        turtle.pu()
        turtle.goto(centerX, centerY)
        turtle.setheading(angle * (i - 1))
        turtle.forward(offset)
        turtle.right(90)
        turtle.pd()
        setRandomColor()
        turtle.circle(radius)

# function to draw random patterns
def drawSuperPattern(num=3):
    for i in range(1, num + 1):
        mode = randint(1, 2)
        # rectangle
        if mode == 1:
            # set random parameters
            xPos = randint(-400, 400)
            yPos = randint(-300, 300)
            randOffset = randint(-100, 100)
            randHeight = randint(1, 200)
            randWidth = randint(1, 200)
            randCount = randint(1, 100)
            randRotation = randint(0, 90)
            drawRectanglePattern(xPos, yPos, randOffset, randWidth, randHeight, randCount, randRotation)
        # circle
        elif mode == 2:
            # set random parameters
            xPos = randint(-400, 400)
            yPos = randint(-300, 300)
            randOffset = randint(-100, 100)
            randRadius = randint(1, 100)
            randCount = randint(1, 100)
            drawCirclePattern(xPos, yPos, randOffset, randRadius, randCount)

# function to set a random color
def setRandomColor():
    color = randint(1, 4)
    if color == 1:
        turtle.color("orange")
    if color == 2:
        turtle.color("green")
    if color == 3:
        turtle.color("blue")
    if color == 4:
        turtle.color("purple")

# function to keep turtle window after we finish
def done():
    turtle.done()

