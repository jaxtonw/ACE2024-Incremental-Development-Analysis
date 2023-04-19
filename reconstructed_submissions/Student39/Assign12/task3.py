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
        playerHand.append(deck.draw())  # Single line

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
            sortByTitle(playerHand)  # Single line
        elif choice == 3:
            sortByGang(playerHand)  # Single line
        elif choice == 4:
            searchForCard(playerHand)  # Single line
        elif choice == 5:
            print("Hope you enjoyed playing good Sir")
            return False  # Not a function and not 'break'


def thinking():
    for i in range(5):
        print(".", end="")
        sleep(0.5)
    print()


def displayHand(hand):
    for i in hand:
        print(i)
          

# Add other functions you need below


def sortByTitle(title):
    sort = len(title)
    for i in range(sort - 1):
        for j in range(0, sort - i - 1):
            if title[j].getID() % len(TITLE) > title[j + 1].getID() % len(TITLE):
                title[j], title[j + 1] = title[j + 1], title[j]
    print("Bubble sort by Title", end="")
    thinking()
                

def sortByGang(gang):
    for i in range(len(gang)):
        minIndex = i
        for j in range(i + 1, len(gang)):
            if gang[minIndex] > gang[j]:
                minIndex = j     
        if minIndex != i:
            gang[i], gang[minIndex] = gang[minIndex], gang[i]
    print("Selection sort by Gang", end="")
    thinking()
        

def searchForCard(inputList):
    displayTitles()
    inputTitle = eval(input("Choose a Title: "))
    displayGangs()
    inputGang = eval(input("Choose a Gang: "))
    print("Selection sort by Gang", end="")
    thinking()
    inputTitle = TITLE[inputTitle - 1]
    inputGang = GANG[inputGang - 1]
    sortByGang(inputList)
    key = convertCardToId(inputTitle, inputGang)
    print("Binary search for " + inputTitle + " of " + inputGang, end="")
    thinking()

    low = 0
    high = len(inputList) - 1
    while high >= low:
        mid = (high + low) // 2
        if key == inputList[mid].getID():
            print("Lucky! You have that card!")
            return
        elif key < inputList[mid].getID():
            high = mid - 1
        else:
            low = mid + 1

    print("Sorry sir, you don't have that card")
            
            
def displayTitles():
    for i in range(len(TITLE)):
        print(str(i + 1) + ") " + TITLE[i])
        

def displayGangs():
    for i in range(len(GANG)):
        print(str(i + 1) + ") " + GANG[i])

    
main()

