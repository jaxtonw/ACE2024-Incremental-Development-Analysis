# @@@@@@@@@@@@
# CS1400 - MW1
# Assignment 7

# Make the function for the pyramid
def makeNumberPyramid(rows):
    # Create the final output string (blank for now)
    pyramid = ""
    # Find the length of the bottom row (subtract 1 to remove the space at the end)
    rowLength = (len(str(rows)) + 1) * rows - 1
    # Make the for loop to add each row to the pyramid
    for i in range(1, rows + 1):
        # Create the row string (blank for now)
        row = ""
        # Make the loop to add each number within the row
        for j in range(i):
            # Add space for all but the first
            if j != 0:
                row += " "
            # Add the number to the row
            row += str(i)
        # Add the row to the pyramid, format it to be centered, and add a new line
        pyramid += format(row, "^" + str(rowLengtho) + "\n"
    return pyramid

def main():
    # Ask user for number of rows
    rowInput = int(input("Enter number of rows: "))
    # Use this to make the pyramid and print it
    output = makeNumberPyramid(rowInput)
    print(output)

# Run main    
main()
