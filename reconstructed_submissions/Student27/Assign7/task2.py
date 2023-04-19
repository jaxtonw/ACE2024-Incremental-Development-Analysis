# @@@@@@@@@@@@@
# CS1400 - MW1
# Assignment 7

#### Add Import Statement(s) as needed ####

from chessboard import drawChessboard

#### End Add Import Statement(s) ####

def main():
    #### Add Code to get input from user ####
    startX = input("Enter the starting position (X):")
    startY = input("Enter the starting position (Y):")
    height = input("Enter the height of the board:")
    width = input("Enter the width of the board:")
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
