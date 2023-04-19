# @@@@@@@@@@@@@@
# CS1400 - MW2
# Assignment 7
import turtle


def drawChessboard(startX, startY, width=250, height=250):
    # First we need to set up turtle so that we are ready to draw
    turtle.speed(0)
    turtle.pu()
    turtle.goto(startX, startY)
    turtle.setheading(0)
    turtle.color("red")
    # Then we draw the outline of the chessboard in red
    turtle.pd()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    # then we set turtle up to start drawing and filling the black squares
    turtle.setheading(0)
    turtle.color("black")
    turtle.fillcolor("black")
    drawAllRectangles(width, height)
    turtle.goto(startX + width / 8, startY + height / 8)
    drawAllRectangles(width, height)
    turtle.done()
    
    
def drawAllRectangles(width, height):
    # This loop will draw 4 black squres, then realign to be two rows above the last row drawn.
    # This function will be called twice, as it only draws 16 black squares
    for i in range(4):
        # This loop handles drawing the 4 black squares in each row.
        for j in range(4):
            drawRectangle(width, height)
            turtle.forward(width / 4)
        turtle.left(90)
        turtle.forward(height / 4)
        turtle.left(90)
        turtle.forward(width)
        turtle.setheading(0)
        
        
def drawRectangle(width, heightt:
    # This creates a rectangle with a width and height that is one eighth of the whole chessboard's width and length
    turtle.pd()
    turtle.begin_fill()
    turtle.forward(width / 8)
    turtle.left(90)
    turtle.forward(height / 8)
    turtle.left(90)
    turtle.forward(width / 8)
    turtle.left(90)
    turtle.forward(height / 8)
    turtle.end_fill()
    turtle.setheading(0)
    turtle.pu()
        
    
