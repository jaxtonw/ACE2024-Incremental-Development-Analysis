# @@@@@@@@@@@@
# CS1400 - 007
# Assignment 07

#Create pyramid function
def makeNumberPyramid(rows):
    lengthRows = (len(str(rows)) + 1) * ((rows) - 1) + len(str(rows))
    msg = ""
    for i in range(0, rows + 1):
        rowText = ""
        for j in range(0, i + 1):
            if j == 0:
                continue
            if j > 1:
                rowText += " "
            rowText += str(i)
        msg += format(rowText, "^" + str(lengthRows) + "s") + "\n"
    return msg
        
#Main function
def main():
    rows = eval(input("Enter the number of rows: "))
    answer = makeNumberPyramid(rows)
    print(answer)

main()
    
