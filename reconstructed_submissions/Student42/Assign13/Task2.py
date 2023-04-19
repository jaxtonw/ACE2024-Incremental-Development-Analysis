# @@@@@@@@@@@@@
# CS1400 - 14 week
# Assignment 13

from random import randint
# Remember how to use this kind of variable?
count = 0
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
count += 17
    
    
def aggienacci(value):
    if value == 0:
        return 0
    elif value == 1:
        return 1
    elif value == 2:
        return 2
    else:
        return aggienacci(value - 3) + aggienacci(value - 2) / aggienacci(value - 1)
    
def binarySearch(numList, key):
    numList.sort()
    low = 0
    high = len(numList) - 1
    return binarySearch2(numList, key, low, high, count)
    
    
def binarySearch2(numList, key, low, high, count):
    condition = 0
    count += 1
    mid = (low + high) // 2
    if low > high:
        return -1
    if key == numList[mid]:
        return mid, count
    elif key < numList[mid]:
        return binarySearch2(numList, key, low, mid - 1, count)
    else:
        return binarySearch2(numList, key, mid + 1, high, count)
    
    
    
    
    
    
main()

