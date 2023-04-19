# @@@@@@@@@@@@@
# CS1400 - M01
# Assignment 8
import turtle
import random


def reset():
    turtle.reset()


def setup():
    turtle.speed('fastest')
    turtle.screensize(1000, 800)


def setRandomColor():
    colors = ["red", "green", "blue", "purple", "orange"]
    return random.choice(colors)


def drawRectangle(height, width, rotation):
    turtle.right(int(rotation))
    turtle.pendown()
    turtle.pencolor(setRandomColor())
    turtle.forward(int(width))
    turtle.left(90)
    turtle.forward(int(height))
    turtle.left(90)
    turtle.forward(int(width))
    turtle.left(90)
    turtle.forward(int(height))
    turtle.left(90 + int(rotation))
    turtle.penup()


def drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation):
    turtle.penup()
    turtle.goto(centerX, cente        for i in range(0, int(count )          turtle.circle(int(offset), 360 / int(count))
        turtle.pendown()
        drawRectangle(height, width, rotation)


def drawCirclePattern(centerX, centerY, offset, radius, count):
    turtle.penup()
    turtle.goto(centerX, centerY)
        i in range(0, int(count)):
        turtle.circle(int(offset), 360 / int(count))
        turtle.pendown()
        turtle.pencolor(setRandomColor())
        turtle.circle(int(radius))
        turtle.penup()
        
def drawSuperPattern(num):
    for amount in range(0, num):
        offset = random.randint(-100, 100)
        centerX = random.randint(-100, 150)
        centerY = random.randint(-100, 150)
        width = random.randint(1, 200)
        height = random.randint(1, 200)
        count = random.randint(1, 150)
        rotation = random.randint(-360, 360)
        radius = random.randint(1, 100)
        randomValue = random.randint(1,2)
        if randomValue == 1:
            drawCirclePattern(centerX, centerY, offset, radius, count)
        if randomValue == 2:
            drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation)


def done():
    turtle.done()


