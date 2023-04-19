# @@@@@@@@@@@  
# CS 1400 - MW1 XL
# Assignment 006

from random import seed
from random import randint
import time

start = int(time.time_ns())
# setting up the variables that will be used in the fluky checking process
factor = 1
factor2 = 2
seedNumber = 0
loop = 0
totalFluky = 0

# for loop setting the range for the fluky test
for fluky in range(1, 10000):
    # this while loop determines the factors of the potential fluky number
    # the + 1 at the end of factor makes the program only check factors less than itself
    while factor + 1 < fluky:
        if fluky % factor == 0 and factor2 > factor:
            factor2 = fluky/factor
            if factor2 == fluky or factor2 == factor:
                seedNumber += factor
            else:
                seedNumber += factor
                seedNumber += factor2
            loop += 1
            factor += 1
        elif factor2 > factor:
            factor += 1
            loop += 1
        else:
            factor = fluky-1
            loop += 1
            
    # coming up with the "random" number called check which will 
    seed(seedNumber)
    check = randint(0, fluky)
    
    # now the random number is chosen and checked to see if it is the same as the fluky number
    # also checks to see that fluky is not = 1
    if check == fluky and not fluky == factor:
        print("fluky number: " + str(fluky))
        totalFluky += 1
    if totalFluky == 7:
        break
    factor = 1
    seedNumber = 0
    loop += 1
end = int(time.time_ns())
totalTime = (end - start)/(10 ** 9)
totalTime = format(totalTime, ".2f")
print("Run Time: " + str(totalTime))
print("total loops: " + str(loop))

