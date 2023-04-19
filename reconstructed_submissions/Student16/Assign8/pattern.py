# @@@@@@@@@@@@@@
# CS1400 - MW2
# Assignment 8
import turtle
import random
from random import randint


def reset():
    turtle.reset()
    setup()


def setup():
    turtle.speed(0)
    turtle.setup(1000, 800)
    turtle.pensize(2)


def drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation):
    # get the turtle in the right spot
    turtle.pu()
    turtle.goto(centerX, centerY)
    turtle.setheading(0)

    # Create a loop that will draw many colored rectangles around a circle based off the offset
    for i in range(1, count + 1):
        setRandomColor()

        turtle.left(i / 360)
        turtle.forward(offset)
        turtle.right(rotation)
        drawRectangle(width, height)
        turtle.goto(centerX, centerX)
        turtle.setheading(0)
        turtle.left((i / count) * 360)

# This function only draws a rectangle  
def drawRectangle(width, height):
    turtle.pd()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.pu()


# the draw Circle Pattern needs a center x and y coordinate, a radius and a count
def drawCirclePattern(centerX, centerY, offset, radius, count):
    # set up the pattern to start drawing
    turtle.pu()
    turtle.goto(centerX, centerY)
    turtle.setheading(0)

    # create a loop to draw many circles
    for i in range(1, count + 1):
        # call the set Random Color function
        setRandomColor()

        # set the turtle to the offset and draw the circle
        turtle.forward(offset)
        turtle.pd()
        turtle.circle(radius)
        turtle.pu()

        # have the turtle return to the center, and reorient it to draw a circle at a different place.
        turtle.goto(centerX, centerY)
        turtle.setheading(0)
        turtle.left((i / count) * 360)

# Super Pattern Definition
def drawSuperPattern(num=3):
    for i in range(num):
        # a random number determines the pattern type
        patternType = randint(1, 1)

        # These are the parameters that will be used in the functions to get random outputs
        randX = randint(-700, 700)
        randY = randint(-500, 500)
        randOffset = randint(-150, 150)
        randCount = randint(2, 100)

        # These variables are only used in the draw rectangle function
        randWidth = randint(1, 100)
        randHeight = randint(1, 100)
        randRotation = randint(0, 360)

        # This Variable is unique to the drawCirclePattern function
        randRadius = randint(1, 150)

        if patternType == 1:
            drawRectanglePattern(randX, randY, randOffset, randWidth, randHeight, randCount, randRotation)
            
        elif patternType == 2:
            drawCirclePattern(randX, randY, randOffset, randRadius, randCount)


def setRandomColor():
    color = random.randint(1, 4)
    if color == 1:
        color = "red"
    elif color == 2:
        color = "blue"
    elif color == 3:
        color = "green"
    elif color == 4:
        color = "purple"
    turtle.color(color)


def done():
    turtle.done()

