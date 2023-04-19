# @@@@@@@@@@@@
# CS1400 - MW1 (14 week)
# Assignment 6

import turtle


def drawChessboard(startX, startY, width=250, length=250):
    turtle.penup()
    turtle.goto(startX, startY)
    drawRectangle(width, length, "blue", "white")
    drawAllRectangles(startX, startY, width/8, length/8)
    turtle.done()


def drawAllRectangles(startX, startY, width, length):
    for j in range(0, 8, 2):
        for i in range(0, 8):
            if i % 2 == 0:
                turtle.goto(startX + (i * width), startY + length + (j * length))
                drawRectangle(width, length)
            
            else:
                turtle.goto(startX + (i * width), startY + (j * length))
                drawRectangle(width, length)
    


def drawRectangle(width, length, color="black", fillColor="black"):
    turtle.color(color)
    turtle.fillcolor(fillColor)
    turtle.begin_fill()
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(width)
    turtle.setheading(90)
    turtle.forward(length)
    turtle.setheading(180)
    turtle.forward(width)
    turtle.setheading(-90)
    turtle.forward(length)
    turtle.setheading(90)
    turtle.end_fill()
    turtle.penup()

