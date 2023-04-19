
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

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
    face = <Fill-In>
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


main()# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

