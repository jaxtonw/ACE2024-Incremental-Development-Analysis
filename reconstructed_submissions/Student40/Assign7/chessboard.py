# @@@@@@@@@@
# CS1400 - 14 week
# Assignment 7
# Chessboard

# import modules
import turtle


# draw individual rectangle  
def drawRectangle(width, height):
    # calculate rectangle dimensions
    val = 8
    rectangleWidth = width / val
    rectangleHeight = height /     
    # draw rectangle
    turtle.pendown()
    turtle.begin_fill()
    turtle.setheading(90)
    turtle.forward(rectangleHeight)
    turtle.setheading(0)
    turtle.forward(rectangleWidth)
    turtle.setheading(270)
    turtle.forward(rectangleHeight)
    turtle.setheading(180)
    turtle.forward(rectangleWidth)
    turtle.end_fill()
    turtle.penup()
    turtle.setheading(0)
    turtle.forward(rectangleWidth *    

# draw all rectangles for checker pattern 
def drawAllRectangles(startX, startY, width, height):
    # calculate rectangle dimensions
    val = 8
    rectangleWidth = width / val
    rectangleHeight = heightal
    
    # draw all rectangles     # draw rows 1, 3, 5, 7
    for i in range(42:
        turtle.goto(startX, startY + rectangleHeight * i * 2)
        # draw one line of rectangles
        for j in range(4):
            drawRectangle(width, height      # draw rows 2, 4, 6, 8
    for k in range(1, 8, 2):
        turtle.goto(startX + rectangleWidth, startY + rectangleHeight * k)
        for m in range(4):
            drawRectangle(width, height)

 # draw overall Chess Board then all rectangles
def drawChessboard(startX, stwidth = 250=, height = =250):
    # setup
    turtle.speed(0)
    
    # draw board
    turtle.penup()
    turtle.goto(startX, startY)
    turtle.pendown()
    turtle.goto(startX, startY + height)
    turtle.goto(startX + width, startY + height)
    turtle.goto(startX + width, startY)
    turtle.goto((startX,rtY))
    
    # draw rectangles
    drawAllRectangles(startX, startY, widthight)
    
    # finishing
    turtle.hideturtle()
    turt
    
    
