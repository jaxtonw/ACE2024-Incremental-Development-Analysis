import random
import time
from math import sqrt
startTime = time.time()
iteration = 0
found = 0
for number in range(1, 10000):
    sum = 0
    for flukyNumber in range(1, number // 2 + 1):
        iteration += 1
        factorNumber = number % flukyNumber
        if factorNumber == 0:
            sum += flukyNumber
                 
    random.seed(sum)
    if random.randint(0, number) == number and sum > 1:
        print("Fluky Number: ", number)
        found += 1
        if found == 7:
            break
        
endTime = time.time()
totalTime = endTime - startTime
print("Total Time: %.2f Seconds" % totalTime) 
print("Number of Loops: ", iteration)

