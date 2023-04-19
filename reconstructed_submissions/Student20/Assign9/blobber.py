#@@@@@@@@@@@@@
#Cs 1400
#Assignment 9

import time
class Blobber:

    def displayName(self):
        return self.__name
    
    def changeName(self, name):
        self.__name = name.capitalize()
        return self.__name

    def displayColor(self):
        return self.__color

    def changeColor(self, color):

        self.__color = color.lower()
        return self.__color
    
    def __init__(self, radius, height, color, name):
        self.__radius = radius
        self.__actualRadius= radius
        self.__height = height
        self.__color = color.lower()
        self.__name = name.capitalize()
        self.__baseTime = time()
    
    def vitalsOK(self):
        originalVolume = pi *(self.__radius ** 2) * self.__height
        currentVolume = pi* (self.__actualRadius ** 2) * self.__height
        self.__actualRadius -= (time() - self.__baseTime) * .002 * self.__radius
        self.__happiness = currentVolume / originalVolume
        if .90 <= self.__happiness <= 1.1:
            return self.__happiness, True

        else:
            return self.__happiness, False

    def feedBlobber(self, food):
        self.vitalsOK():
        self.__currentRadius += food

    def blobberSpeak(self):
        self.vitalsOK()

        return "My name is " + self.__name + ", and I am " + self.__color + ".\nMy current happiness level is " + format(
            self.__happiness, ".2%")


