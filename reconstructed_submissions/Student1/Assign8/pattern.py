# @@@@@@@@@@@@@
# CS1400 - MW1
# Assignment 8

import turtle
from random import randint


def setup():
    # set up
    turtle.setup(1000, 800)
    turtle.speed(0)
    turtle.penup()
    
def drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation):
    for i in range(count):
        # get cursor in position
        turtle.goto(centerX, centerY)
        turtle.setheading(0)
        turtle.left(i * (360/count))
        turtle.forward(offset)
        turtle.right(rotation)
        
        # draw rectangle
        drawRectangle(width, height)
        
def drawRectangle(width, height):
    # set color
    turtle.pencolor(setRandomColor())
    turtle.pendown()
    # draw rectangle
    for i in range(2):
        turtle.forward(height)
        turtle.left(90)
        turtle.forward(width)
        turtle.left(90)
    turtle.penup()
    
def drawCirclePattern(centerX, centerY, offset, radius, count):
    for i in range(count):
        # get cursor in position
        turtle.goto(centerX, centerY)
        turtle.setheading(0)
        turtle.left(i * (360/count))
        turtle.forward(offset)
        turtle.left(90)
        
        # draw circle
        turtle.pencolor(setRandomColor())
        turtle.pendown()
        turtle.circle(radius)
        turtle.penup()
        
def drawSuperPattern(num = 3):
    for i in range(num):
        centerX = randint(-400, 400)
        centerY = randint(-300, 300)
        offset = randint(-75, 75)
        count = randint(1, 50)
        randomNum = randint(1, 2)
        if randomNum == 1:
            width = randint(1, 200)
            height = randint(1, 200)
            rotation = randint(0, 180)
            drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation)
        elif randomNum == 2:
            radius = randint(1, 100)
            drawCirclePattern(centerX, centerY, offset, radius, count)
            
def setRandomColor():
    randomNum = randint(1, 4)
    if randomNum == 1:
        return "black"
    elif randomNum == 2:
        return "blue"
    elif randomNum == 3:
        return "red"
    elif randomNum == 4:
        return "green"
    
def reset():
    turtle.clear()
    turtle.penup()

def done():
    turtle.hideturtle()
    turtle.done()
        
        
    
