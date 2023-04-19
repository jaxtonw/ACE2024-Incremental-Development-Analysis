# @@@@@@@@@@@@@@
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
        
    def isSmile(self):
        return self.__smile
        
    def isHappy(self):
        return self.__happy
        
    def isDarkEyes(self):
        return self.__darkEyes
        
    def changeMouth(self):
        self.__smile = False if self.__smile else True
        self.draw_face()
        
    def changeEmotion(self):
        self.__happy = False if self.__happy else True
        self.draw_face()
        
    def changeEyes(self):
        self.__darkEyes = False if self.__happy else True
        self.draw_face()

    def __drawHead(self):
        # Yellow Happy Head
        if self.__happy:
            turtle.setheading(0)
            turtle.penup()
            turtle.goto(0, 0)
            turtle.pendown()
            turtle.begin_fill()
            turtle.fillcolor("yellow")
            turtle.circle(100)
            turtle.end_fill()
        # Red Angry Head
        else:
            turtle.setheading(0)
            turtle.penup()
            turtle.goto(0, 0)
            turtle.pendown()
            turtle.begin_fill()
            turtle.fillcolor("red")
            turtle.circle(100)
            turtle.end_fill()

    def __drawEyes(self):
        # Black eyes
        if self.__darkEyes:
            turtle.penup()
            turtle.begin_fill()
            turtle.fillcolor("black")
            turtle.goto(25, 134)
            turtle.pendown()
            turtle.circle(15)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-50, 134)
            turtle.begin_fill()
            turtle.fillcolor("black")
            turtle.pendown()
            turtle.circle(15)
            turtle.end_fill()
        # Blue Eyes
        else:
            turtle.penup()
            turtle.begin_fill()
            turtle.fillcolor("blue")
            turtle.goto(25, 134)
            turtle.pendown()
            turtle.circle(15)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-50, 134)
            turtle.begin_fill()
            turtle.fillcolor("blue")
            turtle.pendown()
            turtle.circle(15)
            turtle.end_fill()

    def __drawMouth(self):
        # Smile
        if self.__smile:
            turtle.penup()
            turtle.goto(-65, 66)
            turtle.width(5)
            turtle.setheading(315)
            turtle.pendown()
            turtle.circle(90, 90)
            turtle.width(1)
        # Frown
        else:
            turtle.penup()
            turtle.goto(65, 46)
            turtle.pendown()
            turtle.width(5)
            turtle.setheading(135)
            turtle.circle(90, 90)
            turtle.width(1)

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

