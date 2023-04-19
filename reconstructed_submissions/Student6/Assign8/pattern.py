# @@@@@@@@@@@@@
# CS1400 - 001
# Assignment 8

import turtle 
import random 

colors = ["red", "purple", "green", "orange", "blue", "yellow"]

def reset():
    turtle.reset()
    turtle.speed(0)


def setup():
    turtle.speed(0)
    turtle.setup(1000, 800)
    

def drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation):
    for i in range(count, 0, -1):
        shapeRotation = 360 / count
        drawRectangle(centerX, centerY, offset, width, height, rotation + i * shapeRotation)


def drawRectangle(centerX, centerY, offset, width, height, rotation):
    turtle.penup()
    turtle.setheading(rotation)
    turtle.goto(centerX, centerY)
    turtle.forward(offset)
    turtle.color(random.choice(colors))
    turtle.pendown()
    turtle.forward(width)
    turtle.setheading(rotation + 90)
    turtle.forward(height)
    turtle.setheading(rotation + 180)
    turtle.forward(width)
    turtle.setheading(rotation + 270)
    turtle.forward(height)


def drawCirclePattern(centerX, centerY, offset, radius, count):
    shapeRotation = 360 / count
    for i in range(count, 0, -1):
        drawCircle(centerX, centerY, offset, radius, shapeRotation * i - shapeRotation)


def drawCircle(centerX, centerY, offset, radius, shapeRotation):
    turtle.penup()
    turtle.goto(centerX, centerY)
    turtle.setheading(shapeRotation)
    turtle.forward(offset)
    turtle.setheading(0)
    turtle.color(random.choice(colors))
    turtle.pendown()
    turtle.circle(radius)
    
def drawSuperPattern(num):
    for i in range(num, 0, -1):
        centerX = random.randint(-500, 500)
        centerY = random.randint(-400,400)
        height = random.randint(-200, 200)
        width = random.randint(-200,200)
        radius = random.randint(-200, 200)
        offset = random.randint(-200, 200)
        rotation = random.randint(-360, 360)
        count = random.randint(10,100)
        
        if i % 2 == 0:
            drawCirclePattern(centerX, centerY, offset, radius, count)
        else:
            drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation)

def done():
    turtle.done()
    
       
        
       
       
    
