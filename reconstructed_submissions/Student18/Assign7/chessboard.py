# @@@@@@@@@@@
# CS 1400 - A01 XL
# Assignment 7

import turtle

# Draw Chessboard 
def drawChessboard(startX, startY, height = 250, width = 250):
    
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    #call the draw rectangles function 
    drawAllRectangles(startX, startY, height, width)    

# Loop the draw rectangle and adjust the position by 1/4 of the board  
def drawAllRectangles(startX, startY, height = 250, width = 250):
    startYSquare = startY
    for row in range(4): 
        startXSquare = startX
        for column in range(4): 
            turtle.penup()
            turtle.goto(startXSquare,startYSquare)
            turtle.pendown()
            # call the draw rectangle function 
            drawRectangle(height/8, width/8)
            startXSquare += width / 4
        startYSquare += height / 4
    startYSquare = startY
    startYSquare += height/8
    for row in range(4):
        startXSquare = startX
        startXSquare += width/8 
        for column in range(4):
            turtle.penup()
            turtle.goto(startXSquare, startYSquare)
            turtle.pendown()
            # call the draw rectangle function 
            drawRectangle(height / 8, width / 8)
            startXSquare += width / 4
        startYSquare += height / 4
           

    # Draw the single rectangle function 
def drawRectangle(height, width):
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor("black")
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.end_fill()
    turtle.penup()
  
   
             
                       
        
        
        
