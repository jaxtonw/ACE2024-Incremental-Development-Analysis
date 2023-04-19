# @@@@@@@@@@@
# Assignment 7 Plan 1
# CS 1400 14 Week

# Define makeNumberPyramid
def makeNumberPyramid(val):
    msg = "\n"
    maxLength = len(str(val + 1)) * val - 1
# Outer loop to make a row
    for i in range(1, val + 1):
# Inner loop to fill a row
        for j in range(1, i + 1):
            msg += format(i, "^" + str(len(str(val)) + 1))
        msg += "\n"
    return msg
    
# Define main, gets input from user
def main():
    rowNum = eval(input("How many rows would you like? "))
    print(makeNumberPyramid(rowNum))
    
main()
