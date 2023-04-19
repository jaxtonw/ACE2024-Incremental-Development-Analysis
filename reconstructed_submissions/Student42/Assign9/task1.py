# @@@@@@@@@@@@@
# CS1400 - 14 week
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
        self.__smile = not self.__smile + self.__smile
        
    def isHappy(self):
        self.__happy = not self.__happy + self.__happy
        
    def isDarkEyes(self):
        self.__darkEyes = not self.__darkEyes + self.__darkEyes
        
    def changeMouth(self):
        self.isSmile()
        self.draw_face()
        
    def changeEmotion(self):
        self.isHappy()
        self.draw_face()
        
    def changeEyes(self):
        self.isDarkEyes()
        self.draw_face()

    def __drawHead(self):
        if self.__happy is True:
            color = "yellow"
        else:
            color = "red"
        turtle.setheading(0)
        turtle.pu()
        turtle.goto(0, 0)
        turtle.color(color)
        turtle.pu()
        turtle.right(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.pd()
        turtle.begin_fill()
        turtle.circle(100)
        turtle.end_fill()
        turtle.color("black")
        
    def __drawEyes(self):
        if self.__darkEyes is True:
            color = "black"
        else:
            color = "blue"
        turtle.color(color)
        turtle.pu()
        turtle.goto(40, 20)
        turtle.pd()
        turtle.begin_fill()
        turtle.circle(10)
        turtle.end_fill()
        turtle.pu()
        turtle.goto(-40, 20)
        turtle.pd()
        turtle.begin_fill()
        turtle.circle(10)
        turtle.end_fill()
        turtle.pu()
        turtle.end_fill()
        turtle.color("black")
    
    def __drawMouth(self):
        turtle.width(7)
        if self.__smile is True:
            turtle.color("black")
            turtle.pu()
            turtle.goto(-57, -45)
            turtle.pd()
            turtle.setheading(-35)
            turtle.circle(100, 70)
            turtle.width(1)
        elif self.__smile is False:
            turtle.color("black")
            turtle.pu()
            turtle.goto(55, -45)
            turtle.setheading(145)
            turtle.pd()
            turtle.circle(100, 70)
            turtle.width(1)


def main():
    face = Face()
    face.draw_face()
    done = False
    while not done:
        print("Change My Face")
        mouth = "frown" or "smile"
        emotion = "angry" or "happy"
        eyes = "blue" or "black"
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

