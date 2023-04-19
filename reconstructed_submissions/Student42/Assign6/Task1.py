# @@@@@@@@@@@@@
# CS1400 - 14 week
# Assignment 6

import random
from random import randint
import time

start_time = time.time()

msg = 0
val = 1
loopCount = 0
while val < 10000:
    if val == 1:
        val += 1
    count = 2
    seed = 0
    while count <= val:
        mod = val % count
        if mod == 0:
            seed += val / count
        count += 1
    random.seed(seed)
    seedVal = randint(0, val)
    if seedVal == val:
        print("Fluky Number: " + str(val))
    val += 1
    loopCount += 1
    if seedVal == 1895:
        break
print("Total Time: " + str(round(time.time() - start_time, 2)) + " seconds")
print("Total Loops: " + str(loopCount))

