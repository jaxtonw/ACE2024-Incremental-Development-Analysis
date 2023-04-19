# @@@@@@@@@@@@@@@@
# CECS1400 - MW1
# Assignment 7-Task 1

# create makeNumberPyramid function
def makeNumberPyramid(numRows):
    sizeBottomRow = len(str(numRows)) * numRows + numRows - 2
    for i in range(1, numRows + 1):
        sizeCurrentRow = len(str(i)) * i + i - 2
        sizeDiff = sizeBottomRow - sizeCurrentRow
        row = ""
        for k in range(sizeDiff // 2):
            row += " "
        for j in range(i):
            row += (str(i) + " ")
        print(row)

# create main function
def main():
    # get user input for number of rows in pyramid
    numRows = eval(input("How many rows should your pyramid have? "))
    makeNumberPyramid(numRows)

# call main function    
main()
