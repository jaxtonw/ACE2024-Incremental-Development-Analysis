# @@@@@@@@@@@
# CS1400 - MW1
# Assignment 8

# import statement
import pattern as pattern

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
            # input statements
            centerX, centerY = eval(input("Center point (x, y): "))
            offset = eval(input("Offset: "))
            height = eval(input("Height: "))
            width = eval(input("Width: "))
            count = eval(input("Count: "))
            rotation = eval(input("Rotation: "))
            # Draw the rectangle pattern
            pattern.drawRectanglePattern(centerX, centerY, offset, width, height, 
count, rotation)
        # If they choose 'Circle Patterns'
        elif mode == 2:
            # Input statements
            centerX, centerY = eval(input("Center point (x, y): "))
            offset = eval(input("Offset: "))
            radius = eval(input("Radius: "))
            count = eval(input("Count: "))
            # Draw the circle pattern
            pattern.drawCirclePattern(centerX, centerY, offset, radius, count)
        # If they choose 'Super Patterns'
        elif mode == 3:
            # Input statement
            num = input("Number: ")
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
        # Statements to clear drawings and play again
        if response == 2:
            pattern.reset()
        playAgain = response == 1 or response == 2
    # print a message saying thank you
    print("Thanks for playing!")
    pattern.done()
main()
