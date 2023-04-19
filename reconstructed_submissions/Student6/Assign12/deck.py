# @@@@@@@@@@@@@
# CS1400 - 001
# Assignment 12
import random

from gronkyutil import TITLE, GANG
from card import Card
from random import shuffle

class Deck:
    def __init__(self):
        self.shuffle()

    def shuffle(self):
        self.__deck = []
        totalCards = 0 # Do not use a numeric literal

        for i in range(totalCards):
            self.__deck.append(Card(i)) # Single line of code
        shuffle(self.__deck)

    def draw(self):
        return self.__deck.pop() # Single line of code

