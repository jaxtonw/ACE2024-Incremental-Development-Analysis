# @@@-@@@@@@@-Assn6
# CS1400 - 14 week
# task 1

# importing the necessary modules
import time
from random import randint
from random import seed

# starting the time function to track the amount of time
startTime = time.time()

# creating count variable to track number of loops
count = 0
# creating number variable to 
number = 0
flukyCount = 0

# while loop to add conditional statements at end of loop
while True:
    # create variable for the factors and make it a list
    # adding 1 to count the number of loops
    # incrementing the number count for each loop
    factors = []
    number += 1
    count += 1
    
    # for loop for i in range of 1 to the number we want to factor
    # added factor.append to insert the factors into a list for easy sum
    for i in range(1, number):
        if number % i == 0:
            factors.append(i)
    # we don't want the seed to include 1 
    if sum(factors) == 0:
        continue
    # value for seed is the sum of all factors of the number
    # seedValue generates the random number from the seed value
    seed(sum(factors))
    seedValue = randint(0, number)
    
    # seedValue should equal number if it is a fluky number
    # flukyNumber variable adds one for each add fluky number
    if seedValue == number:
        print("Fluky Number: ", number)
        flukyCount += 1
        
    # if the fluky count reaches 7 we want to terminate 
    if flukyCount == 7:
        break
    # create if statement for if number reaches 10,000 before fluky number reaches 7
    if number > 10000:
        break

# ending the time function to count the time needed to execute loops
endTime = time.time()
    
# print the total time with 2 decimal places
# print total loop iterations
print("Total time: %.2f seconds" % (endTime - startTime))
print("Total Loops: ", count)

    
    
