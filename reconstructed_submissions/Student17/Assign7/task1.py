def makeNumberPyramid (numOfRows):
    msg = ""
    row = ""
    #this will center the pyramid
    if numOfRows < 10:
        bottomlength = (2 * numOfRows) -1
    elif 10 <= numOfRows < 100:
        bottomlength = (3 * numOfRows) - 1
    elif 100 <= numOfRows < 1000:
        bottomlength = (4 * numOfRows) - 1
    #This will make the pyramid
    for i in range(0, numOfRows + 1):
        for j in range(i):
            if len(row) != 0:
                row += " "
            row += str(i)
        msg += format(row, "^" + str(bottomlength))
        msg += "\n"
        row = ""
    return msg        
        
def main():
    numOfRows = eval(input("how many rows will this pyramid have?" ))
    pyramid = makeNumberPyramid(numOfRows)
    print(pyramid)
    
main()
