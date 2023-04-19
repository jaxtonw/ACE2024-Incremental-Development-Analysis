# @@@@@@@@@@@@
# CS1400 - 006
# Assignment 06

from random import seed
from random import randint
import time
import math
#Start time
startTime = time.time()

#set variables to gather total innerloops, flukynumber counter
totalLoop = 0
flukyNumberCount = 0

#find factors for all numbers
for i in range(1, 10001):
    sumFactors = 0
    if flukyNumberCount == 7:
        break
    for j in range(1, (i // 2) + 1):
        totalLoop += 1
        if i % j == 0 and i != j:
            sumFactors += j
    seed(sumFactors)

#find fluky numbers and stop when 7 are found
    if randint(0, i) == i and i != 1:
        print("Fluky Numbers: " + str(i))
        flukyNumberCount += 1
        
#find and print total seconds
endTime = time.time()
totalSeconds = format((endTime - startTime), ".2f")

print("Total time: " + totalSeconds + " seconds")

#total loops
print("Total Loops: " + str(totalLoop))

