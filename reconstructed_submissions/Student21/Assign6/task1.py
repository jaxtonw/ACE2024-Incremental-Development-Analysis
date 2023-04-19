# @@@@@@@@@@@@@@@@
# CECS1400 - MW1
# Assignment 6-Task 1

# import random module and time module
import random
import time

# find fluky numbers from 1 to 10000
loopCount = 0
startTime = time.time()
flukyCount = 0
for possibleFlukyNum in range(1, 10000 + 1):
    sum = 0
    for possibleFactor in range(1, possibleFlukyNum):
        loopCount += 1
        if possibleFlukyNum % possibleFactor == 0:    
            sum += possibleFactor
    if sum <= 0:
        continue   

    random.seed(sum)
    randomValue = random.randint(0, possibleFlukyNum)
    if randomValue == possibleFlukyNum:
        print("Found Fluky Number: " + str(possibleFlukyNum))
        flukyCount += 1
    
    if flukyCount >= 7:
        break
endTime = time.time()

print("Total time: " + str(round((endTime - startTime), 2)))
print("Total Loops: " + str(loopCount))

