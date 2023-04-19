# @@@@@@@@@@@@@
# CS1400 - MW1
# Assignment 7

# define draw rectangle
def drawRectangle(startX, startY, width, height):
    #draw individual rectangle of width/8 and height/8
    import turtle
    turtle.speed(0)
    turtle.pendown()
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.forward(width / 8)
    turtle.left(90)
    turtle.forward(height / 8)
    turtle.left(90)
    turtle.forward(width / 8)
    turtle.left(90)
    turtle.forward(height / 8)
    turtle.left(90)
    turtle.end_fill()
    turtle.penup()
    
def drawAllRectangles(startX, startY, width, height):
    
    import turtle
    turtle.penup()
    turtle.speed(0)
    #loop to draw all rectangles
    j = 0
    while j < 4:
        turtle.penup()
        turtle.left(90)
        turtle.goto(int(startX), int(startY) + (height * j) / 4)
        turtle.right(90)
        j += 1
    
        i = 0
        while i < 4:
            drawRectangle(startX, startY, width, height)
            turtle.forward(width / 4)             
            i += 1

# define draw chessboard
def drawChessboard(startX, startY, width = 250, height = 250):
    #draw chessboard - rectangle of height and width, calls all rectangles
    import turtle
    turtle.penup()
    turtle.speed(0)
    turtle.goto(int(startX), int(startY))
    turtle.pendown()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.penup()

    #call draw all rectangles twice so it draws 
    # then moves and draws the second half
    drawAllRectangles(startX, startY, width, height)
    
    drawAllRectangles(int(startX) + (width / 8), int(startY) + (height / 8), width, height)
    #end turtle
    turtle.done()


