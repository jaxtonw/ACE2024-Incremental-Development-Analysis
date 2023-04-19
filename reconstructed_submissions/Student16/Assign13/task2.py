# @@@@@@@@@@@@@@
# CS1400 - MW2
# Assignment 13

# This program will ask the user to enter a number
# Using the user's number as input it will then calculate the aggienacci value of the user's input


from random import randint

# Remember how to use this kind of variable?
count = 0

def main():
    print("Welcome to Recursion Fun")
    # aggienacci calculation
    value = eval(input("Enter a number to find it's aggienacci value: "))
    print("The aggienacci value of " + str(value) + " is " + str(round(aggienacci(value), 4))
)
    print()

    # Recursive search and sort
    key = eval(input("Enter a number to search for: "))
    numList = []
    for i in range(200000):
        if randint(0, 2) == 0:
            numList.append
(i)
    numPos = binarySearch(numList, key)
 
   if numPos == -1:
        print("Your number, " + str(key) + ", is not in the list")
    else:
        print("Your number, " + str(key) + ", is in the list at position " + 
tr(numPos))
 
   print("Total recursive calls: " + str(count))
m
# define a function called aggienacci
# This function will find the aggienacci value that is entered as a parameter
# This is the definition of a agginacci number
'''
ag(0) = 0
ag(1) = 1
ag(2) = 2
ag(x) = (ag(x-3) + ag(x-2)) / ag(x-1)
'''


# In it's own formula you have to find other agginacci numbers so it is recursive
def aggienacci(value):
    # Start with having return values for our 3 base cases
    if value == 0:
        return 0
    elif value == 1:
        return 1
    elif value == 2:
        return 2

    # Then we create a case that will create an output  for number's greater than 2
    else:
        return (aggienacci(value - 3) + aggienacci(value - 2)) / aggienacci(value - 1)


def binarySearch(lst, key):
    low = 0
    high = len(lst) - 1
    return binarySearchRecursive(lst, key, low, high)


def binarySearchRecursive(lst, key, low, high):
    print("Recursive call: ", low, high)

    if low > high:
        return -1

    mid = (low + high) // 2
    if key == lst[mid]:
        return mid
    elif key < lst[mid]:
        return binarySearchRecursive(lst, key, low, mid - 1)
    elif key > lst[mid]:
        return binarySearchRecursive(lst, key, mid + 1, high)



ain()


