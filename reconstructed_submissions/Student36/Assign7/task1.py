# @@@@@@@@@@@@@@@
# CS 1400-14 week
# Assignment 7


#fucktion
#parameter for number of rows
def makeNumberPyramid(number):
    pyramid = ""

    for i in range(0,number + 1):
        numberInRow = ""
        coolSpace = ""
        for j in range(0, i):
            if j == 0:
                numberInRow += str(i)
            else:
                numberInRow += " " + str(i)
        if number <= 9:
            numberSpacing = ((2 * number) - 1 - len(numberInRow)) // 2
        else:
            numberSpacing = ((3 * number) - 1 - len(numberInRow)) // 2
        for b in range(0,numberSpacing):
            coolSpace += " "
        pyramid += coolSpace + numberInRow + "\n"
    return pyramid




def main():
    numberOfRows = input("Input the number of rows: ")
    print(makeNumberPyramid(int(numberOfRows)))
    





main()
