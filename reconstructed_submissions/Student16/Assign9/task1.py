# @@@@@@@@@@@@@@
# CS1400 - MW2
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
        # create return Statement for what state the Moody's mood is
        return self.__smile
    def isHappy(self):
        # Create return Statement for what state the Moody's mood is
        return self.__happy
    def isDarkEyes(self):
        # create return Statement for what state Moody's Eyes are
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

            
    def __drawHead(self):
        # This If else block will change the variable for the fill color of the face.
        if self.isHappy():
            faceColor = "yellow"
        else:
            faceColor = "red"
        
        # The state of Moody determines the face color
        turtle.fillcolor(faceColor)
            
        # Have turtle draw a circle centered on (0,0) with a face color determined by the Mr. Moody
        turtle.pu()
        turtle.goto(0, -100)
        turtle.setheading(0)
        turtle.pd()
        turtle.begin_fill()
        turtle.circle(100)
        turtle.end_fill()
        
    def __drawEyes(self):
        if self.isDarkEyes():
            eyeColor = "black"
        else:
            eyeColor = "Blue"
        
        # Change fill color for the Eyes based on the isDarkEyes method
        turtle.fillcolor(eyeColor)
        
        # Draw to small circles that fill in with  the eye color
        turtle.pu()
        turtle.goto(-30, 30)
        turtle.setheading(0)
        turtle.pd()
        turtle.begin_fill()
        turtle.circle(10)

        turtle.pu()
        turtle.goto(30, 30)
        turtle.setheading(0)
        turtle.pd()
        turtle.circle(10)
        turtle.end_fill()
            
    def __drawMouth(self):
        # Create an if else block that checks if Mr. Moody is smiling or not, and changes the angle of the mouth
        if self.isSmile():
            angle = 315

            turtle.pensize(3)

            turtle.pu()
            turtle.goto(-35, -45)
            turtle.setheading(angle)
            turtle.pd()
            turtle.circle(50, 90)
        else:
            angle = 135

            turtle.pensize(3)

            turtle.pu()
            turtle.goto(35, -45)
            turtle.setheading(angle)
            turtle.pd()
            turtle.circle(50, 90)
    
        # revert the turtle to its original size after drawing the mouth
        turtle.pensize(1)
        
def main():
    face = Face()
    face.draw_face()
    done = False
    while not done:
        print("Change My Face")
        mouth = "frown"  "smile"
        emotion = "angry"  "happy"
        eyes = "blue"  "black"
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
