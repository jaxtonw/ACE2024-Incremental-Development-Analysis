# @@@@@@@@@@@
# Assignment 6 Task 1
# CS 1400 14 Week

from random import randint
from random import seed
import time

# Function to sum factors of a number
def factorSum(num):
    sum = 0
    countFactor = 0
    for j in range(1, num):
        if num % j == 0:
            sum += j
        countFactor += 1
    return sum

# Start Time
startTime = time.time()

# Start a loops = 0

ount = 0

# Find flucky numbers
for i in range(1, 10001):
    if factorSum(i) > 0:
        seed(factorSum(i))
        if i == randint(0, i):
            print("Flucky Number: " + str(i))
    count += 1
            
# End Time
endTime = time.time()

# Amount of time passed
print("Total Time: " + str(round(endTime - startTime,2)) + " seconds")

# Number of Loops
print("Total Loops: " + str(count))
