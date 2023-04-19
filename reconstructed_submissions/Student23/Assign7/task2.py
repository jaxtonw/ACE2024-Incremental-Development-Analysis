# @@@@@@@@@@@@@@
# CS1400 - 001
# Assignment 7

from chessboard import drawChessboard


def main():
    startX, startY = eval(input("Enter starting position: "))
    width = input("Enter the width: ")
    height = input("Enter the height: ")
    
    if width == "" and height == "":
        drawChessboard(startX, startY)
    elif height == "":
        drawChessboard(startX, startY, width=eval(width))
    elif width == "":
        drawChessboard(startX, startY, height=eval(height))
    else:
        drawChessboard(startX, startY, eval(width), eval(height))


main()

