# @@@@@@@@@@@@@@@
# CS1400 - 14 Week
# Assignment 13

from random import randint
count = 0
def main():
    def aggienacci(val):
        if val == 0:
            return 0
        elif val == 1:
            return 1
        elif val == 2:
            return 2
        else:
            return aggienacci(val - 3) + aggienacci(val - 2) / aggienacci(val - 1)
    def binarySearch(num,key):
        low = 0
        high = len(num) - 1
        return binarySearchRecursive(num, key, low, high)w
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
hi  print("Welcome to Recursion Fun")
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
        print("Your number, " + str(key) + ", is in the list at position " + str(numPos))
    print("Total recursive calls: " + str(count))


main()

    
        
