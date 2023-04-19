# @@@@@@@@@@@
# CS1400 - 007
# Assignment 06
import random
import time

#measuring time 
start = time.time()
#define variables
val = 0
n = 2
#set while statement
#nested loop
while True:
    #import liberies
    from math import sqrt
    val += 1
    sum = 0 
    #set for loop and calculate the sqrt of the integer of n + 1 with the range from 1
    #set the fluky number for loop.
    for i in range(1, int(sqrt(n)) + 1):
        #define value to set posibilities
        val += 1
        if i == 1:
            continue
        if n % i == 0:
            if n // i == i:
                random.seed(i)
                sum += random.randint(1, n)
            else:
                #First seed
                random.seed(i)
                sum += random.randint(1, n)
                #Second seed of  number 
                random.seed(n // i)
                sum += random.randint(1, n)
    random.seed(1)
    sum += random.randint(1, n)
    if sum == n:
        #print out the fluky number
        print("Fluky Number: ", n)
    n += 1
    if n > 10000:
        break
#set finial definitions
end = time.time()
totalTime = end - start
#print statments
print("Total Time: ", round(totalTime, 2), "seconds")
print("Total Loops: ", val)
