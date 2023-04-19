# @@@@@@@@@@@@@@@@
# CECS1400 - MW1

import random


# cardValue = input("what symbol, number or letter do you want to find the ASCII value of? ")
# 
# cardSymbol = random.randint(33, 126)
# 
# print(cardSymbol)
# print(chr(cardSymbol))
# print(ord(cardValue))
   

numCol = int(input("Enter the number of columns on the board: "))
numRows = int(input("Enter the number of rows on the board: "))
# 
# cardSpace = []
# gameBoard = cardSpace * numCol
# 
# print(gameBoard)

def main():
    # Create a two dimensional list of random numbers
    list1 = []
    for i in range(numRows):
        list1.append([])
        for j in range(numCol):
            list1[i].append(random.randint(0, 9))


    #Access by index
    print("Access by Index")
    for i in range(len(list1)):
        for j in range(len(list1[i])):
            print(list1[i][j], end=" ")
        print()

    #Access by element
    print("\nAccess by Element")
    for row in list1:
        for num in row:
            print(num, end=" ")
        print()

main()
