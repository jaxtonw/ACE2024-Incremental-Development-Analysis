# @@@@@@@@@@@
# CS1400 - MW1
# Assignment 12

from modules.deck import Deck
from time import sleep
from modules.gronkyutil import convertCardToId
from modules.gronkyutil import TITLE, GANG
from modules.card import Card

def main():
    print("Welcome to Gronky Cards\n")
    print("Shuffling Cards", end="")
    thinking()

    deck = Deck()
    playerHand = []

    cardCount = int(input("How many cards would you like?: "))

    for i in range(cardCount):
        playerHand.append(i + 1) # Single line
    print(playerHand) # not supposed to happen 

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
            done = True # Not a function and not 'break'

def thinking():
    for i in range(5):
        print(".", end="")
        sleep(0.5)
    print()

def displayHand(hand):
    cardID = Deck.draw(hand)
    for i in range(hand):
        cardTitle = Card(cardID).getTitle
        cardGang = Card(cardID).getGang()
        card = str(cardTitle) + " of " + str(cardGang)
        print(card)
    # Not a single line. The entire function body

# Add other functions you need below

def titleSort(hand):
    didSwap = True

    while didSwap:
        didSwap = False
        sortCnt = 1

        for i in range(len(hand) - sortCnt):
            if hand[i] > hand[i + 1]:
                hand[i], hand[i + 1] = hand[i + 1], hand[i]
                didSwap = True

        sortCnt += 1
    print("Bubble Sort", end="")
    thinking()
        
def gangSort(hand):
    for i in range(1, len(hand)):
        currElement = hand[i]
        j = i - 1
        while j >= 0 and hand[j] > currElement:
            hand[j + 1] = hand[j]
            j -= 1

        hand[j + 1] = currElement
    print("Insertion Sort", end="")
    thinking()
    
def cardSearch(hand):
    # title selection
    print("Search for Card")
    for i in range(len(TITLE)):
        print("[" + str(i + 1) + "] " + str(TITLE[i]))
    titleChoice = eval(input("Choose a title: "))
    
    # gang selection
    for i in range(len(GANG)):
        print("[" + str(i + 1) + "] " + str(GANG[i]))
    gangChoice = eval(input("Choose a gang: "))
    
    # ID
    cardID = convertCardToId(titleChoice, gangChoice)
    
    # bubble/gang sort
    gangSort(hand)
    
    # binary search
    low = 0
    high = len(hand) - 1
    result = -1
    while high >= low:
        print(low, high)
        mid = (high + low) // 2
        if cardID == hand[mid]:
            result = mid
        elif cardID < hand[mid]:
            high = mid - 1
        else:
            low = mid + 1
    
    if result == -1:
        print("Sorry, you do not have that card")
    else:
        print("You have that card!")


main()
