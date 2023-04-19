#@@@@@@@@@@@@@
# Cs 1400
#Assignment 8

import turtle
import random
def reset():
    return turtle.reset()
def setup():
    turtle.screensize(1000,800)
    turtle.speed(0)
    return ""
def setRandomColor():
    colors = ["green","blue","pink", "red", "orange","brown","aquamarine"]

    return random.choice(colors)
def drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation):
    for i in range(count):
        turtle.penup()
        turtle.goto(centerX, centerY)
        turtle.setheading(i*(360/count))
        turtle.forward(offset)
        drawRectangle(width, height, i * (360 / count) + rotation)
    return turtle.done
def drawRectangle(width, height,rotation):
    turtle.pencolor(setRandomColor())

    turtle.setheading(rotation)
    turtle.pendown()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    return ""
def drawCirclePattern(centerX, centerY, offset, radius, count):
    for i in range(count):
        turtle.penup()
        turtle.goto(centerX,centerY)
        turtle.setheading(i*(360/count))
        turtle.forward(offset)
        turtle.pendown()
        turtle.pencolor(setRandomColor())
        turtle.circle(radius)
    return turtle.done
def drawSuperPattern(num=random.randint(0,20)):
    if num<10:
        drawCirclePattern(random.randint(-300,222),random.randint(-299,225),random.randint(-20,120), random.randint(2,70),random.randint(1,100))
    elif num>=10:
        drawRectanglePattern(random.randint(-300,222),random.randint(-287,321),random.randint(-45,99), random.randint(5,300),random.randint(2,187),random.randint(2,70),random.randint(0,270))
    return turtle.done
def done():
    return turtle.done
