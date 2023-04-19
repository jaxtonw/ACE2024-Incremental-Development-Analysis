# @@@@@@@@@@@@@@@@@@
# CS1400 - 001
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
        turtle.reset()
        
        if self.__happy:
            faceColor = "yellow"
        elif self.__happy == False:
            faceColor = "red"
        
               
        turtle.speed(0)
        turtle.penup()
        turtle.goto(0, -50)
        turtle.pendown()
        turtle.fillcolor(faceColor)
        turtle.begin_fill()
        turtle.circle(100)
        turtle.end_fill()
    
    def __drawEyes(self):
        
        if self.__darkEyes:
            eyeColor = "black"
        elif self.__darkEyes == False:
            eyeColor = "blue"
            
            
        
        turtle.penup()
        turtle.goto(-25, 65)
        turtle.fillcolor(eyeColor)
        turtle.begin_fill()
        turtle.pendown()
        turtle.circle(10)
        turtle.end_fill()
        turtle.penup()
        turtle.forward(50)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(10)
        turtle.end_fill()
        
        
    def __drawMouth(self):
        
        if self.__smile:
            turtle.color("black")
            turtle.penup()
            turtle.goto(-75, 50)
            turtle.pendown()
            turtle.pensize(5)
            turtle.right(90)
            turtle.circle(75, 180)
            turtle.width(0)

            
        elif self.__smile == False:
        
        
            turtle.penup()
            turtle.color("black")
            turtle.goto(-50, -20)
            turtle.pendown()
            turtle.pensize(5)
            turtle.right(90)
            turtle.circle(50, -180)
            turtle.width(0)
            turtle.hideturtle()

    def isSmile(self):
        return self.__smile

    def isHappy(self):
        return self.__happy

    def isDarkEyes(self):
        return self.__darkEyes
        
    def changeMouth(self):
        if self.__smile:
            self.__smile = False
        else:
            self.__smile = True

        self.draw_face()

    def changeEmotion(self):
        
        if self.__happy:
            self.__happy = False
        else:
            self.__happy = True 
        
        self.draw_face()

    def changeEyes(self):
        if self.__darkEyes:
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
