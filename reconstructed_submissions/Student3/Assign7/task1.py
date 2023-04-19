# @@@@@@@@@@@
# CS1400 - MW1
# Assignment 7

# makeNumberPyramid function
def makeNumberPyramid(num):
    msg = ""
    for i in range(0, num + 1):
        rowOfText = ""
        for j in range(1, i + 1):
            if j != 1:
                rowOfText += " " + str(i)
            else:
                rowOfText += str(i)
        numSpace = str(len((str(num) + " ") * (num - 1) + str(num)))
        msg += format(str(rowOfText), "^" + numSpace) + "\n"
    return msg


def main():
    num = eval(input("Number of rows to print: "))
    result = makeNumberPyramid(num)
    return result
    
    
print(main())

