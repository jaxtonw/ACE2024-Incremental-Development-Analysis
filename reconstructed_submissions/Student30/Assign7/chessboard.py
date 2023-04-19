# @@@@@@@@@@@@@@@@@@
# CS1400 - 001
# Assignment 7
import turtle
    

#Draw Outline of the board, then call drawAll Rectangles
def drawChessboard(startX, startY, width=250, height=250):
    turtle.penup()
    turtle.goto(startX, startY)

    turtle.setheading(0)
    turtle.pendown()
    turtle.goto(width + startX, startY)
    turtle.goto(width + startX, startY + height)
    turtle.goto(startX, startY + height)
    turtle.goto(startX, startY)
    drawAllRectangles(startX, startY, width, height)


#Drawing of all black rectangles by calling drawRectangle(), may call twice    
def drawAllRectangles(startX, startY, width, height):
    #odd Rows
    
    for oddRow1 in range(0, 4):

        drawRectangle(startX + ( .25 * width * oddRow1), startY, (width / 8), (height / 8))


    for oddRow2 in range(0, 4):
        drawRectangle(startX + ( .25 * width * oddRow2), startY + .25 * height, (width / 8), (height / 8))

    for oddRow3 in range(0, 4):
        drawRectangle(startX + ( .25 * width * oddRow3), startY + .50 * height, (width / 8), (height / 8))
        
    for oddRow4 in range(0, 4):
        drawRectangle(startX + ( .25 * width * oddRow4), startY + .75 * height, (width / 8), (height / 8))
    

    
    #even Rows
    
    for evenRow1 in range(0, 4):
        drawRectangle((startX + (.25 * width * evenRow1)) + .125 * width, startY + .125 * height, (width / 8), (height / 8))
    
    for evenRow2 in range(0, 4):
        drawRectangle((startX + (.25 * width * evenRow2)) + .125 * width, startY + .375 * height, (width / 8), (height / 8))

    for evenRow3 in range(0, 4):
        drawRectangle((startX + (.25 * width * evenRow3)) + .125 * width, startY + .625 * height, (width / 8), (height / 8))
        
    for evenRow4 in range(0, 4):
        drawRectangle((startX + (.25 * width * evenRow4)) + .125 * width, startY + .875 * height, (width / 8), (height / 8))
    
    
    turtle.hideturtle()
    turtle.done()
    
#Draw a single black regtangle, will be called many times with a loop.
def drawRectangle(startX, startY, width, height):
    

    turtle.penup()
    turtle.goto(startX, startY)
    turtle.setheading(0)
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    turtle.goto(width + startX, startY)
    turtle.goto(width + startX, startY + height)
    turtle.goto(startX, startY + height)
    turtle.goto(startX, startY)
    turtle.end_fill()
    turtle.penup()
    
    
    
