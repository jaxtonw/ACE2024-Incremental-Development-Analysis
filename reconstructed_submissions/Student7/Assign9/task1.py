# @@@@@@@@@@@@
# CS 1400 (14 week)
# Assignment 9

import turtle

# Create Face Class
class Face:
    def __init__(self):
        self.__smile = True
        self.__happy = True
        self.__darkEyes = True

    def draw_face(self):
        turtle.clear()
        self.__drawHead()
        self.__drawEyes()
        self.__drawMouth()

    # Determine attributes of face
    def isSmile(self):
        return self.__smile

    def isHappy(self):
        return self.__happy

    def isDarkEyes(self):
        return self.__darkEyes

    # Change attributes
    def changeMouth(self):
        self.__smile = not self.__smile
        self.draw_face()

    def changeEmotion(self):
        self.__happy = not self.__happy
        self.draw_face()

    def changeEyes(self):
        self.__darkEyes = not self.__darkEyes
        self.draw_face()
    
    # Draw each piece of the face    
    def __drawHead(self):
        turtle.penup()
        turtle.goto(0,-50)
        turtle.setheading(0)
        turtle.width(1)
        turtle.pendown()
        if self.__happy:
            turtle.fillcolor("Yellow")
        else:
            turtle.fillcolor("Red")
        turtle.begin_fill()
        turtle.circle(100)
        turtle.end_fill()
    
    def __drawEyes(self):
        turtle.penup()
        turtle.goto(-30,80)
        turtle.setheading(0)
        turtle.width(1)
        turtle.pendown()
        if self.__darkEyes:
            turtle.fillcolor("Black")
        else:
            turtle.fillcolor("Blue")
        turtle.begin_fill()
        turtle.circle(10)
        turtle.penup()
        turtle.forward(60)
        turtle.pendown()
        turtle.circle(10)
        turtle.end_fill()
        
    def __drawMouth(self):
        turtle.penup()
        turtle.width(5)
        if self.__smile:
            turtle.goto(-70,20)
            turtle.setheading(-45)
            turtle.pendown()
            turtle.circle(100,90)
        else:
            turtle.goto(70,15)
            turtle.setheading(135)
            turtle.pendown()
            turtle.circle(100,90)
        


def main():
    # Create a face object and draw it
    face = Face()
    face.draw_face()

    done = False

    while not done:
        print("Change My Face")
        mouth = "frown" if face.isSmile() else "smile"
        emotion = "angry" if face.isHappy() else "happy"
        eyes = "blue" if face.isDarkEyes() else "black"
        print("1) Make me", mouth)
        print("2) Make me", emotion)
        print("3) Make my eyes", eyes)
        print("0) Quit")

        # Ask user for input
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


main()

