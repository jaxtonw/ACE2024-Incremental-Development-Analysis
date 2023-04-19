# @@@@@@@@@@
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
        
    def __drawHead(self):
        turtle.pensize(3)
        if self.isHappy():
            turtle.fillcolor("yellow")
        else:
            turtle.fillcolor("red")
        turtle.penup()
        turtle.goto(0, -100)
        turtle.setheading(0)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(100)
        turtle.end_fill()
        
    def __drawEyes(self):
        if self.isDarkEyes():
            turtle.fillcolor("black)"
        else:
            turtle.fillcolor("blue")
        turtle.penup()
        turtle.goto(-40, 10)
        turtle.setheading(0)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(10)
        turtle.end_fill()
        
        turtle.penup()
        turtle.goto(40, 10)
        turtle.setheading(0)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(10)
        turtle.end_fill()
        
    def __drawMouth(self):
        turtle.penup()
        turtle.color("black")
        turtle.pensize(7)
        if self.isSmile():
            turtle.goto(-50, -20)
            turtle.pendown()
            turtle.setheading(270)
            turtle.circle(50, 180)
        else:
            turtle.goto(50, -40)
            turtle.setheading(90)
            turtle.pendown()
            turtle.circle(50, 180)
            
    
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


