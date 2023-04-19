# @@@@@@@@@@@@@@@
# CS1400 - 14 Week
# Assignment 8
import random
from random import randint
import turtle

turtle.penup()

def reset():
    turtle.reset()
def setup():
    turtle.speed(100)
    turtle.screensize(1000,800)

def setRandomColor(color):
    color = str(color)
    rand = randint(0, 3)
    if rand == 0:
        color = "black"
    elif rand == 1:
        color = "yellow"
    elif rand == 2:
        color = "blue"
    elif rand == 3:
        color = "red"
def drawRectanglePattern(centerX,centerY,height, width,offset,count,rotation,color):

    centerX = int(centerX)
    centerY = int(centerY)
    height = int(height)
    wdth = int(width)
    count= int(count)
    s = (360/int(count))
    for j in range(count):
        color = str(color)
        rand = randint(0, 3)
        if rand == 0:
            color = "black"
        elif rand == 1:
            color = "yellow"
        elif rand == 2:
            color = "blue"
        elif rand == 3:
            color = "red"
        turtle.goto(centerX, centerY)
        turtle.left(s)
        turtle.forward(int(offset))
        turtle.right(int(rotation))
        turtle.color(color)
        drawRectangle(height,width)
        
def drawRectangle(height,width):
setRandomColor(color)
    height = int(height)
    width = int(width)
   tle.color(cward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.penup()
def drawCirclePattern(centerX, centerY, offset, radius, count,color):

    centerX = int(centerX)
    centerY = int(centerY)
    count= int(count)
    s = (360/int(count))
    for j in range(count):        color = str(color)
        rand = randint(0, 3)
        if rand == 0:
            color = "black"
        elif rand == 1:
            color = "yellow"
        elif rand == 2:
            color = "blue"
        elif rand == 3:
            color = "red"

       turtle.goto(centerX, centerY)
        turtle.left(s)
        turtle.forward(int(offset))
        turtle.pendown()
        turtle.color(color)
        turtle.circle(int(radius))
        turtle.penup()
def drawSuperPattern(centerX,centerY,height, width,radius,offset,count,rotation,color):
    centerX = randint(1,1000)
    centerY = randint(1,800)
    height = randint(1,360)
    width = randint(1,360)
    radius = randint(1,360)
    offset = randint(1,360)
    count = randint(1,360)
    rotation = randint(1,360)
    color = ""
    num = input("Number:")
    sq = randint(1,2)
    for i in range(int(num)):
        color = str(color)
        rand = randint(0, 3)
        if rand == 0:
            color = "black"
        elif rand == 1:
            color = "yellow"
        elif rand == 2:
            color = "blue"
        elif rand == 3:
            color = "red"
        if sq == 1:
            drawRectanglePattern(centerX,centerY,height, width,offset,count,rotation,color)
        else:
            drawCirclePattern(centerX, centerY, offset, radius, count,color)
    print(num)
            
            
    

def done():
    turtle.done()



