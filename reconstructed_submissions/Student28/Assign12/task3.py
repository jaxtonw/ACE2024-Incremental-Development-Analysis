# @@@@@@@@@@@
# Assingment 12 Task 3
# CS 1400 14 week

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

# Menu choices
        if choice == 1:
            displayHand(playerHand)
        elif choice == 2:
            sortTitle(playerHand) # Single line
        elif choice == 3:
            sortGang(playerHand) # Single line
        elif choice == 4:
            search(playerHand) # Single line
        elif choice == 5:
            done = True # Not a function and not 'break'

def thinking():
    for i in range(5):
        print(".", end="")
        sleep(0.5)
    print()

def displayHand(hand):  # Not a single line. The entire function body
    for i in hand:
        print(str(i.getTitle()) + " of " + str(i.getGang()))

# Add other functions you need below

def sortTitle(hand):
    # Animation
    print("Selection Sort by Title", end="")
    thinking()

# Selection sort
    for i in range(len(hand) - 1):
        currMinIndex = i

        for j in range(i + 1, len(hand)):
            if hand[currMinIndex].getID() % len(TITLE) > hand[j].getID() % len(TITLE): # Get id and turn into title id
                currMinIndex = j

        if currMinIndex != i:
            hand[i], hand[currMinIndex] = hand[currMinIndex], hand[i]       # Perform swap
    
def sortGang(hand):
    # Animate
    print("Bubble Sort by Gang", end="")
    thinking()
    
    swap = True
    
    while swap:
        swap = False
        count = 1
    
        for i in range(len(hand) - count):
            if (hand[i].getID() // len(TITLE)) > (hand[i + 1].getID() // len(TITLE)): # Get id and turn into gang id
                hand[i], hand[i + 1] = hand[i + 1], hand[i]         # Perform swap
                swap = True
            
        count += 1

def search(hand):
    sortGang(hand)          # Sort to start
    for i in range(len(TITLE)):         # Present user with list of title options
        print(str(i + 1) + ") ", end="")
        print(TITLE[i])
    titleChoice = TITLE[eval(input("Select title: ")) - 1]      # Ask user for title looking for
    for i in range(len(GANG)):              # Present user with list of gang options
        print(str(i + 1) + ") ", end="")
        print(GANG[i])
    gangChoice = GANG[eval(input("Select gang: ")) - 1]         # Ask user for gang looking for
    
    id = convertCardToId(titleChoice, gangChoice)           # Take choice and create the id
    conclusion = binarySearch(hand, id)                 # Do the search on choice
    if conclusion == -1:
        print("You do not have that card.")             # Card not found
    else:
        print("You have that card.")                    # Card found
    
            
def binarySearch(hand, key):        # Take id from choice prompt
    low = 0                     # Starting point of search set
    high = len(hand) - 1        # Ending point of search set
    while high >= low:
        mid = (high + low) // 2     # Create two sections
        if key == hand[mid].getID():    # If lucky and find on first go, spit out result
            return mid
        elif key < hand[mid].getID():   # Create new section below previous
            high = mid - 1
        else:                           # Create new section above previous
            low = mid + 1

    return -1

main()
