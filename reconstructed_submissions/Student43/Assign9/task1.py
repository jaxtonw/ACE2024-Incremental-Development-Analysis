# @@@@@@@@@@@@@
# CS1400 - MW1 XL
# Assignment 9

# Import turtle module
import turtle


# Define Face class
class Face:
    # Define initial method
    def __init__(self):
        self.__smile = True
        self.__happy = True
        self.__darkEyes = True
    
    # Define method to draw whole face
    def draw_face(self):
        turtle.clear()
        self.__drawHead()
        self.__drawEyes()
        self.__drawMouth()
        
    # Define method that only draws the head and fills it in
    def __drawHead(self):
        # Set conditional to either draw yellow face or red face
        if self.__happy:
            turtle.penup()
            turtle.setheading(0)
            turtle.goto(0, -100)
            turtle.fillcolor("yellow")
            turtle.begin_fill()
            turtle.pendown()
            turtle.circle(100)
            turtle.end_fill()
        elif not self.__happy:
            turtle.penup()
            turtle.setheading(0)
            turtle.goto(0, -100)
            turtle.fillcolor("red")
            turtle.begin_fill()
            turtle.pendown()
            turtle.circle(100)
            turtle.end_fill()
    
    # Define method that only draws the eyes
    def __drawEyes(self):
        turtle.penup()
        turtle.goto(-25, 30)
        # Set conditional to either draw black eyes or blue eyes
        if self.__darkEyes:
            # Draw the left eye
            turtle.fillcolor("black")
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(10)
            turtle.end_fill()
            # Draw the right eye
            turtle.penup()
            turtle.goto(25, 30)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(10)
            turtle.end_fill()
          
        elif not self.__darkEyes:
            # Draw the left eye
            turtle.fillcolor("blue")
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(10)
            turtle.end_fill()
            # Draw the right eye
            turtle.penup()
            turtle.goto(25, 30)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(10)
            turtle.end_fill()

    # Define methods that only draws the mouth
    def __drawMouth(self):
        # Set conditional to either draw a smile or a frown
        if self.__smile:
            turtle.penup()
            turtle.goto(-50, -43)
            turtle.width(5)
            turtle.pendown()
            turtle.setheading(320)
            turtle.circle(80, 80)
            turtle.width(1)
        elif not self.__smile:
            turtle.penup()
            turtle.goto(50, -43)
            turtle.width(5)
            turtle.pendown()
            turtle.setheading(140)
            turtle.circle(80, 80)
            turtle.width(1)
        
    # Define methods
    def isSmile(self):
        return self.__smile

    def isHappy(self):
        return self.__happy

    def isDarkEyes(self):
        return self.__darkEyes

    # Define methods that change parts of the face
    def changeMouth(self):
        self.__smile = not self.__smile
        self.draw_face()

    def changeEmotion(self):
        self.__happy = not self.__happy
        self.draw_face()

    def changeEyes(self):
        self.__darkEyes = not self.__darkEyes
        self.draw_face()


# Define main function
def main():
    face = Face()
    face.draw_face()

    done = False

    # Create loop to print menu an redraw face if necessary
    while not done:
        print("Change My Face")
        mouth = "frown" if face.isSmile() else "smile"
        emotion = "angry" if face.isHappy() else "happy"
        eyes = "blue" if face.isDarkEyes() else "black"
        print("1) Make me", mouth)
        print("2) Make me", emotion)
        print("3) Make my eyes", eyes)
        print("0) Quit")

        menu = eval(input("Enter a selection: "))

        if menu == 1:
            face.changeMouth()
        elif menu == 2:
            face.changeEmotion()
        elif menu == 3:
            face.changeEyes()
        else:
            break

    print("Thanks for Playing")

    turtle.hideturtle()
    turtle.done()


# Call the main function
main()

