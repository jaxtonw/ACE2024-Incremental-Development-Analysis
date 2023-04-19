#J@@@@a @@@@@@
#Cs 1400
#Assignment 7


#### Add Import Statement(s) as needed ####
import chessboard
#### End Add Import Statement(s) ####

def main():
    #### Add Code to get input from user ####
    startX, startY = eval(input("Enter start position(x,y): ")) 
    width = str(input("Enter a width: ") or 250)
    height = str(input("Enter a height: ") or 250)

    
    #### End Add Code to get input from user ####

    if width == "" and height == "":
        chessboard.drawChessboard(startX, startY)
    elif height == "":
        chessboard.drawChessboard(startX, startY, width=eval(width))
    elif width == "":
        chessboard.drawChessboard(startX, startY, height=eval(height))
    else:
        chessboard.drawChessboard(startX, startY, eval(width), eval(height))


main()
