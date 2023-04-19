# @@@@@@@@@@@@@@
# CS1400 - 001
# module patterns

import random
import turtle as t


# function to reset drawing
def reset():
    t.reset()
    t.speed(0)


# function to setup drawing space
def setup():
    t.speed(0)
    t.setup(1000, 800)


# function to draw rectangle pattern
def drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation):
    t.penup()
    t.goto(centerX, centerY)
    rotationDegree = 0
    for i in range(count):
        val = 1
        while rotationDegree < 360:
            t.forward(offset)
            t.right(rotation)
            drawRectangle(height, width)
            t.penup()
            t.goto(centerX, centerY)
            t.setheading((360 / count) * val)
            rotationDegree += 360 / count
            val += 1
    t.hideturtle()
        
    
# function to draw an individual rectangle
def drawRectangle(height, width):
    t.pendown()
    setRandomColor()
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    
    
# function to draw circle pattern
def drawCirclePattern(centerX, centerY, offset, radius, count):
    t.penup()
    t.goto(centerX, centerY)
    rotationDegree = 0
    for i in range(count):
        val = 1
        while rotationDegree < 360:
            t.forward(offset)
            t.pendown()
            setRandomColor()
            t.circle(radius)
            t.penup()
            t.goto(centerX, centerY)
            t.setheading((360 / count) * val)
            rotationDegree += 360 / count
            val += 1
    t.hideturtle()

# function to draw random circle and rectangle patterns 
def drawSuperPattern(num):
    shapeCount = 1
    while shapeCount <= num:
        superRandom = random.randint(1, 2)
        if superRandom == 1:
            centerX = random.randint(-700, 350)
            centerY = random.randint(-700, 350)
            offset = random.randint(-200, 200)
            height = random.randint(1, 600)
            width = random.randint(1, 600)
            count = random.randint(1, 100)
            rotation = random.randint(0, 360)
            drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation)
            shapeCount += 1
        elif superRandom == 2:
            centerX = random.randint(-700, 350)
            centerY = random.randint(-700, 350)
            offset = random.randint(-200, 200)
            radius = random.randint(1, 300)
            count = random.randint(1, 100)
            drawCirclePattern(centerX, centerY, offset, radius, count)
            shapeCount += 1
    t.hideturtle()   
    
# function to set turtle pen color to a random color
def setRandomColor():
    randomColor = random.randint(1, 4)
    if randomColor == 1:
        t.pencolor("blue")
    elif randomColor == 2:
        t.pencolor("green")
    elif randomColor == 3:
        t.pencolor("red")
    elif randomColor == 4:
        t.pencolor("magenta")


# function to end 
def done():
    t.done()    

