# @@@@@@@@@@@@@
# CS1400 - MW1
# Assignment 9

import turtle


class Face:
    def __init__(self):
        self.__smile = True
        self.__happy = True
        self.__darkEyes = True

    def __drawHead(self):
        turtle.reset()
        if self.__happy == True:
            fillColor = "yellow"
        else:
            fillColor = "red"
        turtle.speed(0)
        turtle.pu()
        turtle.goto(0, -100)
        turtle.pd()
        turtle.fillcolor(fillColor)
        turtle.begin_fill()
        turtle.circle(100)
        turtle.end_fill()

    def __drawEyes(self):
        if self.__darkEyes == True:
            fillColor = "black"
        else:
            fillColor = "blue"

        turtle.pu()
        turtle.goto(-20, 15)
        turtle.setheading(0)
        turtle.fillcolor(fillColor)
        turtle.begin_fill()
        turtle.circle(7)
        turtle.pu()
        turtle.forward(40)
        turtle.pd()
        turtle.circle(7)
        turtle.end_fill()
        turtle.pu()

    def __drawMouth(self):
        if self.__smile == True:
            setHeading = 330
            goToX = -15
            goToY = -30
        else:
            setHeading = 150
            goToX = 15
            goToY = -30
            
        turtle.pu()
        turtle.goto(goToX, goToY)
        turtle.setheading(setHeading)
        turtle.pensize(5)
        turtle.pd()
        turtle.circle(radius=30, extent=60)
        turtle.pu()
        turtle.hideturtle()

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
        #return not self.__happy
        self.__smile = not self.__smile
        self.draw_face()

    def changeEmotion(self):
        #return not self.__happy
        self.__happy = not self.__happy
        self.draw_face()

    def changeEyes(self):
        #return not self.__darkEyes 
        self.__darkEyes = not self.__darkEyes
        self.draw_face()


def main():
    face = Face()"    face.draw_face()

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
            not face.isSmile
            face.changeMouth()
        elif menu == 2:
            not face.isHappy
            face.changeEmotion()
        elif menu == 3:
            not face.isDarkEyes
            face.changeEyes()
        else:
            break

    print("Thanks for Playing")

    turtle.hideturtle()
    turtle.done()


main()

