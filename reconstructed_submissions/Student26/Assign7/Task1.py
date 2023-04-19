# @@@@@@@@@@@@@
# CS1400 - M01
# Assignment 7

# Number of rows
def makeNumberPyramid(numOfRows):
    returnVar = ""
    for i in range(0, numOfRows+1):
        rowOfText = ""
        
# What is on each row
        for j in range(1, i+1):
            if j != 0:
                rowOfText += " "
                
# Connect all of it together
            rowOfText += str(i)
        returnVar += format(rowOfText, "^75s") + "\n"
    return returnVar

# User input and calling everything    
def main():
    numOfRows = eval(input("Enter the number of rows: "))
    result1 = makeNumberPyramid(numOfRows)
    print(result1)
main()
