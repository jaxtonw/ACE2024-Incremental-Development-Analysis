# @@@@@@@@@@@  
# CS 1400 - MW1 XL
# Assignment 012

def main():
    run = True
    baseList = []
    while run:
        item = input("Enter a Number: ")
        if str(item) == "":
            run = False
        else:
            run = True
            baseList.append(int(item))
    # this gets how many total variables there are
    numberValues = len(baseList)
    
    # this is the min value finder
    minVal = min(baseList)
    maxVal = minVal
    # this finds the max value by iterating until it finds a bigger value
    for i in range(numberValues):
        currentValue = baseList[i]
        if currentValue > maxVal:
            maxVal = currentValue
    
    # this finds the total sum of the list
    total = 0
    for i in range(numberValues):
        total += baseList[i]
    
    # average takes two already found values and divides them      
    average = total/numberValues
    
    print("The number of values entered was: " + str(numberValues))
    print("The maximum value in the list is: " + str(maxVal))
    print("The minimum value in the list is: " + str(minVal))
    print("The sum of all values in the list is: " + str(total))
    print("The average value of the list is: " + str(average))
    
    
main()

