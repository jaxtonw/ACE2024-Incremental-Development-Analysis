# @@@@@@@@@@@@@
# CS1400 - 001
# Assignment 13

from random import randint
# Remember how to use this kind of variable?
count = 0

def aggienacci(i):
    global count 
    if i == 0:
        return 0
    elif i == 1:
        return 1
    elif i == 2:
        return 2
    else:
        count = count + 3
        return aggienacci(i - 3) + aggienacci(i -2) / aggienacci(i -1)
    
    
def binarySearch(list1, key):
    global count
    low = 0
    high = len(list1) - 1
    
    if high >= low:
            
        mid = (high + low) // 2
            
        if list1[mid] == key:
            return mid
            
        elif list1[mid] > key:
            count = count + 1
        
        else:
            count = count + 1 
            return binarySearch(list1, mid + 1, high, key)
    else:
        return - 1 
    
    
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
    
main()

