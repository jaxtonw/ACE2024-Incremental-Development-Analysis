# @@@@@@@@@@
# CS1400 - 14 week
# Assignment 8

import turtle
from random import randint


# setup
def setup():
    turtle.setup(1000, 800)
    turtle.speed(0)


def setRandomColor():
    # random color
    val = randint(1, 5)
    if val == 1:
        return "red"
    elif val == 2:
        return "blue"
    elif val == 3:
        return "green"
    elif val == 4:
        return "purple"
    elif val == 5:
        return "orange"


# rectangle pattern
def drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation):
    turtle.penup()
    turtle.goto(centerX, centerY)
    for j in range(count):
        turtle.penup()
        turtle.goto((centerX, centerY))
        turtle.setheading(j * 360 / count)
        turtle.forward(offset)
        drawRectangle(centerX, centerY, offset, width, height, count, rotation)
    

# one rectangle
def drawRectangle(centerX, centerY, offset, width, height, count, rotation): 
    # random color

    # draw rectangle
    turtle.color(setRandomColor())
    turtle.pendown()
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.penup()
    
    
# circle pattern
def drawCirclePattern(centerX, centerY, offset, radius, count):
    for k in range(count):
        # random color
        turtle.color(setRandomColor())
        
        # draw circle
        turtle.penup()
        turtle.goto(centerX, centerY)
        turtle.setheading(k * 360 / count)
        turtle.forward(offset)
        turtle.right(90)
        turtle.pendown()
        turtle.circle(radius)
        
    
# super pattern
def drawSuperPattern(num):
    for m in range(num):
        # choose shape
        shape = randint(1, 2)
        # get random values for parameters
        centerX = randint(-400, 400)
        centerY = randint(-300, 300)
        offset = randint(-100, 100)
        width = randint(10, 200)
        height = randint(10, 200)
        count = randint(10, 50)
        rotation = randint(0, 360)
        radius = randint(10, 200)
        # rectangle
        if shape == 1:
            drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation)
        # circle       
        if shape == 2:
            drawCirclePattern(centerX, centerY, offset, radius, count)
    
    
# clear
def clear():
    turtle.reset()
    turtle.speed(0)
    
    
# done
def done():
    turtle.done()
    
    
# testing
# drawRectanglePattern(10, 10, 30, 50, 70, 3, 0)
# drawCirclePattern(10, 10, 30, 30, 4)

