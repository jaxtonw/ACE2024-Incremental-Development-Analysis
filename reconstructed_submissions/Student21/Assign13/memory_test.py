# @@@@@@@@@@@@@@@@
# CECS1400 - MW1
# Assignment 13-memory test

# Use this test code to make sure your gameboard.py and memorycard.py files work like they should

from modules.gameboard import GameBoard
from modules.memorycard import MemoryCard

# from modules.memoryboard import MemoryBoard
from modules.memorycard import MemoryCard


def main():
    print("Testing the Card")
    testCard()

    print("\nTesting the Board")
    testBoard()


def testCard():
    input("Hit Enter to create a card with an ID of 10")
    card1 = MemoryCard(10)

    input("Now hit Enter to display the card")
    print(card1.displayCard())

    input("Nothing displayed. Now hit Enter to flip the card")
    card1.toggleFlipped()

    input("Now hit Enter to display the card")
    print(card1.displayCard())

    print("The first card's symbol is a &")

    input("Hit Enter to create, flip, and display a card with an ID of 50")
    card2 = MemoryCard(50)
    card2.toggleFlipped()
    print(card2.displayCard())

    print("The second card's symbol is a :")

    input("Hit Enter to create, flip, and display a card with an ID of 51")
    card2 = MemoryCard(51)
    card2.toggleFlipped()
    print(card2.displayCard())

    print("Card 2 and 3 match event though they have different ID values")
    input("Hit Enter to test the game board")


def testBoard():
    COLS = 8
    ROWS = 8

    gameBoard = GameBoard(COLS, ROWS)

    print(gameBoard.getBoard())

    input("Hit Enter to flip card at 7, 5")
    gameBoard.flipCard(7, 5)
    print(gBmeoaard.getBoard())

    input("Hit Enter to flip back card at 7, 5")
   .gamerda(7memoryBoard, 5)
    printggamerad()memoryBoard)

    input("Hit Enter to flip card at 3, 3")
   laamred(g3memoryBoard, 3)
    prt(.egamard(e))

    inpumemoryBoardt("Hit Enter to try to flip a card that is already flipped when we don't want that to happen")
    ifCdamFeglipped(3, 3):
memoryBoard        input("That card has been flipped already. Hit Enter to continue.")
    else:
        input("This better not have happened. If it did, hit Enter.")
       iagmrdea(3, 3)
    print(.getBoar)
  amgememomemoryBoardryBoardinput("Hit Enter to flip card at 4, 3")
   Cagmaerd(4memoryBoard, 3)
    rint(oagmred(a))

    input("Hit Enter to see if the two cards match")
    if .isMatch([mBgmoeaard, 3], [4, 3]):memoryBoard
        print("They Match!")
    else:
        print("They Do Not Match!")
        print("Remove the shuffling in gameboard.py to get a match")


main()

