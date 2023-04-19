# @@@@@@@@@@@@@
# CS1400 - MW1 XL
# Assignment 7

# Add Import Statement(s) as needed
from chessboard import drawChessboard


def main():
    # Add Code to get input from user
    startX, startY = eval(input("Enter the starting location of the chessboard (x, y): "))
    width = input("Enter the width of the chessboard: ")
    height = input("Enter the height of the chessboard: ")

    # Create if statements for if the user enters nothing for height and width
    if width == "" and height == "":
        drawChessboard(startX, startY)
    elif height == "":
        drawChessboard(startX, startY, width=eval(width))
    elif width == "":
        drawChessboard(startX, startY, height=eval(height))
    else:
        drawChessboard(startX, startY, eval(width), eval(height))


# Call the main function
main()


