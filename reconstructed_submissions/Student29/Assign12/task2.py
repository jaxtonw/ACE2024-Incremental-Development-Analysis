# @@@@@@@@@@@@@@
# CS1400 - MW1
# Assignment 12

]repeat = True
list1 = []

while repeat == True:
    
    
    inputValue = input("Enter a number: ", )
    
    
    if inputValue == "":
        repeat = False
        
        print(list1)
        
    else:
        list1.append(int(inputValue))
        
sumOfAllValues = 0
for i in range(len(list1)):
    sumOfAllValues += list1[i]
    
    
def bubbleSort(inputList):
    didSwap = True

    while didSwap:
        didSwap = False
        sortCnt = 1

        for i in range(len(inputList) - sortCnt):
            if inputList[i] > inputList[i + 1]:
                inputList[i], inputList[i + 1] = inputList[i + 1], inputList[i]
                didSwap = True

        sortCnt += 1
        
bubbleSort(list1)
        
print("Number of Values Entered: " + str(len(list1)))
print("Maximum Value of The List: " + str(list1[len(list1) - 1]))
print("Minimum Value of the List: " + str(min(list1)))
print("Sum of all value is:  " + str(sumOfAllValues))
print("The average value is: " + str((sumOfAllValues/(len(list1)))))
    
        
    
    




