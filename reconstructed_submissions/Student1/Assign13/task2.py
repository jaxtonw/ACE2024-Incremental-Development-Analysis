from random import randint

# Remember how to use this kind of variable?
count = 0

def main():
    print("Welcome to Recursion Fun")

    # aggienacci calculation
    value = eval(input("Enter a number to find its aggienacci value: "))
    print("The aggienacci value of " + str(value) + " is " + str(round(aggienacci(value), 4)))

    print()

    # Recursive search and sort
    key = eval(input("Enter a number to search for: "))
    numList = []
    for i in range(50):
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
    else:
        return (aggienacci(num - 3) + aggienacci(num - 2)) / aggienacci(num - 1)


def binarySearch(list, key):
    low = 0
    high = len(list) - 1
    return rbinarySearch(list, key, high, low)


def rbinarySearch(list, key, high, low):
    global count
    count += 1
    mid = (low + high) // 2
    if low > high:
        return -1
    elif key == list[mid]:
        return mid
    elif key < list[mid]:
        return rbinarySearch(list, key, mid - 1, low)
    else:
        return rbinarySearch(list, key, high, mid + 1)


main()


    
    
