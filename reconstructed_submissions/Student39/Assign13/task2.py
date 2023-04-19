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

    numPos = binarySearch(0, len(numList) - 1, numList, key)

    if numPos == -1:
        print("Your number, " + str(key) + ", is not in the list")
    else:
        print("Your number, " + str(key) + ", is in the list at position " + str(numPos))

    print("Total recursive calls: " + str(count))
    
    
def binarySearch(first, last, numList, key):
    global count
    count += 1
    if last >= first:
        middle = (last + first) // 2
        if numList[middle] == key:
            return key
        elif numList[middle] > key:
            return binarySearch(first, middle - 1, numList, key)
        else:
            return binarySearch(middle + 1, last, numList, key)
    else:
        return -1
    

def aggienacci(value):
    if value == 0:
        return 0
    elif value == 1:
        return 1
    elif value == 2:
        return 2
    else:
        return (aggienacci(value-3) + aggienacci(value-2)) / aggienacci(value-1)
    
    
main()

