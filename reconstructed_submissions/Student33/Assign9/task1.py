# @@@@@@@@@@@@
# CS1400 - 009
# Assignment 009

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
        if self.__happy:
            turtle.width(5)
            turtle.penup()
            turtle.goto(0,-100)
            turtle.setheading(0)
            turtle.fillcolor("yellow")
            turtle.begin_fill()
            turtle.pendown()
            turtle.circle(100)
            turtle.end_fill()
        else:
            turtle.penup()
            turtle.goto(0, -100)
            turtle.setheading(0)
            turtle.fillcolor("red")
            turtle.begin_fill()
            turtle.pendown()
            turtle.circle(100)
            turtle.end_fill()
        
    def __drawEyes(self):
        if self.__darkEyes:
            turtle.penup()
            turtle.goto(-25, 30)
            turtle.setheading(0)
            turtle.fillcolor("black")
            turtle.begin_fill()
            turtle.pendown()
            turtle.circle(15)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(25, 30)
            turtle.setheading(0)
            turtle.begin_fill()
            turtle.pendown()
            turtle.circle(15)
            turtle.end_fill()
        else:
            turtle.penup()
            turtle.goto(-25, 30)
            turtle.setheading(0)
            turtle.fillcolor("blue")
            turtle.begin_fill()
            turtle.pendown()
            turtle.circle(15)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(25, 30)
            turtle.setheading(0)
            turtle.begin_fill()
            turtle.pendown()
            turtle.circle(15)
            turtle.end_fill()
        
    def __drawMouth(self):
        if self.__smile:
            turtle.penup()
            turtle.goto(-55,-30)
            turtle.setheading(315)
            turtle.pendown()
            turtle.width(5)
            turtle.circle(80, 90)
        else:
            turtle.penup()
            turtle.goto(55, -30)
            turtle.setheading(135)
            turtle.pendown()
            turtle.width(5)
            turtle.circle(80, 90)

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
        self.__darkEyes = not self.__darkEyes"        self.draw_face()


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
            face.changeEyes()"        else:
            break

    print("Thanks for Playing")

    turtle.hideturtle()
    turtle.done()


main()

