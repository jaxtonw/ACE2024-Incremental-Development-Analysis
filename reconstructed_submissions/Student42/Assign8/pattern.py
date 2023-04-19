# @@@@@@@@@@@@@
# CS1400 - 14 week
# Assignment 8

import turtle
import random
from random import randint


def setup():
    turtle.setup(1000, 800)
    turtle.speed(0)


def reset():
    turtle.reset()
    turtle.speed(0)
    turtle.setup(1000, 800)

def done():
    turtle.done()


def drawRectangle(width, height, rotation):
    color = "blue"
    num = random.randint(1, 4)
    if num == 1:
        color = "blue"
    elif num == 2:
        color = "red"
    elif num == 3:
        color = "green"
    elif num == 4:
        color = "orange"
    turtle.color(color)
    turtle.setheading(rotation)
    turtle.forward(width)
    turtle.setheading(rotation + 90)
    turtle.forward(height)
    turtle.setheading(rotation + 180)
    turtle.forward(width)
    turtle.setheading(rotation + 270)
    turtle.forward(height)

setup()

def drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation):
    for i in range(1, count + 1):
        angle = 360 / count
        angle += angle * i
        turtle.pu()
        turtle.goto(centerX, centerY)
        turtle.setheading(angle)
        turtle.forward(offset)
        turtle.pd()
        drawRectangle(width, height, rotation + angle)
        
def drawCirclePattern(centerX, centerY, offset, radius, count):
    for i in range(1, count + 1):
        angle = 360 / count
        angle += angle * i
        color = "blue"
        num = random.randint(1, 4)
        if num == 1:
            color = "blue"
        elif num == 2:
            color = "red"
        elif num == 3:
            color = "green"
        elif num == 4:
            color = "orange"
        turtle.color(color)
        turtle.pu()
        turtle.goto(centerX, centerY)
        turtle.setheading(angle)
        turtle.forward(offset + radius)
        turtle.setheading(270)
        turtle.forward(radius)
        turtle.setheading(0)
        turtle.pd()
        turtle.circle(radius)
        
def drawSuperPattern(num=""):
    if num == "":
        num = randint(1, 10)
    for i in range(1, num + 1):
        choose = random.randint(1, 2)
        if choose == 1:
            drawRectanglePattern(randint(-250, 250), randint(-200, 200), randint(0, 200), randint(0, 200), randint(0, 200), randint(0, 200), randint(-360, 360))
        elif choose == 2:
                drawCirclePattern(randint(-250, 250), randint(-200, 200), randint(0, 200), randint(0, 200),  randint(0, 200))
            
