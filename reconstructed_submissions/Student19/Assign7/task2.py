# @@@@@@@@@@@@
# CS1400 - MW1 (14 week)
# Assignment 6

#### Add Import Statement(s) as needed ####
from chessboard import drawChessboard
#### End Add Import Statement(s) ####

def main():
    #### Add Code to get input from user ####
    startX, startY = ((input("Starting Coordinates (x, Y): ")).split())
    startX, startY = int(startX.strip(",")), int(startY.strip(","))
    height = input("Height of Board: ")
    width = input("Width of Board: ")
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
