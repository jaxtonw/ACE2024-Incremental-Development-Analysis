# @@@@@@@@@@@@@
# CS1400 - MW1
# Assignment 8

import pattern

def main():
    # Setup pattern
    pattern.setup()
    print("Welcome to the Pattern Drawing Program!")
    # Play again loop
    playAgain = True
    while playAgain:
        # Present a menu to the user
        # Let them select 'Super' mode or 'Single' mode
        print("Choose a mode")
        print("1) Rectangle Pattern")
        print("2) Circle Pattern")
        print("3) Super Pattern")
        mode = eval(input("Which mode do you want to play? 1, 2 or 3: "))
        # If they choose 'Rectangle Patterns'
        if mode == 1:
            centerX, centerY = input("Coordinates? (x,y): ").split(",")
            offset = eval(input("Offset? : "))
            width = eval(input("Width? : "))
            height = eval(input("Height? : "))
            count = eval(input("Count? : "))
            rotation = eval(input("Rotation? : "))
            # Draw the rectangle pattern
            pattern.drawRectanglePattern(eval(centerX), eval(centerY), offset, width, height, 
count, rotation)
        # If they choose 'Circle Patterns'
        elif mode == 2:
            centerX, centerY = input("Coordinates? (x,y): ").split(",")
            offset = eval(input("Offset? : "))
            radius = eval(input("Radius? : "))
            count = eval(input("Count? : "))
            # Draw the circle pattern
            pattern.drawCirclePattern(eval(centerX), eval(centerY), offset, radius, count)
        # If they choose 'Super Patterns'
        elif mode == 3:
            num = input("Number of patterns? : ")
            if num == "":
                pattern.drawSuperPattern()
            else:
                pattern.drawSuperPattern(eval(num))
        # Play again?
        print("Do you want to play again?")
        print("1) Yes, and keep drawings")
        print("2) Yes, and clear drawings")
        print("3) No, I am all done")
        response = eval(input("Choose 1, 2, or 3: "))
        if response == 1:
            print("OK! We will keep going.")
        elif response == 2:
            pattern.reset()
            print("OK! Drawing board has been reset.")       
        else:
            print("OK. Ending program.")
            playAgain = False
    # print a message saying thank you
    print("Thanks for playing!")
    pattern.done()


main()



