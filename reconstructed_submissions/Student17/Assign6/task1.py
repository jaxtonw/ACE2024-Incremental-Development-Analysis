#@@@@@@@@@@@@@@ CS1400 14Week
#import needed modules
from random import randint
from random import seed
from time import time
#set variables to start
startingTime = time()
val1 = 1
flukyNumber = 0
iterations = 0
#loop through to find the fluky numbers
while val1 <= 10000:
    factorsSummed = 0
    allFactors = 1
    while allFactors <= (val1 / 2):
        factors = False
        if val1 == allFactors:
            factors = False
        elif val1 % allFactors == 0:
            factors = True
        if factors:
            factorsSummed += allFactors
            allFactors += 1
        else:
            allFactors += 1
            iterations += 1
    if factorsSummed > 0:
        seed(factorsSummed)
        randomNum = randint(0, val1)
        if randomNum == val1:
            print("Fluky Number: " + str(val1))
            flukyNumber += 1
            if flukyNumber == 7:
                break
    val1 += 1
    #print final message
endingTime = time()
totalTime = round(endingTime - startingTime, 2)
print("Total time: " + str(totalTime) + " seconds")
print("Total loops: " + str(iterations))
