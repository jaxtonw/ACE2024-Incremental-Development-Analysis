# @@@@@@@@@@@@@@
# CS1400 - 001
# Assignment 6 task 1

from random import seed
from random import randint
from time import time

# start timer 
startTime = time()

# Start counting number of loops
numOfLoops = 0

# loop to go through numbers from 1 - 10000
for num in range(1, 10000 + 1):
    # start adding the factors to find the sum
    sum = 0
    # this loop finds the factors
    for i in range(1, num):
        if num % i == 0:
            factor = i
            sum += factor
        numOfLoops += 1
    seed(sum)
    
    # determine if a number is fluky or not
    if randint(0, num) == num:
        if num == 1:
            print(" ")
        else:
            print("Fluky Number: " + str(num))
    
# end the timer
endTime = time()  

# calculate the time it took
totalTime = endTime - startTime

# print the time in seconds
print("Total Time: " + str(format(totalTime, "2.2f")) + " seconds ")

# print number of loop iterations
print("Total Loops: " + str(numOfLoops))
    
