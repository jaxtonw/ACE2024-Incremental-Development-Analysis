# @@@@@@@@@@@@@
# CS1400 - MW1
# Assignment 7

from chessboard import drawChessboard

def main():
    startX, startY = input("Please enter desired coordinates (x,y): ").split(",")
    width = input("Please enter desired width of board: ")
    height = input("Please enter desired height of board: ")
    if width == "" and height == "":
        drawChessboard(startX, startY)
    elif height == "":
        drawChessboard(startX, startY, width=eval(width))
    elif width == "":
        drawChessboard(startX, startY, height=eval(height))
    else:
        drawChessboard(startX, startY, eval(width), eval(height))

main()

