# @@@@@@@@@@@@@
# CS 1400 - MW1
# Assignment 12

# create the list
numberList = []

# define a marker variable
notBlank = True

# continually prompt user for input and add to the list as long as a number is entered
while notBlank:
    
    # prompt user to input a number
    userNumber = input("Please enter a number: ")
    
    # verify input received is an integer or a float
    try:
        
        eval(userNumber)
        
        # append the received number to the list
        numberList.append(userNumber)
    
    # end the program if a non-number input is provided 
    except:
        
        notBlank = False

# calculate the number of values in the list and save
numberCount = len(numberList)

# find the maximum value in the list manually and save
for i in range(len(numberList) - 1):
    if numberList[i] > numberList[i + 1]:  # compare two values side-by-side
        numberList[i], numberList[i + 1] = numberList[i + 1], numberList[i]  # swap the two values
        
maxValue = numberList[len(numberList) - 1]

# find the minimum value and save
minimumValue = min(numberList)

# calculate sum the values of the list using a loop and save
sumList = 0
for i in numberList:
    sumList += eval(i)
    
# find the average of the values in the list using the sum and save
averageList = sumList / len(numberList)

# create a message variable and print
msg = ""

msg += "\n"

msg += "Number of values entered: "
msg += str(numberCount)

msg += "\n"

msg += "Maximum value entered: "
msg += str(maxValue)

msg += "\n"

msg += "Minimum value entered: "
msg += str(minimumValue)

msg += "\n"

msg += "Sum of values entered: "
msg += str(sumList)

msg += "\n"

msg += "Average of values entered: "
msg += str(averageList)

print(msg)

