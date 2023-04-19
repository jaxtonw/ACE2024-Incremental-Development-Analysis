# @@@@@@@@@@
# CS1400 - 14 week
# Assignment 8

# import
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
            # get input
            centerX, centerY = eval(input("Enter the center point (x, y): "))
            offset = eval(input("Enter the offset: "))
            width = eval(input("Enter the width: "))
            height = eval(input("Enter the height: "))
            count = eval(input("Enter the count: "))
            rotation = eval(input("Enter the rotation angle: "))

            # Draw the rectangle pattern
            pattern.drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation)

        # If they choose 'Circle Patterns'
        elif mode == 2:
            # Get input
            centerX, centerY = eval(input("Enter the center point (x, y): "))
            offset = eval(input("Enter the offset: "))
            radius = eval(input("Enter the radius: "))
            count = eval(input("Enter the count: "))

            # Draw the circle pattern
            pattern.drawCirclePattern(centerX, centerY, offset, radius, count)

        # If they choose 'Super Patterns'
        elif mode == 3:
            # Get input
            num = input("Number: ")
            
            if num == "":
                pattern.drawSuperPattern(num)
            else:
                pattern.drawSuperPattern(eval(num))

        # Play again?
        print("Do you want to play again?")
        print("1) Yes, and keep drawings")
        print("2) Yes, and clear drawings")
        print("3) No, I am all done")
        response = eval(input("Choose 1, 2, or 3: "))

        # play again? clear or keep drawings
        playAgain = response == 1 or response == 2
        if response == 2:
            # clear drawings
            pattern.clear()
        
    # print a message saying thank you
    print("Thanks for playing!")
    pattern.done()


main()
raw the circle pattern
            pattern.drawCirclePattern(centerX, centerY, offset, radius, count)

        # If they choose 'Super Pat    tern       elif mode == 3:
            #### Add Input Statement(s) as needed ####

            #### End Add Inputs Statement(s) ####
        # play again? clear or keep drawingswngs"    playAgain = response == 1 or response == 2
        if response == 2:
            # clear drawings
            turtle.reset()
        
     response = eval(input("Choose 1, 2, or 3: "))

        #### Add Statement(s) to clear drawings and play again ####

        #### End Add Inputs Statement(s) ####

    # print a message saying thank you
    print("Thanks for playing!")
    pattern.done(
