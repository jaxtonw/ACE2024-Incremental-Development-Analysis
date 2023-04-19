# @@@@@@@@@@@@@@@@
# CS1400 - 14 Week
# Assignment 006
import random
import time

loops = 0
# time variable assignment 
startTime = time.time()

# begin fluky number testing
numFlukyFinder = 0
for possibleFluky in range(1, 10001):
    loops += 1
    sum = 0
    upperBound = possibleFluky
    # factor number
    innerLoop = 0
    for possibleFactor in range(1, possibleFluky+1):
        loops += 1
        innerLoop += 1
        if possibleFactor >= int(possibleFluky / 2):
            break
        if upperBound <= possibleFactor:
            break
        if possibleFluky % possibleFactor == 0:
            if possibleFactor == 1:
                sum = 1
            elif possibleFactor == possibleFluky / possibleFactor:
                sum += possibleFactor
                break
            else:
                sum = sum + possibleFactor + possibleFluky / possibleFactor
            upperBound = possibleFluky/possibleFactor
        # end if possibleFluky % possibleFactor == 0:
    # end for possibleFactor in range(1, possibleFluky):
    
    if sum == 0:
        continue
        
    # check for seed
    random.seed(sum)
    randomNumber = random.randint(0, possibleFluky)
    if randomNumber == possibleFluky:
        numFlukyFinder += 1
        print("Fluky Number: " + str(possibleFluky))
    if numFlukyFinder == 7:
        break
# end for possibleFluky in range(1, 10001):

endTime = time.time()
timeElapsed = endTime - startTime
print("Total Time:  " + str(round(timeElapsed, 2)))
print("Total Loops: " + str(loops))
