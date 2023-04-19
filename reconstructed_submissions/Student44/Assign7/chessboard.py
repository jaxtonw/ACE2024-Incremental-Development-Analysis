# @@@@@@@@@@@@
# CS1400 - MW 1
# Assignment 7

import turtle


# define function to draw board
def drawChessboard(startX, startY, width=250, height=250):
    
    # draw the board outline
    turtle.penup()
    turtle.color("red")
    turtle.goto(startX, startY)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.color("black")
    turtle.penup()
    
    # drawing all black squares
    drawAllRectangles(startX, startY, width, height)
    
    # keeping window open
    turtle.done()
 
 
# define function to draw the black squares on the board
def drawAllRectangles(startX, startY, width, height):
    
    for l in range(0, 4):
        turtle.sety(startY + (height / 4) * l)
        turtle.setx(startX)
        for i in range(0, 4):
            drawRecangle(width, height)
            turtle.setx(turtle.xcor() + (width / 8) * 2)
            
    # using these to make the rectangles offset in the x and y directions   
    xRef = startX + (width / 8)
    yRef = startY + (height / 8)
    
    
    # loop to reposition in the y direction
    for k in range(0, 4):
        turtle.sety(yRef + (height / 4) * k)
        turtle.setx(xRef)
        
        # loop for the rectangles 
        for j in range(1, 5):
            drawRecangle(width, height)
            turtle.setx(turtle.xcor() + (width / 8) * 2)
            
            
# define function to draw a single black square  
def drawRecangle(width, height):
    
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor("black")
    turtle.setheading(0)
    turtle.forward(width / 8)
    turtle.left(90)
    turtle.forward(height / 8)
    turtle.left(90)
    turtle.forward(width / 8)
    turtle.left(90)
    turtle.forward(height / 8)
    turtle.penup()
    turtle.end_fill()
    
