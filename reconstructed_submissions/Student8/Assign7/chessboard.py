# @@@@@@@@@@@@@
# CS1400 - MW1
# Assignment 7

import turtle

# define the drawChessBoard() function
def drawChessboard(startX, startY, width=250, height=250):
    
    # set the turtle speed to something quick
    turtle.speed(200)

    # draw the outline of the chessboard
    turtle.penup()
    turtle.goto(startX, startY)
    turtle.pendown()
    turtle.setheading(0) # sets heading to the right
    turtle.forward(width)
    turtle.left(90) # turn left by 90 degrees
    turtle.forward(height)
    turtle.left(90) # turn left by 90 degrees
    turtle.forward(width)
    turtle.left(90) # turn left by 90 degrees
    turtle.forward(height)
    
    # call drawAllRectangles() for rows 1, 3, 5, and 7
    drawAllRectangles(startX, startY, width, height)
    
    # call drawAllRectangles() for rows 2, 4, 6, and 8
    turtle.penup()
    turtle.goto(startX + (width / 8), startY + (height / 8))
    turtle.pendown()
    drawAllRectangles(startX + (width / 8), startY + (height / 8), width, height)
    
    # keeps the drawing on screen
    turtle.done()

    
# define drawAllRectangles() function
def drawAllRectangles(startX, startY, width, height):
    
    # find the width and height of each individual rectangle in the chessboard
    rectangleWidth = width / 8
    rectangleHeight = height / 8
    
    # make a loop for every other row
    for i in range(2, 10, 2):
        
        # make a loop for every black rectangle in the row
        for j in range(4):
            
            # keep track of number of rectangles drawn with this variable
            rectangleNumber = 0
            
            # draw a black rectangle using the drawRectangle function
            drawRectangle(rectangleWidth, rectangleHeight)
            rectangleNumber += 1
            
            # skip over the white rectangle
            if rectangleNumber < 4:
                
                turtle.setheading(0) # sets heading to the right
                turtle.penup()
                turtle.forward(rectangleWidth * 2)
                turtle.pendown()
            
        # go up two rows
        turtle.penup()
        turtle.goto(startX, startY + (rectangleHeight * i))
        turtle.pendown()

        
# define the drawRectangle() function
def drawRectangle(rectangleWidth, rectangleHeight):
    
    # set the rectangle color to black
    turtle.fillcolor("black")

    # draw the rectangle
    turtle.begin_fill()
    turtle.setheading(0) # line starts out going to the right
    turtle.forward(rectangleWidth)
    turtle.left(90)  # turn left by 90 degrees
    turtle.forward(rectangleHeight)
    turtle.left(90)  # turn left by 90 degrees
    turtle.forward(rectangleWidth)
    turtle.left(90)  # turn left by 90 degrees
    turtle.forward(rectangleHeight)
    turtle.end_fill()
