# @@@@@@@@@@@
# Assignment 7 Task 2
# CS 1400 14 Week

# Import needed functions from turtle
import turtle
from turtle import penup
from turtle import pendown
from turtle import goto
from turtle import forward
from turtle import setheading
from turtle import begin_fill
from turtle import end_fill

# Define drawChessboard
def drawChessboard(inputX, inputY, inputWidth = 250, inputHeight = 250):
    penup()
    goto(inputX, inputY)
    pendown()
    forward(inputWidth)
    setheading(90)
    forward(inputHeight)
    setheading(180)
    forward(inputWidth)
    setheading(270)
    forward(inputHeight)
# Start to call other functions
    drawAllRectangles(inputX, inputY, inputWidth, inputHeight)
    turtle.done()
    
def drawAllRectangles(valX, valY, valWidth, valHeight):
# Create nested for loop
# Outer loop makes number of rows
    for i in range(0, 4):
        penup()
# Tells turtle where to go for certain index
        goto(valX, valY + i * valHeight / 4)
# Inner loop fills in a single row
        for j in range(0, 4):
            penup()
# Tells turtle where to go for certain index
            goto(valX + j * valWidth / 4, valY + i * valHeight / 4)
            drawRectangle(valWidth, valHeight)
# Second such loop for even numbered rows
    for i in range(0, 4):
        penup()
        goto(valX + valWidth / 8, valY + i * valHeight / 4 + valHeight / 8)
        for j in range(0, 4):
            penup()
            goto(valX + j * valWidth / 4 + valWidth / 8, valY + i * valHeight / 4 + valHeight / 8)
            drawRectangle(valWidth, valHeight)
  
# Function to draw a rectangle
def drawRectangle(sectorWidth, sectorHeight):
    setheading(0)
    pendown()
    begin_fill()
    forward(sectorWidth / 8)
    setheading(90)
    forward(sectorHeight / 8)
    setheading(180)
    forward(sectorWidth / 8)
    setheading(270)
    forward(sectorHeight / 8)
    end_fill()
    penup()
