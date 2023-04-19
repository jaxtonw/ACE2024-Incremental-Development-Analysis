# @@@@@@@@@@@@@@
# CS1400 - 001
# Assignment 7

def makeNumberPyramid(numberOfRows):
    pyramid = str()
    bottomWidth = str()
    for j in range(0, numberOfRows):
        if j > 0:
            bottomWidth += " "
        bottomWidth += str(numberOfRows)
    bottomRowLen = len(bottomWidth)
    for i in range(0, numberOfRows+1):
        rows = str()
        format(rows, "^5")
        for j in range(0, i):
            if j > 0:
                rows += " "
            rows += str(i)
        pyramid += format(rows, "^" + str(bottomRowLen) + "s")
        pyramid += "\n"
    return pyramid
        
        
def main():
    numberOfRows = eval(input("Enter the number of rows to print: "))
    returnValue = makeNumberPyramid(numberOfRows)
    print(returnValue)


main()

