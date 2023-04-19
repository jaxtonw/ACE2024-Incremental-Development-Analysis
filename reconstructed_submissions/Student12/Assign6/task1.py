# @@@@@@@@@@@@
# CS1400 - 14 Week
# Assignment 6

# modules
from random import seed
from random import randint
from time import time
# introduce variables to use later (scope)
# start time
t = time
# i = iterations
i = 0
var = 0
# loops
for count in range(1, 10001):
    val = 0
    for num in range(1, count + 1):
        i += 1
        if count % num == 0:
            val += num
        else:
            continue
    total = val - count
    seed(total)
# print out each fluky number - loop through
    if total > 1 and (randint(0, count)) == count:
        print("Fluky Number: " + str(count))
        var += 1
    elif total < 1:
        continue
    elif var == 7:
        break
    elif i == 10000000:
        break
# final statements - totals
print("Total Time: " + str(round(t(), 2)) + " seconds")
print("Total Loops: " + str(i))
# didn't know how to reduce the loops down even more

