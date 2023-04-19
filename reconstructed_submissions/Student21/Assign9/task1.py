# @@@@@@@@@@@@@@@@
# CECS1400 - MW1
# Assignment 9-Task 1


import turtle


class Face:
    def __init__(self):
        self.__smile = True
        self.__happy = True
        self.__darkEyes = True
    # draw head
    def __drawHead(self):
        # draw yellow face
        if self.__happy:
            turtle.penup()
            turtle.goto(0, -100)
            turtle.setheading(0)
            turtle.pendown()
            turtle.pensize(1)
            turtle.fillcolor("yellow")
            turtle.begin_fill()
            turtle.circle(100)
            turtle.end_fill()
            turtle.penup()
        # draw red face
        else:
            turtle.penup()
            turtle.goto(0, -100)
            turtle.setheading(0)
            turtle.pendown()
            turtle.pensize(1)
            turtle.fillcolor("red")
            turtle.begin_fill()
            turtle.circle(100)
            turtle.end_fill()
            turtle.penup()
     
    # draw right eye, then left eye    
    def __drawEyes(self):
        # draw black eyes
        if self.__darkEyes:
            turtle.penup()
            turtle.goto(30, 40)
            turtle.pendown()
            turtle.pensize(1)
            turtle.fillcolor("black")
            turtle.begin_fill()
            turtle.circle(10)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-30, 40)
            turtle.pendown()
            turtle.fillcolor("black")
            turtle.begin_fill()
            turtle.circle(10)
            turtle.end_fill()
            turtle.penup()
        # draw blue eyes
        else:
            turtle.penup()
            turtle.goto(30, 40)
            turtle.pendown()
            turtle.pensize(1)
            turtle.fillcolor("blue")
            turtle.begin_fill()
            turtle.circle(10)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-30, 40)
            turtle.pendown()
            turtle.fillcolor("blue")
            turtle.begin_fill()
            turtle.circle(10)
            turtle.end_fill()
            turtle.penup()
    
    # draw mouth (smile)    
    def __drawMouth(self):
        # draw smile
        if self.__smile:
            turtle.goto(-35, -30)
            turtle.pendown()
            turtle.pensize(10)
            turtle.color("black")
            turtle.setheading(320)
            turtle.circle(60, 80)
            turtle.penup()
        # draw frown
        else:
            turtle.goto(-35, -30)
            turtle.pendown()
            turtle.pensize(10)
            turtle.color("black")
            turtle.setheading(40)
            turtle.circle(-60, 80)
            turtle.penup()
    
    
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
        self.__smile = not self.isSmile()
        self.draw_face()

    def changeEmotion(self):
        self.__happy = not self.isHappy()
        self.draw_face()

    def changeEyes(self):
        self.__darkEyes = not self.isDarkEyes()
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
