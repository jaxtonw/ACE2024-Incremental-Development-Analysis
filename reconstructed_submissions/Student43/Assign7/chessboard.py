# @@@@@@@@@@@@@
# CS1400 - MW1 XL
# Assignment 7

# Import turtle module and set turtle settings
import turtle 
turtle.hideturtle()
turtle.speed(0)


# Define drawChessboard function, with width and height default parameters at 250
def drawChessboard(startX, startY, width=250, height=250):
    # Draw outline of chessboard
    turtle.penup()
    turtle.goto(startX, startY)
    turtle.color("red")
    turtle.setheading(90)
    turtle.pendown()
    turtle.forward(height)
    turtle.setheading(0)
    turtle.forward(width)
    turtle.setheading(270)
    turtle.forward(height)
    turtle.setheading(180)
    turtle.forward(width)
    
    # Call drawAllRectangles to draw four rows of rectangles
    drawAllRectangles(startX, startY, width, height)
    
    # Go to the last four rows of rectangles and draw them with drawAllRectangles
    turtle.penup()
    turtle.goto(startX + (1/8) * width, startY + (1/8) * height)
    turtle.pendown()
    drawAllRectangles(startX, startY, width, height)
    turtle.done()
    

# Define drawAllRectangles function 
def drawAllRectangles(startX, startY, width, height):
    # Set a loop that will draw four rows of the chessboard
    for i in range(0, 4):
        
        # Set a loop to draw four rectangles in the row
        count = 0
        while count < 4:
            drawRectangle(startX, startY, width, height)
            turtle.setheading(0)
            turtle.penup()
            turtle.forward(width * (2/8))
            turtle.pendown()
            count += 1
            
        # Go two rows above
        turtle.setheading(180)
        turtle.penup()
        turtle.forward(width)
        turtle.setheading(90)
        turtle.forward(height * 2/8)
        

# Define drawRectangle function
def drawRectangle(startX, startY, width, height):
    # Draw one rectangle
    turtle.setheading(0)
    turtle.color("black")
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.forward(width * (1/8))
    turtle.setheading(90)
    turtle.forward(height * (1/8))
    turtle.setheading(180)
    turtle.forward(width * (1/8))
    turtle.setheading(270)
    turtle.forward(height * (1/8))
    turtle.end_fill()

