# @@@@@@@@@@@@@@
# CS1400 - 001
# Assignment 7 task 2

#### Add Import Statement(s) as needed ####
from chessboard import drawChessboard
#### End Add Import Statement(s) ####

def main():
    
    
    #### Add Code to get input from user ####
    # get the x and y location from the user
    startX, startY = eval(input("Choose a starting position (x,y): "))
    # get the width from the user 
    width = input("How wide do you want the board? (default is 250): ")
    # get the height from the user 
    height = input("How tall do you want the board? (default is 250): ")
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

