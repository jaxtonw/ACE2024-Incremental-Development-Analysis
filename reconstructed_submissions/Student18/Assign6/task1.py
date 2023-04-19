# @@@@@@@@@@@
# CS 1400 - A01 XL
# Assignment 6

from random import seed
from random import randint
import time

startTime = time.time()
numberOfFluky = 0
loopCounter = 0 
msg = ""
for i in range(1,10000): 
    sumOfRandomNumber = 0 
    for j in range(1, i): 
        loopCounter += 1
        if i % j == 0: 
            seed(j)
            sumOfRandomNumber += randint(1,i)
        if j > i/2: 
            break
        if sumOfRandomNumber > i: 
            break
    if sumOfRandomNumber == i:
        numberOfFluky += 1 
        msg += "Fluky Number: "
        msg += str(i) + "\n"
        
    if numberOfFluky == 7: 
        break 
endTime = time.time() 
totalTime = endTime - startTime
msg += "Total Time: " + str(round(totalTime,2)) + "\n"
msg += "Total Loops: " + str(loopCounter)
print(msg)

    
        



