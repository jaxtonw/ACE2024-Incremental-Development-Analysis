# @@@@@@@@@
# CS1400 - MW1
# Assignment 7 - task2

#### Add Import Statement(s) ####
from chessboard import drawChessboard
#### End Add Import Statement(s) ####

def main():
    #### Add Code to get input from user ####
    startX, startY = eval(input("Enter Starting Position (x, y): "))
    width = input("Enter Chessboard Width: ")
    height = input("Enter Chessboard Height: ")
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


