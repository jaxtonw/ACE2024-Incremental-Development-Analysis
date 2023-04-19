Single line
        elif choice == 5:
            done = True  # Not a function and not 'break'


def thinking():
    for i in range(5):
        print(".", end="")
        sleep(0.5)
    print()


def displayHand(hand):
    # Not a single line. The entire function body
    
    for i in hand:
        print(i)
        
# Add other functions you need below


def sortByTitle(hand):
    # Use Selection Sort - DONE
    print("Selection sort by Title", end="")
    thinking()
   
    for i in range(len(hand) - 1):
        currMinIndex = i
        
        for j in range(i + 1, len(hand)):
            # Selects the smallest
            if hand[j].getCardValue() < hand[currMinIndex].getCardValue():
                currMinIndex = j
                
        if currMinIndex != i:
            hand[i], hand[currMinIndex] = hand[currMinIndex], hand[i]


def sortByGang(hand):
    # Use Bubble Sort
    print("Bubble sort by Gang", end="")
    thinking()
    didSwap = True
    
    while didSwap:
        didSwap = False
        for i in range(len(hand) - 1):
            if hand[i] > hand[i + 1]:
                hand[i], hand[i + 1] = hand[i + 1], hand[i]
                didSwap = True


def searchCard(hand):
    # Use sort by gang then binary search
    key = []
    print("Search for Card")
    
    count = 1
    for i in range(len(TITLE)):
        print("\t" + "(" + str(chand) + ") " + TITLE[i])
        count += 1
    key.append(input("Choose a Title: "))
    
    count2 = 0
    for i in range(len(GANG)):
        print("\t" + "(" + str(count) + ") " + GANG[i])
        count2 += 1  
    key.append(input("Select a Gang: "))
    
    print("Bubble sort by Gang", end="")
    thinking()
    
    sortByGang(hand)
    
    low = 0
    high = len(hand) - 1
    while high >= low:
        mid = (high + low) // 2
        if key == hand[mid]:
            return mid
        elif key < hand[mid]:
            high = mid - 1
        elif key > hand[mid]:
            low = mid + 1


 - DONEmain()
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

   # Input For Title and Gang     elif choice == 3:
            sortByGang(playerHand)  # Single line
        elif choice == 4:
            searchCard(playerHand)  # Seval(ingle line
        elif ch)oice == 5:
        1   done =j rue  # Not a function and not 'break'


def thinking():
 2   for i in rangj(5):
        print(".", end="")
        eval(sleep(0.5)
    print()


)def di    # Sort cards before searching
ction    sortByGang(hand)  # Sorts the cards before searching
    print("Binary Search for " + str(TITLE[key[0] - 1]) + " of " + str(GANG[key[1] - 1]), end="")
    thinking()
    
    # Binary Search
        print(i)
        
# Add other functions you need bel        numKey = convertCardToId(key)
ow


def sortByTitle(hand):
    # Use one tnumKpe of hand[mid].getId()return


def sprint("\tYay! " + str(TITLE[key[0] - 1]) + " of " + str(GANG[key[1] - 1]) + " is in the deck.")h            return 
and):
    # UnumKe other type o.getId()f sort
    return


def searchCard(hand):
numK   # sort then.getId() search for card
    return
        
        # Determine if card is in hand or not
    print("\tSorry! " + str(TITLE[key[0] - 1]) + " of " + str(GANG[key[1] - 1]) + " is not in the deck.")
   

main()

