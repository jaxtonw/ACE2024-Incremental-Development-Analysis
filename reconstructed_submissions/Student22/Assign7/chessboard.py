# @@@@@@@@@@@  
# CS 1400 - MW1 XL
# Assignment 007

import turtle

turtle.speed(0)


# here is the chessboard function, it is mostly a looping function, just really long
def drawChessboard(startX, startY, width=250, height=250):
    # line 20
    drawOutline(startX, startY, width, height)
    # line 56
    drawAllRectangles(startX, startY, width, height)
    
    turtle.done()


def drawOutline(startX, startY, width, height):
    # this is the outline of the chessboard
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
    turtle.left(90)


# this is a basic rectangle function, move forward, turn left, move forward etc
def drawRectangle(width, height):
    turtle.pendown()
    turtle.fillcolor("black")
    width1 = width / 8
    height1 = height / 8
    turtle.begin_fill()
    turtle.forward(width1)
    turtle.left(90)
    turtle.forward(height1)
    turtle.left(90)
    turtle.forward(width1)
    turtle.left(90)
    turtle.forward(height1)
    turtle.left(90)
    turtle.forward(width1)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(width1)
    
    
def drawAllRectangles(startX, startY, width, height):
    width1 = width/8
    height1 = height/8
    # here is most of the code, it is just drawing the rectangles
    # I did them line by line, the loop does every square
    # in the rectangle function turtle moves forward 1 width at the end of the movement
    for i in range(0, 8):
        if i % 2 == 0:
            turtle.goto(startX, startY + height1 * i)
        else:
            turtle.goto(startX, startY + height1 * i)
            turtle.forward(width1)
        for j in range(1, 5):
            # line 36
            drawRectangle(width, height)

