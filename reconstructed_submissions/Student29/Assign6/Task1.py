# @@@@@@@@@@@@@@
# CS1400 - MW1 XL
# Assignment #6

from random import seed
from random import randint
import time 

startTime = time.time()
totalLoops = 0
totalFlukyNumbers = 0
for theNumber in range(1, 10001):

    sum = 0
    for possibleFactor in range(1, int(theNumber ** 0.5) + 1):
        totalLoops += 1
        if theNumber % possibleFactor == 0:
            sum += possibleFactor
            
            if theNumber // possibleFactor == theNumber:
                sum += 0
                
            elif theNumber//possibleFactor == possibleFactor:
                sum += 0
                
            else:
                sum += theNumber // possibleFactor
           

    

    seedValue = sum 
    if seedValue <= 0:
        continue
    seed(seedValue)
    randomNumber = randint(0, theNumber)
    if theNumber == randomNumber:
        totalFlukyNumbers += 1
        print("Fluky Number: " + str(theNumber))
   
    if totalFlukyNumbers == 7:
        break
endTime = time.time() 
totalTime = (endTime - startTime)
print("Total Time: " + str(round(totalTime, 2)) + " seconds")
print("Total Loops: " + str(totalLoops))

