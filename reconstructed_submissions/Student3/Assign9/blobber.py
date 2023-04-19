# @@@@@@@@@@@
# CS1400 - MW1
# Assignment 9

import math
import time


class myBlobber:
    # constructor with private data
    def __init__(self, radius, height, color, name):
        self.__radius = radius
        self.__height = height
        self.__color = color.lower()
        self.__name = name.capitalize()
        
    def time(self):
        
        
    # name accessor    
    def getName(self):
        return self.__name
    
    # color accessor    
    def getColor(self):
        return self.__color
    
    # name mutator    
    def setName(self, name):
        self.__color = name
    
    # color mutator    
    def setColor(self, color):
        self.__color = color
    
    # feeding    
    def feedBlobber(self):
        
    
    # speaking
    def blobberSpeak(self):
        msg = "My name is " + myBlobber.getName() + ", and I am " myBlobber.getColor()
        msg += ".\nMy current happiness level is " + #??????
        return msg
        
    # vitals
    def vitalsOK(self):
        volume = math.pi * (self.__radius ** 2) * self.__height
        if volume == 
        

