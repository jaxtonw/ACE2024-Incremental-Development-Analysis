# @@@@@@@@@@@  
# CS 1400 - MW1 XL
# Assignment 007

from chessboard import drawChessboard


# here us the main function, only thing that is added is the prompts to get the user input
def main():
    startX, startY = eval(input("Enter starting position (x, y): "))
    width = input("Enter the width of the chess board: ")
    height = input("Enter the height of the chess board: ")

    if width == "" and height == "":
        drawChessboard(startX, startY)
    elif height == "":
        drawChessboard(startX, startY, width=eval(width))
    elif width == "":
        drawChessboard(startX, startY, height=eval(height))
    else:
        drawChessboard(startX, startY, eval(width), eval(height))


main()
eval)


main()
