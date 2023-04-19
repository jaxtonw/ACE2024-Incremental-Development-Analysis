import turtle
import random


# setup
def setup():
    # set the speed of turtle
    turtle.speed(0)



def drawChessboard(startX, startY, width, height):
    
    turtle.penup()
    turtle.speed(0)
    turtle.setheading(0)
    turtle.goto(startX, startY)
    turtle.pendown()
    turtle.forward(width)
    turtle.setheading(90)
    turtle.forward(height)
    turtle.setheading(180)
    turtle.forward(width)
    turtle.setheading(270)
    turtle.forward(height)
    turtle.setheading(0)
    squareX = width/8
    squareY = height/8
    for j in range(1,5):
        
        for i in range(1,5):
            turtle.begin_fill()
            turtle.forward(squareX)
            turtle.setheading(90)
            turtle.forward(squareY)
            turtle.setheading(180)
            turtle.forward(squareX)
            turtle.setheading(270)
            turtle.forward(squareY)
            turtle.setheading(0)
            turtle.forward(squareX)
            turtle.end_fill()
            turtle.forward(squareX)
            turtle.setheading(90)
            turtle.forward(squareY)
            turtle.setheading(180)
            turtle.forward(squareX)
            turtle.setheading(270)
            turtle.forward(squareY)
            turtle.setheading(0)
            turtle.forward(squareX)
        turtle.penup()
        turtle.setheading(180)
        turtle.forward(width)
        turtle.setheading(90)
        turtle.forward(squareY)
        turtle.setheading(0)
        turtle.pendown()
        for k in range(1, 5):
            turtle.forward(squareX)
            turtle.setheading(90)
            turtle.forward(squareY)
            turtle.setheading(180)
            turtle.forward(squareX)
            turtle.setheading(270)
            turtle.forward(squareY)
            turtle.setheading(0)
            turtle.forward(squareX)
            turtle.begin_fill()
            turtle.forward(squareX)
            turtle.setheading(90)
            turtle.forward(squareY)
            turtle.setheading(180)
            turtle.forward(squareX)
            turtle.setheading(270)
            turtle.forward(squareY)
            turtle.setheading(0)
            turtle.forward(squareX)
            turtle.end_fill()
        turtle.penup()
        turtle.setheading(180)
        turtle.forward(width)
        turtle.setheading(90)
        turtle.forward(squareY)
        turtle.setheading(0)
        turtle.pendown()


# done()
#def done():
    turtle.done()

