# @@@@@@@@@@@@@
# CS1400 - MW1
# Assignment 7

# make number pyramid
def makeNumberPyramid(rowNumber):
    
    # calculate width based off the number of characters in the number for the number of rows
    # take away 1 from the width to get rid of space in front of the first number
    width = ((len(str(rowNumber)) + 1) * rowNumber) - 1

    # create string variable that will be returned
    message = ""
    
    # loop from 0 to the number of rows provided
    for i in range(rowNumber + 1):
        
        # create a string variable for the row of text
        rowText = ""
        
        # create a loop from 0 to the current row number
        for j in range(i):
            
            # concatenate a space to the text if its not the first character of the row
            if j > 0:
                rowText += " "
            
            # concatenate the row number to the string
            rowText += str(i)

        rowText = format(rowText, "^" + str(width) + "s")
            
        # add the row of text string to the message variable
        message += rowText
        
        # add a new line
        message += "\n"
    
    # return the string message    
    return message


# define main function            
def main():
    
    # get user input for number of rows and save
    userRows = int(input("Enter the number of desired rows: "))
    
    # call makeNumberPyramid function
    answer = makeNumberPyramid(userRows)
    
    # print the return value
    print(answer)

# call the main function
main()
