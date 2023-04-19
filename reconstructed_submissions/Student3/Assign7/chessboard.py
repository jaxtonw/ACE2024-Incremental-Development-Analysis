# @@@@@@@@@@@
# CS1400 - MW1
# Assignment 7

import turtle 

def drawChessboard(startX, startY, height=250, width=250):
    # draw outline of board
    turtle.pu()
    turtle.goto(startX, startY)
    turtle.pd()
    turtle.goto(width + startX, startY)
    turtle.goto(width + startX, height + startY)
    turtle.goto(startX, height + startY)
    turtle.goto(startX, startY)
    turtle.pu()

    # call drawAllRectangles
    drawAllRectangles(startX, startY, height, width)
    return

def drawAllRectangles(startX, startY, height, width):
    # initial setup
    count = 1
    xPos = startX
    yPos = startY

    # first 16 rectangles
    while count <= 16:
        # call drawRectangle
        drawRectangle(xPos, yPos, height, width)
        xPos += width / 4
        # new row
        if count % 4 == 0:
            yPos += height / 4
            xPos = startX
        count += 1
    # re-setup
    count = 1
    xPos = startX
    yPos = startY
    # next 16 rectangles
    while count <= 16:
        # call drawRectangle
        drawRectangle(xPos + width / 8, yPos + height / 8, height, width)
        xPos += width / 4
        # new row
        if count % 4 == 0:
            yPos += height / 4
            xPos = startX
        count += 1


def drawRectangle(xPos, yPos, height, width):
    # setup
    newHeight = height / 8
    newWidth = width / 8
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.goto(xPos, yPos)
    turtle.pd()
    # draw rectangle
    turtle.goto(xPos + newWidth, yPos)
    turtle.goto(xPos + newWidth, yPos + newHeight)
    turtle.goto(xPos, yPos + newHeight)
    turtle.goto(xPos, yPos)
    turtle.end_fill()
    turtle.pu()
    return
    
