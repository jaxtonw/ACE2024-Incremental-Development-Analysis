# @@@@@@@@@@@@@@@@
# CECS1400 - MW1
# Assignment 7-Task 2(line 7 and lines 12-22 provided from starter code)

from chessboard import drawChessboard

def main():
    startX, startY = eval(input("Enter the starting position (x, y): "))
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
