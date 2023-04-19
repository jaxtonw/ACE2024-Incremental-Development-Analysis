# @@@@@@@@@@@@@
# CS-1400 MW1
# Assignment 13
from random import randint
# Remember how to use this kind of variable?
count = 0


def aggienacci(val):
    if val == 0:
        return 0
    elif val == 1:
        return 1
    elif val == 2:
        return 2
    else:
        return (aggienacci(val - 3) + aggienacci(val - 2)) / aggienacci(val - 1)


def binarySearch(numbList, keY):
    low = 0
    high = len(numbList) - 1
    return binarySearchRecursive(numbList, keY, low, high)


def binarySearchRecursive(numbList, keY, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if keY == numbList[mid]:
        return mid
    elif keY < numbList[mid]:
        return binarySearchRecursive(numbList, keY, low, mid - 1)
    else:
        return binarySearchRecursive(numbList, keY, mid + 1, high)

def main():
    print("Welcome to Recursion Fun")
    # aggienacci calculation
    value = eval(input("Enter a number to find it's aggienacci value: "))
    print("The aggienacci value of " + str(value) + " is " + 
str(round(aggienacci(value), 4)))
    print()
    # Recursive search and sort
    key = eval(input("Enter a number to search for: "))
    numList = []
    for i in range(200000):
        if randint(0, 2) == 0:
            numList.append(i)
    numPos = binarySearch(numList, key)
    if numPos == -1:
        print("Your number, " + str(key) + ", is not in the list")
    else:
        print("Your number, " + str(key) + ", is in the list at position " + 
str(numPos))
    print("Total recursive calls: " + str(count))
main()


        
    
