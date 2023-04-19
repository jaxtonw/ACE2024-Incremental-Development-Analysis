# @@@@@@@@@@@@@@
# CS1400 - 14 week
# Assignment 9 task 1

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

    # module to draw the shape of the head 
    def __drawHead(self):
        turtle.pensize(1)
        turtle.penup()
        turtle.goto(0, 0)
        turtle.goto(0, -100)
        turtle.begin_fill()
        turtle.pendown()
        turtle.circle(100)
        # statement to have the head be red or yellow
        if self.__happy is False:
            turtle.color("red")
        else:
            turtle.color("Yellow")
        turtle.end_fill()
        turtle.penup()
    
    # module to draw both  eyes 
    def __drawEyes(self):
        turtle.pensize(1)
        turtle.penup()
        turtle.goto(-30, 25)
        turtle.pendown()
        turtle.fillcolor()
        turtle.begin_fill()
        turtle.circle(20)
        turtle.penup()
        turtle.goto(30, 25)
        turtle.pendown()
        turtle.circle(20)
        # statement to have the eyes be blue of black
        if self.__darkEyes is False:
            turtle.color("blue")
        else:
            turtle.color("black")
        turtle.end_fill()
        turtle.penup()
        
    # module that will draw a mouth
    def __drawMouth(self):
        turtle.penup()
        turtle.goto(-50, -30)
        turtle.pensize(6)
        turtle.color("black")
        turtle.pendown()
        # statement to draw a frown or smile
        if self.__smile is True:
            turtle.setheading(-60)
            turtle.circle(60, 120)
        else:
            turtle.penup()
            turtle.goto(50, -45)
            turtle.pendown()
            turtle.setheading(120)
            turtle.circle(60, 120)
        turtle.setheading(0)


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

