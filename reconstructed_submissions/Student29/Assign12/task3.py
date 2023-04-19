# @@@@@@@@@@@@@@
# CS1400 - MW1
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
        playerHand.append(deck.draw()) # Single line

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
            selectionSort(playerHand)

        elif choice == 3:
            bubbleSort(playerHand)

        elif choice == 4:
            binarySearch(playerHand)
        elif choice == 5:
            done = True
            print("Thanks for playing!")
            
def thinking():
    for i in range(5):
        print(".", end="")
        sleep(0.5)
    print()

def displayHand(hand):
    for card in hand:
        print(card)

def selectionSort(hand):
    print("Selection Sort by Title", end="")
    thinking()
    
    for i in range(len(hand) - 1):
        currMinIndex = i

        for j in range(i + 1, len(hand)):
            if TITLE.index(hand[currMinIndex].getTitle()) > TITLE.index(hand[j].getTitle()):
                currMinIndex = j

        if currMinIndex != i:
            hand[i], hand[currMinIndex] = hand[currMinIndex], hand[i]
    
def bubbleSort(hand):
    
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
        
def binarySearch(hand):
    
    bubbleSort(hand)
    
    for i in range(len(TITLE)):
        print(i+1, TITLE[i])
        
    titleChosen = int(input("Choose a Title:", ))
    
    titleUsed = TITLE[titleChosen - 1]
    
    for i in range(len(GANG)):
        print(i+1, GANG[i])
        
    gangChosen = int(input("Choose a Gang:", ))
    
    gangUsed = GANG[gangChosen - 1]
    
    key = convertCardToId(titleUsed, gangUsed)
    
    low = 0
    high = len(hand) - 1
    while high >= low:
        mid = (high + low) // 2
        if key == hand[mid].getID():
            print("Binary Search for " + titleUsed + " of " + gangUsed, end="")
            thinking()
            print("Congrats! You have that card!")
            return mid

        elif key < hand[mid].getID():
            high = mid - 1
        else:
            low = mid + 1
    print("Binary Search for " + titleUsed + " of " + gangUsed, end="")
    thinking()
    print("Sorry, you do not have that card")
    return -1
    
    
        
        
    
    
    


main()
