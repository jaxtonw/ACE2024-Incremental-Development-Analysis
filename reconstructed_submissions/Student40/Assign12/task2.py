# @@@@@@@@@@
# CS 1400 - 14 Week
# Assignment 12

def main():
    go = True
    userList = []
    
    while go:
        number = input("Enter a number: ")
        if number != "":
            userList.append(eval(number))
        else:
            go = False
        
    valueCount = len(userList)
    
    selectionSort(userList)
    maxVal = userList[len(userList) - 1]
    
    minVal = min(userList)
    
    sumVal = 0
    for k in range(len(userList)):
        sumVal += userList[k]
        
    aveVal = sumVal / valueCount
    
    msg = "\n"
    msg += "You entered " + str(valueCount) + " numbers" + "\n"
    msg += "The maximum value is " + str(maxVal) + "\n"
    msg += "The minimum value is " + str(minVal) + "\n"
    msg += "The sum is " + str(sumVal) + "\n"
    msg += "The average value is " + str(round(aveVal, 2))
    
    print(msg)
    

def selectionSort(lst):
    for i in range(len(lst) - 1):
        currMinIndex = i

        for j in range(i + 1, len(lst)):
            if lst[currMinIndex] > lst[j]:
                currMinIndex = j

        if currMinIndex != i:
            lst[i], lst[currMinIndex] = lst[currMinIndex], lst[i]

        
main()

