# @@@@@@@@@@@
# Assignment 8 Task 1
# CS 1400 14 week

#### Add Import Statement(s) as needed ####
import pattern
from random import randint
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
            centerX, centerY = eval(input("Pick the center point (x, y): "))
            width = eval(input("Input width: "))
            height = eval(input("Input height: "))
            offset = eval(input("Choose offset: "))
            count = eval(input("How many rectangles? "))
            rotation = eval(input("Input angle of rotation: "))
            #### End Add Inputs Statement(s) ####
            # Draw the rectangle pattern
            pattern.drawRectanglePattern(centerX, centerY, offset, width, height, 
count, rotation)
        # If they choose 'Circle Patterns'
        elif mode == 2:
            #### Add Input Statement(s) as needed ####
            centerX, centerY = eval(input("Pick the center point (x, y): "))
            radius = eval(input("Input radius: "))
            offset = eval(input("Choose offset: "))
            count = eval(input("How many circles? "))
            #### End Add Inputs Statement(s) ####
            # Draw the circle pattern
            pattern.drawCirclePattern(centerX, centerY, offset, radius, count)
        # If they choose 'Super Patterns'
        elif mode == 3:
            #### Add Input Statement(s) as needed ####
            num = input("How many patterns would you like? ")
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
        # Clears board
        if response == 2:
            pattern.reset()
        
        # Countinues program    
        playAgain = response == 1 or response == 2
        #### End Add Inputs Statement(s) ####
    # print a message saying thank you
    print("Thanks for playing!")
    pattern.done()
main()
