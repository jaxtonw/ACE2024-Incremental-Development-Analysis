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
        self.__smile = not self.__smile
        self.draw_face()
    
    def changeEmotion(self):
        self.__happy = not self.__happy
        self.draw_face()
        
    def changeEyes(self):
        self.__darkEyes = not self.__darkEyes
        self.draw_face()

    def __drawMouth(self):
        turtle.setheading(0)
        if self.__smile:    
            turtle.goto(-45, 10)
            turtle.pensize(5)
            turtle.right(60)
            turtle.pendown()
            turtle.circle(50, 120)
            turtle.penup()
            turtle.pensize(1)
        else:
            turtle.goto(45, 10)
            turtle.pensize(5)
            turtle.left(120)
            turtle.pendown()
            turtle.circle(50, 120)
            turtle.penup()
            turtle.pensize(1)
        
    def __drawEyes(self):
        turtle.color("black")
        if not self.__darkEyes:
            turtle.color("blue")
        turtle.goto(-30, 60)
        turtle.begin_fill()
        turtle.pendown()
        turtle.circle(10)
        turtle.penup()
        turtle.goto(30, 60)
        turtle.pendown()
        turtle.circle(10)
        turtle.end_fill()
        turtle.penup()
        turtle.color("black")

    def __drawHead(self):
        turtle.setheading(0)
        turtle.penup()
        turtle.goto(0, -50)
        turtle.begin_fill()
        turtle.pendown()
        turtle.circle(100)
        turtle.color("yellow")
        if not self.__happy:
            turtle.color("red")
        turtle.end_fill()
        turtle.penup()


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

