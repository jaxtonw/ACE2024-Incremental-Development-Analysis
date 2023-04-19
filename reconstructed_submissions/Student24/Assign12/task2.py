# @@@@@@@@@@@@
# CS1400 - MW1
# Assignment 12

def main():
	# The purpose is to prompt user for input until the user does not
	# give input. So we create a variable to be true and then create a 
	# while loop that performs until the user does not give input
	userHasNotHitEnter = True
	# Create an empty list for us to add all our numbers to
	allNumbers = []
	# Create our while loop to add items to the list
	while userHasNotHitEnter == True:
		userInput = input("Enter a number: ")
		# If the user gives an input, add it to the list
		if userInput:
			allNumbers.append(int(userInput))
		# If the user does not give an input, kill the loop
		if not userInput:
			userHasNotHitEnter = False

	# Display how many numbers are in the list
	print("The number of values entered is " + str(len(allNumbers)))
	
	# Display the maximum value
	print("The maximum value is " + str(maximumValue(allNumbers)))
	
	# Display the minimum value
	print("The minimum value is " + str(min(allNumbers)))
	
	# Display the sum of all the values
	print("The sum of the values is " + str(sumValues(allNumbers)))
	
	# Display the average of all the values
	print("The average value is " + str(averageValue(allNumbers)))
	
	
# Create a bubble sort to sort the list of inputted values	
def bubbleSort(inputList):
	didSwap = True
	
	while didSwap:
		didSwap = False
		sortCount = 1
		
		for i in range(len(inputList) - sortCount):
			if inputList[i] > inputList[i + 1]:
				inputList[i], inputList[i + 1] = inputList[i + 1], inputList[i]
				didSwap = True
	
# Create a new function that will return the maximum value of our sorted list	
def maximumValue(sortedList):
	bubbleSort(sortedList)
	return sortedList[len(sortedList) - 1]

# Create a function that will return the sum of the values in a list
def sumValues(inputList):
	sum = 0
	for i in inputList:
		sum += i
	return sum

# Create a function that will return the average value in a list
def averageValue(inputList):
	average = sumValues(inputList) / len(inputList)
	# I don't want the average to just be an integer, but I also don't
	# want a ton of decimals. So format the average to just 2 decimal places.
	return format(average, ".2f")


main()	
