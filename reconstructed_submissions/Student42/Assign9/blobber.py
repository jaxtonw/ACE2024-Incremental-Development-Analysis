# @@@@@@@@@@@@@
# CS1400 - 14 week
# Assignment 9
from math import pi
from time import time
class Blobber:
    def __init__(self, name, color, radius, height):
        self.__radius = radius
        self.__height = height
        self.__color = color
        self.__name = name.capitalize()
        self.__blobberVitality = 1.00
        self.__blobberVolume = pi * self.__radius ** 2 * self.__height
        self.__originalRadius = self.__radius
        self.__time = time()
        
    def setColor(self, color):
        self.__color = color.lower()
        
    def getColor(self):
        return self.__color
    
    def setName(self, name):
        self.__name = name.capitalize()
        
    def getName(self):
        return self.__name
    
    def feedBlobber(self, food):
        self.__radius += food
        
    def blobberSpeak(self):
        return "My name is " + self.__name + ", and I'm " + self.__color + "." "\n" \
                        "My current happiness level is " + str(self.__blobberVitality * 100) + "%"
        
    def __blobberSetUp(self):
        blobberTime = time() - self.__time
        self.__time += blobberTime
        decreseRadius = blobberTime * (self.__originalRadius * .002)
        self.__radius -= decreseRadius
        newVolume = pi * self.__radius ** 2 * self.__height
        self.__blobberVitality = newVolume / self.__blobberVolume
        
    def vitalsOK(self):
        self.__blobberSetUp()
        vitals = self.__blobberVitality
        if 1.10 > self.__blobberVitality > .90:
            blobberOK = True
        else:
            blobberOK = False
        return vitals, blobberOK
