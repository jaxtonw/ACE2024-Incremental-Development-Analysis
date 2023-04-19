# @@@@@@@@@@@
# CS 1400 - A01 XL
# Assignment 7

'''
    This is the starter file. Only fill in the areas indicated.
    Do not modify existing code.
    Replace this file header with the normal file header (name, etc)
'''

from chessboard import drawChessboard


#### End Add Import Statement(s) ####

def main():
    startX = eval(input("What is your starting x coordinate?: "))
    startY = eval(input("What is your starting y coordinate?: "))
    width = input("What is your width?: ")
    height =input("What is your height?: ")

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

