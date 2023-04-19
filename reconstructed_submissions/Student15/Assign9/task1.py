# @@@@@@@@@@@@@@
# CS 1400 - 14 week
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
        turtle.setup(500, 500)
        turtle.width(1)
        turtle.setheading(0)
        turtle.penup()
        turtle.goto(0, -100)
        turtle.color("black")
        turtle.begin_fill()
        turtle.pendown()
        if self.__happy:
            turtle.fillcolor("yellow")
        else:
            turtle.fillcolor("red")
        turtle.circle(100)
        turtle.end_fill()
        turtle.penup()
        
    def __drawEyes(self):
        for i in range(2):
            turtle.goto(-30 - (-30 * 2 * i), 40)
            turtle.pendown()
            turtle.begin_fill()
            if self.__darkEyes:
                turtle.fillcolor("black")
            else:
                turtle.fillcolor("blue")
            turtle.circle(5)
            turtle.end_fill()
            turtle.penup()
        
    def __drawMouth(self):
        turtle.goto(0, 0)
        if self.__smile:
            turtle.setheading(225)
            turtle.forward(70)
            turtle.setheading(315)
            turtle.pendown()
            turtle.width(3)
            turtle.circle(70, 90)        
            turtle.penup()
        else:
            turtle.setheading(315)
            turtle.forward(70)
            turtle.setheading(135)
            turtle.pendown()
            turtle.width(5)
            turtle.circle(70, 90)        
            turtle.penup()
        
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
        self.__darkEyes = False if self.__darkEyes == True else True
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
