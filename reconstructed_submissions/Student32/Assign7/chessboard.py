# @@@@@@@@@@@@@@
# CS1400 - 001
# Chessboard module

# import turtle module
import turtle as t


# create a function that draws the chessboard outline
def drawChessboard(startX, startY, width=250, height=250):
    t.setup(1000, 1000)
    t.penup()
    t.goto(startX, startY)
    t.pendown()
    t.right(360)
    t.forward(width)
    t.right(270)
    t.forward(height)
    t.right(270)
    t.forward(width)
    t.right(270)
    t.forward(height)
    drawAllRectangles(startX, startY, width, height)
    done()


# function that draws all of the rectangles 
def drawAllRectangles(startX, startY, width, height):
    t.penup()
    t.goto(startX, startY)
    t.setheading(0)
    multiplier = 1
    # this does the row with the first square touches the left side of the board
    for j in range(4):
        for i in range(4):
            t.pendown()
            drawRectangle(startX, startY, width, height)
            t.penup()
            t.setheading(0)
            t.forward(width / 4)
            
        t.goto(startX, startY)
        t.setheading(90)
        t.forward((height / 8) * multiplier)
        t.setheading(0)
        t.forward(width / 8)
        multiplier += 1
        
        # this draws the row above that is offset from the left edge
        for i in range(4):
            t.pendown()
            drawRectangle(startX, startY, width, height)
            t.penup()
            t.setheading(0)
            t.forward(width / 4)
        
        t.goto(startX, startY)
        t.setheading(90)
        t.forward((height / 8) * multiplier)
        t.setheading(0)
        multiplier += 1    
           
           
# function that draws a single rectangle
def drawRectangle(startX, startY, width, height):
    t.begin_fill()
    t.fillcolor("black")
    t.pendown()
    t.forward(width / 8)
    t.right(270)
    t.forward(height / 8)
    t.right(270)
    t.forward(width / 8)
    t.right(270)
    t.forward(height / 8)
    t.end_fill()
    

# function to keep turtle drawing up after code has ran    
def done():
    t.done()
    
    
