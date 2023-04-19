# @@@@@@@@@@@@
# CS 1400 - 14 Weeks
# Assignment 8

import turtle
import random


def reset():
    turtle.reset()


def setup():
    turtle.speed(0)
    turtle.screensize(1000, 800)


def drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation): 
    for i in range(0, count):
        turtle.penup()
        turtle.goto(centerX, centerY)
        turtle.setheading(i * (360 / count))
        turtle.forward(offset)
        turtle.right(rotation)
        drawRectangle(width, height)


def drawRectangle(width, height):
    turtle.pendown()
    setRandomColor()
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)


def drawCirclePattern(centerX, centerY, offset, radius, count):
    for i in range(0, count):
        turtle.penup()
        turtle.goto(centerX, centerY)
        turtle.setheading(i * (360 / count))
        turtle.forward(offset)
        turtle.right(90)
        setRandomColor()
        turtle.pendown()
        turtle.circle(radius)


def drawSuperPattern(num=3):
    for i in range(0, num):
        randomNum = random.randint(1, 2)
        if randomNum == 1:
            randomXPos = random.randint(-300, 300)
            randomYPos = random.randint(-250, 250)
            randomOffset = random.randint(-50, 50)
            randomWidth = random.randint(10, 200)
            randomHeight = random.randint(10, 200)
            randomCount = random.randint(2, 50)
            randomRotation = random.randint(-360, 360)
            drawRectanglePattern(randomXPos, randomYPos, randomOffset, randomWidth, randomHeight, 
                                 randomCount, randomRotation)
        if randomNum == 2:
            randomXPos = random.randint(-300, 300)
            randomYPos = random.randint(-250, 250)
            randomOffset = random.randint(-50, 50)
            randomRadius = random.randint(5, 50)
            randomCount = random.randint(2, 50)
            drawCirclePattern(randomXPos, randomYPos, randomOffset, randomRadius, randomCount)
            

def setRandomColor():
    randomNum = random.randint(1, 4)
    if randomNum == 1:
        turtle.color("red")
    if randomNum == 2:
        turtle.color("green")
    if randomNum == 3:
        turtle.color("blue")
    if randomNum == 4:
        turtle.color("purple")
    
    
def done():
    turtle.done()

