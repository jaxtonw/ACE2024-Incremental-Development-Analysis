#@@@@@@@@@@@@@@ CS1400 14Week
import turtle
def drawChessboard(startX, startY, width = 250, height = 250):
    turtle.pu()
    turtle.goto(startX, startY)
    turtle.pd()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    drawAllRectangles(startX, startY, width, height)
    turtle.hideturtle()
    turtle.done()
def drawAllRectangles(startX, startY, width, height):
    row = 1
    for i in range(8):
        for j in range(4):
            turtle.left(90)
            turtle.goto(startX, startY)
            turtle.pd()
            drawRectangle(width/8, height/8)
            turtle.pu()
            startX += width/4
        if row % 2 == 0:
            startX -= (9 * width)/8
            startY += height / 8
        elif row % 2 != 0:
            startX -= (7 * width) / 8
            startY += height/8
        row += 1
def drawRectangle(widthOfRectangle, heightOfRectangle):
    turtle.begin_fill()
    turtle.forward(widthOfRectangle)
    turtle.left(90)
    turtle.forward(heightOfRectangle)
    turtle.left(90)
    turtle.forward(widthOfRectangle)
    turtle.left(90)
    turtle.forward(heightOfRectangle)
    turtle.end_fill()


    
    
