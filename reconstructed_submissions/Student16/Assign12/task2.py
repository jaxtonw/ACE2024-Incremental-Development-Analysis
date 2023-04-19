# @@@@@@@@@@@@@@
# CS1400 - MW2
# Assignment 12

# Define the main function
def main():
    # Initialize the list that the user will add to
    theList = []
    
    # Create a variable that will keep the while loop going
    done = False
    
    # While loop will allow the user to enter as many numbers as they wnat until they enter an empty string
    while not done:
        # Get and save user input
        userInput = input("Enter a number (Enter nothing when done) ")
        
        # append the user's input if it is a number and convert to a float
        if userInput.isdigit():
            userInput = float(userInput)
            theList.append(userInput)

        # if the user inputs an empty string the while loop will be done
        if userInput == "":
            done = True
    
    # Print the number of values in the list
    print("The length of the list is: " + str(len(theList)
))    
    # display the maximum value in the list
    
    # Create a value to start comparing with
    max = theList[0]
    for i in theList:
        if i > max:
            # Replace the max value if there is a value larger than it
            max = i
            
    print("The max value in the list is: " + str(max))
    
    # display the minimum value in the list
    theList.sort()
    print("the smallest value in the list is: " + str(theList[0]))
    
    # display the sum of all values
    sum = 0
    for i in range(len(theList)):
        sum += theList[i]
        
    print("The sum of the values in the list are: " + str(sum))
    
    # display the average value of the values of the list
    average = sum / (len(theList) + 1)
    
    print("The average value is: " + str(average))
    



main()

