# @@@@@@@@@@@
# Assignment 9 Task 1
# CS 1400 14 week

import turtle


class Face:
    # Initializer
    def __init__(self):
        self.__smile = True
        self.__happy = True
        self.__darkEyes = True

    # Method to draw a face
    def draw_face(self):
        turtle.clear()
        self.__drawHead()
        self.__drawEyes()
        self.__drawMouth()

    # Returns boolean of if face is smiling
    def isSmile(self):
        return self.__smile
            
    # Returns boolean of if face is happy
    def isHappy(self):
        return self.__happy
        
    # Returns boolean of if face has dark eyes
    def isDarkEyes(self):
        return self.__darkEyes

    # Switches __smile boolean and redraws face
    def changeMouth(self):
        self.__smile = not self.__smile
        self.draw_face()

    # Switches __happy boolean and redraws face
    def changeEmotion(self):
        self.__happy = not self.__happy
        self.draw_face()

    # Switches __darkEyes boolean and redraws face
    def changeEyes(self):
        self.__darkEyes = not self.__darkEyes
        self.draw_face()
    
    # Draws yellow face if happy and red if angry
    def __drawHead(self):
    # to draw yellow face
        if self.isHappy():
            turtle.penup()
            turtle.goto(0, -100)
            turtle.setheading(0)
            turtle.pendown()
            turtle.begin_fill()
            turtle.fillcolor("yellow")
            turtle.circle(100)
            turtle.end_fill()
            turtle.penup()
    # to draw red face
        else:
            turtle.penup()
            turtle.goto(0, -100)
            turtle.setheading(0)
            turtle.pendown()
            turtle.begin_fill()
            turtle.fillcolor("red")
            turtle.circle(100)
            turtle.end_fill()
            turtle.penup()
    
    # Draws black eyes if darkeyes and blue eyes if not
    def __drawEyes(self):
    # to draw black eyes
        if self.isDarkEyes():
            turtle.penup()
            turtle.goto(-25, 40)
            turtle.pendown()
            turtle.begin_fill()
            turtle.fillcolor("black")
            turtle.circle(10)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(25, 40)
            turtle.pendown()
            turtle.begin_fill()
            turtle.fillcolor("black")
            turtle.circle(10)
            turtle.end_fill()
            turtle.penup()
    # to draw blue eyes
        else:
            turtle.penup()
            turtle.goto(-25, 40)
            turtle.pendown()
            turtle.begin_fill()
            turtle.fillcolor("blue")
            turtle.circle(10)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(25, 40)
            turtle.pendown()
            turtle.begin_fill()
            turtle.fillcolor("blue")
            turtle.circle(10)
            turtle.end_fill()
            turtle.penup()
    
    # Draws smile if smiling and frown if not
    def __drawMouth(self):
    # if need to draw smile
        if self.isSmile():    
            turtle.penup()
            turtle.goto(-55, -25)
            turtle.pendown()
            turtle.width(10)
            turtle.setheading(-45)
            turtle.circle(80, 90)
            turtle.penup()
            turtle.width(0)
    # to draw frown
        else:
            turtle.penup()
            turtle.goto(55, -50)
            turtle.pendown()
            turtle.width(10)
            turtle.setheading(135)
            turtle.circle(80, 90)
            turtle.penup()
            turtle.width(0)


def main():
    # Draws initial face
    face = Face()
    face.draw_face()

    done = False

    # User interface menu prompting for change selection
    while not done:
        print("Change My Face")
    # Swaps from frown to smile if face is frowning
        mouth = "frown" or "smile"
    # Swaps from angry to happy if face is angry
        emotion = "angry" or "happy"
    # Swaps from blue to black if eyes are blue
        eyes = "blue" or "black"
    # Asks user for input
        print("1) Make me", mouth)
        print("2) Make me", emotion)
        print("3) Make my eyes", eyes)
        print("0) Quit")

        menu = eval(input("Enter a selection: "))

    # Operates specified change
        # Smile to frown and back
        if menu == 1:
            face.changeMouth()
        # Emotion from angry to happy and back
        elif menu == 2:
            face.changeEmotion()
        # Eyes from blue to black and back
        elif menu == 3:
            face.changeEyes()
        else:
            break

    print("Thanks for Playing")

    # Turtle hiden and done
    turtle.hideturtle()
    turtle.done()


main()

