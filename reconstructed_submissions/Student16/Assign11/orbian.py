# @@@@@@@@@@@@@@
# CS1400 - MW2
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
            self.growUp()
            
    ####### ADD OTHER REQUIRED METHODS BELOW. SEE THE ASSIGNMENT DESCRIPTION AND 
# OTHER STARTER CODE FOR INSIGHT ######

    def getName(self):
        if not self.__adult:
            self.__ageCheck()
        return self.__NAME
    
    def getVolume(self):
        if not self.__adult:
            self.__ageCheck()
        return round(self.__getBodyVolume() + self.__getHeadVolume())
    
    def getAge(self):
        Age = time.time() - self.__BIRTH_TIME
        self.age = Age // 5
        return round(self.age)
    
    def __getHeadRadius(self):
        return self.__HEAD_RADIUS
    
    def __getBodyRadius(self):
        return self.__BODY_RADIUS
    
    def __getBodyHeight(self):
        return self.__BODY_HEIGHT
    
    def __gt__(self, other):
        return (self.__getBodyVolume() + self.__getHeadVolume()) > (other.__getBodyVolume() + other.__getHeadVolume())
    
    def __eq__(self, other):
        return (self.__getBodyVolume() + self.__getHeadVolume()) == (other.__getBodyVolume() + other.__getHeadVolume())
    
    def __len__(self): 
        # total height is the cylinder height and the diameter of the sphere
        return self.__BODY_HEIGHT + self.__HEAD_RADIUS * 2
    
    def __add__(self, other):
        # concatenate the parents' names
        nameBase = self.__NAME + other.__NAME
        
        # iterate through the parents' names to turn each character to an item in a list
        nameList = []
        for i in nameBase:
            nameList += i
            
        # shuffle the list
        shuffle(nameList)
        
        # iterate through half of the shuffled list to get the baby's name
        babyName = ""
        for i in range(len(nameList) // 2):
            babyName += nameList[i]
        
        # Capitalize the baby's name
        babyName = babyName.capitalize()
        babyHeadRadius = round((self.__HEAD_RADIUS + other.__HEAD_RADIUS) * .25)
        babyBodyRadius = round((self.__BODY_RADIUS + other.__BODY_RADIUS) * .25)
        babyBodyHeight = round((self.__BODY_HEIGHT + other.__BODY_HEIGHT) * .125)
        return Orbian(babyName, babyHeadRadius, babyBodyRadius, babyBodyHeight)
    
    # Create a string representation for the Orbian
    def __repr__(self):
        return "I am Orbian " + self.__NAME
    
    def growUp(self):
            self.__HEAD_RADIUS += self.__HEAD_RADIUS
            self.__BODY_RADIUS += self.__BODY_RADIUS
            self.__BODY_HEIGHT += self.__BODY_HEIGHT * 3
            
            
