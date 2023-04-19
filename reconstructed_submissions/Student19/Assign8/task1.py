# @@@@@@@@@@@@
# CS1400 - MW1 (14 week)
# Assignment 8

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
            centerX = int(input("What would you like the center x coordinate to be: "))
            centerY = int(input("What would you like the center y coordinate to be: "))
            offset = int(input("What would you like the distance from the Center to be: "))
            width = int(input("What would you like the width of the rectangle to be: "))
            height = int(input("What would you like the height of the rectangle to be: "))
            count = int(input("How many rectangles would you like me to draw: "))
            rotation = int(input("What would you like the rotation of the rectangle to be: "))
            #### End Add Inputs Statement(s) ####
            # Draw the rectangle pattern
            pattern.drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation)
        # If they choose 'Circle Patterns'
        elif mode == 2:
            #### Add Input Statement(s) as needed ####
            centerX = int(input("What would you like the center x coordinate to be: "))
            centerY = int(input("What would you like the center y coordinate to be: "))
            offset = int(input("What would you like the distance from the Center to be: "))
            radius = int(input("What would you like the circle radius to be: "))
            count = int(input("How many circles would you like me to draw: "))
            #### End Add Inputs Statement(s) ####
            # Draw the circle pattern
            pattern.drawCirclePattern(centerX, centerY, offset, radius, count)
        # If they choose 'Super Patterns'
        elif mode == 3:
            #### Add Input Statement(s) as needed ####
            num = input("Would you like to add a number?: ")
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
        elif response >= 3 or response <= 0:
            playAgain = False
        
        #### End Add Inputs Statement(s) ####
    # print a message saying thank you
    print("Thanks for playing!")
    pattern.done()
main()

