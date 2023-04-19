# @@@@@@@@@@@@@
# CS1400 - M01
# Assignment 6

import time
from random import seed
from random import randint

# Start the counters
count = 0
count1 = 0

# Start the time
time1 = time.time()

# First loop to start The Numbers
for number in range(1, 10001):
    sumOfFactors = 0
    count1 += 1
    
# Nested loop to find and add the factors of The Numbers
    for factor in range(1, number-1):
        if number % factor == 0:
            sumOfFactors += factor
    count += 1

# Finding the seed
    if sumOfFactors <= 0:
        continue
    else:
        seed(sumOfFactors)

    # Stopping the loop
    if count1 > 1895:
        break
        
# Matching the seed to The Number
    random1 = randint(0, number)
    if random1 == number:
        print("Fluky Number: " + str(random1))
        
# Time Stuff
time2 = time.time()
totalTime = time2 - time1
totalTime1 = format(totalTime, "<1.2")
print("Total Time: " + str(totalTime1) + " seconds")
print("Number of loops: " + str(count)) 

