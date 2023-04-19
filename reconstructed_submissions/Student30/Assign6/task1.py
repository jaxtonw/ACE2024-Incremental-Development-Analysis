# @@@@@@@@@@@@@@@@@@
# CS1400 - 001
# Assignment 6
import random
import time

beginTime = time.time()

loopCount = 0
flukyNumberPrints = 0

for k in range(1, 10001):
    seedNumber = 1
    if flukyNumberPrints >= 7:
        break
    for i in range(2, (k // 2) + 1):
        loopCount += 1
        if seedNumber >= 397:
            break
        if k % i == 0:
            seedNumber += i            
    random.seed(seedNumber)
    if k == random.randint(0, k):
        print("Fluky Number: " + str(k))
        flukyNumberPrints += 1
        if flukyNumberPrints >= 7:
            break
endTime = time.time()
runTime = round(endTime - beginTime, 2)
print("Total Time: " + str(runTime) + " seconds")
print("Total Loops: " + str(loopCount))



        
    
            
    
