# @@@@@@@@@@
# CS 1400 - 14 week
# Assignment 7

import turtle

#draw the whole chessboard function
def drawChessboard(xPos, yPos, width = 250, height = 250):
    turtle.speed(0)
    turtle.pu()
    #draw outline
    turtle.goto(xPos, yPos)
    turtle.pd()
    turtle.setheading(0)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    #fill in the board
    drawAllRectangles(xPos, yPos, width, height)
    turtle.hideturtle()
    turtle.done()

#draw all the rectangles function    
def drawAllRectangles(xPos, yPos, width, height):
    rectWidth = width / 8
    rectHeight = height / 8
    #draw rows 1, 3, 5, and 7
    for i in range(0, 4):
        turtle.pu()
        turtle.goto(xPos, yPos + 2 * i * rectHeight)
        for j in range(0, 4):
            turtle.pd()
            drawRectangle(rectWidth, rectHeight)
            turtle.setheading(0)
            turtle.pu()
            turtle.forward(2 * rectWidth)
    #draw rows 2, 4, 6, and 8
    for k in range(0, 4):
        turtle.pu()
        turtle.goto(xPos + rectWidth, yPos + (2 * k + 1) * rectHeight)
        for l in range(0, 4):
            turtle.pd()
            drawRectangle(rectWidth, rectHeight)
            turtle.setheading(0)
            turtle.pu()
            turtle.forward(2 * rectWidth)  

#draw one rectangle function    
def drawRectangle(width, height):
    turtle.color("black")
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.end_fill()
    
