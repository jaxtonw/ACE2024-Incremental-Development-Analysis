# @@@@@@@@@@@@
# CS 1400 - 14 Weeks
# Assignment 6

import time
import random

startTime = time.time()

flukyCount = 0
loopCount = 0

for i in range(1, 10001):
    sumFactors = 0
    for j in range(1, (i // 2 + 1)):
        if i % j == 0:
            sumFactors += j
        loopCount += 1
    random.seed(sumFactors)
    randomNumber = random.randint(0, i)
    if randomNumber == i:
        print("Fluky Number: " + str(i))
        flukyCount += 1
    if flukyCount == 7:
        break

totalTime = round(time.time() - startTime, 2)

print("Total Time: " + str(totalTime) + " seconds")
print("Total Loops: " + str(loopCount))

