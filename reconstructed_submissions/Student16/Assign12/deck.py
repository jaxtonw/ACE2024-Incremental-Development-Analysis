# @@@@@@@@@@@@@@
# CS1400 - MW2
# Assignment 12
from gronkyutil import TITLE
from gronkyutil import GANG
from card import Card
from random import shuffle

# Create a class for a deck of Gronky cards
class Deck:
    # Initialize the class
    def __init__(self):
        self.shuffle()
        
    def shuffle(self):
        # Create an empty list and append the number of cards in a gronky deck (17 * 6)
        self.__deck = []
        
        
        for i in range(len(TITLE) * len(GANG)):
            self.__deck.append(Card(i))
            
        # Shuffle the deck using the random function: shuffle
        shuffle(self.__deck)
        
    def draw(self):
        return self.__deck.pop()
