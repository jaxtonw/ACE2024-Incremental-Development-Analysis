# @@@@@@@@@@@@@
# CS1400 - MW1
# Assignment ??

print("Welcome to the Amazing Multiplication Table Calculator")

# Get input
begNum = eval(input("Enter the beginning number: "))
endNum = eval(input("Enter the ending number: "))
step = eval(input("Enter the step size: "))

# Calculate spacing
numSpace = len(str(endNum ** 2)) + 2
rowHeadSpace = len(str(endNum)) + 2
totalWidth = rowHeadSpace + numSpace * ((endNum - begNum) // step + 1)

# Create message string
msg = ""

msg += format("Multiplication Table", "^" + str(totalWidth) + "s")
msg += "\n\n"

# Create column header
msg += format("", str(rowHeadSpace) + "s")
for i in range(begNum, endNum + 1, step):
    msg += format(i, ">" + str(numSpace) + "d")
msg += "\n"

# Create dashed line
for i in range(0, totalWidth):
    msg += "-"
msg += "\n"

# create each row
for i in range(begNum, endNum + 1, step):
    msg += format(str(i) + " |", ">" + str(rowHeadSpace) + "s")
    for j in range(begNum, endNum + 1, step):
        msg += format(i * j, ">" + str(numSpace) + "d")
    msg += "\n"

# print output
print(msg)


