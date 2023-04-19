from chessboard import drawChessboard


def main():
    startX, startY = eval(input("Where would you like to start? (x, y): "))
    width = input("How wide is your board?: ")
    height = input("How tall is your board?: ")
    if width == "" and height == "":
        drawChessboard(startX, startY)
    elif height == "":
        drawChessboard(startX, startY, width=eval(width))
    elif width == "":
        drawChessboard(startX, startY, height=eval(height))
    else:
        drawChessboard(startX, startY, eval(width), eval(height)) 
        
        
main()

