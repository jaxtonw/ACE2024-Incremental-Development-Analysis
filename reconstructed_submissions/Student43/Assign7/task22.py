# @@@@@@@@@@@@@
# CS1400 - MW1 XL
# Assignment 7

#### Add Import Statement(s) as needed ####
import turtle
from chessboard import drawChessboard
from chessboard import drawAllRectangles
from chessboard import drawRectangle
#### End Add Import Statement(s) ####

def main():
    #### Add Code to get input from user ####
    startX, startY = eval(input("Enter the starting location of the chessboard (x, y): "))
    width = input("Enter the width of the chessboard: ")
    height = input("Enter the height of the chessboard: ")
    #### End Add Code to get input from user ####

    if width == "" and height == "":
        drawChessboard(startX, startY)
    elif height == "":
        drawChessboard(startX, startY, width=eval(width))
    elif width == "":
        drawChessboard(startX, startY, height=eval(height))
    else:
        drawChessboard(startX, startY, eval(width), eval(height))


main()


