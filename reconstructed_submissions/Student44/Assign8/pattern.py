# @@@@@@@@@@@@
# CS1400 - MW 1
# Assignment 8

import turtle
import random


def reset():
    
    # turtle function to erase all drawings
    turtle.reset()
    turtle.speed(0)    
    
    
def setup():
    
    # set turtle speed and screen size
    turtle.speed(0)
    turtle.setup(1000, 800)
    
    
def drawRectanglePattern(width, height, centerX, centerY, offset, count, rotation):
    
    # angle constant
    angleSetting = 360 // count
    # loop for number of rectangles drawn
    for i in range(count):
        turtle.penup()
        # go to center 
        turtle.setx(centerX)
        turtle.sety(centerY)
        # set heading to where the rectangle should go
        turtle.setheading(angleSetting * i)
        # travel forward the offset distance
        turtle.forward(offset)
        turtle.setheading(rotation)
        setrandomColor()
        drawRectangle(width, height)
        turtle.goto(centerX, centerY)
    

def drawCirclePattern(centerX, centerY, offset, radius, count):
    
    # draw circles until the count number is met
    for i in range(count):
        # angle setting constant
        angleSetting = 360 // count
    
        turtle.penup()
        turtle.setx(centerX)
        turtle.sety(centerY)
        turtle.setheading(angleSetting * i)
        turtle.forward(offset)
        setrandomColor()
        turtle.pendown()
        turtle.setheading((angleSetting * i - angleSetting))
        turtle.circle(radius)
    
    
def drawSuperPattern(num=random.randint(1, 30)):
    # generate random values for all parameters 
    width = random.randint(1, 400)
    height = random.randint(1, 400)
    centerX = random.randint(-500, 500)
    centerY = random.randint(-400, 400)
    offset = random.randint(-400, 400)
    rotation = random.randint(1, 360)
    patternType = random.randint(1, 2)
    radius = random.randint(1, 300)
    # conditionals to decide what pattern to draw
    if patternType == 1:
        drawCirclePattern(centerX, centerY, offset, radius, num)
    elif patternType == 2:
        drawRectanglePattern(centerX, centerY, width, height, offset, num, rotation)
    
    
def drawRectangle(width, height):
    
    # draw a single rectangle
    turtle.pendown()
    for i in range(2):
        
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.penup()
    
    
def setrandomColor():
    
    # generate random num to pick color
    num = random.randint(1,4)
    if num == 1:
        turtle.color("black")
    elif num == 2:
        turtle.color("red")
    elif num == 3:
        turtle.color("cyan")
    else:
        turtle.color("green")
        
        
def done():
    # keep window open
    turtle.done()

