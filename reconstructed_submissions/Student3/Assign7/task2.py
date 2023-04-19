# @@@@@@@@@@@
# CS1400 - MW1
# Assignment 7

# Add Import Statement
from chessboard import drawChessboard

def main():
    # Add Code to get input from user
    startX, startY = eval(input("What is the starting location for the board (x, y)? "))
    height = input("What is the height of the board? ")
    width = input("What is the width of the board? ")
    if width == "" and height == "":
        drawChessboard(startX, startY)
    elif height == "":
        drawChessboard(startX, startY, width=eval(width))
    elif width == "":
        drawChessboard(startX, startY, height=eval(height))
    else:
        drawChessboard(startX, startY, eval(width), eval(height))
main()
