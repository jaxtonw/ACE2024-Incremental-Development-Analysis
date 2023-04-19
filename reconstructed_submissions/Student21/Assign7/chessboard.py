# @@@@@@@@@@@@@@@@
# CECS1400 - MW1
# Assignment 7-Chessboard

import turtle

# define drawRectangle
def drawRectangle(width, height):
    turtle.setheading(90)
    turtle.pendown()
    turtle.color("black")
    turtle.width(1)
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.forward(height * (1/8))
    turtle.right(90)
    turtle.forward(width * (1/8))
    turtle.right(90)
    turtle.forward(height * (1/8))
    turtle.right(90)
    turtle.forward(width * (1/8))
    turtle.right(90)
    turtle.end_fill()
    turtle.penup()

# define drawAllRectangles
def drawAllRectangles(startX, startY, width, height):
    # row 1, 3, 5, 7
    for i in range(0, 8, 2):
        for j in range(0, 8, 2):
            turtle.goto(startX + (width * (1 /8) * j), startY + (height * (1 / 8)) * i)
            drawRectangle(width, height)
    # row 2, 4, 6, 8
    for k in range(1, 9, 2):
        for l in range(1, 9, 2):
            turtle.goto(startX + (width * (1 / 8) * l), startY + (height * (1 / 8)) * k)
            drawRectangle(width, height)

# define drawChessboard
def drawChessboard(startX, startY, width=250, height=250):
    turtle.goto(startX, startY)
    turtle.setheading(90)
    turtle.pendown()
    turtle.color("black")
    turtle.width(1)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.penup()
    drawAllRectangles(startX, startY, width, height)

    turtle.done()
###
