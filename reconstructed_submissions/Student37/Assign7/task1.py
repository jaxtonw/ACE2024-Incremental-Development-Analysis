# @@@@@@@@@
# CS1400 - MW1
# Assignment 7 - task1

#1. Create formal parameter for the number of rows from the caller of the function
def makePyramid(rows):
    # 2. Create a string variable that will be returned. Start as an empty string.
    returnVar = ""

    for i in range(1, rows + 1): #3. Create a loop from 0 to the number of rows (including the number of rows value)
        rowString = ""     # a. Create a string variable for the row of text 
        
        for j in range(0, i): # b. Create a loop from 0 to the current row number
       
            if j != 0:    # i. Create a conditional to concatenate a space to the text if it's not the first character of the row
                rowString += " "
                rowString += str(i)
            else:    #ii. Concatenate the row number to the string
                rowString += str(i)
        
        formatRowString = format(rowString, "^" + str(rows * 2 + (rows - 2))) #format the added line to be centered
        returnVar += formatRowString + "\n"

    return returnVar   #4. Return the string message

def main():
    rows = int(input("Enter the number of rows: "))
    pyramid = makePyramid(rows)
    print(pyramid)

main()
    
