# @@@@@@@@@@@@@@@
# CS 1400-14 week
# Assignment 8

import turtle
from random import randint
import math

def reset():
    turtle.reset()


def setup():
    turtle.speed(0)
    turtle.screensize(1000,800)


def drawRectangle(width, height):
    turtle.pendown()
    turtle.color(setRandomColor())
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    

def drawRectanglePattern(centerX,centerY, offset, width, height, count, rotation):
    for i in range(0,count):
        turtle.penup()
        turtle.setheading(0)
        turtle.goto(centerX,centerY)
        currentRotation = (360 / count) * i
        turtle.right(currentRotation)
        turtle.forward(offset)
        turtle.right(rotation)
        turtle.right(270)
        turtle.pendown()
        drawRectangle(width,height)


def drawCirclePattern(centerX, centerY, offset, radius, count):
    for i in range(0,count):
        turtle.penup()
        turtle.setheading(0)
        turtle.goto(centerX,centerY)
        currentPosition = (360 / count) * i
        turtle.right(currentPosition)
        turtle.forward(offset)
        turtle.right(90)
        turtle.pendown()
        turtle.color(setRandomColor())
        turtle.circle(radius)
        
        
def drawSuperPattern(num = ""):
    if num == "":
        num = randint(1,50)
    for i in range(0,num):
        randomPattern = randint(1,2)
        if randomPattern == 1:
            drawCirclePattern(randint(-500,500), randint(-400,400), randint(-100,100),randint(1,500),randint(1,200))
        elif randomPattern == 2:
            drawRectanglePattern(randint(-500,500), randint(-400,400), randint(-100,100),randint(1,200), randint(1,200), randint(1,200), randint(1,360))
    
        
        
        
def setRandomColor():
    random = randint(1,4)
    if random == 1:
        return "green"
    elif random == 2:
        return "red"
    elif random == 3:
        return "blue"
    else:
        return "purple"
    
def done():
    turtle.done()
    
