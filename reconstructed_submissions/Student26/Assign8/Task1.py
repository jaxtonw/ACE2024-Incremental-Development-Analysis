# @@@@@@@@@@@@@
# CS1400 - M01
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
            centerX, centerY = eval(input("Enter the starting place (x,y): "))
            offset = input("Enter the offset: )"
            width = input("Enter the width: ")
            height = input("Enter the height: ")
            count = input("Enter the count: ")
            rotation = input("Enter the rotation: ")
            
            # Draw the rectangle pattern
            pattern.drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation)

        # If they choose 'Circle Patterns'
        elif mode == 2:
            centerX, centerY = eval(input("Enter the starting place (x,y): "))
            offset = input("Enter the offset: ")
            count = input("Enter the count: ")
            radius = input("Enter the radius: ")

            # Draw the circle pattern
            pattern.drawCirclePattern(centerX, centerY, offset, radius, count)

        # If they choose 'Super Patterns'
        elif mode == 3:
            num = input("Enter the number of Super patterns to draw: ")
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
            continue
        elif response == 2:
            pattern.reset()
            pattern.setup()
            continue
        else:
            break

    # print a message saying thank you
    print("Thanks for playing!")
    pattern.done()


main()

