# @@@@@@@@@@@@@@@
# CS1400 - 14 Week
# Assignment 9
from math import pi
import time

class Blobber:
    def __init__(self,name,color,radius,height):
        self.__radius = radius
        self.__height = height
        self.__color = color
        self.__name = name
        self.__line1 = ""
        self.__start = time.time()
        
    def get_name(self):
        return self.__name
    
    def set_name(self):
        self.__name = ""
        
    def get_color(self):
        return self.__color

    def set_color(self):
        self.__color = ""
        
    def feedBlobber(self,food):
        blob = Blobber()
        food = float(food)
        var = blob.__radius
        var2 = var + food
    def blobberSpeak(self,name,color):
        self.__line1 = "My name is "+ self.__name + " and I am "+ self.__color +" right now!"
        self.__line1 += "My happiness level is " + + "% right now!"
    
    def get_speak(self):
        return self.__line1
        
    def vitalsOK(self):
        rad=float(self.__radius)
        hei=self.__height
        area = (rad**2)*(pi)
        volume = area*hei
        happy = 0
        now = time.time()
        diff = now-self.__start
        sec = volume/500
        loss = diff*sec
        
        happy = volume-loss
        
        if happy >= 90 and happy <= 110:
            blobberOK = True
        else:
            blobberOK = False
        
    
        

