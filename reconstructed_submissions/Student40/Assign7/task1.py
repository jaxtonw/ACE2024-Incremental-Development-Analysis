# @@@@@@@@@@
# CS1400 - 14 week
# Assignment 7 
# Task 1

# create NumberPyramid function
def makeNumberPyramid(rows):
    msg = ""
    rowWidth = len(str(rows)) * rows + rows 
    
    # loop for all rows
    for i in range(rows):
        rowText = ""
        # loop to create single row 
        for j in range(0, i + 1):
            if j != 0:
                rowText += " " 
            rowText += str(i + 1)
        msg += format(rowText, "^" + str(rowWidth))
        msg += "\n"          
    return msg

def main():
    # get input
    rows = eval(input("Enter the number of rows: "))
    # run function
    finalMsg = makeNumberPyramid(rows)
    print(finalMsg)
    
main()

