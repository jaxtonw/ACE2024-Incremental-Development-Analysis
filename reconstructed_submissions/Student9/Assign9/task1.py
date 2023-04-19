# @@@@@@@@@@@@@@@
# CS1400 - 14 Week
# Assignment 9

import turtle
class Face:
    def __init__(self):
        self.__smile = True
        self.__happy = True
        self.__darkEyes = True
        
    def get_smile(self):
        return self.__smile

    def get_happy(self):
        return self.__happy
        
    def get_eyes(self):
        return self.__darkEyes

    def draw_face(self):
        turtle.clear()
        self.__drawHead()
        self.__drawEyes()
        self.__drawMouth()
        
    def isSmile(self):
        self.__smile = True
        
    def isHappy(self):
        self.__happy = True
        
    def isDarkEyes(self):
        self.__darkEyes = True
        
    def changeMouth(self):
        self.__smile = False
        self.draw_face()
        
    def changeEmotion(self):
        self.__happy = False
        self.draw_face()
        
    def changeEyes(self):
        self.__darkEyes = False
        self.draw_face()         
    def __drawHead(self):
        self.__happy

            
    def __drawEyes(self):
        self.__darkEyes

    
    def __drawMouth(self):
        self.__smile

            
        
= Face()
    face.draw_Face()raw_face()draw_face()
    smile = face.get_smile
    happy = face.get_happy
    dark = face.get_eyes
        smile = face.get_smile()
    happy = face.get_happy()
    eyes = face.get_eyessmileneif smile == False else =frowne
    while not done:happy  if<happy == False else Fangryn>Change My Face")black  ifsdark == False else mblue= True else n" if Face.__smile == True angr "sifmhappy == True else ihapp        emotion = "angry"if_eyes == True else _ha= T<Fill-In>
    fa<Fill-In>ll-In>rue els  s == True else "black"
      print("0<Fill-In            if smile:
                smile = False
            elif not smile:
                smile = True

            if happy:
                turtle.begin_fill()
                turtle.fillcolor("yellow")
                turtle.goto(0, 0)
                turtle.pendown()
                turtle.circle(100)
                turtle.penup()
                turtle.end_fill()
            elif not happy:
                turtle.begin_fill()
                turtle.fillcolor("red")
                turtle.goto(0, 0)
                turtle.pendown()
                turtle.circle(100)
                turtle.penup()
                turtle.end_fill()
                
            if dark:
                turtle.goto(-25, 125)
                turtle.pendown()
                turtle.begin_fill()
                turtle.fillcolor("black")
                turtle.circle(10)
                turtle.end_fill()
                turtle.penup()
                turtle.goto(25, 125)
                turtle.pendown()
                turtle.begin_fill()
                turtle.fillcolor("black")
                turtle.circle(10)
                turtle.end_fill()
                turtle.penup()
            elif not dark:
                turtle.goto(-25, 125)
                turtle.pendown()
                turtle.begin_fill()
                turtle.fillcolor("blue")
                turtle.circle(10)
                turtle.end_fill()
                turtle.penup()
                turtle.goto(25, 125)
                turtle.pendown()
                turtle.begin_fill()
                turtle.fillcolor("blue")
                turtle.circle(10)
                turtle.end_fill()
                turtle.penup()

            if smile:
                turtle.penup()
                turtle.goto(-65, 50)
                turtle.right(45)
                turtle.pendown()
                turtle.pensize(10)
                turtle.circle(90, 100)
                turtle.right(55)
                turtle.penup()
                turtle.pensize(1)
            elif not smile:
                turtle.goto(70, 50)
                turtle.left(130)
                turtle.pendown()
                turtle.pensize(10)
                turtle.circle(90, 100)
                turtle.left(130)
                turtle.penup()
                turtle.pensize(1)
            
                
            
Fill-In 
        elif me            if happy:
                happy = False
            elif not happy:
                happy = True

            if happy:
                turtle.begin_fill()
                turtle.fillcolor("yellow")
                turtle.goto(0, 0)
                turtle.pendown()
                turtle.circle(100)
                turtle.penup()
                turtle.end_fill()
            elif not happy:
                turtle.begin_fill()
                turtle.fillcolor("red")
                turtle.goto(0, 0)
                turtle.pendown()
                turtle.circle(100)
                turtle.penup()
                turtle.end_fill()

            if dark:
                turtle.goto(-25, 125)
                turtle.pendown()
                turtle.begin_fill()
                turtle.fillcolor("black")
                turtle.circle(10)
                turtle.end_fill()
                turtle.penup()
                turtle.goto(25, 125)
                turtle.pendown()
                turtle.begin_fill()
                turtle.fillcolor("black")
                turtle.circle(10)
                turtle.end_fill()
                turtle.penup()
            elif not dark:
                turtle.goto(-25, 125)
                turtle.pendown()
                turtle.begin_fill()
                turtle.fillcolor("blue")
                turtle.circle(10)
                turtle.end_fill()
                turtle.penup()
                turtle.goto(25, 125)
                turtle.pendown()
                turtle.begin_fill()
                turtle.fillcolor("blue")
                turtle.circle(10)
                turtle.end_fill()
                turtle.penup()

            if smile:
                turtle.penup()
                turtle.goto(-65, 50)
                turtle.right(45)
                turtle.pendown()
                turtle.pensize(10)
                turtle.circle(90, 100)
                turtle.right(55)
                turtle.penup()
                turtle.pensize(1)
            elif not smile:
                turtle.goto(70, 50)
                turtle.left(130)
                turtle.pendown()
                turtle.pensize(10)
                turtle.circle(90, 100)
                turtle.left(130)
                turtle.penup()
                turtle.pensize(1)
Fill-In>
        elif me            if dark:
                dark = False
            elif not dark:
                dark = True
                
            if happy:
                turtle.begin_fill()
                turtle.fillcolor("yellow")
                turtle.goto(0, 0)
                turtle.pendown()
                turtle.circle(100)
                turtle.penup()
                turtle.end_fill()
            elif not happy:
                turtle.begin_fill()
                turtle.fillcolor("red")
                turtle.goto(0, 0)
                turtle.pendown()
                turtle.circle(100)
                turtle.penup()
                turtle.end_fill()

            if dark:
                turtle.goto(-25, 125)
                turtle.pendown()
                turtle.begin_fill()
                turtle.fillcolor("black")
                turtle.circle(10)
                turtle.end_fill()
                turtle.penup()
                turtle.goto(25, 125)
                turtle.pendown()
                turtle.begin_fill()
                turtle.fillcolor("black")
                turtle.circle(10)
                turtle.end_fill()
                turtle.penup()
            elif not dark:
                turtle.goto(-25, 125)
                turtle.pendown()
                turtle.begin_fill()
                turtle.fillcolor("blue")
                turtle.circle(10)
                turtle.end_fill()
                turtle.penup()
                turtle.goto(25, 125)
                turtle.pendown()
                turtle.begin_fill()
                turtle.fillcolor("blue")
                turtle.circle(10)
                turtle.end_fill()
                turtle.penup()

            if smile:
                turtle.penup()
                turtle.goto(-65, 50)
                turtle.right(45)
                turtle.pendown()
                turtle.pensize(10)
                turtle.circle(90, 100)
                turtle.right(55)
                turtle.penup()
                turtle.pensize(1)
            elif not smile:
                turtle.goto(70, 50)
                turtle.left(130)
                turtle.pendown()
                turtle.pensize(10)
                turtle.circle(90, 100)
                turtle.left(130)
                turtle.penup()
                turtle.pensize(1)
            
Fill-In>:
        

            if happy ==  face.isHappy()
            else:
         tion()

            if eyes == True:
<Fill-In>                face.isDarkEyes()
            else:
                face.changeEyes()
               
            if smile == True:
                face.isSmile()
            else:
                face.changeMouth()

  
