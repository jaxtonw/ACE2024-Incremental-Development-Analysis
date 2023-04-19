# @@@@@@@@@@@@@@@@
# CECS1400 - MW1
# Assignment 12-task 2

def main():
    list1 = []
    print("When done entering numbers for your list just press enter without typing a number.")
    userInput = " "
    countItems = 0
    while "" != userInput:
        userInput = input("Enter a number: ")
        if userInput.isdigit():
            modifiedInput = eval(userInput)
            list1.append(modifiedInput)
            countItems += 1

   
    bubbleSort(list1)
    print("The number of values you entered is " + str(countItems))
    
    maxVal = list1[countItems - 1]
    print("The Maximum Value = " + str(maxVal))
    
    minVal = min(list1)
    print("The Minimum Value = " + str(minVal))

    listSum = 0
    
    for i in list1:
        listSum += i
    
    print("The sum of all values = " + str(listSum))
    
    avgVal = listSum / countItems
    print("The Average value = " + str((round(avgVal, 2))))
        

def bubbleSort(list1):
    didSwap = True

    while didSwap:
        didSwap = False
        sortCnt = 1

        for i in range(len(list1) - sortCnt):
            if list1[i] > list1[i + 1]:
                list1[i], list1[i + 1] = list1[i + 1], list1[i]
                didSwap = True

        sortCnt += 1

main()
