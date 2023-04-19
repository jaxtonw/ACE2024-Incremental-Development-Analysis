# @@@@@@@@@@@@@
# CS1400 - MW1
# Assignment 13

class MemoryCard:
    def __init__(self, id):
        self.__id = id
        self.__value = (id // 2) + 33
        self.__flipped = False
        
    def getValue(self):
        return self.__value
    
    def toggleFlipped(self):
        self.__flipped = not self.__flipped
        
    def isFlipped(self):
        return self.__flipped
    
    def displayCard(self):
        return chr(self.__value)
        
        
        



