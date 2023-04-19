import turtle
import random
#reset the board
def reset():
    turtle.reset()
    turtle.speed(0)
# setup
def setup():
    # set the speed of the turtle
    turtle.speed(0)
    # set window size to 1000 x 800
    turtle.setup(1000, 800)
#This function makes it so that each rectangle/circle is a different random color
def setRandomColor():
    recColor = random.randint(1, 4)
    if recColor == 1:
        color = "red"
    elif recColor == 2:
        color = "orange"
    elif recColor == 3:
        color = "green"
    else:
        color = "purple"
    return color
#draw the rectangular pattern
def drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation):
    turtle.speed(0)
    turtle.pu()
    turtle.goto(centerX, centerY)
    turtle.pd()
    head = 0
    for i in range(count):
        turtle.pu()
        turtle.goto(centerX, centerY)
        turtle.setheading(head)
        turtle.forward(offset)
        turtle.pd()
        turtle.left(rotation)
        drawRectangle(width, height)
        head += 360 / count
#draw the individual rectangle 
def drawRectangle(widthOfRectangle, heightOfRectangle):
    turtle.color(setRandomColor())
    turtle.forward(widthOfRectangle)
    turtle.left(90)
    turtle.forward(heightOfRectangle)
    turtle.left(90)
    turtle.forward(widthOfRectangle)
    turtle.left(90)
    turtle.forward(heightOfRectangle)
#draw the circular pattern
def drawCirclePattern(centerX, centerY, offset, radius, count):
    turtle.speed(0)
    turtle.pu()
    turtle.goto(centerX, centerY)
    turtle.pd()
    head = 0
    for i in range(count):
        turtle.pu()
        turtle.goto(centerX, centerY)
        turtle.setheading(head)
        turtle.forward(offset * 2)
        turtle.pd()
        drawCircle(radius)
        head += 360 / count
#draw individual circle
def drawCircle(radiusOfCircle):
    turtle.color(setRandomColor())
    turtle.pu()
    turtle.pd()
    turtle.circle(radiusOfCircle)
def done():
    turtle.done()
def drawSuperPattern(numberOfPatterns=5):
    print(str(numberOfPatterns))
