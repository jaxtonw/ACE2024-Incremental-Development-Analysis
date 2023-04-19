# @@@@@@@@@@@@
# CS 1400 - 14-week
# Assignment 8

# Import pattern module
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
            # Obtain needed information
            centerX, centerY = eval(input("Enter the starting position (x,y): "))
            offset = eval(input("Enter the offset: "))
            width = eval(input("Enter the width: "))
            height = eval(input("Enter the height: "))
            count = eval(input("Enter the count: "))
            rotation = eval(input("Enter the rotation: "))
            
            # Draw the rectangle pattern
            pattern.drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation)

        # If they choose 'Circle Patterns'
        elif mode == 2:
            # Obtain needed information
            centerX, centerY = eval(input("Enter the starting position (x,y): "))
            offset = eval(input("Enter the offset: "))
            radius = eval(input("Enter the radius: "))
            count = eval(input("Enter the count: "))

            # Draw the circle pattern
            pattern.drawCirclePattern(centerX, centerY, offset, radius, count)

        # If they choose 'Super Patterns'
        elif mode == 3:
            # Get number of patterns
            num = input("Enter the number of patterns (blank for default): ")
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

        # Determine if it will run again and clear drawings
        playAgain = response == 1 or response == 2
        if response == 2:
            pattern.reset()

    # print a message saying thank you
    print("Thanks for playing!")
    pattern.done()


main()

