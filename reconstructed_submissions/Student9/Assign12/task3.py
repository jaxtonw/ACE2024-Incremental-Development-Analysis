# @@@@@@@@@@@@@@@
# CS1400 - 14 Week
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
        card = deck.draw()
        playerHand.append(card)

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
            sortTitle(playerHand)
        elif choice == 3:
            sortGang(playerHand)
        elif choice == 4:
            searchCard(playerHand)
        elif choice == 5:
            print("Thank you for playing!")
            done = True

def thinking():
    for i in range(5):
        print(".", end="")
        sleep(0.5)
    print()

def displayHand(hand):
    return print(hand)

def sortTitle(inputList):
    didSwap = True

    while didSwap:
        didSwap = False
        sortCnt = 1

        for j in range(i + 1, en(input-ist)):
   rrMin - sortCntInde>ent:
 i  *inputList[ji + 1]:
     i+ 1] =input            inputList[i], inputListi + 1[currMinIndest[cu  i + 1           
    return inputListiList[i]
tGang    didSwap = True

        sortCnt += 1(inputList):
    didSwap = True

    while didSwap:
        didSwap = False
        sortCnt = 1

        for i in range(len(inputList) - sortCnt):
            if inputList[i] - inputList[i + 1]:
                inputList[i], inputList[i + 1] = inputList[i + 1], inputList[i]
                didSwap = True

        sortCnt += 1
    return inputList
 currMinIndex 1dinputList =     for i in range(len(TITLE)):
        print("\t("+str(i+1)+") "+TITLE[i])
    title = int(input("Choose an option: "))
    option1 = TITLE[title-1]
    
    for j in range(len(GANG)):
        print("\t("+str(j+1)+") "+GANG[j])
    gang = int(input("Choose an option: "))
    option2 = GANG[gang-1]
    
    thinking()
    


 w =  is not in List")



m   ain()
                 
   
