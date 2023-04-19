# @@@@@@@@@@@@
# CS1400 - 001
# Assignment 7

# new parameters
def drawRectangle(xPosNew, yPosNew, widthSq, heightSq):
    import turtle
    # draws one black square
    turtle.pu()
    turtle.goto(xPosNew, yPosNew)
    turtle.pencolor("black")
    turtle.pd()
    turtle.begin_fill()
    turtle.fd(widthSq)
    turtle.left(90)
    turtle.fd(heightSq)
    turtle.left(90)
    turtle.fd(widthSq)
    turtle.left(90)
    turtle.fd(heightSq)
    turtle.left(90)
    turtle.end_fill()
    turtle.pu()


def drawAllRectangles(xPos, yPos, width, height):
    # new
    heightSq = height / 8
    widthSq = width / 8
    xPosNew = xPos
    yPosNew = yPos
    xPosNew2 = xPosNew + widthSq
    yPosNew2 = yPos + heightSq
    # draws first set of 4 rows(black squares) in the red rectangle
    for i in range(4):
        for j in range(4):
            drawRectangle(xPosNew, yPosNew, widthSq, heightSq)
            xPosNew += widthSq * 2
        yPosNew += 2 * heightSq
        xPosNew = xPos
# draws the secon    d set of 4 rows in the red rectangle 
    for a in range(4):
        for b in range(4):
            drawRectangle(xPosNew2, yPosNew2, widthSq, heightSq)
            xPosNew2 += widthSq * 2
        yPosNew2 += 2 * heightSq
        xPosNew2 = xPos + widthSq

# draws a red rectangle (perimeter of chessboard)
def drawChessboard(xPos, yPos, width, height):
    import turtle
    turtle.speed(10)
    turtle.pu()
    turtle.goto(xPos, yPos) 
    turtle.color("red")
    turtle.pd()
    turtl.fd(width)
    turtle.left(90)
    turtle.fd(height)
    turtle.left(90)
    turtle.fd(width)
    turtle.left(90)
    turtle.fd(height)
    turtle.left(90)
    turtle.pencolor("black")
    turtle.fillcolor("black")
    drawAllRectangles(xPos, yPos, width, height)

        turtle.exitonclick()
    turtle.don()
   
