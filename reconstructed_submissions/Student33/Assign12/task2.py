# @@@@@@@@@@@@
# CS1400 - 012
# Assignment 12

def main():
    list = []
    done = False
    count = 0
    while not done:
        value = input("Enter number to list: ")
        if value == "":
            done = True
        else:
            list.append(eval(value))
            count += 1
    print("")
    print("Number of values entered:", count)
    print("Maximum value:", maxValue(list))
    print("Minimum value:", min(list))
    print("Sum of all values:", sumList(list))
    print("Average value:", sumList(list) // len(list))
    
def maxValue(myList):
    for i in range(len(myList) - 1):
        currMinIndex = i
        
        for j in range(i + 1, len(myList)):
            if myList[currMinIndex] > myList[j]:
                currMinIndex = j
                
        if currMinIndex != i:
            myList[i], myList[currMinIndex] = myList[currMinIndex], myList[i]
            
    return myList[len(myList) - 1]

def sumList(myList):
    totalSum = 0
    for i in range(len(myList)):
        totalSum += myList[i]
        
    return totalSum
    
main()
