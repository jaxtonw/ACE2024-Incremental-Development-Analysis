# @@@@@@@@@@@
# CS1400 - MW1 XL
# Assignment 6 - Task 1

from random import seed
from random import randint

import time
start = time.time()

loopNum = 0
fluky = 0

while fluky < 7:
    for i in range(1, 10001):
        sumFactors = 1
        for j in range(2, 10000):
            if i % j == 0 and i / j != 1:
                sumFactors = sumFactors + j
                loopNum = loopNum + 1
        if sumFactors != 1:
            seed(sumFactors)
            testNum = randint(0, i)
            if testNum == i:
                print("Fluky Number: " + str(testNum))
                fluky = fluky + 1
                if fluky == 7:
                    break

end = time.time()
totalTime = round(end - start, 2)
print("Total time: ", totalTime, " seconds")
print("Total number of loops: ", loopNum)


print("Total number of loops: ", loopNum)



