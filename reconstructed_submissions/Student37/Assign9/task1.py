# @@@@@@@@@
# CS1400 - MW1
# Assignment 9 - task1

import turtle
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
        
        
    def isSmile(self):
        if self.__smile:
            return True
        else:
            return False
        
        
    def isHappy(self):
        if self.__happy:
            return True
        else:
            return False
        
        
    def isDarkEyes(self):
        if self.__darkEyes:
            return True
        else:
            return False
        
        
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
        
    def __drawHead(self):
        turtle.pensize(1)
        if self.__happy:
            turtle.fillcolor("yellow")
        else:
            turtle.fillcolor("red")
        turtle.up()
        turtle.goto(0, -100)
        turtle.setheading(0)
        turtle.down()
        turtle.begin_fill()
        turtle.circle(200)
        turtle.end_fill()
        turtle.up()
        
    def __drawEyes(self):
        turtle.pensize(1)
        if self.__darkEyes:
            turtle.fillcolor("black")
        else:
            turtle.fillcolor("blue")
        turtle.up()
        turtle.goto(-50, 150)
        turtle.setheading(0)
        turtle.down()
        turtle.begin_fill()
        turtle.circle(25)
        turtle.end_fill()

        turtle.up()
        turtle.goto(50, 150)
        turtle.setheading(0)
        turtle.down()
        turtle.begin_fill()
        turtle.circle(25)
        turtle.end_fill()
        turtle.up()
        
    def __drawMouth(self):
        if self.__smile:
            turtle.up()
            turtle.goto(-90, 25)
            turtle.setheading(0)
            turtle.color("black")
            turtle.pensize(10)
            turtle.left(-30)
            turtle.down()
            turtle.circle(180, 60)
            turtle.up()
        else:
            turtle.up()
            turtle.goto(90, 25)
            turtle.setheading(180)
            turtle.pensize(10)
            turtle.left(-30)
            turtle.down()
            turtle.circle(180, 60)
            turtle.up()
            
        
def main():
    face = Face()
    face.draw_face()
    done = False
    
    mouth = "frown" or "smile"
    emotion = "angry" or "happy" #I did my best, but I couldn't figure out how to do it with these inside the
    eyes = "blue" or "black"     #loop. I wasn't sure what you were looking for with the blank between the two values
    
    while not done:
        print("Change My Face")
        print("1) Make me", mouth)
        print("2) Make me", emotion)
        print("3) Make my eyes", eyes)
        print("0) Quit")
        menu = eval(input("Enter a selection: "))
        if menu == 1:
            if mouth == "frown":
                mouth = "smile"
            else:
                mouth = "frown"
            face.changeMouth()
        elif menu == 2:
            if emotion == "happy":
                emotion = "angry"
            else:
                emotion = "happy"
            face.changeEmotion()
        elif menu == 3:
            if eyes == "black":
                eyes = "blue"
            else:
                eyes = "black"
            face.changeEyes()
        else:
            break
    print("Thanks for Playing")
    turtle.hideturtle()
    turtle.done()
    
main()
