# @@@@@@@@@@
# CS 1400 - 14 week
# Assignment 10

class Wordinator:
    def __init__(self, word):
        self.__word = word
        
    def getWord(self):
        return self.__word
    
    # first word alphabetically
    def __lt__(self, other):
        letter1 = self.__word[0]
        letter2 = other.getWord()[0]
        if min(letter1, letter2) == letter1:
            return self.__word
        else:
            return other.getWord()
        
    # get big word
    def __add__(self, other):
        return self.__word + other.getWord()
    
    # get word factor (repeated num times)
    def __mul__(self, other):
        return self.__word.upper() * other
    
    # mix words
    def __truediv__(self, other):
        if len(self.__word) > len(other.getWord()):
            long = self.__word
            short = other.getWord()
        else:
            long = other.getWord()
            short = self.__word
        mixWord = ""
        for i in long:
            mixWord += i + " "
        for j in short:
            mixWord = mixWord.replace(" ", j, 1)
        mixWord = mixWord.replace(" ", "")
        return mixWord.capitalize()
    
    # mid words 
    def __mod__(self, other):           
        # even length words - word1    
        if len(self.__word) % 2 == 0:
            half = len(self.__word) / 2
            if half % 2 == 0:
                inside = outside = half
            else:
                inside = (len(self.__word) / 2) - 1
                outside = (len(self.__word) / 2) + 1
            start = int(outside / 2)
            end = int(start + inside)
            midword1 = self.__word[start:end]
            
        # odd length words - word1
        elif len(self.__word) % 2 == 1:
            half = len(self.__word) // 2
            if half % 2 == 0:
                inside = (len(self.__word) / 2 ) + (1 / 2)
                outside = (len(self.__word) / 2) - (1 / 2)
            else:
                inside = (len(self.__word) / 2) - (1 / 2)
                outside = (len(self.__word) / 2) + (1 / 2)
            start = int(outside / 2)
            end = int(start + inside)
            midword1 = self.__word[start:end]

        # even length words - word2   
        if len(other.getWord()) % 2 == 0:
            half = len(other.getWord()) / 2
            if half % 2 == 0:
                inside = outside = half
            else:
                inside = (len(other.getWord()) / 2) - 1
                outside = (len(other.getWord()) / 2) + 1
            start = int(outside / 2)
            end = int(start + inside)
            midword2 = other.getWord()[start:end]

        # odd length words - word2
        elif len(other.getWord()) % 2 == 1:
            half = len(other.getWord()) // 2
            if half % 2 == 0:
                inside = (len(other.getWord()) / 2) + (1 / 2)
                outside = (len(other.getWord()) / 2) - (1 / 2)
            else:
                inside = (len(other.getWord()) / 2) - (1 / 2)
                outside = (len(other.getWord()) / 2) + (1 / 2)
            start = int(outside / 2)
            end = int(start + inside)
            midword2 = other.getWord()[start:end]
            
        return midword1, midword2
        
    
    # switch case
    def __sub__(self, other):
        return self.__word.swapcase(), other.getWord().swapcase()
    
    # print backwards
    def backWordSlice(self):
        return self.__word[len(self.__word): : -1]
    
    # print backwards manually (without slice operator)
    def backWordManual(self):
        backwards = ""
        for i in self.__word:
            backwards = str(i) + backwards
        return backwards
    
    def __str__(self):
        return str(self.__word)
