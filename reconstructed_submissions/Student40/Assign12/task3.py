# @@@@@@@@@@
# CS 1400 - 14 Week
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
            titleSort(playerHand)
        elif choice == 3:
            gangSort(playerHand)
        elif choice == 4:
            search(playerHand)
        elif choice == 5:
            done = True

def thinking():
    for i in range(5):
        print(".", end="")
        sleep(0.5)
    print()

def displayHand(hand):
    thinking()
    print("YOUR HAND:")
    msg = ""
    for i in range(len(hand)):
        msg += str(hand[i])
        msg += "\n"
    print(msg)
        

# Add other functions you need below
def titleSort(hand):
    print("Selection Sort by Title", end="")
    thinking()
    for i in range(len(hand) - 1):
        currMinIndex = i
        for j in range(i + 1, len(hand)):
            if hand[j].getID() % len(TITLE) < hand[currMinIndex].getID() % len(TITLE):
                currMinIndex = j
        if currMinIndex != i:
            hand[i], hand[currMinIndex] = hand[currMinIndex], hand[i]
   

def gangSort(hand):
    print("Bubble Sort by Gang", end="")
    thinking()
    didSwap = True
    while didSwap:
        didSwap = False
        sortCount = 1
        
        for i in range(len(hand) - sortCount):
            if hand[i] > hand[i + 1]:
                hand[i], hand[i + 1] = hand[i + 1], hand[i]
                didSwap = True
        sortCount += 1
        
def search(hand):
    
    # user picks gang 
    gangChoice = ""
    for i in range(len(GANG)):
        gangChoice += str(i + 1)
        gangChoice += "-"
        gangChoice += GANG[i]
        gangChoice += "\n"
    print(gangChoice)
    gang = eval(input("Choose a Gang: "))
    
    # user picks title
    titleChoice = ""
    for i in range(len(TITLE)):
        titleChoice += str(i + 1)
        titleChoice += "-"
        titleChoice += TITLE[i]
        titleChoice += "\n"
    print(titleChoice)
    title = eval(input("Choose a title: "))
    
    # convert gang and title to id (key)
    key = convertCardToId(TITLE[title-1], GANG[gang-1])
    result = searching(hand, key)
    if result == -1:
        print("You do not have this card.")
    else:
        print("You have this card!")
    
def searching(hand, key):
    print("Binary Search in Progress", end="")
    thinking()
    low = 0
    high = len(hand) - 1
    while high > low:
        mid = (high + low) // 2
        if key == hand[mid].getID():
            return mid
        elif key < hand[mid].getID():
            high = mid - 1
        elif key > hand[mid].getID():
            low = mid + 1
    return -1

main()



