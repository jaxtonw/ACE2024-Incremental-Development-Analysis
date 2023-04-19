# # @@@@@@@@@@@@@@
# # CS1400 - MW1
# # Assignment ??
# 
# # mode = input(" Choose a mode\n 1)Rectangle \n 2)Circle  \n 3)Super pattern \n Which one do you choose?:", )
# # print(mode)
# 
import turtle
from random import randint



def setup():
    turtle.speed(0)
    turtle.screensize(1000, 800)
    
    
# setup()
def reset():
    turtle.clear()
    


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


# setRandomColor()



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



def drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation):
    setup()
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
    
    angleOfRotation = (360 / count)
    for drawingCircles in range(count):
        setRandomColor()
        turtle.pu()
        turtle.goto(centerX, centerY)
        turtle.left(angleOfRotation)
        turtle.forward(offset)
        turtle.pd()
        turtle.right(90)
        turtle.circle(radius)
        turtle.left(90)
        


#

# 



def drawSuperPattern(num = 7):
    for superPattern in range(num):
        centerX = randint(-200, 200)
        centerY = randint(-200, 200)
        offset = randint(-100, 100)
        radius = randint(10, 50)
        count = randint(10, 50)
        width = randint(10, 50)
        height = randint(10, 50)
        rotation = randint(10, 50)
        whichOne = randint(1, 2)

        if whichOne == 1:
            drawCirclePattern(centerX, centerY, offset, radius, count)

        elif whichOne == 2:
            drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation)




def done():
    turtle.done()
    

        
        
    

    

