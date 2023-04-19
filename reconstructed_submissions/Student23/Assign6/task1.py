# @@@@@@@@@@@@@@
# CS1400 - 001
# Assignment 6

import random
import time
from math import sqrt

# Start time and define variables
startTime = time.time()
loopCount = 0
numberofFluky = 0
TheNumber = 0

# Loop through numbers
while numberofFluky < 7:
    TheNumber += 1
    seed = 0
    # Find Factors (Inner loop)
    for i in range(1, int(sqrt(TheNumber) + 1)):
        if TheNumber % i == 0:
            seed += i
            # Include partner factor and except if one or perfect squares 
            if i > 1 and i < sqrt(TheNumber):
                seed += (TheNumber / i)
        loopCount += 1
    # Set seed, calculate random number, check if fluky
    random.seed(seed)
    if random.randint(0, TheNumber) == TheNumber and seed > 0:
        numberofFluky += 1
        print("Fluky Number: " + str(TheNumber))
# Calculate total time
endTime = time.time()
totalTime = round(endTime - startTime, 2)
print("Total time: " + str(format(totalTime, ".2f")) + " seconds")

# Print loop count
print("Total loops: " + str(loopCount))

