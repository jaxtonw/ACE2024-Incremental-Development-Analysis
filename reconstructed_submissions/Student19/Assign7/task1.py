# @@@@@@@@@@@@
# CS1400 - MW1 (14 week)
# Assignment 6?

def makeNumberPyramid(rows):
    final = ""
    for i in range(0, rows+1):
        row = ""
        for j in range(0, i):
            if j != 0:
                row += " "
            row += str(i)
        row = format(row, "^" + str(len(str(rows) + " ") * rows))
        final += row + "\n"
    return final


def main():
    userInput = input("Number of rows to print? : ")
    result = makeNumberPyramid(int(userInput))
    print(result)


main()
?

