# @@@@@@@@@@@
# Assignment 13 Task 2
# CS 1400 14 week

from random import randint

# Remember how to use this kind of variable?
count = 0

def binarySearch(inputList, key):
    low = 0  # Starting point of search set
    high = len(inputList) - 1  # Ending point of search set
    while high >= low:
        mid = (high + low) // 2  # Create two sections
        if key == inputList[mid]:  # If the key is in the middle position
            return mid
        elif key < inputList[mid]: # Throws away top part of list
            high = mid - 1
        else:                      # Throws away bottom of list
            low = mid + 1
            
    return -1

def aggienacci(val):
    if val == 0:    # Base case 1
        return 0
    elif val == 1:  # Base case 2
        return 1
    elif val == 2:  # Base case 3
        return 2
    else:           # Recursive definition
        return (aggienacci(val - 3) + aggienacci(val - 2)) / aggienacci(val - 1)
    


def main():
    print("Welcome to Recursion Fun")
    
    # aggienacci calculation
    value = eval(input("Enter a number to find it's aggienacci value: "))
    print("The aggienacci value of " + str(value) + " is " + 
str(round(aggienacci(value), 4)))   # Round to 4 decimal places
    
    print()
    # Recursive search and sort
    key = eval(input("Enter a number to search for: "))
    numList = []
    for i in range(200000):         # Create a list to search for
        if randint(0, 2) == 0:
            numList.append(i)
            
    # Run seach and then display results
    numPos = binarySearch(numList, key)
    if numPos == -1:
        print("Your number, " + str(key) + ", is not in the list")
    else:
        print("Your number, " + str(key) + ", is in the list at position " + 
str(numPos))
        
    print("Total recursive calls: " + str(count))   # Print the total number of iterations
    

main()
