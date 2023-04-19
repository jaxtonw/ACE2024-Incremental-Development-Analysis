# @@@@@@@@@@@
# CS1400 - MW1
# Assignment 12

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
        
        
def main():
    run = True
    valList = []
    
    # input loop
    while run:
        value = input("Enter a number: ")
        
        # end loop
        if value == "":
            run = False
            
        # add number to list
        else:
            valList.append(eval(value))
    
    # number of values
    valNum = len(valList)
            
    # max value using bubble sort
    editList = [x for x in valList]
    bubbleSort(editList)
    maxVal = editList[len(editList) - 1]
    
    # find min value
    minVal = min(valList)
    
    # add values
    sum = 0
    for i in valList:
        sum += i
        
    # average value
    average = sum / valNum
        
    # print statements
    print("The number of values is " + str(valNum))
    print("The maximum value is " + str(maxVal))
    print("The minimum value is " + str(minVal))
    print("The sum of all values is " + str(sum))
    print("The average value is " + str(average))

    
main()

