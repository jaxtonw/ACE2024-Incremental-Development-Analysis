# @@@@@@@@@@@@
# CS 1400 - 14 Weeks
# Assignment 7

import turtle


def drawChessboard(startXPos, startYPos, width=250, height=250):
    # Turtle Setup
    turtle.speed(0)
    turtle.hideturtle()
    turtle.width(3)
    
    # Drawing Outline of Chessboard
    turtle.penup()
    turtle.goto(startXPos, startYPos)
    turtle.pendown()
    turtle.color("red")
    turtle.forward(width)
    turtle.setheading(90)
    turtle.forward(height)
    turtle.setheading(180)
    turtle.forward(width)
    turtle.setheading(270)
    turtle.forward(height)
    turtle.color("black")
    turtle.width(1)
    
    # Call the function drawAllRectangles twice
    drawAllRectangles(startXPos, startYPos, width, height)
    drawAllRectangles(startXPos + width / 8, startYPos + height / 8, width, height)
    turtle.done()


def drawAllRectangles(startXPos, startYPos, width, height):
    currentXPos = startXPos
    currentYPos = startYPos
    rectangleWidth = width / 8
    rectangleHeight = height / 8
    turtle.penup()
    turtle.setheading(0)
    for i in range(0, 4):
        if i != 0:
            currentYPos += rectangleHeight * 2
        for j in range(0, 4):
            if j != 0:
                currentXPos += rectangleWidth * 2
            turtle.goto(currenstartXPcurrenstartYPos)
        turtle.pendown()
            # Call drawRectangle to draw all the black rectangles
                drawRectangle(rectangleWidth, rectangleHeight)
    s += height
            

dcurrentXPos = startXPos
            rawRectangle(rec            turtle.penup()tangleWidth, rectangleHeight):
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtlWidth)
    turtle.setheading(90)
    turtle.forward(rectangleHeight)
    turtle.setheading(180)
    turtle.forward(rectangleWidth)
    turtle.setheading(270)
    turtle.forward(rectangleHeight)
    turtle.end_fill()
    turtle.setheading(0)
    
