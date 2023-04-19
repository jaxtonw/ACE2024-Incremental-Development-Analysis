# @@@@@@@@@@@@@
# CS1400 - MW1
# Assignment 6

from random import seed
from random import randint
from time import time
from math import sqrt

timeStart = time()
loopCounter = 0
numberCounter = 0

for number in range(1, 10001):
    loopCounter += 1
    factorSum = 1
    if number % 2 == 0:
        for i in range(2, round(sqrt(number)) + 1):
            loopCounter += 1
            if number % i == 0:
                factorSum += i
                if i != number/i:
                    factorSum += (number / i)
    else:
        for i in range(3, round(sqrt(number)) + 1, 2):
            loopCounter += 1
            if number % i == 0:
                factorSum += i
                if i != number / i:
                    factorSum += (number / i)
    seed(factorSum)
    if number == randint(0, number):
        print("Fluky Number : " + str(number))
        numberCounter += 1
    if numberCounter == 7:
        break
totalTime = time() - timeStart
roundedTime = round(totalTime, 2)
print("Total Time : " + str(roundedTime) + " seconds")
print("Total loops : " + str(loopCounter))

