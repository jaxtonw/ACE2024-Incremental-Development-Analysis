# @@@@@@@@@@@@@@
# CS1400 - 001
# Assignment 7 task 1

def main():
    rowNum = eval(input("Enter the number of rows: "))
    makeNumberPyramid(rowNum)
    return len(str(rowNum))
    
def makeNumberPyramid(rowNum):
    pyramid = ""
    for i in range(rowNum + 1):
        val = ""
        for j in range(0, rowNum):
            " "
            val += str(rowNum)
        #pyramid += 1
        pyramid += "\n"
    return pyramid
            
            
main()

