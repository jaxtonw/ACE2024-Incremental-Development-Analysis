# @@@@@@@@@@@@
# CS1400 - MW1 (14 week)
# Assignment 12

play = True
uList = []
uSum = 0

while play == True:
    uInput = input("Enter a number, or just hit enter to compute: ").strip()
    
    if uInput == "":
        play = False
    else:
        uList.append(uInput)

uLen = str(len(uList))
print("Number of Values: " + uLen)
for i in range(-1, len(uList)):
    if i == -1:
        uMax = uList[0]
    elif uMax < uList[i]:
        uMax = uList[i]
print("The Max: " + str(uMax))
uMin = min(uList)
print("The Min: " + str(uMin))
for i in uList:
    uSum += int(i)
print("Sum of all values: " + str(uSum))
uAvg = int(uSum)/int(uLen)
print("The average Value: " + str(int(uAvg)))
