# @@@@@@@@@@@@@@
# CS1400 - 001
# Assignment 7

import turtle

def drawChessboard(startX, startY, width=250, height=250):
    # Draw chessboard
    turtle.penup()
    turtle.goto(startX, startY)
    turtle.pendown()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    drawAllRectangles(startX, startY, width, height)

    turtle.hideturtle()
    turtle.done()


def drawAllRectangles(startX, startY, width, height):
    x = 0
    littleWidth = width / 8
    littleHeight = height / 8
    turtle.speed(0)
    # First row
    for i in range(0, 4):    
        turtle.penup()
        turtle.goto(startX + x, startY)
        turtle.pendown()
        turtle.left(90)
        turtle.begin_fill()
        turtle.forward(littleWidth)
        turtle.left(90)
        turtle.forward(littleHeight)
        turtle.left(90)
        turtle.forward(littleWidth)
        turtle.left(90)
        turtle.forward(littleHeight)
        turtle.end_fill()
        x += (2 * littleWidth)
    x = 0
    # Second row
    for i in range(0, 4):
        turtle.penup()
        turtle.goto(startX + x, startY + (2 * littleHeight))
        turtle.pendown()
        turtle.left(90)
        turtle.begin_fill()
        turtle.forward(littleWidth)
        turtle.left(90)
        turtle.forward(littleHeight)
        turtle.left(90)
        turtle.forward(littleWidth)
        turtle.left(90)
        turtle.forward(littleHeight)
        turtle.end_fill()
        x += (2 * littleWidth)
    x = 0
    # Third row
    for i in range(0, 4):
        turtle.penup()
        turtle.goto(startX + x, startY + (4 * littleHeight))
        turtle.pendown()
        turtle.left(90)
        turtle.begin_fill()
        turtle.forward(littleWidth)
        turtle.left(90)
        turtle.forward(littleHeight)
        turtle.left(90)
        turtle.forward(littleWidth)
        turtle.left(90)
        turtle.forward(littleHeight)
        turtle.end_fill()
        x += (2 * littleWidth)
    x = 0
    # Second row
    for i in range(0, 4):
        turtle.penup()
        turtle.goto(startX + x, startY + (6 * littleHeight))
        turtle.pendown()
        turtle.left(90)
        turtle.begin_fill()
        turtle.forward(littleWidth)
        turtle.left(90)
        turtle.forward(littleHeight)
        turtle.left(90)
        turtle.forward(littleWidth)
        turtle.left(90)
        turtle.forward(littleHeight)
        turtle.end_fill()
        x += (2 * littleWidth)
        
    # First offset row
    x = 0
    for i in range(0, 4):
        turtle.penup()
        turtle.goto(startX + littleWidth + x, startY + littleHeight)
        turtle.pendown()
        turtle.left(90)
        turtle.begin_fill()
        turtle.forward(littleWidth)
        turtle.left(90)
        turtle.forward(littleHeight)
        turtle.left(90)
        turtle.forward(littleWidth)
        turtle.left(90)
        turtle.forward(littleHeight)
        turtle.end_fill()
        x += (2 * littleWidth)
    x = 0
    # Second offset row
    for i in range(0, 4):
        turtle.penup()
        turtle.goto(startX + littleWidth + x, startY + (3 * littleHeight))
        turtle.pendown()
        turtle.left(90)
        turtle.begin_fill()
        turtle.forward(littleWidth)
        turtle.left(90)
        turtle.forward(littleHeight)
        turtle.left(90)
        turtle.forward(littleWidth)
        turtle.left(90)
        turtle.forward(littleHeight)
        turtle.end_fill()
        x += (2 * littleWidth)
    x = 0
    # Third offset row
    for i in range(0, 4):
        turtle.penup()
        turtle.goto(startX + littleWidth + x, startY + (5 * littleHeight))
        turtle.pendown()
        turtle.left(90)
        turtle.begin_fill()
        turtle.forward(littleWidth)
        turtle.left(90)
        turtle.forward(littleHeight)
        turtle.left(90)
        turtle.forward(littleWidth)
        turtle.left(90)
        turtle.forward(littleHeight)
        turtle.end_fill()
        x += (2 * littleWidth)
    x = 0
    # Forth offset row
    for i in range(0, 4):
        turtle.penup()
        turtle.goto(startX + littleWidth + x, startY + (7 * littleHeight))
        turtle.pendown()
        turtle.left(90)
        turtle.begin_fill()
        turtle.forward(littleWidth)
        turtle.left(90)
        turtle.forward(littleHeight)
        turtle.left(90)
        turtle.forward(littleWidth)
        turtle.left(90)
        turtle.forward(littleHeight)
        turtle.end_fill()
        x += (2 * littleWidth)

