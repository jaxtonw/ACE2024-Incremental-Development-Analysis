# @@@@@@@@@@@@@@@
# CS 1400- 14 week
# Assignment 7


'''
    This is the starter file. Only fill in the areas indicated.
    Do not modify existing code.
    Replace this file header with the normal file header (name, etc)
'''

from chessboard import drawChessboard


def main():
    #input statements
    startX, startY = eval(input("Enter the starting location (x,y): "))
    width = input("Enter the width (enter nothing for default): ")
    height = input("Enter the height (enter nothing for default: ")

    if width == "" and height == "":
        drawChessboard(startX, startY)
    elif height == "":
        drawChessboard(startX, startY, width=eval(width))
    elif width == "":
        drawChessboard(startX, startY, height=eval(height))
    else:
        drawChessboard(startX, startY, eval(width), eval(height))
main()

