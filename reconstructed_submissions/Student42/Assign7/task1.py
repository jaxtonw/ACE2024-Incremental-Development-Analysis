# @@@@@@@@@@@@@
# CS1400 - 14week
# Assignment 7

def row_number(num):
    count = 0
    val = 1
    while count < num:
        print(val)
        val += 1
        count += 1


row_number(eval(input("Enter number of rows: ")))

