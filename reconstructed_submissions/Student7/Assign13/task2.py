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


def binarySearch(list, key):
    global count
    low = 0
    high = len(list) - 1
    list.sort()
    return binaryRecursive(low,high,list,key)


def binaryRecursive(low,high,list,key):
    global count
    count += 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if list[mid] == key:
        return mid
    elif list[mid] < key:
        binaryRecursive(mid + 1,high,list,key)
    else:
        binaryRecursive(low,mid - 1,list,key)
    
    
def aggienacci(num):
    global count
    return num

main()
