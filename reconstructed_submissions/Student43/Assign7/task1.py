# @@@@@@@@@@@@@
# CS1400 - MW1 XL
# Assignment 7

# Define the makeNumberPyramid function
def makeNumberPyramid(numberOfRows):
    # msg = Final message that will be printed
    msg = ""
    # currentRow = Current row number
    currentRow = 0
    # rowSpace = The number of characters in the last row
    rowSpace = numberOfRows * (len(str(numberOfRows)) + 1) - 1
    for i in range(0, numberOfRows):
        # rowOfText = Variable for a single row of text
        rowOfText = ""
        currentRow += 1
        for j in range(0, currentRow):
            # Concatenate a space to the text if it is not the first character
            if j != 0:
                rowOfText += " "
            rowOfText += str(currentRow)
        # Add rowOfText to the message variable and format it
        msg += format(rowOfText, "^" + str(rowSpace) + "s")
        msg += "\n"
    return msg


# Define the main function
def main():
    # userNumberOfRows = Number of rows the user decides to input
    userNumberOfRows = eval(input("Enter the number of rows: "))
    finalMsg = makeNumberPyramid(userNumberOfRows)
    print(finalMsg)
    

main()
    # @@@@@@@@@@@@@
# CS1400 - MW1 XL
# Assignment 7

def makeNumberPyramid(rows):
    msg = ""
    count = 0
    while count <= rows:
        hmmm = ""
        for i in range(0, rows):
            
        

