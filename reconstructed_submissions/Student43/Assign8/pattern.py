# @@@@@@@@@@@@@
# CS1400 - MW1 XL
# Assignment 8

# Import the required modules
import random
import turtle


# Define the reset and clear function
def reset():
    turtle.clearscreen()
    # Call setup function to make sure turtle settings stay the same
    setup()
    

# Define the turtle setup function
def setup():
    turtle.speed(0)
    turtle.hideturtle()
    turtle.Screen().setup(1000, 800)
    
    
# Define the function that draws all of the rectangles
def drawRectanglePattern(centerX, centerY, offset, height, width, count, rotation):
    # Create a loop to draw all of the rectangles
    # loopCount = Counting variable used for while loop
    loopCount = 1
    while loopCount <= count:
        turtle.penup()
        turtle.goto(centerX, centerY)
        turtle.setheading(rotation)
        turtle.forward(offset)
        # Call the color function to set squares to random colors
        setRandomColor()
        # Call the function that draws one rectangle
        drawRectangle(centerX, centerY, offset, height, width, count, rotation)
        rotation += 360 / count
        loopCount += 1
        
        
# Define the function that draws only one rectangle
def drawRectangle(centerX, centerY, offset, height, width, count, rotation):
    # Draw a rectangle using user inputs
    turtle.pendown()
    turtle.forward(height)
    turtle.setheading(rotation + 90)
    turtle.forward(width)
    turtle.setheading(rotation + 180)
    turtle.forward(height)
    turtle.setheading(rotation + 270)
    turtle.forward(width)
    

# Define the function that draws all of the circles
def drawCirclePattern(centerX, centerY, offset, radius, count):
    # Create a loop to draw all of the circles
    loopCount = 1
    # circleRotate = Draws the next circle enough degrees away so that 
    # there are the correct amount of circles according to the count
    circleRotate = 0
    while loopCount <= count:
        turtle.penup()
        turtle.goto(centerX, centerY)
        turtle.setheading(circleRotate)
        turtle.forward(offset)
        turtle.setheading(90)
        turtle.pendown()
        # Call the color function to set circles to random colors
        setRandomColor()
        turtle.circle(radius)
        circleRotate += 360 / count
        loopCount += 1


# Define the function that draws the super random pattern
def drawSuperPattern(num=random.randint(1, 10)):
    loopCount = 1
    # Create a loop that sets variables to random numbers and draws the correct number of patterns
    while loopCount <= num:
        centerX = random.randint(-300, 300)
        centerY = random.randint(-200, 200)
        offset = random.randint(-150, 150)
        height = random.randint(10, 300)
        width = random.randint(10, 200)
        radius = random.randint(10, 200)
        count = random.randint(2, 100)
        rotation = random.randint(10, 90)
        
        # super = Decides if function will draw a rectangle or circle pattern
        super = random.randint(0, 1)
        # If super == 0, draw rectangles
        if super == 0:
            setRandomColor()
            drawRectanglePattern(centerX, centerY, offset, height, width, count, rotation)
        # If super == 1, draw circles
        else:
            setRandomColor()
            drawCirclePattern(centerX, centerY, offset, radius, count)
        loopCount += 1
    
  
# Define a function to set shapes to random colors  
def setRandomColor():
    color = random.randint(1, 4)
    if color == 1:
        turtle.color("red")
    elif color == 2:
        turtle.color("green")
    elif color == 3:
        turtle.color("yellow")
    else:
        turtle.color("purple")


# Define a function that returns the final turtle screen
def done():
    turtle.done()

