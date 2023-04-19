import turtle
import random


def setup():
    turtle.speed(0)
    turtle.setup(1000, 800)


def drawRectanglePattern(centerX, centerY, width, height, rotation, count, offset):
    for rectangle in range(count):
        turtle.penup()
        turtle.goto(centerX, centerY)
        turtle.setheading(rotation)
        turtle.left((360 / count) * rectangle)
        turtle.forward(offset)
        turtle.pendown()
        turtle.color(setRandomColor())
        drawRectangle(width, height)
       
            
def drawCirclePattern(centerX, centerY, offset, radius, count):
    for circle in range(count):
        turtle.penup()
        turtle.goto(centerX, centerY)
        turtle.setheading(0)
        turtle.left((360 / count) * circle) 
        turtle.forward(offset)
        turtle.right(90)
        turtle.pendown()
        turtle.color(setRandomColor())
        drawCircle(radius)
        turtle.left(90)
        
        
def drawCircle(radius):
    turtle.circle(radius)
            
            
def drawRectangle(width, height):
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    
    
def drawSuperPattern(num):
    for superPattern in range(num):
        randomPattern = random.randint(1, 2)
        if randomPattern == 1:
            drawRectanglePattern(centerX=random.randint(-350, 350), centerY=random.randint(-200, 200), 
                                 width=random.randint(5, 125), height=random.randint(5, 125),
                                 rotation=random.randint(-90, 90),
                                 count=random.randint(10, 75), offset=random.randint(-100, 100))
        elif randomPattern == 2:
            drawCirclePattern(centerX=random.randint(-350, 350), centerY=random.randint(-200, 200),
                              count=random.randint(10, 75), offset=random.randint(-100, 100),
                              radius=random.randint(10, 100))
    
    
def setRandomColor():
    color = random.randint(1, 5)
    if color == 1:
        return "blue"
    elif color == 2:
        return "green"
    elif color == 3:
        return "black"
    elif color == 4:
        return "red"
    else:
        return "orange"
    
    
def done():
    turtle.done()
    
    
def reset():
    turtle.reset()
    turtle.speed(0)
    
