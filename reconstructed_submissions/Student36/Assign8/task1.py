# @@@@@@@@@@@@@@@
# CS 1400-14 week
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
            centerX,centerY = eval(input("Enter the center location(x,y): "))
            offset = int(input("Enter the offset: "))
            width = int(input("Enter the length: "))
            height = int(input("Enter the height: "))
            count = int(input("Enter the count: "))
            rotation = int(input("Enter the rotation: "))

            pattern.drawRectanglePattern(centerX, centerY, offset, width, height, 
count, rotation)
        # If they choose 'Circle Patterns'
        elif mode == 2:
            centerX, centerY = eval(input("Enter the center location(x,y): "))
            offset = int(input("Enter the offset: "))
            radius = int(input("Enter the radius: "))
            count = int(input("Enter the count: "))

            pattern.drawCirclePattern(centerX, centerY, offset, radius, count)
        # If they choose 'Super Patterns'
        elif mode == 3:
            num = input("Number? ")
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
            playAgain = True
            pattern.setup()
        elif response == 2:
            pattern.reset()
            playAgain = True
            pattern.setup()
        elif response == 3:
            playAgain = False
    print("Thanks for playing!")
    pattern.done()
main()
