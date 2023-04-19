rowCount = 10
msg = ""

for rowNum in range(1, int(rowCount) + 1):
    rowText = str(rowNum)
    for i in range(2, rowNum + 1):
        numSpace = len(str(rowNum))
        totalWidth = 2 * numSpace * rowNum
        if i != rowNum + 1:
            rowText += " "
        rowText += format(str(rowNum), "^" + str((totalWidth/2 - i) + "s"))
    msg += rowText + "\n"
    

print(msg)
