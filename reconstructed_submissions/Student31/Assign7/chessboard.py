# @@@@@@@@@@@
# CS1400 - MW1 XL
# Assignment 7
import turtle

width = 100
height = 100
def drawAllRectangles(width, height):
    rectangleWidth = width/8
    rectangleHeight = height/8
    turtle.penup()
    turtle.goto(startX, startY)
    turtle.pendown()
    turtle.begin_fill(black)
    turtle.forward(rectangleWidth)
    turtle.right(-90)
    turtle.forward(rectangleHeight)
    turtle.right(-90)
    turtle.forward(rectangleWidth)
    turtle.right(-90)
    turtle.forward(rectangleHeight)
    turtle.penup()
    turtle.forward(2 * rectangleWidth)
    
def drawChessboard (startX, startY):
    import math
    import turtle
    turtle.goto(startX, startY)
    turtle.pendown()
    turtle.forward(width)
    turtle.right(-90)
    turtle.forward(height)
    turtle.right(-90)
    turtle.forward(width)
    turtle.right(-90)
    turtle.forward(height)
    turtle.done()
    drawAllRectangles(100,100)
    
drawChessboard(0,0)


