# @@@@@@@@@@@  
# CS 1400 - MW1 XL
# Assignment 008
import turtle
import random


# sets up the window, and the turtle speed
def setup():
    turtle.screensize(1000, 800, "black")
    turtle.speed(0)


# random color function to alternate colors
def setRandomColor():
    color = random.randint(1, 4)
    if color == 1:
        turtle.color("#42c6ff")
    elif color == 2:
        turtle.color("#ff0055")
    elif color == 3:
        turtle.color("#0000b3")
    else:
        turtle.color("#006600")


# this draws the rectangle to be called later
def drawRectangle(width, height):
    turtle.pendown()
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.penup()


# this is the rectangle pattern function    
def drawRectanglePattern(centerX, centerY, offset, width=20, height=100th=25, cou)t=    # angle sets up the rotation for each rectangle
2   angle = 360/count
    # this loop does each rectangle and uses the loop number to find the angle
    for i in range(0, count):
        setRandomColor()
        turtle.setheading(0)
        turtle.penup()
        turtle.goto(centerX, centerY)
        turtle.left(angle * i)
        turtle.forward(offset)
        turtle.right(rotation)
        turtle.pendown()
        drawRectangle(width, height)


# here is the circle pattern function
# the circle pattern is almost identical to the rectangle
# it just needs radius and diameter instead
def drawCirclePattern(centerX, centerY, offset=20, rad=50, cou30):
    angle 60/count
    diameter = radius * 2
    for i in range(0, count):
        setRandomColor()
        turtle.penup()
        turtle.goto(centerX, centerY)
        turtle.setheading(0)
        turtle.left(angle * i)
        turtle.forward(offset)
        turtle.right(90)
        turtle.pendown()
        turtle.circle(diameter)
    
    
# here is the super pattern function
# the random numbers are in a range to where you should be able to see every pattern
# when it shows up
# The program draws a random number of rectangles and circles based on if the
# random number is a 1 or 2
def drawSuperPattern(num=3):
    for i in range(0, num):
        pattern = random.randint(1, 2)
        if pattern == 1:
            centerX = random.randint(-600, 600)
            centerY = random.randint(-200, 200)
            offset = random.randint(-50, 50)
            width = random.randint(10, 100)
            height = random.randint(10, 100)
            count = random.randint(1, 100)
            rotation = random.randint(0, 360)
            drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation)
        else:
            centerX = random.randint(-600, 600)
            centerY = random.randint(-200, 200)
            offset = random.randint(-50, 50)
            radius = random.randint(10, 100)
            count = random.randint(10, 100)
            drawCirclePattern(centerX, centerY, offset, radius, count)


# wipes the turtle drawing clear
def clear():
    turtle.reset()


# this function just keeps the turtle window open
def done():
    turtle.done()

