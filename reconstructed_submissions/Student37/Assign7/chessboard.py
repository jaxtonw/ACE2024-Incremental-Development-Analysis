# @@@@@@@@@
# CS1400 - MW1
# Assignment 7 - task2 (chessboard)

import turtle

t = turtle
t.pencolor("#000000")  # format color
t.fillcolor("#000000")
t.speed(0)


def drawChessboard(startX, startY, width=250, height=250):
    t.screensize(width, height)  # format window

    t.up()
    t.goto(startX, startY)
    t.setheading(0)
    t.down()

    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)  # creates the box
    t.left(90)
    t.forward(height)
    t.left(90)

    drawAllRectangles(startX, startY, width, height)

    t.done()


def drawAllRectangles(startX, startY, width, height):
    oneWidth = width / 8
    oneHeight = height / 8

    for i in range(0, 8):
        t.up()
        t.forward(oneHeight * i)

        if i % 2 == 0:  # this if/else actually creates the checkerboard pattern
            t.setheading(0)
        else:
            t.up()
            t.setheading(0)
            t.forward(oneWidth)  # moves to next position

        for j in range(0, 4):
            drawRectangle(oneWidth, oneHeight)
            t.setheading(0)
            t.up()
            t.forward(oneWidth * 2)  # moves to next position

        t.up()
        t.goto(startX, startY)
        t.setheading(0)  # moves up to the next row
        t.left(90)


def drawRectangle(width, height):
    t.down()
    t.begin_fill()

    t.forward(width)
    t.left(90)
    t.forward(height)  # draws one rectangle
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)

    t.end_fill()

