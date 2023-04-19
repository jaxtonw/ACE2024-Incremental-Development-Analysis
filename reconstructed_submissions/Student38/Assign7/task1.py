# @@@@@@@@@@@@@
# CS-1400 MW1
# Assignment 7


# create function for pyramid, in correct format
def makeNumberPyramid(rowNum):
    rowString = ""
    rowSpace = rowNum * 2
    formatDef= "^" + str(rowSpace) + "s"
    for i in range(0, rowNum + 1):
        rowText = ""
        for j in range(0, i):
            if j != 0:
                rowText += " "
            rowText += str(i)
        rowString += format(rowText, formatDef) + "\n"
    return rowString


# create main and get actual parameters
def main():
    num = eval(input("Enter number of rows for the pyramid: "))
    pyramid = makeNumberPyramid(num)
    print(pyramid)

    
# call main  
main()
