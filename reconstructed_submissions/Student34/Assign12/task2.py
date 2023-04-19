# @@@@@@@@@@@@
# CS 1400 - 14 Weeks
# Assignment 12

def main():
    list1 = []
    done = False
    
    while not done:
        userInput = input("Enter a number: ")
        if userInput == "":
            done = True
        else:
            list1.append(eval(userInput.strip()))
    
    print("\nNumber of values entered: " + str(len(list1)))
    
    maxValue = findMaxValue(list1)

    print("Maximum Value: " + str(maxValue))
    
    print("Minimum Value: " + str(min(list1)))
    
    sumOfValues = 0
    for i in list1:
        sumOfValues += i
    
    print("Sum of Values: " + str(sumOfValues))
    
    listAverage = sumOfValues / len(list1)
    
    print("Average Value: " + str(listAverage))

def findMaxValue(numList):
    maxNum = numList[0]
    for i in range(1, len(numList)):
        if maxNum < numList[i]:
            maxNum = numList[i]
    
    return maxNum


main()

