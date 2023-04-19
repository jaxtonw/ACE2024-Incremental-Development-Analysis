# @@@@@@@@@@@@@
# CS1400 - M01
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
        playerHand.append(deck.draw())
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
            searchForCard(playerHand)
        elif choice == 5:
            done = True


def thinking():
    for i in range(5):
        print(".", end="")
        sleep(0.5)
    print()


def displayHand(hand):
    for i in range(len(hand)):
        print(str(hand[i]))


def sortByTitle(hand):
    print("Selection Sort by Title", end="")
    thinking()
    for i in range(len(hand) - 1):
        currMinIndex = i
        for j in range(i + 1, len(hand)):
            if TITLE.index(hand[currMinIndex].getTitle()) > TITLE.index(hand[j].getTitle()):
                currMinIndex = j
        if currMinIndex != i:
            hand[i], hand[currMinIndex] = hand[currMinIndex], hand[i]


def sortByGang(hand):
    print("Bubble Sort by Gang", end="")
    thinking()
    didChange = True
    while didChange:
        didChange = False
        sortCnt = 1
        for i in range(len(hand) - sortCnt):
            if GANG.index(hand[i].getGang()) > GANG.index(hand[i + 1].getGang()):
                hand[i], hand[i + 1] = hand[i + 1], hand[i]
                didChange = True
        sortCnt += 1


def searchForCard(hand):
    for i in range(len(TITLE)):
        print("(" + str(i+1) + ")" + TITLE[i])
    chooseTitle = eval(input("Choose a title: "))
    for j in range(len(GANG)):
        print("(" + str(j+1) + ")" + GANG[j])
    chooseGang = eval(input("Choose a gang: "))
    sortByTitle(hand)
    print("Binary Search for " + TITLE[chooseTitle-1] + " of " + GANG[chooseGang-1], end="")
    thinking()
    foundCard = False
    low = 0 
    high = len(hand) - 1
    while high >= low:
        mid = (high + low) // 2
        if convertCardToId(TITLE[chooseTitle-1], GANG[chooseGang-1]) == convertCardToId(hand[mid].getTitle(), hand[mid].getGang()):
            foundCard = True
            break
        elif convertCardToId(TITLE[chooseTitle-1], GANG[chooseGang-1]) < convertCardToId(hand[mid].getTitle(), hand[mid].getGang()):
            high = mid - 1
        else:
            low = mid + 1
    if foundCard == True:
        print("Yay! You found the card!")
    else:
        print("The card is not in the deck.")
        
        
        
main()

