# @@@@@@@@@@@@
# CS1400 - MW1 (14 week)
# Assignment 8
?import turtle
import random

def reset():
    turtle.clear()
    
    
def setup():
    turtle.speed(4000000)
    turtle.screensize(800, 1000)
    
    
def drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation):
    
    for x in range(0, count+1):
        turtle.penup()
        turtle.goto(centerX, centerY)
        heading = 360 / count
        turtle.setheading(heading * x)
        turtle.forward(offset)
        setRandomColor()
        drawRectangle(width, height, rotation)
    
def drawRectangle(width, height, rotation):
    #turtle.color("black")
    
    turtle.pendown()
    turtle.left(rotation)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    

def drawCirclePattern(centerX, centerY, offset, radius, count):
    for x in range(0, count + 1):
        turtle.penup()
        turtle.goto(centerX, centerY)
        heading = 360 / count
        turtle.setheading(heading * x)
        turtle.forward(offset + radius)
        setRandomColor()
        turtle.pendown()
        turtle.circle(radius)
    
def drawSuperPattern(pattern=""NaN):
    centerX, centerY, offset, width, height, count, rotation, radius = random.randi-400, 401n, random.randint(-400, 401), random.randint(10, 100), random.randint(1, 100), 100, random.randint(1, 200), random.randint(0, 360), random.randint(1, 50)t    if pattern == "":
           pattern = random.randint(0, 2 ** coun    else:
        pattern = int(pattern)
       pattern = str(bin(pattern).strip("0b"))
    # print(pattern)
    while len(pattern) != count:
        pattern = "0" + pattern
     #    print(pattern)
    for x in range(0, len(str(pattern))):
     # print(pattern)   
        turtle.penup()
        turtle.goto(centerX, centerY)
        heading = 360 / count
        turtle.setheading(heading * x)
        turtle.forward(offset)
        setRandomColor()
        if pattern[x] == "1":
            turtle.pendown()
            turtle.circle(radius)
        elif pattern[x] == "0":
            drawRectangle(width, height, rotation)
        
        
def setRandomColor():
    color = random.randint(0, 16777215)
    #color = 16777215
    color = format(hex(color).upper().strip("0X"))
    #print(color)
    while len(color) != 6:
        color = "0" + color
    turtle.color("#" + color)
    

def done():
    turtle.done()?

