# @@@@@@@@@@@@@@
# CS 1400 - 14 week
# Assignment 6

# import random module
from random import seed
from random import randint
import time


# get current time, save as time1
start = time.time()

# create variables for flukyCount, loopCount; assign 0 to all
flukyCount = loopCount = 0

# create for loop of num in range(10000)
for num in range(1, 10001):
    sumFactors = 0

# for loop to find factors of num
    for i in range(1, int((num / 2) + 1)):
        # loopCount += 1
        if num % i == 0:
            # continue

# save and add factors as sumFactors
            sumFactors += i
        # print(loopCount)    
        loopCount += 1
         
    if sumFactors == 0:
        continue

# find 1st generated randint of for seed value sumFactors
    elif sumFactors < 0:
        continue
    else:
        seed(sumFactors)
        randomNum = randint(0, num)
    
# if statement to check if num is fluky
    if num == randomNum:
        print("Fluky Number: " + str(randomNum))
        flukyCount += 1
        
        if flukyCount == 7:
            break
    else:
        continue

# print total time and total loops
end = time.time()
time = end - start
time = format(time, ".2f")
print("Total Time: " + str(time) + " seconds")
print("Total Loops: " + str(loopCount))
