# @@@@@@@@@@@
# Assignment 7 Task 2
# CS 1400 14 Week

#### Add Import Statement(s) as needed ####
from chessboard import drawChessboard
#### End Add Import Statement(s) ####
def main():
    #### Add Code to get input from user ####
    startX, startY = eval(input("Enter the starting coordinates (x, y): "))
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
