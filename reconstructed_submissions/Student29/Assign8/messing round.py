import turtle
from random import randint


# # 
# # 
# #     
# #     
# #     
def setup():
    turtle.speed(0)
    turtle.screensize(1000, 800)
    
setup()





# 
def setRandomColor():
    randomColor = randint(1, 4)

    if randomColor == 1:
        color = turtle.color("blue")

    elif randomColor == 2:
        color = turtle.color("red")

    elif randomColor == 3:
        color = turtle.color("green")

    elif randomColor == 4:
        color = turtle.color("purple")





# 
# # 
# # 
# 
def drawRectangle(width, height, rotation):
    turtle.left(rotation)
    setRandomColor()
    turtle.pd()
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.right(rotation)
    turtle.pd()


# # 
# # # 
def drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation):
    rotationAngle = 0
    rotationAngle = (360 / count)
    for drawingRectangles in range(count):
        turtle.pu()
        turtle.goto(centerX, centerY)
        turtle.left(rotationAngle)
        turtle.forward(offset)
        drawRectangle(width, height, rotation)

        turtle.pd()


        










def drawCirclePattern(centerX, centerY, offset, radius, count):
    setup()
    angleOfRotation = 0
    print(turtle.heading())
    angleOfRotation = (360 / count)
    for drawingCircles in range(count):
        setRandomColor()
        turtle.pu()
        turtle.goto(centerX, centerY)
        turtle.forward(offset)
        turtle.left(angleOfRotation)
        turtle.pd()
        turtle.circle(radius)
        print(turtle.heading())
        
drawCirclePattern(centerX=2, centerY=4, offset= 10, radius=30, count=15)





# 
turtle.done()

num=7
def drawSuperPattern(num):
    for superPattern in range(num):
        centerX = randint(-200, 200)
        centerY = randint(-200, 200)
        offset = randint(-100, 100)
        radius = randint(10, 50)
        count = randint(10, 50)
        width = randint(10, 50)
        height = randint(10, 50)
        rotation = randint(10, 50)
        whichOne = randint(1,2)


        if whichOne == 1:
            drawCirclePattern(centerX, centerY, offset, radius, count)

        elif whichOne == 2:
            drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation)

drawSuperPattern(num)

