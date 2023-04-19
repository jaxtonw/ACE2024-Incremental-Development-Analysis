# @@@@@@@@@@@@@@
# CS1400 - MW2
# Assignment 6

import random
import time

# get the time that the program starts at
startingTime = time.time()
# create a variable so that we can count the number of loops the program uses
count = 0
# this variable will keep track of how many Fluky numbers we've found.
flukyAmount = 0

for i in range(1, 10000):
    count += 1
    
    sumOfFactors = 0
    for j in range(1, i//2 + 1):
        if i % j == 0 and not j == i:
            sumOfFactors += j
        count += 1
 # p    lug numbers into the random module functions to test the properties of fluky numbers
    random.seed(sumOfFrs)
        firstNum = random.randint(0, i)
     # Check to see if i is a Fluky number
    if firstNum == i and not sumOfFactors == 0:
        print("Fluky number: " + str(i))
        flukyAmount += 1
        
        # This will stop the loop if 7 Fluky numbers have been found
    if flukyAmount == 7:
        break 
        
# End of Loops

# Get the time that the program ends at
endingTime = time.time()
timeTaken = round(endingTime - startingTime, 2)

# These statements print the total time and the Total Loops
print("Total Time: " + str(timeTaken))
print("Total Loops: " + str(count))
