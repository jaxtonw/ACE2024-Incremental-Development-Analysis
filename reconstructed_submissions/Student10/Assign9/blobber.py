# @@@@@@@@@@
# CS 1400 - 14 week
# Assignment 9

from math import pi
from time import time

class Blobber:
    def __init__(self, name, color, radius, height):
        self.__name = str(name.capitalize())
        self.__color = str(color.lower())
        self.__radius = radius
        self.__height = height
        self.startTime = time()
        self.__time = time()
        self.elapsedTime = self.__time - self.startTime
        self.newRadius = self.__radius - (self.elapsedTime * (.2))
        self.happiness = (pi * (self.newRadius ** 2) * self.__height) / (pi * (self.__radius ** 2) * self.__height)
        
    def getName(self):
        return self.__name
    
    def getColor(self):
        return self.__color
        
    def setName(self, name):
        self.__name = name.capitalize()
        
    def setColor(self, color):
        self.__color = color.lower()
        
    def setTime(self):
        self.__time = time()
        
    def displayName(self):
        print("You Blobber's name is " + self.__name + ".")
        
    def changeName(self):
        name = input("Enter Blobber's new name: ")
        self.setName(name)  
        self.displayName()
        
    def displayColor(self):
        print("Your Blobber's color is " + self.__color + ".")
        
    def changeColor(self):
        color = input("Enter Blobber's new color: ")
        self.setColor(color)
        self.displayColor()
        
    def feedBlobber(self):
        food = eval(input("Enter amount to you feed your Blobber: "))
        self.newRadius += food
        
    def blobberSpeak(self):
        msg = "My name is " + self.__name + ", and I am " + self.__color + ".\nMy current happiness is " + str(self.happiness) + "%."
        return msg
        
    def vitalsOK(self):
        if self.happiness >= 90 and self.happiness <= 110:
            return False
        else:
            return True

