# @@@@@@@@@@@@@
# CS1400 - 14 week
# Assignment 7



def main():
    width = input("enter width: ")
    height = input("enter height: ")
    startX = input("enter starting x-value: ")
    startY = input("enter starting y-value: ")
    
    if width == "" and height == "":
        drawChessboard(startX, startY)
    elif height == "":
        drawChessboard(startX, startY, width=eval(width))
    elif width == "":
        drawChessboard(startX, startY, height=eval(height))
    else:
        drawChessboard(startX, startY, eval(width), eval(height))
main()
