#@@@@@_@@@@@@@_Assn7


import Chessboard
import Chessboard as drawChessboard
#### End Add Import Statement(s) ####
def main():
    #Ask for a start
    Chessboard.setup()
    
    startX, startY= eval(str(input("Enter the starting position of x,y:" )))
    width = eval(input("Enter width (blank for default):" ))
    height = eval(input("Enter height (blank for default):"   ))
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
