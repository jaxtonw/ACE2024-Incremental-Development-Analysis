# @@@@@@@@@@@
# CS1400 - MW1
# Assignment 8

import turtle
import random

def reset():
    turtle.resetscreen()
    turtle.speed(0)
    

def setup():
    turtle.speed(0)
    turtle.setup(1000, 800)
    

def drawRectanglePattern(centerX, centerY, offset, height, width, count, rotation):
    # number of rectangles
    for i in range(count):
        turtle.pu()
        # orientation
        turtle.goto(centerX, centerY)
        turtle.setheading(360 / count * i)
        turtle.forward(offset)
        turtle.setheading((360 / count * i) + rotation)
        # drawings
        drawRectangle(height, width)
    

def drawRectangle(height, width):
    # setup
    turtle.pu()
    setRandomColor()
    turtle.pd()
    # rectangle loop
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    

def drawCirclePattern(centerX, centerY, offset, radius, count):
    # number of circles
    for i in range(count):
        # setup
        turtle.pu()
        turtle.goto(centerX, centerY)
        turtle.setheading(360 / count * i)
        turtle.forward(offset + radius)
        # color and draw
        setRandomColor()
        turtle.pd()
        turtle.circle(radius)
    

def drawSuperPattern(num=random.randint(1, 10)):
    for i in range(num):
        # random variables setup
        centerX = random.randint(-800, 800)
        centerY = random.randint(-600, 600)
        offset = random.randint(-100, 100)
        height = random.randint(0, 200)
        width = random.randint(0, 200)
        radius = random.randint(0, 100)
        count = random.randint(2, 80)
        rotation = random.randint(1, 360)
        val = random.randint(1, 2)
        # random choices
        if val == 1:
            drawRectanglePattern(centerX, centerY, offset, height, width, count, rotation)
        elif val == 2:
            drawCirclePattern(centerX, centerY, offset, radius, count)
    

def setRandomColor():
    # number of color options
    val = random.randint(1, 4)
    # assign colors to numbers
    if val == 1:
        color = "orange"
    elif val == 2:
        color = "red"
    elif val == 3:
        color = "blue"
    elif val == 4:
        color = "green"
    # set color
    turtle.color(color)
    

def done():
    turtle.done()


