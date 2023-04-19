# @@@@@@@@@@@@@@@
# CS 1400- 14 week
# Assignment 6

#import statements
from random import seed
from random import randint
from time import time

#start time
start = time()
#variables
theNumber = 0

count = 0
flukyLoops = 0


#number increment
for theNumber in range(1, 10001):
    sumFactor = 0
    divisor = 1
    
    while divisor < (theNumber / 2) + 1 and flukyLoops < 7:
        #factoring
        mod = theNumber % divisor

        #adding factors  
        if mod == 0:
            factors = divisor
            sumFactor += factors

        divisor += 1
        count += 1
    #fluky check
    if sumFactor > 1:
        seed(sumFactor)
        randi = randint(0,theNumber)
        if randi == theNumber:
            fluky = theNumber
            
            print("Fluky Number: " + str(fluky))
            
            flukyLoops += 1

   
print("Total loops: " + str(count))
end = time()
print("Total time: " + str(round(end - start, 2)))

