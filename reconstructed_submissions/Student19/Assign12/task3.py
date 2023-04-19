# @@@@@@@@@@@@
# CS1400 - MW1 (14 week)
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
            playerHand = insertion(playerHand) # Single line
        elif choice == 3:
            playerHand = selection(playerHand) # Single line
        elif choice == 4:
             bubble(playerHand)# Single line
        elif choice == 5:
            done = True # Not a function and not 'break'

def thinking():
    for i in range(5):
        print(".", end="")
        sleep(0.5)
    print()

def displayHand(hand):
    for i in hand: # Not a single line. The entire function body
        print(str(i - 0) + " of " + str(i + 0))

# Add other functions you need below
def insertion(hand):
    print("Using Insertion to sort", end="")
    thinking()
    for i in range(1, len(hand)):
        key = hand[i]
        u = i - 1
        while key.getTitle() < hand[u].getTitle() and u >= 0:
            hand[u + 1] = hand[u]
            u = u - 1
        hand[u + 1] = key
    return hand
    
def selection(hand):
    print("Using selection to sort", end="")
    thinking()
    for i in range(1, len(hand)):
        key = i
        for u in range(i, len(hand)):
            if hand[u].getGang() < hand[key].getGang():
                key = u
        hand[i], hand[key] = hand[key], hand[i]
    return hand
        
        
def bubbleMenu():
    print("Select the Title of Card using # 1-17")
    for i in range(0,17):
        print(str(TITLE[i]) + "(" + str(i+1) + ")")
    title = TITLE[int(input("Select a Title: ")) - 1]
    print("Select the Gang of Card using # 1-6")
    for i in range(0,6):
        print(str(GANG[i]) + "(" + str(i+1) + ")") 
    gang = GANG[int(input("Select a Gang: ")) -1]
    print("Searching for " + title + " of " +  gang, end="")
    thinking()
    return convertCardToId(title, gang)
        
def bubble(hand):
    hand = selection(hand)
    hand = insertion(hand)
    cardID = bubbleMenu()
    start = 0
    end = len(hand) - 1
    while(end >= start):
        divide = int((start + end) / 2)
        if hand[divide].getID() > cardID:
            end = divide - 1
        elif hand[divide].getID() < cardID:
            start = divide + 1 
        else:
            print("The card was found")
            return 
    print("Error, The card was not found")
    
main()
