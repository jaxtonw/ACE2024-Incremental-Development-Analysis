# @@@@@@@@@@@@
# CS1400 - MW 1
# Assignment 6

import time
import random

# setting iteration count and time start
i = 1
totalIterations = 0
startTime = time.time()
flukeNum = 0
# while loop to go through all numbers 1 to 10000
while i < 10000:
    seedNum = 0
    
    # if we found 7 fluky numbers stop the loop 
    if flukeNum == 7:
        break
        
    # finding seed numbers 
    for j in range(1, i):
        totalIterations += 1
        # break the loop if tis trying to find factors in numbers greater than half the number
        if j > (.5 * i):
            break
        # finding factors of i
        testingNum = i % j
        
        if testingNum == 0:
            seedNum += j
        
    random.seed(seedNum)
    
    # generate random number from seed
    if i == random.randint(0, i) and i != 1:
        print("Fluky Number: " + str(i))
        flukeNum += 1 
    
    i += 1
    
# calculate total time elapsed
endTime = time.time()
finalTime = endTime - startTime
finalTime = round(finalTime, 2)

# time print statement
print("Total Time: " + str(finalTime))

# total iterations statement
print("Total Iterations: " + str(totalIterations))
    
            

        

