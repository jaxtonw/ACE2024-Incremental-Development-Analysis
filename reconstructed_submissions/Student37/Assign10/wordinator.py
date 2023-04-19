# @@@@@@@@@
# CS1400 - MW1
# Assignment 10 - wordinator


class Wordinator:
    
    def __init__(self, word):
        self.__word = word
        
    def __add__(self, other):
        return self.__word.capitalize() + other.getWord().lower()
    
    def __mul__(self, other):
        return self.__word.upper() * other
    
    def __truediv__(self, other):
        if len(self.__word) > len(other.getWord()):
            longerWord = self.__word
            shorterWord = other.getWord()  #I'm sure there is a more concise way to do this but I dont know how haha
        else:
            longerWord = other.getWord()
            shorterWord = self.__word
            
        mixWord = ""
        
        for i in range(len(longerWord)):  #this does make it so the longer word gets added first, but it wasn't 
            if i < len(shorterWord):      #specified that the first word had to go first so i figured it was okay
                mixWord += longerWord[i]
                mixWord += shorterWord[i]
            else:
                mixWord += longerWord[i]
        return mixWord
    
    
    def __mod__(self, other):
        startSplit1 = len(self.__word) // 4 #the first quarter will be split off
        endSplit1 = len(self.__word) * 3 // 4  #the last quarter will be split off

        startSplit2 = len(other.getWord()) // 4
        endSplit2 = len(other.getWord()) * 3 // 4
        
        return self.__word[startSplit1:endSplit1], other.getWord()[startSplit2:endSplit2]
    
    
    def __sub__(self, other):
        word1 = ""
        word2 = ""
        
        for i in range(len(self.__word)):
            if self.__word[i].isupper():
                word1 += self.__word[i].lower()
            else:
                word1 += self.__word[i].upper()
        
        for i in range(len(other.getWord())):
            if other.getWord()[i].isupper():
                word2 += other.getWord()[i].lower()
            else:
                word2 += other.getWord()[i].upper()
        
        return word1, word2
    
    
    def __str__(self):
        return str(self.getWord())
    
    
    def __lt__(self, other):
        return self.__word[0] < other.getWord()[0]
    
    
    def getWord(self):
        return self.__word
    
    
    def backWordSlice(self):
        return self.__word[(len(self.__word) + 1)::-1]
    
    
    def backWordManual(self):
        word = ""
        for i in range(len(self.__word)):
                word += self.__word[len(self.__word) - 1 - i]
        return word
