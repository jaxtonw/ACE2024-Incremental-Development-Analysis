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
            centerX, centerY = input("Enter a cernter point (x, y): ", )
            offset = input("Offset?: ", )
            width = input("Width?: ", )
            height = input("Height?: ", )
            count = input("Count?: ", )
            rotation = input("Rotation?: ", )

            # Draw the rectangle pattern
            pattern.drawRectanglePattern(centerX, centerY, offset, width, height,
                                         count, rotation)
        # If they choose 'Circle Patterns'
        elif mode == 2:
            centerX, centerY = input("Enter a cernter point (x, y): ", )
            offset = input("Offset?: ", )
            radius = input("Enter a radius: ", )
            count = input("Count?: ", )

            # Draw the circle pattern
            pattern.drawCirclePattern(centerX, centerY, offset, radius, count)
        # If they choose 'Super Patterns'
        elif mode == 3:

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
        #### Add Statement(s) to clear drawings and play again ####
        #### End Add Inputs Statement(s) ####
    # print a message saying thank you
    print("Thanks for playing!")
    pattern.done()


main()
# @@@@@@@@@@@@@@
# CS1400 - MW1
# Assignment ??

