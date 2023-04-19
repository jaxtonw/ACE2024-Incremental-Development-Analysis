# @@@@@@@@@@@@
# CS 1400 - 14 Weeks
# Assignment 7

#### Add Import Statement(s) as needed ####
import turtle

from chessboard import drawChessboard
#### End Add Import Statement(s) ####


def main():
    #### Add Code to get input from user ####
    startX = eval(turtle.textinput("Chessboard Setup", "Enter the starting X position of the chessboard: "))
    startY = eval(turtle.textinput("Chessboard Setup", "Enter the starting Y position of the chessboard: "))
    width = turtle.textinput("Chessboard Setup", "Enter the width of the chessboard: ")
    height = turtle.textinput("Chessboard Setup", "Enter the height of the chessboard: ")

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
