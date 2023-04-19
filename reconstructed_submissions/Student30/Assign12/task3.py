# @@@@@@@@@@@@@@@@@@
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
            titleSort(playerHand) # Single line
        elif choice == 3:
            gangSort(playerHand) # Single line
        elif choice == 4:
            cardSearch(playerHand) # Single line
        elif choice == 5:
            print("Thanks for playing Gronky!") # Not a function and not 'break'
            done = True
            
def thinking():
    for i in range(5):
        print(".", end="")
        sleep(0.5)
    print()

def displayHand(hand):
     for i in hand: 
        print(i) # Not a single line. The entire function body

def titleSort(inputList):
    print("Bubble Sort by Title", end="")
    thinking()
    
    didSwap = True
    
    while didSwap:
        didSwap = False
        sortCnt = 1

        for i in range(len(inputList) - sortCnt):
            if inputList[i].getID() % len(TITLE) > inputList[i + 1].getID() % len(TITLE):
                inputList[i], inputList[i + 1] = inputList[i + 1], inputList[i]
                didSwap = True

        sortCnt += 1
    
def gangSort(inputList):
    print("Selection Sort by Gang", end="")
    thinking()
    
    for i in range(len(inputList) - 1):
        currMinIndex = i

        for j in range(i + 1, len(inputList)):
            if inputList[currMinIndex] > inputList[j]:
                currMinIndex = j

        if currMinIndex != i:
            inputList[i], inputList[currMinIndex] = inputList[currMinIndex], inputList[i]

def cardSearch(inputList):
    
    print("Search for Card")
    titleMenu()
    cardTitle = eval(input("Choose a Title: "))
    gangMenu()
    cardGang = eval(input("Choose a Gang: "))
    
    cardTitle = TITLE[cardTitle - 1]
    cardGang = GANG[cardGang - 1]
    gangSort(inputList)
    key = convertCardToId(cardTitle, cardGang)
    print("Binary Search for " + cardTitle + " of " + cardGang, end="")
    thinking()
    
    low = 0
    high = len(inputList) - 1
    while high >= low:
        mid = (high + low) // 2
        if key == inputList[mid].getID():
            print("\t" + "Congrats! This card is in your hand!")
            return
        elif key < inputList[mid].getID():
            high = mid - 1
        else:
            low = mid + 1
        
    print("This card is not in your hand!")

def titleMenu():
    for i in range(len(TITLE)):
        print(str(i + 1) + ") " + TITLE[i])
        
def gangMenu():
    for i in range(len(GANG)):
        print(str(i + 1) + ") " + GANG[i])

# Add other functions you need below


main()

