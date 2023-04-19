# @@@@@@@@@@@@@@@@
# CECS1400 - MW1
# Assignment 12-task 3

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
            sortByTitle(playerHand) # Single line
        elif choice == 3:
            sortByGang(playerHand) # Single line
        elif choice == 4:
            searchForCard(playerHand) # Single line
        elif choice == 5:
            done = True # Not a function and not 'break'
            print("Thank you for playing Gronky Cards")


def thinking():
    for i in range(5):
        print(".", end="")
        sleep(0.5)
    print()

def displayHand(hand): # Not a single line. The entire function body
    for i in hand:     
        print(i) # something needs to change here - look at this with coach
    
    
# Add other functions you need below

def sortByGang(inputList):
    
    print("Performing a Selection Sort by gang", end="")
    thinking()
    
    for i in range(len(inputList) - 1):
        currentMinIndex = i
        
        for j in range(i + 1, len(inputList)):
            if inputList[currentMinIndex] > inputList[j]:
                currentMinIndex = j
                
        if currentMinIndex != i:
            inputList[i], inputList[currentMinIndex] = inputList[currentMinIndex], inputList[i]
    
    
def sortByTitle(inputList): # insertion sort option

    print("Performing an Insertion Sort by Title", end="")
    thinking()
    
    
    for i in range(1, len(inputList)):
        currElement = inputList[i]
        j = i - 1
        while j >= 0 and inputList[j].getCardValue() > currElement.getCardValue():
            inputList[j + 1] = inputList[j]
            j -= 1

        inputList[j + 1] = currElement
      
# def getCardValue(self):
#     return card.getID() % len(TITLE) + 1



def binarySearch(inputList, key):
    low = 0
    high = len(inputList) - 1
    while high >= low:
        mid = (high + low) // 2
        if key == convertCardToId(inputList[mid].getTitle(), inputList[mid].getGang()):
            return mid
        elif key < convertCardToId(inputList[mid].getTitle(), inputList[mid].getGang()):
            high = mid - 1
        else:
            low = mid + 1

    return -1

def searchForCard(inputList):
    
    print("Search for a Card")
    itemInTitleList = 0
    for i in TITLE:
        itemInTitleList += 1
        print("(" + str(itemInTitleList) + ") " + i)
    
    titleToFind = int(input("Choose a Title: "))
    
    itemInGangList = 0
    for i in GANG:
        itemInGangList += 1
        print("(" + str(itemInGangList) + ") " + i)
        
    gangToFind = int(input("Choose a Gang: "))

    titleIndex = TITLE[titleToFind - 1]
    gangIndex = GANG[gangToFind - 1]
    
    print("Performing a Bubble Sort by gang", end="")
    thinking()
    print("Performing a Binary Search for " + titleIndex + " of " + gangIndex, end="")
    thinking()
    
    # the Bubble Sort actually starts here
    didSwap = True

    while didSwap:
        didSwap = False
        sortCnt = 1

        for i in range(len(inputList) - sortCnt):
            if inputList[i] > inputList[i + 1]:
                inputList[i], inputList[i + 1] = inputList[i + 1], inputList[i]
                didSwap = True

        sortCnt += 1
        
    # the Binary Search actually starts here
    foundCard = binarySearch(inputList, convertCardToId(titleIndex, gangIndex))
    
    if foundCard == -1:
        print("\tBummer! You do not have that card.")
    else:
        print("\tGreat news! You have that card.")
    

    
main()

