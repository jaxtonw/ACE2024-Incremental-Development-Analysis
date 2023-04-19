# @@@@@@@@@@@@@@
# CS1400 - MW2
# Assignment 12

from gronkyutil import TITLE
from gronkyutil import GANG

class Card:
    def __init__(self, id):
        self.__id = id
    
    # Creat a method for getting the title of the card
    def getTITLE(self):
        # mod divide using the length of the list of Titles
         return TITLE[self.__id % len(TITLE)]
         
    # This method returns the card's id
    def getCardId(self):
        return self.__id
         
    # create a method for getting the Gange of a card    
    def getGANG(self):
        # Integer divide the card Id by the length of the list of gangs
        return GANG[self.__id // len(TITLE)]
    
    # Use the repr dunder method so that you can print a card
    def __repr__(self):
        return self.getTITLE() + " of " + self.getGANG()
    
    def __lt__(self, other):
        return self.getCardId() < other.getCardId()
    
