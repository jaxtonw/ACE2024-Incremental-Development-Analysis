# @@@@@@@@@@@@@
# CS1400 - MW1 XL
# Assignment 13

from random import randint

# Remember how to use this kind of variable = 0
# Couldn't figure out the counting variable :(
count = 0

def main():
    print("Welcome to Recursion Fun")

    # aggienacci calculation
    value = eval(input("Enter a number to find it's aggienacci value: "))
    print("The aggienacci value of " + str(value) + " is " + str(round(aggienacci(value), 4)))

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
        print("Your number, " + str(key) + ", is in the list at position " + str(numPos))

    print("Total recursive calls: " + str(count))


def aggienacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    elif num == 2:
        return 2
    elif num >= 3:
        return (aggienacci(num - 3) + aggienacci(num - 2)) / aggienacci(num - 1)


def binarySearch(numList, key):
    low = 0
    high = len(numList) - 1
    return binarySearchRecursiveFunTime(numList, key, low, high)


def binarySearchRecursiveFunTime(numList, key, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    if key == numList[mid]:
        return mid
    elif key < numList[mid]:
        return binarySearchRecursiveFunTime(numList, key, low, mid - 1)
    else:
        return binarySearchRecursiveFunTime(numList, key, mid + 1, high)


main()



