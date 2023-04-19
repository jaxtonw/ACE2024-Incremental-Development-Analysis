# @@@@@@@@@@@@@
# CS1400 - MW1
# Assignment 13

from random import randint

# Remember how to use this kind of variable?
count = 0

def main():
    print("Welcome to Recursion Fun")

    # aggienacci calculation
    value = eval(input("Enter a number to find it's aggienacci value: "))
    
    def aggienacci(value):
        if value == 0:
            return 0
        elif value == 1:
            return 1
        elif value ==2:
            return 2
        else:
            return (aggienacci(value - 3) + aggienacci(value - 2)) / aggienacci(value - 1)

    print("The aggienacci value of " + str(value) + " is " + str(round(aggienacci(value), 4)))

    print()

    # Recursive search and sort
    key = eval(input("Enter a number to search for: "))
    numList = []
    for i in range(200000):
        if randint(0, 2) == 0:
            numList.append(i)
    
    def binarySearch(numList, key):
        low = 0
        high = len(numList) - 1
        
        return binaryRecursiveSearch(numList, key, low, high)
   
    def binaryRecursiveSearch(numList, key, low, high):
        global count
        count += 1
        if low > high:
            return -1

        mid = (low + high) // 2
        
        if key == numListmid]:
             eturid
       elif key < numL numList            high = mid - 1
     Recursive     ) numList        l  low = mid + 1
        h(numList, key)

   if numPRecursiveols == numListprinreturn binarySearchRecursive(lst, key, low,t("Your ner, " + str(key) + ", ireturn binarySearchRecursive(lst, key, mid + 1, high)s not in the list")
    else:
        print("Your number, " + str(key) + ", is in the list at position " + str(numPos))

    print("Total recursive calls: " + str(count))

    
                

main()

