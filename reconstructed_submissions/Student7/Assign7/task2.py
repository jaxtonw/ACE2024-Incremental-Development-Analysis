# @@@@@@@@@@@@
# CS 1400 - 14-week
# Assignment 7

# Import drawChessboard function
from chessboard import drawChessboard

def main():
    # Getting input from user
    startX, startY = eval(input("Enter the starting position (x, y): "))
    width = input("Enter the width (blank for default): ")
    height = input("Enter the height (blank for default): ")

    # Use default values as needed to draw chessboard (depending on input)
    if width == "" and height == "":
        drawChessboard(startX, startY)
    elif height == "":
        drawChessboard(startX, startY, width=eval(width))
    elif width == "":
        drawChessboard(startX, startY, height=eval(height))
    else:
        drawChessboard(startX, startY, eval(width), eval(height))


main()
