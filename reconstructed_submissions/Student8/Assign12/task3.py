# @@@@@@@@@@@@@
# CS 1400 - MW1
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
            sortByTitle(playerHand)  # Single line
        elif choice == 3:
            sortByGang(playerHand)  # Single line
        elif choice == 4:
            searchForCard(playerHand)  # Single line
        #elif choice == 5:
            #<Fill-In> # Not a function and not 'break'

def thinking():
    for i in range(5):
        print(".", end="")
        sleep(0.5)
    print()

def displayHand(hand):
    # Not a single line. The entire function body
    for i in hand:
        print(i)

# Add other functions you need below

# sort the user's cards by title using 
def sortByTitle(hand):
    titleList = [x // 17 for x in hand]
    for i in range(1, len(titleList)):
        currentID = titleList[i]
        j = i - 1
        while j >= 0 and titleList[j] > currentID:
            titleList[j + 1] = titleList[j]
            j -= 1
            
        titleList[j + 1] = currentID
        
    hand = [] + titleList

# sort the user's cards by gang using bubble sort
def sortByGang(hand):
    
    print("Bubble Sort by Gang", end="")
    thinking()
    
    didChange = True  # allows the sorting to end once no longer needed
    
    while didChange:
        
        didChange = False
        sortCount = 1  # makes it so the last object in the list is not analyzed for sorting unnecessarily
        
        for i in range(len(hand) - sortCount):
            if hand[i] > hand[i + 1]:
                hand[i], hand[i + 1] = hand[i + 1], hand[i]
                didChange = True
                
        sortCount += 1
        
def searchForCard(hand):
    
    print("Search for Card")
    for i in range(len(TITLE)):
        print("(" + str(i) + ")" + TITLE[i])
    titleSearch = input("Choose a Title: ")
    titleSearch = int(titleSearch)
    
    
    for i in range(len(GANG)):
        print("(" + str(i) + ")" + GANG[i])
    gangSearch = input("Choose a Gang: ")
    gangSearch = int(gangSearch)
    
    searchID = convertCardToId(TITLE[titleSearch], GANG[gangSearch])
    searchID = int(searchID)
    
    print(binarySearch(hand, searchID, titleSearch, gangSearch))
    
# perform a binary search
def binarySearch(hand, searchID, titleSearch, gangSearch): 
    
    sortByGang(hand)
    
    print("Binary Search for " + TITLE[titleSearch] + " of " + GANG[gangSearch], end="")
    thinking()
    
    low = 0
    high = len(hand) - 1
    
    while high >= low:
        mid = (high + low) // 2
        
        if hand[searchID] == hand[mid]:
            return "Congratulations! That card is in your deck."
        
        elif hand[searchID] < hand[mid]:
            high = mid - 1
            
        else:
            low = mid + 1
            
        return "Card not in deck."
        

main()
