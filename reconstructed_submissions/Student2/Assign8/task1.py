# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#@@@@@-@@@@@@@-Assn8
#CS 1400-MW1 XL


#### Add Import Statement(s) as needed ####

#### End Add Import Statement(s) ####
def main():
    # Setup pattern
    import pattern
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
            from pattern import drawRectanglePattern
            centerX, centerY= eval(input("What is the center point: " , )) 
            width = eval(input("What is the width:  " ))
            height = eval(input("What is the height: " ))
            count = eval(input("What is the count:  " ))
            offset = eval(input("What is the offset: " ) + height)
            rotation = eval(input("What is the rotation: "))
            
            #### End Add Inputs Statement(s) ####
            # Draw the rectangle pattern
            pattern.drawRectanglePattern(centerX, centerY, offset, width, height, 
count, rotation)
        # If they choose 'Circle Patterns'
        elif mode == 2:
            #### Add Input Statement(s) as needed ####
            from pattern import drawCirclePattern
            centerX, centerY = eval(input("What is the center point:  " , ))
            radius = eval(input("What is the radius:  " ))
            count = eval(input("What is the count:  " ))
            offset = eval(input("What is the offset:  " ))+radius
            #### End Add Inputs Statement(s) ####
            # Draw the circle pattern
            pattern.drawCirclePattern(centerX, centerY, offset, radius, count)
        # If they choose 'Super Patterns'
        elif mode == 3:
            #### Add Input Statement(s) as needed ####
            num = eval(input("How many would you like to see?:  "))
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
         
            if response == 1:
            
            elif response ==2:
            
            elif response ==3:
            
            
        #### End Add Inputs Statement(s) ####
    # print a message saying thank you
    print("Thanks for playing!")
    pattern.done()
main()
