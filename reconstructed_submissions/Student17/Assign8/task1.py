'''
    This is the starter file. Only fill in the areas indicated.
    Do not modify existing code.
    Replace this file header with the normal file header (name, etc)
'''
#### Add Import Statement(s) as needed ####
import pattern
#### End Add Import Statement(s) ####
def main():
    # Setup pattern
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
            centerXRec, centerYRec = eval(input("Select a center (x, y): "))
            offsetRec = eval(input("Select an offset: "))
            width = eval(input("Select a width of the individual rectangles: "))
            height = eval(input("Select a height of the individual rectangles: "))
            countRec = eval(input("Select the number of rectangles in the pattern: "))
            rotation = eval(input("Select the angle of which the rectangles will be rotated: "))
            #### End Add Inputs Statement(s) ####
            # Draw the rectangle pattern
            pattern.drawRectanglePattern(centerXRec, centerYRec, offsetRec, width, height, countRec, rotation)
        # If they choose 'Circle Patterns'
        elif mode == 2:
            #### Add Input Statement(s) as needed ####
            centerXCirc, centerYCirc = eval(input("Select a center (x, y): "))
            offsetCirc = eval(input("Select an offset: "))
            radius = eval(input("What is the radius of each individual circle: "))
            countCirc = eval(input("Select the number of circles in the pattern: "))
            #### End Add Inputs Statement(s) ####
            # Draw the circle pattern
            pattern.drawCirclePattern(centerXCirc, centerYCirc, offsetCirc, radius, countCirc)
        # If they choose 'Super Patterns'
        elif mode == 3:
            #### Add Input Statement(s) as needed ####
            num = eval(input("How many patterns will we have: "))
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
        playAgain = response == 1 or response == 2
        #### End Add Inputs Statement(s) ####
    # print a message saying thank you
    print("Thanks for playing!")
    pattern.done()
main()
