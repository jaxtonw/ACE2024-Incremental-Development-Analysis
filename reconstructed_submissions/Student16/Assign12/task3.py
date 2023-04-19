# @@@@@@@@@@@@@@
# CS1400 - MW2
# Assignment 12


# Figure out to make a file a module
from deck import Deck
from time import sleep
# from gronkyutil import convertCardToId
from gronkyutil import TITLE, GANG

def main():
    print("Welcome to Gronky Cards\n")
    print("Shuffling Cards", end="")
    thinking()

    deck = Deck()
    
    playerHand = []

    cardCount = int(input("How many cards would you like?: "))

    for i in range(cardCount):
        # append the drawn card to the player's hand
        playerHand.append(Deck.draw(deck)) 

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
            binarySearch(playerHand)
        elif choice == 5:
            done = True

def thinking():
    for i in range(5):
        print(".", end="")
        sleep(0.5)
    print()

def displayHand(hand):
    # create a loop that will print each card in the list that is the player's hand
    for i in hand:
        print(i , i.getCardId())
        
        
# Add other functions you need below
 
 
# This function Sorts the hand by title
def sortByTitle(hand):
    print("Selection sort by Title", end="")
    thinking()
    
    # Use a selection sort to order the cards in the player's hand by the title

    for i in range(len(hand) - 1):
        currMinIndex = i

        for j in range(i + 1, len(hand)):
            if hand[currMinIndex].getCardId() % len(TITLE) > hand[j].getCardId() % len(TITLE):
                currMinIndex = j

        if currMinIndex != i:
            hand[i], hand[currMinIndex] = hand[currMinIndex], hand[i]

def sortByGang(hand):
    print("Bubble sort by Gang", end="")
    thinking()
    
    # bubble sort by gang
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
    # print a all of the Titles
    for i in range(len(TITLE)):
        print("(" + str(i + 1) + ") " + TITLE[i])
    
    # Have the User choose a title
    chosenTitle = int(input("Choose a title: "))
    
    # print all of the gangs
    for i in range(len(GANG)):
        print("(" + str(i + 1) + ") " + GANG[i])
        
    # Have the user choose the Gange
    chosenGang = int(input("Choose a gang: "))
    
    # Use the user's chosen title and chosen gang to get the key for the search and subtract by one
    key = (chosenGang * chosenTitle) - 1
    
    # Sort the player's hand by gang to have the hand sorted properly
    sortByGang(hand)
    
    # Binary Search
    low = 0
    high = len(hand) - 1
    message = "Card was not found"
    while high >= low:

        mid = (high + low) // 2
        if key == hand[mid].getCardId():
            message = "Congratulation! You have that card!"
            break
        elif key < hand[mid].getCardId():
            high = mid - 1
        elif key > hand[mid].getCardId():
            low = mid + 1

    print(message)


main()



