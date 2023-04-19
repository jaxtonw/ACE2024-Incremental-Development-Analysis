# @@@@@@@@@@@@@
# CS1400 - M01
# Assignment 7

from chessboard import drawChessboard

def main():
# User Input
    startX, startY = eval(input("Enter the starting location (x, y): "))
    width = input("Enter the width of the checkerboard: ")
    height = input("Enter the height of the checkerboard: ")

#If left blank
    if width == "" and height == "":
        drawChessboard(startX, startY, height=250, width=250)
    elif height == "":
        drawChessboard(startX, startY, width=eval(width), height=250)
    elif width == "":
        drastartXwChessboard(, startY, height=eval(height), width=250)
    else:
        drawChessboard(startX, startY, eval(width), eval(height))

# Call Statement
main()
