# @@@@@@@@@@@@@
# CS1400 - MW1 XL
# Assignment 9

class Blobber:
    def __init__(self):
        self.__name = ""
        self.__color = ""
        self.__radius = 0
        self.__height = 0
        
    def getName(self):
        return self.__name
    
    def getColor(self):
        return self.__color
    
    def getRadius(self):
        return self.__radius
    
    def getHeight(self):
        return self.__height
    
    def setName(self, name):
        self.__name = name
        
    def setColor(self, color):
        self.__color = color
        
    def setRadius(self, radius):
        self.__radius = radius
        
    def setHeight(self, height):
        self.__height = height
        
    def feedBlobber(self):
        print("???")
        
    def blobberSpeak(self):
        print("mmm")
        
    def vitalsOK(self):
        print("ye")

