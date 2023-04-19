# @@@@@@@@@@@
# Assignment 8 Pattern
# CS 1400 14 week

import turtle
from random import randint

# setup
def setup():
    turtle.speed(0)
    turtle.setup(1000, 800)
    
# reset
def reset():
    turtle.reset()
    turtle.speed(0)
    
# drawRectanglePattern  
def drawRectanglePattern(valX, valY, valOffest, valWidth, valHeight, valCount, valRotation):
    for i in range(valCount):
        turtle.penup()
        setRandomColor()
        turtle.goto(valX, valY)
        turtle.setheading(i * 360 / valCount)
        turtle.forward(valOffest)
        turtle.right(valRotation)
        drawRectangle(valWidth, valHeight)

# drawRectangle
def drawRectangle(valWidth, valHeight):
    turtle.penup()
    turtle.pendown()
    turtle.forward(valWidth)
    turtle.right(90)
    turtle.forward(valHeight)
    turtle.right(90)
    turtle.forward(valWidth)
    turtle.right(90)
    turtle.forward(valHeight)
    turtle.penup()
    
# drawCirclePattern  
def drawCirclePattern(valX, valY, valOffest, valRadius, valCount):
    for i in range(valCount):
        turtle.penup()
        setRandomColor()
        turtle.goto(valX, valY)
        turtle.setheading(i * 360 / valCount)
        turtle.forward(valOffest)
        turtle.right(90)
        turtle.pendown()
        turtle.circle(valRadius)
        turtle.penup()
        
# drawSuperPattern
def drawSuperPattern(val = randint(4, 8)):
    for i in range(1, val + 1):
        alternator = randint(1, 2)
        if alternator == 1:
            valX = randint(-425, 425)
            valY = randint(-350, 350)
            valRadius = randint(15, 150)
            valCount = randint(5, 50)
            valOffset = randint(-100, 100)
            drawCirclePattern(valX, valY, valOffset, valRadius, valCount)
        else:
            valX = randint(-425, 425)
            valY = randint(-350, 350)
            valOffset = randint(-100, 100)
            valWidth = randint(5, 300)
            valHeight = randint(5, 300)
            valCount = randint(5, 50)
            valRotation = randint(-45, 45)
            drawRectanglePattern(valX, valY, valOffset, valWidth, valHeight, valCount, valRotation)
            
# setRandomColor    
def setRandomColor():
    colorNumber = randint(1, 4)
    if colorNumber == 1:
        turtle.color("blue")
    if colorNumber == 2:
        turtle.color("red")
    if colorNumber == 3:
        turtle.color("green")
    if colorNumber == 4:
        turtle.color("magenta")
 
# done   
def done():
    turtle.done()
