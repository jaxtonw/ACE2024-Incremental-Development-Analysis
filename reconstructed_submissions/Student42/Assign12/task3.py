# @@@@@@@@@@@@@
# CS1400 - 14 week
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
            search(playerHand) # Single line
        elif choice == 5:
            done = True # Not a function and not 'break'

def thinking():
    for i in range(5):
        print(".", end="")
        sleep(0.5)
    print()

def displayHand(hand):
    for i in range(len(hand)):
        print(hand[i])

# Add other functions you need below

# selection sort
def sortByTitle(hand):
    print("Selection sorting by title", end="")
    thinking()
    for i in range(len(hand) - 1):
        currMin = i
        for j in range(i + 1, len(hand)):
            if hand[currMin] > hand[j]:
                currMin = j
        if currMin != i:
            hand[i], hand[currMin] = hand[currMin], hand[i]
    return hand
    
# insertion sort
def sortByGang(hand):
    print("Insertion sorting by Gang", end="")
    thinking()
    for i in range(1, len(hand)):
        currCard = hand[i]
        j = i - 1
        while j >= 0 and hand[j].getID() > currCard.getID():
            hand[j + 1] = hand[j]
            
            j -= 1
        hand[j + 1] = currCard

# search
def search(hand):
    print("Search for card")
    # ask for input
    for i in range(len(TITLE)):
        print("        " + "(" + str(i + 1) + ") " + str(TITLE[i]))
    title = TITLE[eval(input("Choose a title: ")) - 1]
    
    for i in range(len(GANG)):
        print("        " + "(" + str(i + 1) + ") " + str(GANG[i]))
    gang = GANG[eval(input("Choose a Gang: ")) - 1]
    
    key = convertCardToId(title, gang)
    
    print("Insertion sort by gang", end="")
    thinking()
    print("Binary search for " + str(title) + " of " + str(gang), end="")
    thinking()
    
    # sorting
    for i in range(1, len(hand)):
        currCard = hand[i]
        j = i - 1
        while j >= 0 and hand[j].getID() > currCard.getID():
            hand[j + 1] = hand[j]

            j -= 1
        hand[j + 1] = currCard
        
    count = 0
    low = 0
    high = len(hand) - 1
    while high >= low:
        count += 1
        mid = (high + low) // 2
        if key == hand[mid].getID():
            print("        Congrats! you have that card")
            return hand[mid].getID()
        elif key < hand[mid].getID():
            high = mid - 1
        elif key > hand[mid].getID():
            low = mid + 1
    print("        Sorry. you do not have that card")
    return -1
    
    
main()

