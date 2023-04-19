#J@@@@a @@@@@@
#CS 1400
#Assignment 7


#Parameter for number of rows
rows=eval(input("Enter the number of rows: "))
#main function named makeNumberPyramid like in the system design
def makeNumberPyramid(rows):
    #n is a counter for how many times to print a number on each row
    n = 0
    #if rows are less than 10, adjustments will not be made
    if rows < 10 :
        for i in range(1, rows + 1):
            for j in range(1, rows + 1):
                print(" " * (rows - 1), end="")
                rows = rows - 1
                n += 1
                for j in range(1, n + 1):
                    print(n, "", end="")
                print()
    #if rows are greater than 10, 6 spaces will be added to values under 10 to adjust for double digits    
    if rows >= 10 :            
        for i in range(1, rows+1):
            if i<10:
                print(" "*(rows-1),"","","","","","", end="")
                rows = rows - 1
                n += 1
                for j in range(1, n+1):
                    print(n,"",  end="")
                print()
        )   if i>=10:
                print(" "*(rows-1), end="")
                rows = rows - 1
                n += 1
                for j in range(1, n+1):
                    print(n,"", end="")
                print()           


output=makeNumberPyramid(rows)
