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
            sortTitle(playerHand) # Single line
        elif choice == 3:
            sortGang(playerHand) # Single line
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
    for i in hand:# Not a single line. The entire function body
        print(i)
# Add other functions you need below
def sortTitle(hand):
    print("Selection sort by title", end="")
    thinking()
    # Sort by title
    for i in range(len(hand) - 1):
        # Set the current index to the index of the smallest card
        smallestCard = i
        # Make another loop to determine if the other cards are lower
        for j in range(i + 1, len(hand)):
            # Compare the title index numbers
            if hand[j].getID() % len(TITLE) < hand[smallestCard].getID() % len(TITLE):
                # If the index is smaller, set the smallest card index to that
                smallestCard = j
        # Swap the smallest card to the front
        hand[smallestCard], hand[i] = hand[i], hand[smallestCard]
        

def sortGang(hand):
    print("Bubble sort by gang", end="")
    thinking()
    # Set a variable to control the loop, set as True so it will run
    swap = True
    while swap:
        # Set to false so it will stop if we don't swap (i.e. all are sorted)
        swap = False
        # For each card in the hand, compare it to the one before it
        for i in range(1,len(hand)):
            # If the card is smaller than the one before it, swap them
            if hand[i] < hand[i - 1]:
                hand[i], hand[i - 1] = hand[i - 1], hand[i]
                # Set variable to True so it will repeat
                swap = True
    

def cardSearch(hand):
    # Display submenus and get input
    print("Titles")
    for i in range(len(TITLE)):
        print("\t" + str(i + 1) + ") " + str(TITLE[i]))
    cardTitle = eval(input("Select the title of card to search for: "))
    # Determine the title based on index position
    cardTitle = TITLE[cardTitle - 1]
    print("\nGangs")
    for i in range(len(GANG)):
        print("\t" + str(i + 1) + ") " + str(GANG[i]))
    cardGang = eval(input("Select the gang of card to search for: "))
    # Determine the gang based on index position
    cardGang = GANG[cardGang - 1]
    # Find the id of the selected card (so we can search for this)
    idOfCard = convertCardToId(cardTitle,cardGang)
    print()
    # Sort it (by gang so the ids are in order)
    sortGang(hand)
    # Set low and high as lowest and highest index of list
    low = 0
    high = len(hand) - 1
    # Set result to False so we know it isn't there if it stays False
    result = False
    while low <= high:
        # Find the middle number and compare it to the number we are searching for
        mid = (low + high) // 2
        if hand[mid].getID() == idOfCard:
            # If the ids match, we know the card is in the hand
            result = True
            break
        elif hand[mid].getID() < idOfCard:
            low = mid + 1
        else:
            high = mid - 1
    # Print whether or not the card is in the deck based on findings of search
    if result:
        print("You have this card!")
    else:
        print("You do not have this card.")

main()
