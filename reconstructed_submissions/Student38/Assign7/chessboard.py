# @@@@@@@@@@@@@
# CS-1400 MW1
# Assignment 7

# import module
import turtle
# basic starting functions for turtle module
turtle.showturtle()
turtle.speed(0)

# create function to draw a single black rectangle
def drawRectangle(height2, width2):
    turtle.pendown()
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.forward(height2)
    turtle.right(90)
    turtle.forward(width2)
    turtle.right(90)
    turtle.forward(height2)
    turtle.right(90)
    turtle.end_fill()
    turtle.penup()

# create a function to tell other function where and how many times to draw\
    # the black rectangle
def drawAllRectangles(x1, y1, height1, width1):
    recHeight = int(height1 / 8)
    recWidth = int(width1 / 8)
    step1 = int(recHeight * 2)
    step2 = int(recWidth * 2)
    for i in range(y1, (y1 + height1 - recHeight), step1):
        for j in range(x1, (x1 + width1 - recWidth), step2):
            turtle.penup()
            turtle.goto(i, j)
            turtle.setheading(90)
            drawRectangle(recHeight, recWidth)

# create function to draw outside of chessboard, also defines where second\
    # row of rectangles begin
def drawChessboard(xCoor, yCoor, width=250, height=250):
    turtle.penup()
    turtle.goto(xCoor, yCoor)
    turtle.setheading(90)
    turtle.pensize(1)
    turtle.pencolor("red")
    turtle.pendown()
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.penup()
    turtle.goto(xCoor, yCoor)
    turtle.pencolor("black")
    drawAllRectangles(xCoor, yCoor, height, width)
    newX = int(xCoor + (width / 8))
    newY = int(yCoor + (height / 8))
    turtle.goto(newX, newY)
    drawAllRectangles(newX, newY, height, width)
    turtle.hideturtle()
    turtle.done()

    


