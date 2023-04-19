# @@@@@@@@@@
# CS 1400 - 14 week
# Assignment 7

def makeNumberPyramid(rows):
    msg = ""
    for i in range(0, rows+1):
        rowText = ""
        for j in range (0, i):
            if j > 0:
                rowText += " "
            rowText += str(i)
        val = len(str(rows)) * rows + (rows - 1)
        msg += format(rowText, "^" + str(val) + "s") + "\n"
    return msg

def main():
    num = eval(input("Enter the number of rows: "))
    pyramid = makeNumberPyramid(num)
    print(pyramid)
    
main()
