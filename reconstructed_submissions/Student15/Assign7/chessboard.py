# @@@@@@@@@@@@@@
# CS 1400 - 14 week
# Assignment 7

import turtle 

# drawChessboard function
# 1. Create formal parameter for the start position, width and height from the caller of the function
def drawChessboard(startX, startY, width=250, height=250):
    # 2. Draw rectangle starting with r@@@@, then up, then left, then down directions
    turtle.setup(1000, 800)
    turtle.penup()
    turtle.speed(10)
    turtle.pencolor("blue")
    turtle.goto(startX, startY)
    turtle.pendown()
    turtle.goto(startX + width, startY)
    turtle.goto(startX + width, startY + height)
    turtle.goto(startX, startY + height)
    turtle.goto(startX, startY)
    drawAllRectangles(startX, startY, width, height)
    turtle.penup()
    startX = startX + (width / 8)
    startY = startY + (height / 8)
    turtle.goto(startX, startY)
    drawAllRectangles(startX, startY, width, height)
    turtle.done()
    
    
    # 3. call drawAllRectangles

def drawAllRectangles(startX, startY, width, height):
    rowCount = 0
    tileCount = 0
    tileX = width / 8
    tileY = height / 8
    
    turtle.pencolor("black")
    while rowCount != 4:
        for a in range(0, 8, 2):
            yPos = a * tileY
            turtle.goto(startX, startY + yPos)
            while tileCount != 4:
                for i in range(0, 8, 2):
                    
                    turtle.goto(startX + (i * tileX), startY + yPos)
                    drawRectangle(width, height, tileCount)
                    tileCount += 1
            tileCount = 0
            rowCount += 1
        
        
        
    
def drawRectangle(width, height, tileCount):
    turtle.pendown()
    turtle.setheading(0)
    turtle.begin_fill()
    turtle.fillcolor("black")
    turtle.forward(width / 8)
    turtle.setheading(90)
    turtle.forward(height / 8)
    turtle.setheading(180)
    turtle.forward(width / 8)
    turtle.setheading(270)
    turtle.forward(height / 8)
    turtle.end_fill()
    turtle.penup()
    # @@@@@@@@@@@@@@
# CS 1400 - 14 week
# Assignment 7


