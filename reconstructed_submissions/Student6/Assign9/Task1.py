# @@@@@@@@@@@@@
# CS1400 - 001
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

    def __drawHead(self):
        turtle.penup()
        turtle.goto(0, -100)
        turtle.pendown()
        turtle.begin_fill()
        if self.__happy:
            turtle.fillcolor("yellow")
        else:
            turtle.fillcolor("red")
        turtle.circle(100)
        turtle.end_fill()

    def __drawEyes(self):
        turtle.penup()
        turtle.goto(30, 20)
        turtle.pendown()
        turtle.begin_fill()
        if self.__darkEyes:
            turtle.fillcolor("black")
        else:
            turtle.fillcolor("blue")
        turtle.circle(15)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(-30, 20)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(15)
        turtle.end_fill()

    def __drawMouth(self):
        turtle.penup()
        turtle.width(10)
        if self.__smile:
            turtle.goto(-40, -40)
            turtle.pendown()
            turtle.setheading(316)
            turtle.circle(60, 90)
        else:
            turtle.goto(40, -40)
            turtle.pendown()
            turtle.setheading(316)
            turtle.circle(-60, -90)
        turtle.width(1)
        turtle.setheading(0)
        turtle.hideturtle()


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

