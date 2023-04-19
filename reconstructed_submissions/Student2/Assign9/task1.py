# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#Name
#@@@@@-@@@@@@@-Assn9
#CS 1400

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
        <Fill-In>
    def isHappy(self):
        <Fill-In>
    def isDarkEyes(self):
        <Fill-In>
    def changeMouth(self):
        <Fill-In>
        self.draw_face()
    def changeEmotion(self):
        <Fill-In>
        self.draw_face()
    def changeEyes(self):
        <Fill-In>
        self.draw_face()
def main():
    face = turtle.goto(0,0)
    face.<Fill-In>
    done = False
    while not done:
        print("Change My Face")
        mouth = "frown" <Fill-In> "smile"
        emotion = "angry" <Fill-In> "happy"
        eyes = "blue" <Fill-In> "black"
        print("1) Make me", mouth)
        print("2) Make me", emotion)
        print("3) Make my eyes", eyes)
        print("0) Quit")
        menu = eval(input("Enter a selection: "))
        if menu == 1:
            <Fill-In>
        elif menu == 2:
            <Fill-In>
        elif menu == 3:
            < Fill - In >
        else:
            break
    print("Thanks for Playing")
    turtle.hideturtle()
    turtle.done()


main()
