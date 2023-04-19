import turtle


def drawRectangle(width, height):
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
    
    
def drawAllRectangles(startX, startY, width, height):
    for lotsMoreRectangles in range(2):
        for allRectangles in range(4):
            for moreRectangles in range(4):
                turtle.begin_fill()
                rectangleWidth = 1/8 * width
                rectangleHeight = 1/8 * height
                turtle.goto(
                    1/4 * width * allRectangles + 1/8 * width * lotsMoreRectangles + startX,
                    1/4 * height * moreRectangles + 1/8 * height * lotsMoreRectangles + startY
                )
                drawRectangle(rectangleWidth, rectangleHeight)
                turtle.end_fill()
               
                 
def drawChessboard(startX, startY, width=250, height=250):
    turtle.penup()
    turtle.goto(startX, startY)
    turtle.pendown()
    drawRectangle(width, height)
    drawAllRectangles(startX, startY, width, height)
    turtle.hideturtle()
    turtle.done()
    

