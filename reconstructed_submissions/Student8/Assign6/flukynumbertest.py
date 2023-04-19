# @@@@@@@@@@@@@
# CS1400 - MW1
# Assignment ???
import random

theNumber = 1895
total = 0
for i in range(1, ((theNumber // 2) + 1)):

    # when the remainder is 0 and number is a factor and should be added to sum variable
    if i == theNumber:
        continue
    elif (theNumber % i) == 0:
        total += i

random.seed(total)
print(random.randint(0, theNumber))

