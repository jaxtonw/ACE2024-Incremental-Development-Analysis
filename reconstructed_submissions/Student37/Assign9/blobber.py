# @@@@@@@@@
# CS1400 - MW1
# Assignment 9 - blobber

import time
from math import pi

class Blobber:
    
    def __init__(self, name, color, radius, height):
        self.__name = name.capitalize()
        self.__color = color.lower()
        self.__height = height
        self.__radius = radius
        self.__time1 = time.time()
        self.__originalVolume = pi * (self.__radius ** 2) * self.__height
        self.__currentVolume = self.__originalVolume


    def setColor(self, color):
        color = color.lower()
        self.__color = color


    def setName(self, name):
        name = name.capitalize()
        self.__name = name
        
       
    def getTime(self):
        timeNow = time.time()
        totalTime = timeNow - self.__time1
        return totalTime
    
    
    def getHappiness(self):
        happinessLevel = self.getCurrentVolume(self.getTime()) / self.__originalVolume
        return happinessLevel
        
        
    def getName(self):
        return self.__name
    
    
    def getCurrentVolume(self, time):
        self.__currentVolume = self.__currentVolume - (pi * ((self.__radius*(.002 * self.getTime())) ** 2) * self.__height)
        return self.__currentVolume #it looks kinda complicated, but it takes the current volume and subracts a 
                                    # certain volume based on how long it has been. 2% of the radius every second.
        
        
    def getColor(self):
        return self.__color
        
        
    def blobberSpeak(self):
        return self.getName(), self.getColor(), float(self.getHappiness())
        
        
    def feedBlobber(self, amount):
        addVolume = pi * (amount ** 2) * self.__height
        self.__currentVolume = self.getCurrentVolume(self.getTime()) + addVolume 
        #reassigns the currentVolume variable so it becomes the new "original" that way it actually adds 
        #next time you check
        
        
    def vitalsOK(self):
        happinessNow = self.getHappiness()
        if .90 <= happinessNow <= 1.10: #checks if its +/- 10%
            return float(happinessNow), True
        else:
            return float(happinessNow), False


