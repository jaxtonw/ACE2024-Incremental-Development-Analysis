# @@@@@@@@@@@
# Assingment 12 Task 2
# CS 1400 14 week

def main():
    
    userList = []
    
    userInput = not None
    
    while userInput is not None:
        userInput = input("Enter a number: ")
        if userInput == "":
            break
        userList.append(userInput)
    
    print("The length of the list is: " + str(len(userList)))
    
    print("The minimum value of the list is: " + str(min(userList)))
    
    sum = 0
    for i in range(len(userList)):
        sum += int(userList[i])
        
    print("The sum of the list is: " + str(sum))
    
    print("The average value of the list is: " + str(sum/len(userList)))
    
    
main()
