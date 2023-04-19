# @@@@@@@@@@@  
# CS 1400 - MW1 XL
# Assignment 009
from math import pi
from time import time


class Blobber:
    def __init__(self, name, color, radius, height):
        self.blobberOK = False
        self.__name = str.title(name)
        self.__color = color.lower()
        self.__radius = radius
        self.__height = height
        self.__radius2 = radius
        self.__start = time()
        self.__current = time()
        self.__blobberOK = True
        self.__happiness = 100
        self.__food = 0

    def vitalsOK(self):
        self.blobberHunger()
        volume = (self.__radius ** 2) * pi * self.__height
        volume2 = (self.__radius2 ** 2) * pi * self.__height
        change = volume2/volume
        vitals = change
        self.__happiness = change
        if self.__current == 0:
            self.blobberOK = True
        elif 0.9 <= change <= 1.1:
            self.blobberOK = True
        elif not 0.9 <= change <= 1.1:
            self.blobberOK = False
        return vitals, self.blobberOK

    def blobberHunger(self):
        self.__current = time() - self.__start
        radiusDeleter = self.__radius * 0.002
        if self.__current == 0:
            self.__radius2 = self.__radius
        elif self.__food == 0:
            self.__radius2 = self.__radius - (radiusDeleter * self.__current)
        else:
            self.__radius2 = (self.__radius + self.__food) - (radiusDeleter * self.__current)
    
    def showName(self):
        return self.__name

    def changeName(self, name):
        self.__name = str.title(name)
        
    def showColor(self):
        return self.__color
    
    def changeColor(self, color):
        self.__color = color.lower()
    
    def speak(self):
        msg = " My name is " + self.__name + " and I am " + str(self.__color) + "\n My happiness is " +\
              format(self.__happiness, ".2%")
        return msg
    
    def feedBlobber(self, food):
        self.__food += food
        
        
