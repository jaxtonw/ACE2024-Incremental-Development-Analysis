# @@@@@@@@@@@@@@
# CS1400 - MW2
# Assignment 10
from math import floor
from math import ceil

class Wordinator:
    def __init__(self, word):
        self.__word = word
        
    def __add__(self, other):
        return self.__word + other.__word
    
    def __gt__(self, other):
        return str(min(self.__word, other.__word))
    
    def __mul__(self, other):
        return str(self.__word * other)
    
    def __truediv__(self, other):
        newString = ""
        for i in range(len(self.__word + other.__word) // 2):
            newString += self.__word[i]
            newString += other.__word[i]
        return newString.capitalize()
    
    def __mod__(self, other):
        midWord1 = self.__word[ceil(len(self.__word) / 4) : floor(3 * (len(self.__word) / 4))] 
        midWord2 = other.__word[round(len(other.__word) / 4) : round(3 * (len(other.__word) / 4))]
        return midWord1, midWord2
    
    def backWordSlice(self):
        backWord = self.__word[len(self.__word) :: -1]
        return backWord9
    
    def backWordManual(self):
        word = self.__word
        manualBackword = ""
        for i in range(len(word)):
            manualBackword += word[len(word) - 1 - i]
        return manualBackword
            
        
            
            
