# @@@@@@@@@@@@
# CS1400 - 14 week
# Assignment 7

# pyramid function
def makeNumberPyramid(numRows=9):
    msg = ""
    for curRow in range(0, numRows + 1):
        rowsTxt = ""
        for column in range(0, curRow):
            if column != 0:
                rowsTxt += " "
        # formatting - pyramid
            rowsTxt += str(numRows)
        rowWidth = len(str(curRow))
        msg += format(rowsTxt, "^5" + str(rowWidth))
        msg += "\n"
        
    return msg
  
# main function to call pyramid      
def main():
    rowsUser = eval(input("Enter the number of rows: "))
    print(makeNumberPyramid(rowsUser))
    
main()

