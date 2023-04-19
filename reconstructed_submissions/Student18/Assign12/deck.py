from modules.gronkyutil import TITLE, GANG
from modules.card import Card
from random import shuffle


class Deck:
    def __init__(self):
        self.shuffle()

    def shuffle(self):
        self.__deck = []
        totalCards = len(GANG) * len(TITLE)

        for i in range(totalCards):
            self.__deck.append(Card(i))

        shuffle(self.__deck)

    def draw(self):
        return self.__deck.pop()



