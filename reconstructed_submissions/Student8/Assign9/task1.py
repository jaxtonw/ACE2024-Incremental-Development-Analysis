# @@@@@@@@@@@@@
# CS 1400 - MW1
# Assignment 9

# import the turtle module
import turtle

# define the class Face
class Face:
    # create the object
    def __init__(self):
        self.__smile = True
        self.__happy = True
        self.__darkEyes = True

    def draw_face(self):
        turtle.clear()
        self.__drawHead()
        self.__drawEyes()
        self.__drawMouth()

    # draw the mouth
    def __drawMouth(self):
        turtle.pu()
        # change the circles heading and starting position to create either a frown or smile as appropriate
        if self.isSmile():
            turtle.setheading(285)
            turtle.goto(-48.30, -12.94)
        else:
            turtle.setheading(105)
            turtle.goto(48.30, -12.94)
        turtle.pd()
        turtle.pensize(10)
        turtle.circle(50, 150)
        turtle.pensize(1)  # reset line width

    # draw the head
    def __drawHead(self):
        turtle.pu()
        turtle.goto(0, -100)
        turtle.pd()
        # change head color to red if not happy, yellow if happy
        if self.isHappy():
            turtle.fillcolor("yellow")
        else:
            turtle.fillcolor("red")
        turtle.setheading(0)  # position circle correctly
        turtle.begin_fill()
        turtle.circle(100)
        turtle.end_fill()

    # draw the eyes
    def __drawEyes(self):
        turtle.setheading(0)  # position the eyes correctly
        # change the fill color based on whether the eyes are dark or not
        if self.isDarkEyes():
            turtle.fillcolor("black")
        else:
            turtle.fillcolor("blue")
        # draw left eye
        turtle.pu()
        turtle.goto(-50, 25)
        turtle.pd()
        turtle.begin_fill()
        turtle.circle(25)

        # draw right eye
        turtle.end_fill()
        turtle.pu()
        turtle.goto(50, 25)
        turtle.pd()
        turtle.begin_fill()
        turtle.circle(25)
        turtle.end_fill()

# boolean set methods that show whether certain colors or shapes should be used
    def isSmile(self):
        return self.__smile

    def isHappy(self):
        return self.__happy

    def isDarkEyes(self):
        return self.__darkEyes

# changes the values of the above set methods when called
    def changeMouth(self):
        self.__smile = False if self.isSmile() else True
        self.draw_face()

    def changeEmotion(self):
        self.__happy = False if self.isHappy() else True
        self.draw_face()

    def changeEyes(self):
        self.__darkEyes = False if self.isDarkEyes() else True
        self.draw_face()


# define the main() function
def main():
    face = Face()
    face.draw_face()

    done = False

    # loops until something other than 1, 2, or 3 is inputted
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

        # changes the shape or color of various aspects of the face based on user input
        if menu == 1:
            face.changeMouth()
        elif menu == 2:
            face.changeEmotion()
        elif menu == 3:
            face.changeEyes()
        else:
            break  # ends the loop

    print("Thanks for Playing")

    turtle.hideturtle()
    turtle.done()  # keeps the drawing onscreen

# calls the main() function
main()

