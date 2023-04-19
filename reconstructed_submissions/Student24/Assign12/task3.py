# @@@@@@@@@@@@
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
            sortByTitle(playerHand) # Single line
        elif choice == 3:
            sortByGang(playerHand) # Single line
        elif choice == 4: 
            searchForCard(playerHand) # Single line
        elif choice == 5:
            done = True # Not a function and not 'break'

def thinking():
    for i in range(5):
        print(".", end="")
        sleep(0.5)
    print()

def displayHand(hand):
    for i in hand: # Not a single line. The entire function body
        print(i)

# Add other functions you need below
def sortByTitle(hand):
    # For the first sort, we'll do a bubble sort
    # So through long experience, I've discovered we need to first sort the gang, then sort by title. That way the list is sorted by title ascending and then gang ascending.
    # Here is the code to first bubble sort the gang
    didSwapGang = True

    while didSwapGang:
        didSwapGang = False
        gangSortCount = 1

        for i in range(len(hand) - gangSortCount):
            if GANG.index(hand[i].getGang()) > GANG.index(hand[i + 1].getGang()):
                hand[i], hand[i + 1] = hand[i + 1], hand[i]
                didSwapGang = True
        gangSortCount += 1
    
    didSwap = True

    # Now that we have the list sorted by gang, we can sort the list by title and have them all sorted by title and by gang
    while didSwap:
        didSwap = False
        sortCount = 1

        for i in range(len(hand) - sortCount):
            if TITLE.index(hand[i].getTitle()) > TITLE.index(hand[i + 1].getTitle()):
                hand[i], hand[i + 1] = hand[i + 1], hand[i]
                didSwap = True
        sortCount += 1
    
    print("Bubble Sort by Title", end="")
    thinking()
    return hand

def sortByGang(hand):
    # For the second sort, we'll do an insertion sort
    # The same concept applies in this sort: we group together the titles, then sort them by their gang.
    # Code for the sorting of the titles
    for i in range(1, len(hand)):
        currElement = hand[i]
        j = i - 1
        while j >= 0 and TITLE.index(hand[j].getTitle()) > TITLE.index(currElement.getTitle()):
            hand[j + 1] = hand[j]
            j -= 1

        hand[j + 1] = currElement
    
    # Now that the title IDs are in order, we sort the gang IDs for our final output.
    # Code for the sorting of the gangs
    for i in range(1, len(hand)):
        currElement = hand[i]
        j = i - 1
        while j >= 0 and GANG.index(hand[j].getGang()) > GANG.index(currElement.getGang()):
            hand[j + 1] = hand[j]
            j -= 1
            
        hand[j + 1] = currElement
    print("Insertion Sort by Gang", end="")
    thinking()
    return hand
    
def searchForCard(hand):
    print("Search for Card")
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
    cardTitle = int(input("Choose a Title: ")) - 1
    
    print("\t(1) Jets")
    print("\t(2) Pollos")
    print("\t(3) Slugs")
    print("\t(4) Yokels")
    print("\t(5) Keiths")
    print("\t(6) Elbows")
    cardGang = int(input("Choose a Gang: ")) - 1
    
    sortByGang(hand)
    print("Binary Search for " + str(TITLE[cardTitle]) + " of " + str(GANG[cardGang]), end="")
    thinking()
    cardIsInHand = binarySearch(hand, cardTitle, cardGang)
    if cardIsInHand == True:
        print("\tCongrats! You have that card.")
    else:
        print("\tSorry. You do not have that card.")
        
def binarySearch(list, cardTitle, cardGang):
    # Our inputted list is still just titles and gangs. We need a new list of IDs to sort
    listOfIDs = [i.getID() for i in list]
    cardID = convertCardToId(TITLE[cardTitle], GANG[cardGang]) 
    
    low = 0
    high = len(listOfIDs) - 1
    while high >= low:
        mid = (high + low) // 2
        if cardID == listOfIDs[mid]:
            return mid
        elif cardID < listOfIDs[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

main()
