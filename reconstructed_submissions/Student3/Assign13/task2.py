# @@@@@@@@@@@
# CS1400 - MW1
# Assignment 13

from random import randint

# Remember how to use this kind of variable?
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

def aggienacci(value):
    if value >= 0 and  value <= 2:
        return value
    else:
        return (aggienacci(value - 3) + aggienacci(value - 2)) / aggienacci(value - 1)
    
def binarySearch(lst, key):
    low = 0
    high = len(lst) - 1
    return binarySearchRecursive(lst, key, low, high)

def binarySearchRecursive(lst, key, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2
    if key == lst[mid]:
        return mid
    elif key < lst[mid]:
        return binarySearchRecursive(lst, key, low, mid - 1)
    else:
        return binarySearchRecursive(lst, key, mid + 1, high)


main()


