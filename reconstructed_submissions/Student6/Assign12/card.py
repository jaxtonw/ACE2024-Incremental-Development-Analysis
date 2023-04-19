# @@@@@@@@@@@@@
# CS1400 - 001
# Assignment 12

from gronkyutil import TITLE, GANG

class Card:
    def __init__(self, id):
        self.__id = id

    def getTitle(self):
        return TITLE[self.__value % 13] # Do not use a numeric literal

    def getGang(self):
        return GANG[self.__value // 13] # Do not use a numeric literal

    def getID(self):
        return self.__id

    # Add two dunder methods below to meet assignment requirements

    def __str__(self):
        return self.getTitle() + " of " + self.getGang()

    def __repr__(self):
        return self.__str__()
