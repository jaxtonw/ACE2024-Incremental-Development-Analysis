# @@@@@@@@@@@@@@@
# CS 1400-14 week
# Assignment 13

def aggienacci(num):
    if num <= 2:
        return num
    else:
        aggienaccieNumber = (num - 3) + (num - 2) / (num - 1)
        return aggienaccieNumber


def binarySearch(list, key):
    low = 0
    high = len(list) - 1
    return binarySearchHelper(list, key, low, high)


def binarySearchHelper(list, key, low, high):
    global count
    count += 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if key == list[mid]:
        return mid
    elif key < list[mid]:
        return binarySearchHelper(list, key, low, mid - 1)
    else:
        return binarySearchHelper(list, key, mid + 1, high)





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
        print("Your number, " + str(key) + ", is in the list at position " + 
str(numPos))
    print("Total recursive calls: " + str(count))
main()



