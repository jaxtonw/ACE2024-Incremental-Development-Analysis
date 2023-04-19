# @@@@@@@@@@@@
# CS1400 - 001
# Assignment 13

from random import randint
# Remember how to use this kind of variable?
count = 0
def binarySearch(numList, key):
    global count
    low = 0
    high = len(numList) - 1
    while high >= low:
        mid = (high + low) // 2
        if key == numList[mid]:
            return mid
        elif key < numList[mid]:
            high = mid - 1
            count += 1
        else:
            low = mid + 1
            count += 1

def aggienacci(val):
    print("Calling aggienacci(" + str(val) + ")")
    if val == 0:
        return 0
    if val == 1:
        return 1
    if val == 2:
        return 2
    else:
        return (aggienacci(val - 3) + aggienacci(val - 2)) / aggienacci(val - 1)

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


