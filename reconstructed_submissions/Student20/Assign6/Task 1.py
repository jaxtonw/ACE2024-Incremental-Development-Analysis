#@@@@@@@@@@@@@ 
#CS 1400 
# Assn6
import random
import time
#start value of n
n = 3
#count of iterations
iterations = 0
#start the timer
start = time.time()
while True:
    iterations += 1
    sum = 0
#start loop to factor from 1 to n
    for i in range(1, n):
#skip i == 1 because it only factors itself
        if i == 1:
            continue
# if n % i == o then it is a factor
        if n % i == 0:
#create random seed and add its sums
            random.seed(i)
            sum += random.randint(1, n)
#include random 1 as it is still relevant for total
    random.seed(1)
    sum += random.randint(1, n)
#this is checking if it is a fluky
    if sum == n:
        print("Flucky number: ", n)
#This counts n to 10000 and stops after so it reaches 10000
    n += 1
    if n > 10000:
        break
end = time.time()    
#printing time and loops
print("Total Time: %.2f seconds " %(end - start))
print("Total loops: ", iterations)
