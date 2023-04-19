# @@@@@@@@@@@@
# CS1400 - 001
# Assignment 7

'''
    This is the starter file. Only fill in the areas indicated.
    Do not modify existing code.
    Replace this file header with the normal file header (name, etc)
'''

#### Add Import Statement(s) as needed ####
from chessboard import drawChessboard
#### End Add Import Statement(s) ####

def main():
    #### Add Code to get input from user ####
    (startX, startY) = eval(input("Enter at start positions (x, y): "))
    width = input("Enter the width: ")
    height = input("Enter the height: ")
    #### End Add Code to get input from user ####

# do not modify this code
    if width == "" and height == "":
        drawChessboard(startX, startY)
    elif height == "":
        drawChessboard(startX, startY, width=eval(width))
    elif width == "":
        drawChessboard(startX, startY, height=eval(height))
    else:
        drawChessboard(startX, startY, eval(width), eval(height))


main()

