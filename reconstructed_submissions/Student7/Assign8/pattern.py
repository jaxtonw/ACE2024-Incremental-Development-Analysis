# @@@@@@@@@@@@
# CS1400 - MW1
# Assignment 8

import turtle
import random

def reset():
    turtle.reset()

def setup():
    turtle.speed(0)
    turtle.setup(1000,800)

def drawRectangle(width,height,color):
    turtle.pendown()
    turtle.pencolor(color)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.penup()

def setRandomColor():
    num = random.randint(1,5)
    if num == 1:
        return "Blue"
    elif num == 2:
        return "Black"
    elif num == 3:
        return "Red"
    elif num == 4:
        return "Green"
    else:
        return "Purple"

def drawRectanglePattern(xPos,yPos,offset,width,height,count,rotation):
    for i in range(count):
        turtle.penup()
        turtle.goto(xPos,yPos)
        color = setRandomColor()
        angle = (360 / count) * i - rotation
        turtle.setheading(angle)
        turtle.forward(offset)
        drawRectangle(width,height,color)

def drawCirclePattern(xPos,yPos,offset,radius,count):
    for i in range(count):
        turtle.penup()
        turtle.goto(xPos,yPos)
        color = setRandomColor()
        angle = (360 / count) * i
        turtle.setheading(angle)
        turtle.forward(offset)
        turtle.right(90)
        turtle.pendown()
        turtle.pencolor(color)
        turtle.circle(radius)
        turtle.penup()

def drawSuperPattern(count=5):
    for i in range(1,count + 1):
        mode = random.randint(1,2)
        if mode == 1:
            xPos = random.randint(-300,300)
            yPos = random.randint(-250,250)
            offset = random.randint(-50,50)
            width = random.randint(1,200)
            height = random.randint(1,200)
            count = random.randint(1,100)
            rotation = random.randint(-180,180)
            drawRectanglePattern(xPos,yPos,offset,width,height,count,rotation)
        if mode == 2:
            xPos = random.randint(-300,300)
            yPos = random.randint(-250,250)
            offset = random.randint(-50,50)
            radius = random.randint(1,200)
            count = random.randint(1,100)
            drawCirclePattern(xPos,yPos,offset,radius,count)

def done():
    turtle.done()
