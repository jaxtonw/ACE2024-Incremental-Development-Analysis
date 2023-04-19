# @@@@@@@@@@@@@@
# CS1400 - 14 week
# Assignment 12 task 3

from modules.deck import Deck
from time import sleep
from modules.gronkyutil import convertCardToId
from modules.gronkyutil import TITLE, GANG

def main():
    print("Welcome to Gronky Cards\n")
    print("Shuffling Cards", end="")
    thinking()

    deck = Deck()
    playerHand = []

    cardCount = int(input("How many cards would you like?: "))

    for i in range(cardCount):
        playerHand.append(deck.draw())# Single line

    done = False
    while not done:
        print()
        print("Menu")
        print("\t(1) Display hand")
        print("\t(2) Sort by title")
        print("\t(3) Sort by gang")
        print("\t(4) Search for card")
        print("\t(5) Quit")
        choice = int(input("Choose an option: "))
        print()

        if choice == 1:
            displayHand(playerHand)
        elif choice == 2:
            titleSort(playerHand)# Single line
        elif choice == 3:
            gangSort()# Single line
        elif choice == 4:
            cardSearch(playerHand)# Single line
        elif choice == 5:
            done = True# Not a function and not 'break'

def thinking():
    for i in range(5):
        print(".", end="")
        sleep(0.5)
    print()

def displayHand(hand):
    # Not a single line. The entire function body
    for i in range(len(hand)):
        print(hand[i])

# Add other functions you need below

def titleSort(inputList):
    print("Insertion sort in progress", end="")
    thinking()
    for i in range(1, len(inputList)):
        currentElement = inputList[i]
        j = i - 1
        while j >= 0 and inputList[j] > currentElement:
            inputList[j + 1] = inputList[j]
            j-= 1
        inputList[j + 1] = currentElement
        
def gangSort(list):
    print("Selection sort in progress", end="")
    thinking()
    for i in range(len(list)-1):
        index = i
        for j in range(i + 1, len(list)):
            if TITLE.index(list[index].getTitle()) > TITLE.index(list[j].getTitle()):
                index = j
        if index !=i:
            list[i], list[index] = list[index], list[i]
            
def cardSearch():
    print("IDK")

main()

