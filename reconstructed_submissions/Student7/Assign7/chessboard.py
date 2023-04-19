# @@@@@@@@@@@@
# CS1400 - MW1
# Assignment 7

import turtle

def drawRectangle(width,height):
    turtle.pendown()
    turtle.pencolor("Black")
    turtle.fillcolor("Black")
    turtle.setheading(0)
    turtle.begin_fill()
    # Draw the sides of the rectangle, rotate each time
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.end_fill()
    turtle.penup()
    turtle.setheading(0)
    # Go to bottom right corner
    turtle.forward(width)

def drawAllRectangles(xPosition,yPosition,width,height):
    # Loop for rows
    for row in range(1,8 + 1):
        if row % 2 == 0:
            # Draw rectangles in the columns
            for columnEvenRow in range(1,8 + 1):
                if columnEvenRow % 2 == 0:
                    turtle.forward(width / 8)
                else:
                    drawRectangle(width / 8,height / 8)
        else:
            for columnOddRow in range(1,8 + 1):
                if columnOddRow % 2 == 0:
                    drawRectangle(width / 8, height / 8)
                else:
                    turtle.forward(width / 8)
        # Move up to the next row
        turtle.goto(xPosition,yPosition + height / 8 * row)

def drawChessboard(xPos, yPos, width=250, height=250):
    turtle.showturtle()
    turtle.speed(0)
    turtle.penup()
    turtle.pencolor("Blue")
    # Move to the starting position
    turtle.goto(xPos, yPos)
    turtle.setheading(0)
    turtle.pendown()
    # Draw the border
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.setheading(0)
    # Draw the rectangles
    drawAllRectangles(xPos,yPos,width,height)
    turtle.hideturtle()
    turtle.done()
