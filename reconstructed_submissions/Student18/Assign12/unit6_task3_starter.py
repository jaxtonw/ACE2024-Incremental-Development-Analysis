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
            searchForACard(playerHand)
        elif choice == 5:
            done = True


def thinking():
    for i in range(5):
        print(".", end="")
        sleep(0.5)
    print()


def displayHand(hand):
    for card in hand:
        print(card)


def sortByGang(hand):
    print("Insertion Sorting by gang", end="")
    for card in range(5):
        print(".", end="")
        sleep(0.5)

    for card in range(1, len(hand)):
        elementNow = hand[card]
        j = card - 1
        while j >= 0 and hand[j].getGang() > elementNow.getGang():
            hand[j + 1] = hand[j]
            j -= 1
        hand[j + 1] = elementNow


def sortByTitle(hand):
    print("Bubble Sorting", end="")
    for card in range(5):
        print(".", end="")
        sleep(0.5)

    didSwap = True
    while didSwap:
        didSwap = False
        sortCount = 1

        for i in range(len(hand) - 1):
            if hand[i].getTitle() > hand[i + 1].getTitle():
                hand[i], hand[i + 1] = hand[i + 1], hand[i]
                didSwap = True
            sortCount += 1


def displayMenuTitle():
    for i in range(len(TITLE)):
        print(i + 1, TITLE[i])
    title = eval(input("Choose a title: "))
    title1 = TITLE[title - 1]
    return title1


def displayMenuGang():
    for i in range(len(GANG)):
        print(i + 1, GANG[i])
    gang = eval(input("Choose a gang: "))
    gang1 = GANG[gang - 1]
    return gang1


def searchForACard(hand):
    title = displayMenuTitle()
    gang = displayMenuGang()
    key = convertCardToId(title, gang)
    sortByGang(hand)
    low = 0
    high = len(hand) - 1
    while high >= low:
        mid = (high + low) // 2
        if key == hand[mid].getID():
            print("Your card is found! ")
            return mid
        elif key < hand[mid].getID():
            high = mid - 1
        else:
            low = mid + 1
    print("Your card was not found! ")
    return -1


main()
