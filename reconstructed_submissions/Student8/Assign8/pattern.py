# @@@@@@@@@@@@@
# CS 1400 - MW1
# Assignment 8

# import needed modules
import turtle
import random


# erase all patterns
def reset():
    turtle.clearscreen()
    
    
# make turtle fast and set a good window size
def setup():
    turtle.speed(0)
    turtle.setup(1000, 800)
    
    
# draw rectangles in a circular pattern
def drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation):
    
    # go to the provided center
    turtle.pu()
    turtle.goto(centerX, centerY)
    
    # find the angular distance between each rectangle
    gap = 360 / count
    
    # define the direction variable
    direction = 0
    
    # repeat this code for every rectangle
    for i in range(count):
        
        # get to corner of the rectangle
        turtle.setheading(direction)
        turtle.forward(offset)
        
        #draw the rectangle
        turtle.pd()
        drawRectangle(width, height, rotation, direction)
        turtle.pu()
        
        # go back to the center
        turtle.goto(centerX, centerY)
        
        # adjust direction
        direction += gap


# draw a single rectangle  
def drawRectangle(width, height, rotation, direction):
    
    # select a random color by calling setRandomColor()
    setRandomColor()
    
    # adjust direction based off direction and rotation
    turtle.setheading(direction - rotation)
    
    # draw half of the rectangle and repeat
    for r in range(2):
        turtle.forward(height)
        turtle.left(90)
        turtle.forward(width)
        turtle.left(90)


# draw a circle pattern
def drawCirclePattern(centerX, centerY, offset, radius, count):
    
    # go to the provided center
    turtle.pu()
    turtle.goto(centerX, centerY)

    # find the angular distance between each rectangle
    gap = 360 / count

    # define the direction variable
    direction = 0

    # repeat this code for every circle
    for i in range(count):
        
        # travel offset length to the starting point for the circle
        turtle.setheading(direction)
        turtle.forward(offset)
        
        # draw the circle
        turtle.pd()
        turtle.right(90)  # the circle() function draws circles to the right
        setRandomColor()
        turtle.circle(radius)
        turtle.pu()
        
        # go back to the center
        turtle.goto(centerX, centerY)

        # adjust direction
        direction += gap
        
        
# create a set number of circle or rectangle patterns with nearly completely random parameters
def drawSuperPattern(num):
    
    # loop until all patterns created
    for p in range(num):
        
        # select a random mode
        mode = random.randint(1, 2)

        # assign random values to the parameters used by both the rectangle pattern function and the circle one
        centerX = random.randint(-400, 400)
        centerY = random.randint(-300, 300)
        offset = random.randint(-100, 100)
        count = random.randint(1, 100)
        
        # draw a rectangle or a circle based on the mode selected
        if mode == 1:
            
            # assign random values to the parameters specific to the rectangle pattern function
            height = random.randint(1, 100)
            width = random.randint(1, 100)
            rotation = random.randint(0, 359)
            
            # draw the rectangle pattern by calling drawRectanglePattern()
            drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation)
            
        else:

            # assign random values to the radius parameter
            radius = random.randint(1, 50)
            
            # draw the circle pattern by calling drawCirclePattern()
            drawCirclePattern(centerX, centerY, offset, radius, count)
            
    
# change turtle's color randomly
def setRandomColor():
    
    # make a list with the colors to be used
    colorList = ["black", "yellow", "orange", "purple"]
    
    # set the pen color to something random in the list colorList
    turtle.pencolor(colorList[random.randint(0, 3)])
    
# keep the turtle drawing onscreen once the user ends the program
def done():
    turtle.done()
