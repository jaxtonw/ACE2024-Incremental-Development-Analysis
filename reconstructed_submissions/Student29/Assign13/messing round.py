# @@@@@@@@@@@@@@
# CS1400 - MW1
# Assignment ??


# @@@@@@@@@@@@@@
# CS1400 - MW1
# Assignment 13

from random import randint

# Remember how to use this kind of variable?
count = 0


def main():
    print("Welcome to Recursion Fun")

    def aggienacci(val):
        print("Calling aggienacci(" + str(val) + ")")
        if val == 0:
            return 0
        elif val == 1:
            return 1
        else:
            return aggienacci(val - 1) + aggienacci(val - 2)

    value = eval(input("Enter a number to find it's aggienacci value: "))
    print("The aggienacci value of " + str(value) + " is " + str(round(aggienacci(value), 4)))

    print()

    # numList.sort()
    # 
    # print(binarySearch(numList, 87))




    key = eval(input("Enter a number to search for: "))
    numList = []
    for i in range(200000):
        if randint(0, 2) == 0:
            numList.append(i)

    def binarySearch(lst, key):
        low = 0
        high = len(lst) - 1
        return binarySearchRecursive(lst, key, low, high)

    def binarySearchRecursive(numList, key, low, high):
        print("Recursive call: ", low, high)
        if low > high:
            return -1

        mid = (low + high) // 2
        if key == numList[mid]:
            return mid
        elif key < numList[mid]:
            return binarySearchRecursive(numList, key, low, mid - 1)
        else:
            return binarySearchRecursive(numList, key, mid + 1, high)
    numPos = binarySearch(numList, key)

    if numPos == -1:
        print("Your number, " + str(key) + ", is not in the list")
    else:
        print("Your number, " + str(key) + ", is in the list at position " + str(numPos))

    print("Total recursive calls: " + str(count))


main()
