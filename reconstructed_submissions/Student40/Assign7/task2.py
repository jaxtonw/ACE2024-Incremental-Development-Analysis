# @@@@@@@@@@
# CS1400 - 14 week
# Assignment 7
# Task 2


from chessboard import drawChessboard


# main function
def main():
    # get input
    startX, startY = eval(input("Enter a starting position (x, y): "))
    width = input("Enter the width: ")
    height = input("Enter the height: ")

    # produce output
    if width == "" and height == "":
        drawChessboard(startX, startY)
    elif height == "":
        drawChessboard(startX, startY, width=eval(width))
    elif width == "":
        drawChessboard(startX, startY, height=eval(height))
    else:
        drawChessboard(startX, startY, eval(width), eval(height))


main()

