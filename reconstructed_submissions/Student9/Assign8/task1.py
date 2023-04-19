# @@@@@@@@@@@@@@@
# CS1400 - 14 Week
# Assignment 8


import pattern
from random import randint
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
            centerX,centerY = input("Where would you like the center to be?").split(",")
            offset = input("Offset?")
            count = input("How many rectangles would you like?")
            rotation = input("Rotation?")
            width = input("What is the width of each rectangle?")
            height = input("What is the height of each rectangle?")
            color = ""
            # Draw the rectangle pattern
            pattern.drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation,color)
        # If they choose 'Circle Patterns'
        elif mode == 2:
            centerX,centerY = input("Where would you like the center to be?").split(",")
            offset = input("Offset?")
            count = input("How many circles would you like?")
            radius = input("What is the radius of each circle?")
            color = ""
            # Draw the circle pattern
            pattern.drawCirclePattern(centerX, centerY, offset, radius, count,color)
        # If they choose 'Super Patterns'
        elif mode == 3:
            centerX = randint(1, 1000)
            centerY = randint(1, 800)
            height = randint(1, 360)
            width = randint(1, 360)
            radius = randint(1, 360)
            offset = randint(1, 360)
            count = randint(1, 360)
            rotation = randint(1, 360)
            color = ""
            pattern.drawSuperPattern(centerX,centerY,height, width,radius,offset,count,rotation,color)

        # Play again?
        again = input("Do you want to play again?(y/n)")
        if again == 'y':
            print("1) Yes, and keep drawings")
        else:
            print("Thank you for playing!")
            pattern.done()
        
        
main()
        


