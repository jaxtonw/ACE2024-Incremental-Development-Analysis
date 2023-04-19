# @@@@@@@@@@@@@@@@
# CECS1400 - MW1
# Assignment 8-Pattern

import turtle
import random

# erase all patterns and start over
def reset():
     # clear drawing space
     # set turtle to draw quickly
     turtle.reset()
     turtle.speed(0)
 
# setup the drawing space
def setup():
     # set the turtle window size to 1000 x 800
     # set turtle to draw quickly
     turtle.setup(1000, 800)
     turtle.speed(0)
     
# set turtle to random color
def setRandomColor():
     color = random.randint(1, 5)
     if color == 1:
          turtle.color("blue")
     elif color == 2:
          turtle.color("orange")
     elif color == 3:
          turtle.color("purple")
     elif color == 4:
          turtle.color("red")
     elif color == 5:
          turtle.color("green")

# draw a rectangle
def drawRectangle(width, height):
     turtle.pendown()
     turtle.width(1)
     turtle.forward(height)
     turtle.right(90)
     turtle.forward(width)
     turtle.right(90)
     turtle.forward(height)
     turtle.right(90)
     turtle.forward(width)
     turtle.right(90)
     turtle.penup()
     
# drawRectanglePattern
def drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation):
     turtle.penup()
     for i in range(count):
          turtle.goto(centerX, centerY)
          turtle.setheading((360 / count) * i)
          turtle.forward(offset)
          turtle.left(rotation)
          setRandomColor()
          drawRectangle(width, height)

# drawCirclePattern
def drawCirclePattern(centerX, centerY, offset, radius, count):
     turtle.penup()
     for i in range(count):
          turtle.goto(centerX, centerY)
          turtle.setheading((360 / count) * i)
          turtle.forward(offset + radius)
          setRandomColor()
          turtle.pendown()
          turtle.circle(radius)
          turtle.penup()
          

# finish program but keeps turtle window open     
def done():
     turtle.done()
     

def drawSuperPattern(num=5):
     turtle.penup()
     for i in range(1, num + 1):
          centerX = random.randint(-300, 300)
          centerY = random.randint(-300, 300)
          offset = random.randint(-60, 60)
          width = random.randint(10, 100)
          height = random.randint(50, 200)
          count = random.randint(10, 60)
          radius = random.randint(15, 100)
          rotation = random.randint(-60, 60)
          pattern = random.randint(1, 6)
          if pattern == 1 or pattern == 3 or pattern == 5:
               drawCirclePattern(centerX, centerY, offset, radius, count)
          elif pattern == 2 or pattern == 4 or pattern == 6:
               drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation)
     
