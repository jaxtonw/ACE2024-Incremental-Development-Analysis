# @@@@@@@@@@@@@@@
# CS 1400- 14 week
# Assignment 7

import turtle

def drawChessboard(startX, startY, width=250, height=250):
    turtle.penup()
    turtle.goto(startX,startY)
    turtle.pendown()
    turtle.goto(startX + width,startY)
    turtle.goto(startX + width, startY + height)
    turtle.goto(startX,startY + height)
    turtle.goto(startX, startY)

    drawAllRectangles(startX, startY, width, height)
    turtle.done()
def drawAllRectangles(startX, startY, width=250, height=250):
    rectangleWidth = width / 8
    rectangleHeight = height / 8
    
    drawAllRectangles2(startX,startY, width ,height)
    drawAllRectangles2(startX + rectangleWidth,startY + rectangleHeight, width ,height)
    
def drawAllRectangles2(startX, startY, width, height):
    rectangleWidth = width / 8
    rectangleHeight = height / 8
    #x for loop
    currentY = startY
    
    
    for i in range(0,4):
        turtle.penup()
        turtle.goto(startX, currentY)
        
        #y for loop
        for j in range(0,4):
            turtle.goto(startX, currentY)
            turtle.pendown()
            drawRectangle(startX, currentY, rectangleWidth, rectangleHeight)
            currentY += rectangleHeight * 2
            turtle.penup()
        currentY = startY
        startX += rectangleWidth * 2
            
def drawRectangle(startX, startY, rectangleWidth, rectangleHeight):
    turtle.penup()
    turtle.goto(startX + rectangleWidth, startY)
    turtle.pendown()
    turtle.begin_fill() 
    turtle.goto(startX + rectangleWidth, startY + rectangleHeight)
    turtle.goto(startX, startY + rectangleHeight)
    turtle.goto(startX, startY)
    turtle.goto(startX + rectangleWidth,startY)
    turtle.end_fill()


