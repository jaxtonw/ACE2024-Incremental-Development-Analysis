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
        <Fill-In> # Single line

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
            <Fill-In> # Single line
        elif choice == 3:
            <Fill-In> # Single line
        elif choice == 4:
            <Fill-In> # Single line
        elif choice == 5:
            <Fill-In> # Not a function and not 'break'

def thinking():
    for i in range(5):
        print(".", end="")
       # sleep(0.5)
    print()

def displayHand(hand):
    <Fill-In> # Not a single line. The entire function body

# Add other functions you need below


main()
