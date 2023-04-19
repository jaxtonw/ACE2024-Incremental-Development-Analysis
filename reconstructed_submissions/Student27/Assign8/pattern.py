# @@@@@@@@@@@@@
# CS1400 - MW1
# Assignment 8

#pattern.py - You must define the following functions
def reset():
    import turtle
    turtle.clearscreen()
     #- Erase all of the patterns and start over

#setup screensize and turtle speed
def setup():
    import turtle
    turtle.speed(0)
    turtle.setup(1000,800)

#calls draw rectangle over and over in a loop while moving in a circle
def drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation):
    import turtle
    from math import pi
    turtle.penup()
    turtle.speed(0)
    turtle.goto(centerX, centerY - offset)
    circ = int(2 * pi * offset)
    turtle.setheading(rotation)
    
    for i in range(1, count + 1):
        space = int(circ * i/ count)
        turtle.pendown()
        drawRectangle(width, height)
        turtle.circle(int(offset), 360 / int(count), space)
        turtle.penup()

#draws single rectangle
def drawRectangle(width, height):
    import turtle
    setRandomColor()
    turtle.penup()
    turtle.color()
    turtle.pendown()
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.penup()
  
#draws circles in a pattern while moving in a circle
def drawCirclePattern(centerX, centerY, offset, radius, count):
    import turtle
    from math import pi
    turtle.penup()
    turtle.speed(0)
    turtle.goto(centerX, centerY - offset)
    circ = int(2 * pi * offset)
    
    for i in range(1, count + 1):
        space = int(circ * i / count)
        setRandomColor()
        turtle.color()
        turtle.pendown()
        turtle.circle(radius)
        turtle.penup()
        turtle.circle(int(offset), 360 / int(count), space)
    
#draws circle and rectangle patterns randomly
def drawSuperPattern(num):
    import turtle
    import random
    turtle.penup()
    for i in range(0, num):
        setRandomColor()
        turtle.color()
        
        #multiple random values
        randomX = random.randint(-400, 400)
        randomY = random.randint(-300, 300)
        random1 = random.randint(5, 100)
        random2 = random.randint(5, 100)
        random3 = random.randint(5, 100)
        random4 = random.randint(10, 50)
        randomRotation = random.randint(0, 361)
        
        turtle.goto(randomX, randomY)
        
        shape = random.randint(1,2)
        turtle.setheading(randomRotation)
        turtle.pendown()
        if shape == 1:
            #drawRectangle(random1, random2)
            drawRectanglePattern(randomX, randomY, random1, random2, random3, random4, randomRotation)
         
        elif shape == 2:
            drawCirclePattern(randomX, randomY, random1, random2, random3)
        turtle.penup()

#assigns a random color
def setRandomColor():
    import turtle
    import random
    colors = ["navy", "gray", "magenta", "cyan"]
    color = random.choice(colors)
    turtle.color(str(color))  
setRandomColor()

#when user is finished. leave turtle screen up
def done():
    import turtle
    turtle.done()
   
    



