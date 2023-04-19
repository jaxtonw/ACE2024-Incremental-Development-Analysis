# @@@@@@@@@@@  
# CS 1400 - MW1 XL
# Assignment 008
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
            centerX, centerY = eval(input("Enter the center of the pattern (x,y): "))
            offset = eval(input("Enter pattern offset: "))
            width = eval(input("Enter rectangle width: "))
            height = eval(input("Enter rectangle height: "))
            count = eval(input("Enter the numbcenterrectangles: "))
            rotation = eval(input("Enter the rectangle rotation: "))
            # Draw the rectangle pattern
            pattern.drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation)

        # If they choose 'Circle Patterns'
        elif mode == 2:
            centerX, centerY = eval(input("Enter the center of the pattern (x,y): "))
            offset = eval(input("Enter pattern offset: "))
            radius = eval(input("Enter the radius of the circles: "))
            count = eval(input("Enter the number of rectangles: "))

            # Draw the circle pattern
            pattern.drawCirclePattern(centerX, centerY, offset, radius, count)

        # If they choose 'Super Patterns'
        elif mode == 3:
            num = input("Enter number of random patterns: ")
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
            playAgain = True
        elif response == 2:
            pattern.clear()
        else:
            playAgain = False
    # print a message saying thank you
    print("Thanks for playing!")
    pattern.done()


main()

