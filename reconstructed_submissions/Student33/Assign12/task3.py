# @@@@@@@@@@@@
# CS1400 - 012
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
    done:
        val    if choice == 1:
            displayHand(playerHand)
        elif choice == 2:
            sortTitle(playerHand)
        elif choice == 3:
            sortGang(playerHand)
        elif choice == 4:
            cardSearch(playerHand)
        elif choice == 5:
            done = True

def thinking():
    for i in range(5):
        print(".", end="")
        sleep(0.5)
    print()

def displayHand(hand):
    for i in range(len(hand)):
        print(hand[i])

# Add other functions you need belowrrdef sortTitle(hand):M    print("Selection Sort by Title", end="")
    thinking()
    
    for i in range(len(hand) - 1):
        currMinIndex = i
        
        for j in range(i + 1, len(hand)):
            if (hand[currMinIndex].getID() % len(TITLE)) + 1 > (hand[j].getID() % len(TITLE)) + 1:
                currMinIndex = j
                
        if currMinIndex != i:
            hand[i], hand[currMinIndex] = hand[currMinIndex], hand[i]


def sortGang(hand):
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

def cardSearch(hand):
    print()
    print("Search for card")
    print("\t(1) One")
    print("\t(2) Two")
    print("\t(3) Three")
    print("\t(4) Four")
    print("\t(5) Five")
    print("\t(6) Six")
    print("\t(7) Seven")
    print("\t(8) Eight")
    print("\t(9) Nine")
    print("\t(10) Ten")
    print("\t(11) Baker")
    print("\t(12) Jester")
    print("\t(13) Page")
    print("\t(14) Scribe")
    print("\t(15) Squire")
    print("\t(16) Armorer")
    print("\t(17) Marshal")
    
    titleChoice = int(input("Choose a Title: "))
    
    if titleChoice == 1:
        titleChoice = "One"
    elif titleChoice == 2:
        titleChoice = "Two"
    elif titleChoice == 3:
        titleChoice = "Three"
    elif titleChoice == 4:
        titleChoice = "Four"
    elif titleChoice == 5:
        titleChoice = "Five"
    elif titleChoice == 6:
        titleChoice = "Six"
    elif titleChoice == 7:
        titleChoice = "Seven"
    elif titleChoice == 8:
        titleChoice = "Eight"
    elif titleChoice == 9:
        titleChoice = "Nine"
    elif titleChoice == 10:
        titleChoice = "Ten"
    elif titleChoice == 11:
        titleChoice = "Baker"
    elif titleChoice == 12:
        titleChoice = "Jester"
    elif titleChoice == 13:
        titleChoice = "Page"
    elif titleChoice == 14:
        titleChoice = "Scribe"
    elif titleChoice == 15:
        titleChoice = "Squire"
    elif titleChoice == 16:
        titleChoice = "Armorer"
    elif titleChoice == 17:
        titleChoice = "Marshal"
    
    print("\t(1) Jets")
    print("\t(2) Pollos")
    print("\t(3) Slugs")
    print("\t(4) Yokels")
    print("\t(5) Keiths")
    print("\t(6) Elbows")

    gangChoice = int(input("Choose a Gang: "))

    if gangChoice == 1:
        gangChoice = "Jets"
    elif gangChoice == 2:
        gangChoice = "Pollos"
    elif gangChoice == 3:
        gangChoice = "Slugs"
    elif gangChoice == 4:
        gangChoice = "Yokels"
    elif gangChoice == 5:
        gangChoice = "Keiths"
    elif gangChoice == 6:
        gangChoice = "Elbows"
         
    sortGang(hand)
    
    key = convertCardToId(titleChoice, gangChoice)
    
    cardName = titleChoice + " of " + gangChoice
    
    result = binarySearch(hand, key, cardName)
    
    if result != -1:
        print("\tCongrats! You have that card")
    else:
        print("\tSorry. You do not have that card")
    
def binarySearch(hand, key, cardName):
    print("Binary Search for", cardName,  end="")
    thinking()

    low = 0
    high = len(hand) - 1
    while high >= low:
        mid = (high + low) // 2
        if key == hand[mid].getID():
            return mid
        elif key < hand[mid].getID():
            high = mid - 1
        else:
            low = mid + 1

    return -1

inIndeain()
