from random import randint

# Remember how to use this kind of variable?
count = 0


def main():
    print("Welcome to Recursion Fun")

    def aggienacci(value):
        print("Calling aggienacci(" + str(value) + ")")
        if value == 0:
            return 0
        elif value == 1:
            return 1
        elif value == 2:
            return 2
        else:
            return aggienacci(value - 3) + aggienacci(value - 2) / aggienacci(value - 1)

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


def binarySearch(list1, key):
    low = 0
    high = len(list1) - 1
    return binarySearchRecursive(list1, key, low, high)


def binarySearchRecursive(list1, key, low, high):
    print("Recursive call: ", low, high)
    count = 0
    for i in range(len(list1)):
        count += 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if key == list1[mid]:
        return mid
    elif key < list1[mid]:
        return binarySearchRecursive(list1, key, low, mid - 1)
    else:
        return binarySearchRecursive(list1, key, mid + 1, high)


main()


