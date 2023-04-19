# @@@@@@@@@@@@
# CS-1400-AO1-XL
# Assignment 6

import time
import math
from random import seed
from random import randint

start = time.time()

Number = randint(0, 10000)

notPrime = False

count = 0
sum = 0
loops = 0

while not notPrime:
    for count in range(2, int(math.sqrt(Number)) + 1):
        loops += 1
        if Number % count == 0:
            sum += count
            seed(sum)
    if sum == Number:
        print("Fluky Number: " + str(Number))
    if Number > 10000:
        break

end = time.time()
time = "{:.2f}".format(start - end)
print("Total Time: " + time + " seconds")
print("Total Loops: " + str(loops))

