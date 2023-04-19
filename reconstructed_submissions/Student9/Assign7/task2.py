# @@@@@@@@@@@@@@@
# CS1400 - 14 Week
# Assignment 7

import turtle

def main():
    startX, startY = input("Enter at start positions:").split(",")
    width = input("Enter the width:")
    height = input("Enter the height")
    def drawChessboard(startX,startY,width,height):
        startX = int(startX)
        startY = int(startY)
        width = int(width)
        height = int(height)

        turtle.showturtle()
        turtle.pendown()
        turtle.goto(startX,startY)
        turtle.goto(startX+width,startY)
        turtle.goto(startX+width,startY+height)
        turtle.goto(startX,startY+height)
        turtle.goto(startX, startY)
        turtle.penup()
        
    if width == "" and height == "":
        drawChessboard(startX, startY)
    elif height == "":
        drawChessboard(startX, startY, width=eval(width))
    elif width == "":
        drawChessboard(startX, startY, height=eval(height))
    else:
        drawChessboard(startX, startY, eval(width), eval(height))


    def drawRectangle(width,height):
        width = int(width)
        height = int(height)
        
        turtle.begin_fill()
        turtle.pendown()
        rWidth = width/8
        rHeight = height/8

        turtle.setheading(90)
        turtle.forward(rHeight)
        turtle.setheading(0)
        turtle.forward(rWidth)
        turtle.setheading(270)
        turtle.forward(rHeight)
        turtle.setheading(180)
        turtle.forward(rWidth)
        turtle.setheading(0)
        turtle.penup()
        turtle.end_fill()
        
    def row(width):
        width = int(width)
        for r in range(4):
            drawRectangle(width, height)
            turtle.forward((width/4))
            
    def drawAllRectangles(startX,startY,width,height):
        startX = int(startX)
        startY = int(startY)
        width = int(width)
        height = int(height)
        row(width)
        turtle.goto((startX+(width/8),startY+(height/8)))
        row(width)
        turtle.goto((startX,startY+((height/8)*2)))
        row(width)
        turtle.goto((startX+(width/8),startY+((height/8)*3)))
        row(width)
        turtle.goto((startX,startY+((height/8)*4)))
        row(width)
        turtle.goto((startX+(width/8),startY+((height/8)*5)))
        row(width)
        turtle.goto((startX,startY+((height/8)*6)))
        row(width)
        turtle.goto((startX+(width/8),startY+((height/8)*7)))
        row(width)
        
        
    

    drawAllRectangles(startX,startY,width,height)r.done()

            g
