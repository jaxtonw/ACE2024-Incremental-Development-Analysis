# @@@@@@@@@@@@@@
# CS1400 - 001
# Assignment 8

import turtle
import random


def reset():
    turtle.clear()
    turtle.reset()
    setup()


def setup():
    turtle.speed(0)
    turtle.screensize(1000, 800)
    

def drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation):
    for i in range(0, count):
        turtle.penup()
        turtle.goto(centerX, centerY)
        turtle.forward(offset)
        turtle.pendown()
        turtle.right(rotation)
        drawRectangle(width, height)
        turtle.left(rotation)
        turtle.right(360 / count)
        
        
def drawRectangle(width, height):
    turtle.pendown()
    setRandomColor()
    for i in range(0, 2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.penup()
  
    
def drawCirclePattern(centerX, centerY, offset, radius, count):
    for i in range(0, count):
        setRandomColor()
        turtle.penup()
        turtle.goto(centerX, centerY)
        turtle.forward(offset)
        turtle.pendown()
        turtle.right(90)
        turtle.circle(radius)
        turtle.left(90)
        turtle.right(360 / count)
    

def drawSuperPattern(num=3):
    for i in range(0, num):
        randomPattern = random.randint(1, 2)
        if randomPattern == 1:
            centerX = random.randint(-400, 400 + 1)
            centerY = random.randint(-300, 300 + 1)
            offset = random.randint(-75, 75 + 1)
            width = random.randint(10, 150 + 1)
            height = random.randint(10, 150 + 1)
            count = random.randint(1, 100 + 1)
            rotation = random.randint(0, 355 + 1)
            drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation)
        elif randomPattern == 2:
            centerX = random.randint(-400, 400 + 1)
            centerY = random.randint(-300, 300 + 1)
            offset = random.randint(-75, 75 + 1)
            radius = random.randint(10, 100 + 1)
            count = random.randint(1, 100 + 1)
            drawCirclePattern(centerX, centerY, offset, radius, count)


def setRandomColor():
    randomColor = random.randint(1, 6 + 1)
    if randomColor == 1:
        turtle.color("blue")
    elif randomColor == 2:
        turtle.color("red")
    elif randomColor == 3:
        turtle.color("purple")
    elif randomColor == 4:
        turtle.color("green")
    elif randomColor == 5:
        turtle.color("pink")
    elif randomColor == 6:
        turtle.color("teal")
    
        
def done():
    turtle.done()

