# @@@@@@@@@@@
# CS 1400 - A01 XL
# Assignment 7



# makeNumberPyramid function
# 1. Create formal parameter for the number of rows from the caller
#     of the function
# 2. Create a string variable that will be returned. Start as an empty string.
# 3. Create a loop from 0 to the number of rows (including the number of
#     rows value)
#     a. Create a string variable for the row of text
#     b. Create a loop from 0 to the current row number
#         i. Create a conditional to concatenate a space to the text
#             if it's not the first character of the row
#         ii. Concatenate the row number to the string
#     c. Add the row of text string to the message variable. Make
#         sure to add a newline at the end
# 4. Return the string message


def makeNumberPyramid(numRows): 
    msg = ""
    for i in range(0, numRows + 1):
        rowOfText = ""
        for j in range (0, i): 
            if j > 0: 
                rowOfText += " "
            rowOfText += str(i)
        msg += rowOfText + "\n"          
    return msg    
    
def main(): 
    numRows = eval(input("Enter the number of rows: "))
    a = makeNumberPyramid(numRows)
    print(a)

main()


