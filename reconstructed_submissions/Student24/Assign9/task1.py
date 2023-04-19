# @@@@@@@@@@@@
# CS1400 - MW1
# Assignment 9

import turtle


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
        
    def __drawHead(self):
        # Set the color of the head
        color = "yellow"
        # Make a conditional for if the face is angry
        if not self.isHappy():
            color = "red"
        # Actually draw the head
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.pu()
        turtle.goto(0, -100)
        turtle.setheading(0)
        turtle.pd()
        turtle.circle(100)
        turtle.end_fill()
        turtle.pu()
        
    def __drawEyes(self):
        # Set the color of the eyes
        color = "black"
        # Make a conditional for if the eyes are not dark
        if not self.isDarkEyes():
            color = "blue"
        # Draw the left eye
        turtle.fillcolor(color)
        turtle.pu()
        turtle.goto(-20, 30)
        turtle.begin_fill()
        turtle.pd()
        turtle.circle(10)
        turtle.end_fill()
        turtle.pu()
        # Draw the right eye
        turtle.goto(20, 30)
        turtle.begin_fill()
        turtle.pd()
        turtle.circle(10)
        turtle.end_fill()
        turtle.pu()
        
    def __drawMouth(self):
        # Create a conditional that checks for smiling or frowning choice
        if self.isSmile():
            turtle.pensize(10)
            turtle.pencolor("black")
            turtle.pu()
            turtle.goto(-40, -20)
            turtle.setheading(315)
            turtle.pd()
            turtle.circle(60, 85)
            turtle.pu()
            turtle.pensize(1)
            # self.isSmile() = False
            
        elif not self.isSmile():
            turtle.pensize(10)
            turtle.pencolor("black")
            turtle.pu()
            turtle.goto(40, -40)
            turtle.setheading(135)
            turtle.pd()
            turtle.circle(60, 85)
            turtle.pu()
            turtle.pensize(1)
            # self. isSmile() = True
            
    def isSmile(self):
        return self.__smile

    def isHappy(self):
        return self.__happy

    def isDarkEyes(self):
        return self.__darkEyes

    def changeMouth(self):
        self.__smile = not self.__smile
        self.draw_face()

    def changeEmotion(self):
        self.__happy = not self.__happy
        self.draw_face()

    def changeEyes(self):
        self.__darkEyes = not self.__darkEyes
        self.draw_face()


def main():
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

