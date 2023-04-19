# @@@@@@@@@@@@
# CS1400 - MW1 (14 week)
# Assignment 6

import random
import time
print(2 % 2)

oldFactor = 0
theNumber = 0
#factorList = [1]
fNum = 0
allFactors = 1
loopCount = 0
timeInit = time.time()

for i in range(1, 10001):
    loopCount += 1
    for i1 in range(3, int(i/2+1)):
        loopCount += 1
        if i % i1 == 0:
            #factorList.append(i1)
            allFactors += i1
            

    #for f in factorList:
        #loopCount += 1
        #allFactors += f
    random.seed(allFactors)
    
    theNumber = random.randint(0, i)
    if theNumber == i:
        print("Fluky Number: " + str(i))
        fNum += 1
    
    # exits loop when all seven are discovered
    if fNum >= 7:
        break
    #resers things
    oldFactor = 0
    if i % 2 == 1:
        allFactors = 3
    else:
        allFactors = 1

timeEnd = time.time()
timeT = timeEnd - timeInit
timeTP = (round(timeT, 2))

print("Total Time: " + str(timeTP))
print("Total Loops: " + str(loopCount))

