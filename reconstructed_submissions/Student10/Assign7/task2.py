# @@@@@@@@@@
# CS 1400 - 14 week
# Assignment 7

#import statements
from chessboard import drawChessboard
from chessboard import drawAllRectangles
from chessboard import drawRectangle

#define main
def main():
    #user input
    startX, startY = eval(input("Enter the start position (x, y): "))
    width = input("Enter the width: ")
    height = input("Enter the height: ")
    #starter code
    if width == "" and height == "":
        drawChessboard(startX, startY)
    elif height == "":
        drawChessboard(startX, startY, width=eval(width))
    elif width == "":
        drawChessboard(startX, startY, height=eval(height))
    else:
        drawChessboard(startX, startY, eval(width), eval(height))

#call main        
main()
