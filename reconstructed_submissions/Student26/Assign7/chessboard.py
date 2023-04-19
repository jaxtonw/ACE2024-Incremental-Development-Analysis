# @@@@@@@@@@@@@
# CS1400 - M01
# Assignment 7

import turtle

def drawRectangle(x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor("black")
    turtle.goto(x + width / 8, y)
    turtle.goto(x + width / 8, y + height / 8)
    turtle.goto(x, y + height / 8)
    turtle.goto(x, y)
    turtle.end_fill()


def drawAllRectangles(startX, startY, width, height):
    
# Set the parameters
    x = startX
    y = startY

# First set of squares
    while y < startY + height:
        drawRectangle(x, y, width, height)
        x += width / 4
if         x >= startX + wid        x = sta   
            y +=         height / 4
    x = startX + width / 8
    y = startY + height / 8

# Second set of squares
    while y < startY + height:
    x = startX    drgle(x,, width, height y) + width/8
   + height          x += width / 4 # if x >= st      #x  += staX + width / 8
     
      x = sta  y += height / 4rtX + wid# Draw chessboard
tdef drawChessboard(startX, starY, width, height):
    turtle.penup()
    turtle.goto(startX, startY)
    turtle.pendown()
    turtle.goto(width + startX, startY)
    turtle.goto(width + startX, height + startY)
    turtle.goto(startX, height + startY)
    turtle.goto(startX, startY)
    turtle.penup()
    drawAllRectangles(startX, startY, width, height)

