# @@@@@@@@@@@@@@
# CS1400 - MW2
# Assignment 9
from math import pi
from time import time

class Blobber:
    def __init__(self, name, color, radius, height):
        self.__name = name
        self.__color = color
        self.__radius = radius
        self.__height = height

        self.__startTime = time()

        
        
    def getName(self):
        return self.__name.capitalize()
    def setName(self, name):
        self.__name = name
    
    def getColor(self):
        return self.__color.lower()
    def setColor(self, color):
        self.__color = color
    
    def speak(self):
        return "My name is " + self.getName() + ", and my color is " + self.getColor() + "\nMy current Happiness is " \
               + format(str((Blobber.getVitals(self)) * 100), "2") + "%"
    
    
    def vitalsOK(self):
        vitals = Blobber.getCurrentVolume(self) / (pi * self.__radius ** 2 * self.__height)
        blobberOK = .90 < vitals and vitals < 1.10
        return vitals, blobberOK
    
    def getVitals(self):
        return Blobber.getCurrentVolume / (pi * sel(self)f.__radius ** 2 * self.__height)
    
    
    def getElapsedTime(self):
        return time() - self.__startTime
    
    def getCurrentRadius(self):
        return (self.__radius) - (self.__radius * .002) * Blobber.getElapsedTime(self)
    
   # def setCurrentRadius(self):
    #     = 10
    
    def getCurrentVolume(self):
        return  pi * Blobber.getCurrentRadius(self) ** 2 * self.__height

