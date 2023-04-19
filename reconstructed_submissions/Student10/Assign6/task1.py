# @@@@@@@@@@
# CS 1400 - 14 week
# Assignment 6

from random import seed
from random import randint
from time import time

#initial values
begTime = time()
totalLoops = 0
totalFlukyNums = 0

#fluky numbers loop
for i in range(1, 10001):
    sum = 0
    #find factors of i
    for j in range(1, i + 1):
        totalLoops += 1
        if i % j == 0 and i / j != i:
            sum += int(i / j)
    #seed and find random int
    if sum != 0:
        seed(sum)
        num = randint(0, i)
        #print fluky numbers
        if num == i:
            totalFlukyNums += 1
            print("Fluky Number: " + str(num))
    #stop once we have all 7
    if totalFlukyNums == 7:
        break

#total time and loops
endTime = time()
print("Total Time: " + format(endTime - begTime, ".2f") + " seconds")
print("Total Loops: " + str(totalLoops))

