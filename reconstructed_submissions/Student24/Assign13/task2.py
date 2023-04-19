# @@@@@@@@@@@@
# CS1400 - MW1
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

# We will start with first the binary search needed for this assignment
def binarySearch(inputList, key):
    # We create our low and high values for the binary search to keep track of
    low = 0
    high = len(inputList) - 1 # The high value is just the last number in the list
    return binarySearchRecursive(inputList, key, low, high)
    
# We created a recursive helper function call in the above function
# Now we need to actually define what that is
def binarySearchRecursive(inputList, key, low, high):
    # Bring in the global count variable to add to it.
    global count
    count += 1
    #print("Recursive call", low, high)  I used this print statement to verify my count was correct
    if low > high:
        return -1
    
    mid = (low + high) // 2
    if key == inputList[mid]:
        return mid
    elif key < inputList[mid]:
        return binarySearchRecursive(inputList, key, low, mid - 1)
    else:
        return binarySearchRecursive(inputList, key, mid + 1, high)
    # We add one to count each time we run this function
    

# We next will define the aggienacci numbers
def aggienacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    elif num == 2:
        return 2
    else:
        return (aggienacci(num - 3) + aggienacci(num - 2)) / aggienacci(num - 1)
    

main()


