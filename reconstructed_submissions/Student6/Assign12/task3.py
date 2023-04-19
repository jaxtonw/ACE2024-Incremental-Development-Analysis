# @@@@@@@@@@@@@
# CS1400 - 001
# Assignment 12


from deck import Deck
from time import sleep
from gronkyutil import convertCardToId
from gronkyutil import TITLE, GANG

def main():
    print("Welcome to Gronky Cards\n")
    print("Shuffling Cards", end="")
    thinking()

    deck = Deck()
    playerHand = []

    cardCount = int(input("How many cards would you like?: "))

    for i in range(cardCount):
        playerHand.append(Deck) # Single line

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
            sortTile(playerHand) # Single line
        elif choice == 3:
            sortGang(playerHand) # Single line
        elif choice == 4:
            searchCard(playerHand) # Single line
        elif choice == 5:
            done = True # Not a function and not 'break'

def thinking():
    for i in range(5):
        print(".", end="")
        sleep(0.5)
    print()

def displayHand(hand):
    
    for i in range(len(playerHand) - 1):
    
    <Fill-In> # Not a single line. The entire function body

# Add other functions you need below


main()
