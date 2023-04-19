# @@@@@@@@@@@@@@
# CS 1400 - 14 week
# Assignment 8


import turtle
import random

# reset function
def reset():
#     1. Erase all the patterns and start over
    turtle.reset()
    turtle.speed(0)


# setup function
def setup():
#     1. configure turtle to draw quickly
    turtle.speed(0)
#     2. configure turtle to have a window of 1000 x 800
    turtle.setup(1000, 800)


# drawRectanglePattern() function
#     1. use appropriate parameters (center position, offset, height, width, count, rotation)
def drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation):

#     2. create loop to run program <count> times
    for i in range(0, count):
        
#         a. set turtle to proper heading and position
        turtle.penup()
        turtle.goto(centerX, centerY)
        turtle.setheading(0 + (i * 360 / count))
        turtle.forward(offset)
        turtle.setheading(rotation + (i * 360 / count))

#         b. call drawRectangle
        drawRectangle(width, height)
    
#         c. increment count variable by 1
#         d. increment angle variable appropriately


# drawRectangle function
def drawRectangle(width, height):
#     1. draw a rectangle
    turtle.pendown()
    setRandomColor()
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.penup()

# drawCirclePattern function
#     1. use appropriate parameters (center position, offset, radius, count)
def drawCirclePattern(centerX, centerY, offset, radius, count):
    
#     2. create loop to run program <count> times
    for i in range(0, count):
#         a. set proper turtle position
        turtle.penup()
        turtle.goto(centerX, centerY)
        turtle.setheading(0 + (i * 360 / count))
        turtle.forward(offset)
    
#         b. call setRandomColor
        setRandomColor()
        
#         c. draw circle
        turtle.pendown()
        turtle.circle(radius)
    
#         d. increment count variable by 1
#         e. increment angle variable appropriately

# drawSuperPattern function
#     1. use appropriate parameters (num)
def drawSuperPattern(num="5"):
#     2. create loop to run program <num> times
    for i in range(0, num):
        
#         a. set random integer to select either rectangle or circle
        shape = random.randint(1, 2)
    
#         b. if statement for drawing the appropriate pattern.
        if shape == 1:
            centerX = random.randint(-300, 300)
            centerY = random.randint(-200, 200)
            offset = random.randint(-100, 100)
            width = random.randint(1, 200)
            height = random.randint(1, 200)
            count = random.randint(1, 100)
            rotation = random.randint(0, 360)
            
            drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation)
            
        elif shape == 2:
            centerX = random.randint(-500, 500)
            centerY = random.randint(-400, 400)
            offset = random.randint(-200, 200)
            radius = random.randint(1, 150)
            count = random.randint(1, 100)
        
            drawCirclePattern(centerX, centerY, offset, radius, count)
        
#         c. increment num variable by 1
#         e. increment angle variable appropriately


# setRandomColor function
def setRandomColor():
#     1. set random integer to select one of ..... colors
    color = random.randint(1, 5)
#     2. create if statement to set color according to random integer
    if color == 1:
        color = "turquoise"
    elif color == 2:
        color = "brown"
    elif color == 3:
        color = "green"
    elif color == 4:
        color = "maroon"
    elif color == 5:
        color = "magenta"
    turtle.pencolor(color)

def done():
    turtle.done()
    
    
