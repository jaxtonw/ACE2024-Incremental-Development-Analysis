#@@@@@-@@@@@@@-Assn8
#CS1400

#Reset

#Setup
import turtle
import random
turtle.speed(0)
turtle.screensize(1000, 800)

#Set random Colors 4
colors=("Blue, Red, Orange, PUrple")
results = random.choices(colors)

#Draw Rectangle
def drawRectangle:
    turtle.penup()
    turtle.pencolor(results)
    turtle.pendown()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.leftt(90)
    turtle.forward(height)
    turtle.tiltangle(rotation)
    turtle.penup

#Draw Rectangle Pattern
def drawRectanglePattern:
    turtle.goto(centerX, centerY)
    turtle.forward(offset)
    for i in range (count):
        drawRectangle()
    turtle.left(i)
    
    
#Draw Circle Pattern
def drawCirclePattern:
    for i in range (count):
        turtle.penup()
        turtle.pencolor(results)
        turtle.goto(centerX, centerY)
        turtle.forward(offset)
        turtle.pendown()
        turtle.cirlce(radius)
    turtle.left(i)
    
        
#Draw Super Pattern 
def drawSuperPattern:
    random(drawCirclePattern(), drawRectanglePattern())
    if drawRectanglePattern():
        centerX = random.int(0, 300)
        centerY = random.int(0, 300)
        count = random.int(1,300)
        width = random.int(0, 200)
        height = random.int(0, 200)
        offset = random.int(0, 180)
        rotation = random.int (0, 90)
        
    elif drawCirclePattern():
        centerX = random.int(0, 300)
        centerY = random.int(0, 300)
        count = random.int(1,300)
        radius = random.int(1,180)
        offset = random.int(0, 180)
        
    
#Done
turtle.done

