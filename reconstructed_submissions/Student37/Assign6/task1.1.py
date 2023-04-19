# @@@@@@@@@
# CS1400 - MW1
# Assignment 6 - task 1.1

import time
from random import seed
from random import randint

# timer
time1 = time.time()

# find all the factors
count = 1
total = 0

while count <= 10000:

    factor = 1
    sqrt = count ** .5

    for i in range(1, (count // 2) + 1):
        for j in range(1, i):

            if i == sqrt:
                factor += i
                i += 1
                total += 1
            elif i * j == count:
                factor += i
                factor += j
                total += 1

    seed(factor)  # generate random number using sum as the seed
    rNumber = randint(0, count)

    if count == rNumber and count - 1 != factor:  # test if random number and initial number are the same
        print("Fluky Number: " + str(count))  # if they are the same, print the number
    count += 1
    total += 1

time2 = time.time()
totalTime = time2 - time1  # total time equation

print("Total time: " + str(totalTime))
print("Total loops: " + str(total))

