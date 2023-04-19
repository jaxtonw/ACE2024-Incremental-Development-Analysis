# @@@@@@@@@@@@@
# CS1400 - 14 week
# Assignment 12
def main():
    
    # set values
    enter = False
    Max = 0
    myList = []
    sum = 0

    # get input
    while not enter:
        num = (input("enter number: "))
        myList.append(num)
        
        if num == "":
            enter = True
            myList.remove('')
            
    print(myList)
    
    # find maximum value
    for i in range(len(myList) - 1):
        if eval(myList[i]) > eval(myList[i + 1]):
            Max = myList[i]
            myList.remove(Max)
            myList.append(Max)
            
    # find minimum value
    Min = min(myList)
    
    # find sum
    for i in range(len(myList)):
        sum += eval(myList[i])
    
    statement = "The number of values entered: "
    statement += str(len(myList))
    statement += "\nThe maximum value is: " + str(Max)
    statement += "\nThe minimum value is: " + str(Min)
    statement += "\nThe sum of the values is: " + str(sum)
    statement += "\nThe average value is: " + str(round(sum / len(myList)))
    print(statement)
    
main()

