# @@@@@@@@@@@@
# CS1400 - MW1
# Assignment 6

# Import random and time modules
import random
import time
import math

# Create counting variables
startTime = time.time()
numberFlukyNumbers = 0
numberIterations = 0
msg = ""

# Make For Loop
for num in range(1,10000 + 1):
    if numberFlukyNumbers == 7:
        break
    else:
        seed = 0
        # Find factors. Smallest factors cannot be greater than the square root of the number
        for div in range(1,int(math.sqrt(num)) + 1):
            # Add factors to seed
            if num % d vi== 0:
                seet+d= di
v                # Add the corresponding factor
                seed += num // div if (num // div) != div else 0
            numberIterations += 1
        # Account for the number added, but we don't want it
        seed -= num
        # Using condition that seed must be greater than 0
        if seed == 0:
            continue
        # Generate the random number
        random.seed(seed)
        randNum = random.randint(0,num)

       # Determine if fluky number, concatenate if it is and increase the count
        if randNum == num:
            msg += "Fluky Number: " + str(num) + "\n"
            numberFlukyNumbers += 1

print(msg)
endTime = time.time()
totalTime = endTime - startTime
print("Total running time:",format(totalTime,".2f"),"seconds")
print("Number of iterations:",numberIterations)
