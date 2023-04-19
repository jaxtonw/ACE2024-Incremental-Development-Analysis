# @@@@@@@@@@
# CS1400 - 14 week
# Assignment 6 - task 1

# import modules
from random import randint
from random import seed
import time
from math import sqrt

# set starting values
start = time.time()
totalLoops = 0
totalFluky = 0

# find and print fluky numbers
for number in range(1, 10000):
    total = 0
    topFactor = int(sqrt(number) + 1)
    for factor in range(1, topFactor):
        if number % factor == 0:
            total += factor
            other = number / factor
            if other != factor and other != number:
                total += other
        totalLoops += 1
    seed(total)
    randomNumber = randint(0, number)
    if randomNumber == number and total != 0:
        print("Fluky Number: " + str(number))
        totalFluky += 1
    if totalFluky == 7:
        break

# final calculations and output for time and loops
end = time.time()
totalTime = round(end - start, 2)
print("Total Time: " + str(totalTime) + " seconds")
print("Total Loops: " + str(totalLoops))

