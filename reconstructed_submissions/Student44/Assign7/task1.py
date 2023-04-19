# @@@@@@@@@@@@
# CS1400 - MW 1
# Assignment 7

# create function with row num formal parameter
def makeNumberPyramid(rowNum):
   
    # create an empty string function
    msg = ""
    
    # calculate the number of spaces required to print pyramid
    rowNum = eval(rowNum)
    numSpace = len(str(rowNum)) * rowNum
    spacesSpace = rowNum - 1
    totalSpace = spacesSpace + numSpace
    
    # loop through to the row number input by user
    for i in range(1, rowNum + 1):
        strrow = ""
        
        # loop from 0 to current number
        for j in range(0, i):
            
            # conditional to add space
            if j >= 1:
                strrow += " "
            strrow += str(i)
        # format string
        msg += format(strrow, "^" + str(totalSpace))
        msg += "\n"
    
    return msg


def main():
    # get input 
    rowNum = input("How many rows do you want to print? ")
    
    msg = makeNumberPyramid(rowNum)
    
    # return the printed version of msg
    return print(msg)


main()



