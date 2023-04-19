# @@@@@@@@@@@@@@@
# CS 1400-14 week
# Assignment 12

def main():
    userInput = True
    numList = []
    sum = 0
    while userInput == True:
        value = input("Enter a number: ")
        if value == "":
            userInput = False
        else:
            numList.append(value)
            sum += int(value)
    
    print("The number of values entered was: " + str(len(numList)))
    print("The maximum value entered was: " + maximum(numList))
    print("The minimum value entered was: " + min(numList))
    print("The sum of all the values is: " + str(sum))
    print("The average of all value is: " + str(sum // len(numList)))
    
    
def maximum(list):
    currentMax = 0
    for i in range(1, len(list)):
        if list[i] > list[currentMax]:
            currentMax = i            
    return list[currentMax]

main()
