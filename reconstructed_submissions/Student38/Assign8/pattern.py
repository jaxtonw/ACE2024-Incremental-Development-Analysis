# @@@@@@@@@@@@@
# CS-1400 MW1
# Assignment 8

import turtle
import random


tr = turtle

# clear window of patterns
def reset():
    tr.clear()

# show turtle, set turtle speed to 0, setup turtle window as 1000 * 800
def setup():
    tr.showturtle()
    tr.speed(0)
    tr.screensize(1000, 800)

# randomly selects one of four colors for turtle pen
def setRandomColor():
    # use random number generator range 0 to 3
    colorNum = random.randint(0, 4)
    # elif statements, set each number with a different color
    if colorNum == 0:
        tr.pencolor("green")
    elif colorNum == 1:
        tr.pencolor("blue")
    elif colorNum == 2:
        tr.pencolor("red")
    else:
        tr.pencolor("black")

# use centerX, centerY, offset, width, height, count, rotation as parameters
def drawRectanglePattern(centerXval, centerYval, offsetVal, widthVal, heightVal, countVal, rotationVal):
    tr.penup()
# draw rectangles in loop, changing angle and location with each iteration
    for i in range(countVal + 1):
        tr.goto(centerXval, centerYval)
        tr.setheading(i * 360 / countVal)
        tr.forward(offsetVal)
        tr.left(rotationVal)
        setRandomColor()
        drawRectangle(widthVal, heightVal)
        tr.penup()
    

# draw one rectangle, use for loop to reduce size of code
def drawRectangle(width3, height3):
    tr.pendown()
    for j in range(2):
        tr.forward(width3)
        tr.left(90)
        tr.forward(height3)
        tr.left(90)
    tr.penup()

# use centerX, centerY, offset, radius, count as parameters
def drawCirclePattern(centerX4, centerY4, offset4, radius4, count4):
    tr.penup()
# draw circles in loop, changing location with each iteration
    for k in range(count4 + 1):
        tr.goto(centerX4, centerY4)
        setRandomColor()
        tr.setheading(k * 360 / count4)
        tr.forward(offset4)
        tr.pendown()
        tr.circle(radius4)
        tr.penup()


# use user input to determine how many patterns to draw, or loop to draw correct number of patterns
def drawSuperPattern(num1):
# elif statements to determine what pattern to draw
    for i in range(0, num1):
        randomNum = random.randint(0, 2)
        if randomNum == 0: # randomize parameters for circle pattern
            centerX1 = random.randint(-400, 400)
            centerY1 = random.randint(-400, 400)
            radius1 = random.randint(5, 300)
            offset1 = random.randint(-100, 100)
            count1 = random.randint(5, 100)
            drawCirclePattern(centerX1, centerY1, offset1, radius1, count1)
        elif randomNum == 1: # randomize parameters for rectangle pattern
            centerX2 = random.randint(-400, 400)
            centerY2 = random.randint(-400, 400)
            width2 = random.randint(5, 200)
            height2 = random.randint(5, 200)
            offset2 = random.randint(-50, 50)
            count2 = random.randint(5, 75)
            rotation2 = random.randint(0, 180)
            drawRectanglePattern(centerX2, centerY2, offset2, width2, height2, count2, rotation2)

# use to exit game
def done():
    turtle.done()


