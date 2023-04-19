# @@@@@@@@@@@@@
# CS1400 - MW1
# Assignment 7

def makeNumberPyramid(rowNum) :
    output = ""
    maxLength = str(len(str(rowNum)) * rowNum + rowNum - 1)
    for i in range(0, rowNum + 1):
        row = ""
        for j in range(0, i):
            if j != 0:
                row += " "
            row += str(i)
        row = format(row, "^" + maxLength)
        row += "\n"
        output += row
    return output


def main():
    userInput = int(input("Enter number of desired rows: "))
    result = makeNumberPyramid(userInput)
    print(result)
    
main()
    

