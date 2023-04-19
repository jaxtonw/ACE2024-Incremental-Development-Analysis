# @@@@@@@@@@@  
# CS 1400 - MW1 XL
# Assignment 009

import turtle

turtle.speed(10)


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

    # this is where my methods begin
    # draw head only needs to change the color of the face
    def __drawHead(self):
        turtle.pensize(2)
        turtle.clear()
        turtle.penup()
        turtle.goto(0, -100)
        turtle.setheading(0)
        turtle.pendown()
        if self.__happy:
            turtle.fillcolor("yellow")
        else:
            turtle.fillcolor("red")
        turtle.begin_fill()
        turtle.circle(100)
        turtle.end_fill()
        turtle.penup()

    # eyes is similar to head, only the eye color needs to change
    def __drawEyes(self):
        turtle.goto(-40, 30)
        turtle.setheading(0)
        turtle.pendown()
        if self.__darkEyes:
            turtle.fillcolor("black")
        else:
            turtle.fillcolor("blue")
        turtle.begin_fill()
        turtle.circle(15)
        turtle.penup()
        turtle.forward(80)
        turtle.pendown()
        turtle.circle(15)
        turtle.end_fill()
        turtle.penup()

    # the mouth changes shape so each if
    # is for a smile or a frown
    def __drawMouth(self):
        turtle.goto(-40, -20)
        turtle.setheading(0)
        turtle.pendown()
        if self.__smile:
            turtle.pensize(10)
            turtle.right(50)
            turtle.circle(50, 90)
        else:
            turtle.pensize(10)
            turtle.left(50)
            turtle.circle(-50, 90)
            
    def isSmile(self):
        return self.__smile

    def isHappy(self):
        return self.__happy

    def isDarkEyes(self):
        return self.__darkEyes

    # these are all the same besides the variable name
    # this switches the bool from what it currently is
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
        # the if statements is how the program switches from one message to the other
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

