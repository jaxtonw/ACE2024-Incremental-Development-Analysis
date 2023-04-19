# @@@@@@@@@@@@@@@@@@
# CS1400 - 001
# Assignment 7


def makeNumberPyramid(inputFromUser):
    entirePyramid = ""    
    for row in range(0, inputFromUser + 1):
        rowText = ""
        maxWidth = ((len(str(inputFromUser)) + 1 ) * inputFromUser) - 1
        spacingWithinRow = len(str(row)) * row + row - 1
        spacing = (maxWidth - spacingWithinRow) // 2
        
        for row3 in range(0, spacing):
            rowText += " "
            
        for printingRowText in range(0, row):
            rowText += str(row) + " "
            
        
        entirePyramid += rowText + "\n"    
    
    return entirePyramid           
            
            
def main():
    inputMain = eval(input("Enter number of rows to print: "))
    printThis = makeNumberPyramid(inputMain)
    print(printThis)

main()



