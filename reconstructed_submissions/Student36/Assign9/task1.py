# @@@@@@@@@@@@@@@
# CS 1400- 14 week
# Assignment 9


import turtle

class Face:
    def __init__(self):
        self.__smile = True
        self.__happy = True
        self.__darkEyes = True
    #start of modifiable
    def __drawHead(self):
        turtle.reset()
        turtle.penup()
        turtle.goto(0,-100)
        turtle.pendown()
        if self.__happy == True:
            turtle.fillcolor("yellow")
        elif self.__happy == False:
            turtle.fillcolor("red")
        turtle.begin_fill()
        turtle.circle(100)
        turtle.end_fill()
    def __drawEyes(self):
        if self.__darkEyes == True:
            turtle.fillcolor("black")
        elif self.__darkEyes == False:
            turtle.fillcolor("blue")
        #left eye
        turtle.penup()
        turtle.goto(-30,30)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(10)
        #right eye
        turtle.penup()
        turtle.goto(30,30)
        turtle.pendown()
        turtle.circle(10)
        turtle.end_fill()
    def __drawMouth(self):
        turtle.penup()
        if self.__smile == True:
            turtle.goto(-50, -60)
            turtle.setheading(330)
        elif self.__smile == False:
            turtle.goto(50,-60)
            turtle.setheading(150)
        turtle.width(4)
        turtle.pendown()
        turtle.circle(100,60)
    #end of modifiable
    def draw_face(self):
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
        if self.__smile == True:
            self.__smile = not True
        elif self.__smile == False:
            self.__smile = True
        self.draw_face()
    def changeEmotion(self):
        if self.__happy == True:
            self.__happy = not True
        elif self.__happy == False:
            self.__happy = True
        self.draw_face()
    def changeEyes(self):
        if self.__darkEyes == True:
            self.__darkEyes = not True
        elif self.__darkEyes == False:
            self.__darkEyes = True
        self.draw_face()
def main():
    face = Face()
    face.draw_face()
    done = False
    while not done:
        print("Change My Face")
        mouth = "frown" if face.isSmile() == True else "smile"
        emotion = "angry" if face.isHappy() == True else "happy"
        eyes = "blue" if face.isDarkEyes() == True else "black"
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
