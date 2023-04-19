# @@@@@@@@@@@@@
# CS1400 - 14 week
# Assignment 8

import pattern


def main():
    # Setup pattern
    pattern.setup()
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
            centerX = eval(input("Enter X-value for pattern: "))
            centerY = eval(input("Enter Y-value for pattern: "))
            offset = eval(input("Enter offset: "))
            width = eval(input("Enter rectangle width: "))
            height = eval(input("Enter rectangle height: "))
            count = eval(input("Enter the number of rectangles: "))
            rotation = eval(input("Enter the rotation of the rectangle(s): "))
            # Draw the rectangle pattern
            pattern.drawRectanglePattern(centerX, centerY, offset, width, height, 
count, rotation)
        # If they choose 'Circle Patterns'
        elif mode == 2:
            centerX = eval(input("Enter X-value for pattern: "))
            centerY = eval(input("Enter Y-value for pattern: "))
            offset = eval(input("Enter offset: "))
            count = eval(input("Enter the number of circle: "))
            radius = eval(input("Enter the radius of the circle(s): "))
            # Draw the circle pattern
            pattern.drawCirclePattern(centerX, centerY, offset, radius, count)
        # If they choose 'Super Patterns'
        elif mode == 3:
            num = input("Enter number of patterns: ")
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
        if response == 2:
            pattern.reset()
        elif response == 3:
            playAgain = False
    # print a message saying thank you
    print("Thanks for playing!")
    pattern.done()
main()

