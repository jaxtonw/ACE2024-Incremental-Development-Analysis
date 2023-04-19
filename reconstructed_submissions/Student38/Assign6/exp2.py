# @@@@@@@@@@@@@
# CS-1400 MW1
# Assignment ???
from random import seed
from random import randint
import time

msg = ""
totalLoops = 0
sum = 0

for j in range(1, 10000):
    #print("mod" + str(mod))
    topNum = j
    i = 1
    while i < topNum:
        topNum = j / i
        if j % i != 0:
            totalLoops += 1
        elif j % i == 0 and i != j:
            sum += i
            if topNum != i and topNum != j:
                sum += topNum
            totalLoops += 1
            # print(i)
        else:
            totalLoops += 1
        i += 1
    if sum != 0:
        # print("this is j" + str(j))
        # print("this is sum" + str(sum))
        seed(sum)
        randNum = randint(0, j)
        if randNum == j:
            msg += "Fluky Number: " + str(j)
            msg += "\n"
            # print(msg)
            sum = 0
        else:
            sum = 0
            continue

print(msg)
total = "Total number of loops: " + str(totalLoops)
print(total)

