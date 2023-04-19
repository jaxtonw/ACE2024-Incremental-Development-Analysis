# @@@@@@@@@@@@@
# CS1400 - MW1
# Assignment 7

import turtle


def drawRectangle(width, height):
    turtle.pendown()
    turtle.fillcolor("black")
    turtle.pencolor("black")
    turtle.begin_fill()
    turtle.forward(width / 8)
    turtle.left(90)
    turtle.forward(height / 8)
    turtle.left(90)
    turtle.forward(width / 8)
    turtle.left(90)
    turtle.forward(height / 8)
    turtle.left(90)
    turtle.end_fill()
    turtle.penup()
   
    
def drawAllRectangles(width, height):
    for i in range(0, 4):
        for j in range(0, 4):
            drawRectangle(width, height)
            turtle.forward(width / 4)
        turtle.back(width)
        turtle.left(90)
        turtle.forward(height/4)
        turtle.right(90)


def drawChessboard(startX, startY, width=250, height=250):
    startX = eval(startX)
    startY = eval(startY)
    turtle.speed(18)
    turtle.penup()
    turtle.goto(startX, startY)
    turtle.setheading(0)
    turtle.pencolor("red")
    turtle.pendown()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.penup()
    drawAllRectangles(width, height)
    turtle.goto(startX + width/8, startY + height/8)
    drawAllRectangles(width, height)
    turtle.hideturtle()
    turtle.done()
    

            

