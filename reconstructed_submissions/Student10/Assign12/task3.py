# @@@@@@@@@@
# CS 1400 - 14 week
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
            searchFor(playerHand)
        elif choice == 5:
            done = True

def thinking():
    for i in range(5):
        print(".", end="")
        sleep(0.5)
    print()

def displayHand(hand):
    print("Your Hand")
    for i in hand:
        print("\t" + str(i))

# Add other functions you need below
def sortByTitle(hand):
    print("Selection Sort by Title", end="")
    #thinking()
    
    for i in range(len(hand) - 1):
        currMinIndex = i
        for j in range(i + 1, len(hand)):
            if hand[currMinIndex].getTitle() > hand[j].getTitle():
                currMinIndex = j
        if currMinIndex != i:
            hand[i], hand[currMinIndex] = hand[currMinIndex], hand[i]

def sortByGang(hand):
    print("Bubble Sort by Gang", end="")
    thinking()
    
    didSwap = True
    while didSwap:
        didSwap = False
        sortCnt = 1
        
        for i in range(len(hand) - sortCnt):
            if hand[i] > hand[i + 1]:
                hand[i], hand[i + 1] = hand[i + 1], hand[i]
                didSwap = True
                
        sortCnt += 1

def searchFor(hand):
    print("Search for Card")
    #title menu
    for i in range(len(TITLE)):
        print("\t (" + str(i + 1) + ") " +  TITLE[i])
    title = eval(input("Choose a Title: "))
    
    #gang menu
    for i in range(len(GANG)):
        print("\t (" + str(i + 1) + ") " + GANG[i])
    gang = eval(input("Choose a Gang: "))
    
    #sort and search
    sortByGang(hand)
    print("Binary Search for " + TITLE[title - 1] + " of " + GANG[gang - 1], end="")
    thinking()
    key = convertCardToId(TITLE[title - 1], GANG[gang - 1])
    handIdList = []
    for i in hand:
        handIdList.append(convertCardToId(i.getTitle(), i.getGang()))
    low = 0
    high = len(hand) - 1
    while high >= low:
        mid = (high + low) // 2
        if key == handIdList[mid]:
            return print("Congrats! You have that card.")
        elif key <= handIdList[mid]:
            high = mid - 1
        else:
            low = mid + 1    
    return print("Sorry. You do not have that card.")    
    


main()
