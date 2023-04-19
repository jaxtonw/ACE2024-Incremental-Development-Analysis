# @@@@@@@@@@@
# CS1400 - MW1 XL
# Assignment 7

#### Add Import Statement(s) as needed ####
import turtle
import math
import chessboard
#### End Add Import Statement (s) ####
    
def main():
    #### Add code it get input from user ####
    startPos = input("Enter at start positions: ")
    width = input("Enter the width: ")
    height = input("Enter the height: ")
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
