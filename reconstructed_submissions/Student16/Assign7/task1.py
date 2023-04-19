# @@@@@@@@@@@@@@
# CS1400 - MW2
# Assignment 7

def makeNumberPyramid(rowNum):
    bottomRowLength = str(((len(str(rowNum)) + 1) * rowNum) - 1)
    msg = ""
    for i in range(1, rowNum + 1):
        rowText = ""
        for j in range(i):
            if j >= 1:
                rowText += " "
            rowText += str(i)
        rowText = format(rowText, "^" + bottomRowLength)
        msg += rowText + "\n"
    format(msg, "^" + bottomRowLength)
    return msg

def main():
    rowNum = eval(input("Enter the number of rows: "))
    msg = makeNumberPyramid(rowNum)
    print(msg)
    
    
main()

        
