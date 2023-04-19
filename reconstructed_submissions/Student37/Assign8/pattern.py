# @@@@@@@@@
# CS1400 - MW1
# Assignment 8 - pattern

import random
import turtle
t = turtle
        
def reset():
    t.reset()
    
    
def setup():
    t.speed(0)
    t.setup(1000, 800)
        
        
def drawRectanglePattern(centerX, centerY, offset, width, height, 
count, rotation):
    
    t.up()
    t.goto(centerX, centerY)
    t.setheading(0)
    t.forward(offset)
    t.left(rotation)
    for i in range(count + 1):
        drawRectangle(width, height)
        t.up()
        t.goto(centerX, centerY)
        t.setheading((360 / count) * i)
        t.forward(offset)
        t.left(rotation)
        
    
        
def drawRectangle(width, height):
    t.down()
    setRandomColor()
    for i in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    
    
def drawCirclePattern(centerX, centerY, offset, radius, count):
    t.up()
    t.goto(centerX, centerY)
    t.setheading(0)
    t.forward(offset + radius)
    for i in range(count + 1):
        drawCircle(radius)
        t.up()
        t.goto(centerX, centerY)
        t.setheading(0)
        t.left((360 / count) * i)
        t.forward(offset + radius)
        
        
def drawCircle(radius):
    setRandomColor()
    t.down()
    t.circle(radius)
        
        
def drawSuperPattern(num):
    rand = random.randint(0, num)
    
    for i in range(num):
        rCenterX = random.randint(-300, 300)
        rCenterY = random.randint(-300, 300)
        rOffset = random.randint(0, 100)
        rRadius = random.randint(1, 150)
        rWidth = random.randint(1, 150)
        rHeight = random.randint(1, 150)
        rRotation = random.randint(0, 360)
        
        circleOrRectangle = random.randint(0,1)
        if circleOrRectangle == 0:
            t.up()
            t.goto(rCenterX, rCenterY)
            t.setheading(rRotation)
            t.forward(rOffset + rRadius)
            drawCircle(rRadius)
        else:
            t.up()
            t.goto(rCenterX, rCCecerY)
                theading(360 /  num * i)
      (rRota forward(rorOffset)
            t.left(rRotation              drawRectangle(rWidth, rHeight)r            
Width, rHeef setRandomColor():
    rand = random.randint(1, 4)
    
    if rand == 1:
        t.pencolor("red")
    elif rand == 2:
        t.pencolor("blue")
    elif rand == 3:
        t.pencolor("green")
    elif rand == 4:
        t.pencolor("orange")
        
def done():
    t.done()
