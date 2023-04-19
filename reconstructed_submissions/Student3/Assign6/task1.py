# @@@@@@@@@@@
# CS1400 - MW1
# Assignment 6

# import
from random import seed
from random import randint
from time import time

# take time
startTime = time()

loop = 0
factors = 0
count = 0
for i in range(1, 10001):
    for j in range(1, 10001):
        if i % j == 0:
            factors += j
            loop += 1
        if j == i:
            continue
    factors -= i
    seed(factors)
    if i == randint(0, i) and factors > 0:
        print("Fluky Number: " + str(i))
        count += 1
    if count == 7:
        break
        

# print totals
totalTime = round((time() - startTime), 2)
print("Total Time: " + str(totalTime) + " seconds")
print("Total Loops: " + str(loop)))

