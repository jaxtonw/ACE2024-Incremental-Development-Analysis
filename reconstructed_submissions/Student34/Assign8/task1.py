# @@@@@@@@@@@@
# CS 1400 - 14 Weeks
# Assignment 8

#### Add Import Statement(s) as needed ####
import pattern
#### End Add Import Statement(s) ####

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
            #### Add Input Statement(s) as needed ####
            centerX = eval(input("Enter the x coordinate of the center position: "))
            centerY = eval(input("Enter the y coordinate of the center position: "))
            offset = eval(input("Enter the offset of the pattern: "))
            width = eval(input("Enter the width of each rectangle in the pattern: "))
            height = eval(input("Enter the height of each rectangle in the pattern: "))
            count = eval(input("Enter the number of rectangles in the pattern: "))
            rotation = eval(input("Enter the rotation of the rectangles in the pattern: "))
            #### End Add Inputs Statement(s) ####


            # Draw the rectangle pattern
            pattern.drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation)

        # If they choose 'Circle Patterns'
        elif mode == 2:
            #### Add Input Statement(s) as needed ####
            centerX = eval(input("Enter the x coordinate of the center position: "))
            centerY = eval(input("Enter the y coordinate of the center position: "))
            offset = eval(input("Enter the offset of the pattern: "))
            radius = eval(input("Enter the radius of each circle in the pattern: "))
            count = eval(input("Enter the number of circles in the pattern: "))
            #### End Add Inputs Statement(s) ####

            # Draw the circle pattern
            pattern.drawCirclePattern(centerX, centerY, offset, radius, count)

        # If they choose 'Super Patterns'
        elif mode == 3:
            #### Add Input Statement(s) as needed ####
            num = input("Enter the number of random patterns to be drawn (default is 3): ")
            #### End Add Inputs Statement(s) ####
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
        if response == 2:
            pattern.reset()
            pattern.setup()
        elif response == 3:
            playAgain = False
        #### End Add Inputs Statement(s) ####

    # print a message saying thank you
    print("Thanks for playing!")
    pattern.done()


main()

