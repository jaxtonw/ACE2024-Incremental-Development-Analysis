# @@@@@@@@@@@@@@@@@@
# CS1400 - 001
# Assignment 8

import random
from math import cos
from math import sin
from math import radians
import turtle


#random.randint(1, 4)

def setRandomColor():
    color = random.randint(1, 4)
    if color == 1:
        turtle.color("purple")
    elif color == 2:
        turtle.color("blue")
    elif color == 3:
        turtle.color("red")
    else:
        turtle.color("green")
    
def done():
    turtle.done()

def reset():
    turtle.reset()
    
def setup():
    turtle.speed(0)
    turtle.setup(1000, 800)

def drawRectangle(width, height, userRotation):
    
      
    turtle.pendown()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)

def drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation):
    
    for position in range(0, count):
        
        
        
        setRandomColor()
        angle = (360 / count) * position        
        angle = radians(angle)
        angleInDegrees = (360 / count) * position
        turtle.penup()
        turtle.goto(centerX + offset * cos(angle), centerY + offset * sin(angle))
        turtle.setheading(angleInDegrees - rotation)
        turtle.pendown()
        drawRectangle(width, height, rotation)
    
                     
def drawCirclePattern(centerX, centerY, offset, radius, count):
    
    for position in range(0, count):
        
        setRandomColor()
        angle = (360 / count) * position
        angle = radians(angle)        
        turtle.penup()
        turtle.goto(centerX + (offset + radius) * cos(angle), centerY + (offset + radius) * sin(angle) - radius+ radius)

 urtle.pendown()
        turtle.circle(radius)

def drawSuperPattern(num = 5):
    
    for i in range(num):
        patternType = random.randint(1, 2)
        if patternType == 1:
            drawRectanglePattern(centerX = random.randint(-300, 300), centerY = random.randint(-300, 300), offset = random.randint(-100, 100),
                             width = random.randint(10, 150), height = random.randint(10, 150), count = random.randint(1, 50), 
                             rotation = random.randint(-360, 360))
        
        else:
            drawCirclePattern(centerX = random.randint(-300, 300), centerY = random.randint(-300, 300), offset = random.randint(-100, 100),
                              radius = random.randint(10, 90), count = random.randint(1, 50))
            
        


    
