# @@@@@@@@@@@@@
# CS1400 - 001
# Assignment 9

import math
import time

class Blobber:
    __radius = float()
    __height = float()
    __color = str()
    __name = str()
    startSize = 0
    
    def __init__(self, color, name, radius=30, height=60):
        self.__radius = radius
        self.__height = height
        self.__color = color 
        self.__name = name 
        self.startSize = (math.pi * radius * radius * height)
        
    def mutator(self, name="$", color="$"):
        if name != "$":
            self.__name = name
        if color != "$":
            self.__color = color
            
    def accessor(self):
        return (self.__name, self.__color)
    
    def feedBlobber(self, radius):
        self.__radius += radius 
        
    def blobberSpeak(self):
        happiness = 0
        num = abs(1-(math.pi * self.__radius * self.__radius * self.__height) / self.startSize) * 100
        if num > 10:
            happiness = 0 
        else: 
            happiness = 100 - (num * 10)
        
    def vitalsOK(self):
        num = abs(1 - (math.pi * self.__radius * self.__radius * self.__height) / self.startSize) * 100
        if num > 10:
            blobberOK = False
            vitals = 0
        else: 
            blobberOK = True 
            vitals = 100 - (num * 10)
    
    def Shinker(self):
        self.__radius = self.__radius * 0.98 
        
