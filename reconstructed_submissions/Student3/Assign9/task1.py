# @@@@@@@@@@@
# CS1400 - MW1
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
        turtle.pu()
        turtle.goto(0, -100)
        turtle.pd()
        turtle.width(1)
        if self.isHappy():
            # happy color
            turtle.fillcolor("yellow")
        else:
            # angry color
            turtle.fillcolor("red")
        turtle.begin_fill()
        turtle.circle(100)
        turtle.end_fill()
        turtle.pu()
        
    def __drawEyes(self):
        for i in range(2):
            turtle.pu()
            # both eyes
            if i == 0:
                turtle.goto(-30, 20)
            else:
                turtle.goto(30, 20)
            turtle.pd()
            turtle.width(1)
            if self.isDarkEyes():
                # black eyes
                turtle.fillcolor("black")
            else:
                # blue eyes
                turtle.fillcolor("blue")
            turtle.begin_fill()
            turtle.circle(10)
            turtle.end_fill()
            turtle.pu()
            
    def __drawMouth(self):
        turtle.pu()
        if self.isSmile():
            # happy smile
            turtle.goto(-60, -30)
            turtle.setheading(315)
        else:
            # frown
            turtle.goto(60, -50)
            turtle.setheading(135)
        turtle.pd()
        turtle.width(10)
        turtle.circle(90, 90)
        turtle.setheading(0)
        turtle.pu()
        
    def isSmile(self):
        return self.__smile
    
    def isHappy(self):
        return self.__happy
    
    def isDarkEyes(self):
        return self.__darkEyes
    
    def changeMouth(self):
        # change smile boolean
        self.__smile = not self.__smile
        self.draw_face()
        
    def changeEmotion(self):
        # change happy boolean
        self.__happy = not self.__happy
        self.draw_face()
        
    def changeEyes(self):
        # change eyes boolean
        self.__darkEyes = not self.__darkEyes
        self.draw_face()
        

def main():
    turtle.speed(0)
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
