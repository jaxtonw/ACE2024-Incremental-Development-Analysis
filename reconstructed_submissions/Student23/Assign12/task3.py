# @@@@@@@@@@@@@@
# CS1400 - 001
# Assignment 12

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
        playerHand.append(deck.draw())

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
            sortByTitle(playerHand)
        elif choice == 3:
            sortByGang(playerHand)
        elif choice == 4:
            searchForCard()
        elif choice == 5:
            done = True

def thinking():
    for i in range(5):
        print(".", end="")
        sleep(0.5)
    print()

def displayHand(hand):
    for i in hand:
        print(i)

# Add other functions you need below
def bianarySearch(hand, key):
    low = 0
    high = len(hand) - 1
    while high >= low:
        middle = (high + low) // 2
        if key == hand[middle].getID():
            return middle
        elif key < hand[middle].getID():
            high = middle - 1
        else:
            low = middle + 1
    return -1
    

def bubbleSort(hand):
    didSwitch = True
    while didSwitch:
        didSwitch = False
        for i in range(len(hand) - 1):
            if hand[i].getID() % len(TITLE) > hand[i + 1].getID() % len(TITLE):
                hand[i], hand[i + 1] = hand[i + 1], hand[i]
                didSwitch = True
            
    
def insertionSort(hand):
    for i in range(1, len(hand)):
        currentCard = hand[i]
        j = i - 1
        while j >= 0 and hand[j] > currentCard:
            hand[j + 1] = hand[j]
            j -= 1
        hand[j + 1] = currentCard

def sortByTitle(hand):
    print("Bubble sort by Title", end="")
    thinking()
    bubbleSort(hand)

def sortByGang(hand):
    print("Insertion sort by Gang", end="")
    thinking()
    insertionSort(hand)


# THIS FUNCTION DOESN'T WORK. RAN OUT OF TIME. CRASHES AT LINE 110
def searchForCard():
    print("Search for Card") 
    for i in TITLE:
        print(i)
    titlePicked = int(input("Choose a Title: "))
    for i in GANG:
        print(i)
    gangPicked = int(input("Choose a Gang: "))
    
    print("Bubble Sort by Title", end="") 
    bubbleSort(TITLE[titlePicked].getTitle())
    thinking()
    # I could not get the card title and gang to print so I simplified so it wouldn't crash
    print(" for the card selected", end="")
    thinking()
    if bianarySearch(titlePicked, gangPicked):
        print("Congrats! You have that card")
    else:
        print("You do not have that card")
        

main()
