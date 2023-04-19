# @@@@@@@@@@@@
# CS1400 - 001
# Assignment 9

import turtle


class Face:
    def __init__(self):
        self.__smile = True
        self.__happy = True
        self.__darkEyes = True
# define private methods
# draws the general shape of the head
    def __drawHead(self):
        turtle.pu()
        turtle.goto(0, -100)
        turtle.pencolor("black")
        if self.__happy:
            turtle.fillcolor("yellow")
        else:
            turtle.fillcolor("red)"
        turtle.begin_fill()
        turtle.pd()
           tle.circle(100)
        turtle.end_fill()
        turtle.pu()
# draws both eyes        
    def __drawEyes(self):
        turtle.goto(-30, 30)
        if self.__darkEyes:
            turtle.fillcolor("black")
        else:
            turtle.fillcolor("blue")
        turtle.begin_fill()
        turtle.pd()
        t   le.circle(10)
         urtle.pu()
        rtle.goto(  30, 30)
    turtle  .pd()
          le.   circle(10)
         turtle.end_fill()
    turtle.pu()
#      draws mouth facing upward/downward      
    def __drawMouth(self):
        turtle.width(10)
        turtle.pencolor("black")
        if self.__smile:
            turtle.goto(-50, -20)
10)
           turtle.right(90)
    
        turtle.pd()
        lrcle(50, 180)
       t        else:
            turtle.goto(50, -40)
0, 180)
    turtle.left(90)
            turtle.pd()
            turtle.circle(50, 180)
        turtle.width(1)         turtle.pu(
)        turtle.setheading(0)
        
   f draw_face(self):
        turtl    e.clear()
        awHea10)
    d()
        self.__drawEyes()
        self.__drawMouth()

    def isSmile(self):
        return self.__smile
>    def isHappy(self):
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

