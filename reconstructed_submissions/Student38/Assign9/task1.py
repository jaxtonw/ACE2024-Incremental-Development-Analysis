# @@@@@@@@@@@@@
# CS-1400 MW1
# Assignment 9

import turtle
turtle.showturtle()
turtle.speed(0)

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
            turtle.pu()
            turtle.goto(0, 0)
            turtle.fillcolor("yellow")
            turtle.setheading(0)
            turtle.pd()
            turtle.begin_fill()
            turtle.circle(100)
            turtle.end_fill()
            turtle.pu()
        else:
            turtle.pu()
            turtle.goto(0, 0)
            turtle.fillcolor("red")
            turtle.setheading(0)
            turtle.pd()
            turtle.begin_fill()
            turtle.circle(100)
            turtle.end_fill()
            turtle.pu()
            
    
    def __drawEyes(self):
        if self.__darkEyes:
            turtle.pu()
            turtle.goto(-40, 110)
            turtle.fillcolor("black")
            turtle.pd()
            turtle.begin_fill()
            turtle.circle(15)
            turtle.pu()
            turtle.goto(40, 110)
            turtle.pd()
            turtle.circle(15)
            turtle.end_fill()
            turtle.pu()
        else:
            turtle.pu()
            turtle.goto(-40, 110)
            turtle.fillcolor("blue")
            turtle.pd()
            turtle.begin_fill()
            turtle.circle(15)
            turtle.pu()
            turtle.goto(40, 110)
            turtle.pd()
            turtle.circle(15)
            turtle.end_fill()
            turtle.pu()
    
    def __drawMouth(self):
        if self.__smile:
            turtle.pu()
            turtle.goto(-40, 50)
            turtle.setheading(320)
            turtle.pd()
            turtle.pensize(5)
            turtle.circle(75, 75)
            turtle.pensize(1)
            turtle.pu()
        else:
            turtle.pu()
            turtle.goto(40, 50)
            turtle.setheading(150)
            turtle.pd()
            turtle.pensize(5)
            turtle.circle(75, 75)
            turtle.pensize(1)
            turtle.pu()

    def isSmile(self):
        return self.__smile

    def isHappy(self):
        return self.__happy

    def isDarkEyes(self):
        return self.__darkEyes

    def changeMouth(self):
        if self.isSmile():
            self.__smile = False
        else:
            self.__smile = True
        self.draw_face()
        

    def changeEmotion(self):
        if self.isHappy():
            self.__happy = False
        else:
            self.__happy = True
        self.draw_face()

    def changeEyes(self):
        if self.isDarkEyes():
            self.__darkEyes = False
        else:
            self.__darkEyes = True
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

