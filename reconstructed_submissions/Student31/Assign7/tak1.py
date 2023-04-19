# @@@@@@@@@@@
# CS1400 - MW1 XL
# Assignment 7

def makeNumberPyramid (rows):
    variable = str()
    for i in range(1, rows+1):
        rowString = str()
        for j in range(0, i+1):
            if j>0:
                rowString = rowString + " " + str(i)
                print(rowString, end= "")
            else:
                rowString = str(i)
                print(rowString)
                
rows = int(input("Enter the number of rows: "))
makeNumberPyramid(rows)
