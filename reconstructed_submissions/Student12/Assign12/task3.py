# @@@@@@@@@@@@
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
           sortTitle(playerHand)
        elif choice == 3:
            sortGang(playerHand)
        elif choice == 4:
           searchCard(playerHand)
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

# sort by gang - bubble
def sortGang(playerHand):
    print("Bubble Sorting")
    thinking()
    done = False
    while not done:
        done = True
        for i in range(len(playerHand) - 1):
            if playerHand[i].getID() > playerHand[i + 1].getID():
                playerHand[i], playerHand[i + 1] = playerHand[i + 1], playerHand[i]
                done = False

# sort by title - selection  
def sortTitle(playerHand):
    print("Selection Sorting")
    thinking()
    for i in range(len(playerHand) - 1):
        minIndex = i
        for j in range(i + 1, len(playerHand)):
            if playerHand[minIndex] > playerHand[j]:
                minIndex = j
        if minIndex != i:
            playerHand[i], playerHand[minIndex] = playerHand[minIndex], playerHand[i]

# search card - binary search
def searchCard(playerHand):
    sortGang(playerHand)
    for i in range(len(TITLE)):
        print("\t(" + str(i + 1) + ") ", end="")
        print(TITLE[i])
    user = eval(input("Choose an option: "))
    for i in range(len(GANG)):
        print("\t(" + str(i + 1) + ") ", end="")
        print(GANG[i])
    msg = eval(input("Choose an option: "))
    num = msg * len(TITLE) + user
    low = 0
    high = len(playerHand) - 1
    print("Binary Search for " + TITLE[user - 1] + " of " + GANG[msg - 1])
    thinking()
    while high >= low:
        mid = (high + low) // 2
        if num == playerHand[mid].getID():
            return print("Yay! The card is found")
        elif num < playerHand[mid].getID():
            high = mid - 1
        else:
            low = mid + 1
    print("Awww... The card was NOT found")
            
    
main()
