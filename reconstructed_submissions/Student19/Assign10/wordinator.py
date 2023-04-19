# @@@@@@@@@@@@
# CS1400 - MW1 (14 week)
# Assignment 101

class Wordinator:
    def __init__(self, word):
        self.__word = word
    def __add__(self, other):
        return wordinator(self.__word + other.__word)
        
        """
        self.__Alpha1 = self.__word[0]
        self.__Alpha2 = self.__word[1]
        
    def firstWord(self):
        __Alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        for i in range(len(__Alpha)):
            if self.__Alpha1[0] == __Alpha[i]:
                print("this is the fist word: " + self.__Alpha1)
            elif self.__Alpha2[0] == __Alpha[i]:
                print("this is the fist word: " + self.__Alpha2)
                
    def bigWord(self):
        print(self.__Alpha1[0] + self.__Alpha1[1:].lower() + self.__Alpha2.lower())
        
    def wordsFactor(self):
        __factor = int(input("enter a integer as a factor: "))
        __word1 = __factor * self.__Alpha1
        __word2 = __factor * self.__Alpha2
        print("word1" + __word1)
        print("word1" + __word2)
        
    def mixWords(self):
        if len(self.__Alpha1) > len(self.Alpha2):
            __lesser = len(self.Alpha2)
        else:
            __lesser = len(self.Alpha1)
        __mix = ""
        for i in range(__lesser*2+1):
            if i < __lesser*2 and i % 2 == 0:
                __mix += self.__Alpha1[i]
            elif i < __lesser*2 and i % 2 == 1:
                __mix += self.__Alpha2[i]
            else:
                if len(self.__Alpha1) > len(self.Alpha2):
                    __mix += self.__Alpha1[i:]
                else:
                    __mix += self.__Alpha2[i:]
                    
    def middleWords(self):
        for i in self.__word:
            __length = len(i)//2            
            __start = (__length//2)-1 
            __stop = ((__length//2)-1) + __length[i]
            print(i[__start:__stop])
            
    def backWordsSlice(self):
        for i in self.__word:
            print(i[len(i):0:-1])
            
    def backWordsManual(self):
            """
            
wordinator = wordinator()
wordinator
        0

