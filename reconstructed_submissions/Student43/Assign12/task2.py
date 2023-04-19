# @@@@@@@@@@@@@
# CS1400 - MW1 XL
# Assignment 12

# Create an empty list for the user to fill in
userList = []

# Use a while loop to add each user number to the list
while True:
    numForList = input("Enter a number: ")
    if numForList == "":
        break
    userList.append(eval(numForList))

# Create a loop to find the number of values and the sum of all of the values in the list
numberOfValues = 0
listSum = 0
for i in range(len(userList)):
    numberOfValues += 1
    listSum += userList[i]

# Use a selection sort to sort the list in order to find the maximum value
def selectionSort(userList):
    for i in range(len(userList) - 1):
        currentMinIndex = i
        
        for j in range(i + 1, len(userList)):
            if userList[j] < userList[currentMinIndex]:
                currentMinIndex = j
                
        userList[i], userList[currentMinIndex] = userList[currentMinIndex], userList[i]


# Apply the selection sort to the list
selectionSort(userList)

# Print the number of values, max and min values, sum of values, and average of values in the list
print("Number of values in list: " + str(numberOfValues))
print("Maximum value in list: " + str(userList[len(userList) - 1]))
print("Minimum value in list: " + str(min(userList)))
print("Sum of all values in list: " + str(listSum))
print("Average value in list: " + str(listSum // numberOfValues))

