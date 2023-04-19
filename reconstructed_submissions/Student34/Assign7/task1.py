# @@@@@@@@@@@@
# CS 1400 - 14 Weeks
# Assignment 7

def makeNumberPyramid(numRows):
    msg = ""
    # First change to fix error
    finalRowLength = (len(str(numRows)) + 1) * numRows - 1
    for i in range(0, numRows + 1):
        rowText = ""
        for j in range(0, i):
            if j != 0:
                rowText += " "
            rowText += str(i)
        # Second change to fix error
        msg += format(rowText, "^" + str(finalRowLength) + "s") + "\n"
    return msg


def main():
    rowQuantity = eval(input("Enter the number of rows to be printed: "))
    msg = makeNumberPyramid(rowQuantity)
    print(msg)
    
    
main()

