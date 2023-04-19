# @@@@@@@@@@@@@
# CS1400 - 001
# Assignment 11

from math import pi
from random import shuffle # Hint hint
from random import randint
import time


class Orbian:
    # DO NOT MODIFY THE CONSTRUCTOR
    def __init__(self, name, headRadius, bodyRadius, bodyHeight):
        # NOTE: These are constants
        self.__HEAD_RADIUS = headRadius
        self.__BODY_RADIUS = bodyRadius
        self.__BODY_HEIGHT = bodyHeight
        self.__NAME = name
        self.__BIRTH_TIME = time.time()
        
        # This is the only variable
        self.__adult = False
        
    def __getHeadVolume(self):
        return 4 / 3 * pi * self.__getHeadRadius() ** 3
    
    def __getBodyVolume(self):
        return pi * self.__getBodyRadius() ** 2 * self.__getBodyHeight()
    
    def __ageCheck(self):
        # Become an adult at 2
        if self.getAge() >= 2:
            self.__adult = True
    ####### ADD OTHER REQUIRED METHODS BELOW. SEE THE ASSIGNMENT DESCRIPTION AND OTHER STARTER CODE FOR INSIGHT ######
    
    def __getBodyRadius(self):
        self.__ageCheck()
        
        if not self.__adult:
            return self.__BODY_RADIUS
        else:
            return self.__BODY_RADIUS * 2
        
    def __getBodyHeight(self):
        self.__ageCheck()
        
        if not self.__adult:
            return self.__BODY_HEIGHT
        else:
            return self.__BODY_HEIGHT * 4

    def __getHeadRadius(self):
        self.__ageCheck()
        
        if not self.__adult:
            return self.__HEAD_RADIUS
        else: 
            return self.__HEAD_RADIUS * 2
        
    def getAge(self):
        age = time.time() - self.__BIRTH_TIME
        return int(age // 5)
    
    def getVolume(self):
        return round(self.__getHeadVolume() + self.__getBodyVolume())
    
    def __str__(self):
        return self.__NAME

    def getName(self):
        return self.__NAME

    def __len__(self):
        return self.__getBodyHeight() + (self.__getHeadRadius() * 2)
    
    def __gt__(self, other):
        if self.getVolume() > other.getVolume():
            return True
        else: 
            return False 
        
    def __eq__(self, other):
        if self.getVolume() == other.getVolume():
            return True
        else: 
            return False 
        
    def __add__(self, other):
        mashName = self.__NAME + other.getName()
        
        nameLen = len(mashName) // 2
        
        babyName = ""
        
        for i in range(nameLen):
            num = randint(0, len(mashName) - 1)
            babyName += mashName[num]
            
        headRadius = round((self.__getHeadRadius() + other.__getHeadRadius()) * 0.25)
        bodyRadius = round((self.__getBodyRadius() + other.__getBodyRadius()) * 0.25)
        bodyHeight = round((len(self) + len(other)) * 0.125)
        
        return Orbian(babyName.capitalize(), headRadius, bodyRadius, bodyHeight)
    
   
        
