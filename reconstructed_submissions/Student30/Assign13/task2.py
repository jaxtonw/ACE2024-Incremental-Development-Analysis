# @@@@@@@@@@@@@@@@@@
# CS1400 - 001
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

def aggienacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return (aggienacci(n-3) + aggienacci(n-2)) / aggienacci(n - 1)
    
def binarySearch(lst, key):
    low = 0
    high = len(lst) - 1
    return binarySearchRecursive(lst, key, low, high)

def binarySearchRecursive(lst, key, low, high):
    global count
    count += 1
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
    

