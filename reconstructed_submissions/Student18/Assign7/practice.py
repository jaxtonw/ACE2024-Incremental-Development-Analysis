# @@@@@@@@@@@
# CS 1400 - A01 XL
# Assignment ??
def makeNumberPyramid(numRows):
    rowOfText = ""
    b = format(rowOfText, "^100")
    msg = ""
    for i in range(0, numRows + 1):
        b = ""
        for j in range(0, i):
            if j > 0:
                b += " "
            b += str(i)
        msg += b + "\n"
    return msg


def main():
    numRows = eval(input("Enter the number of rows: "))
    a = makeNumberPyramid(numRows)
    print(a)


main()


