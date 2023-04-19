# @@@@@@@@@@@@
# CS1400 - MW1
# Assignment 6

# import all the various functions needed for the loops and timing
from random import seed
from random import randint
from time import process_time
from math import sqrt

# Set starting variable values
iteration = 0
flukyCount = 0
num = 0
 
# Begin while loop for counting up to 10000
while (flukyCount < 7) and (num <= 10000):
	num += 1
	numFactors = 0
# Create lists to hold the factors and numbers from the random module
	factors = []
	numFromRand = []
# Check for factors
# Eliminate anything not even
	if num % 2 != 0:
		step = 2
	else:
		step = 1
	
	roof = int(num / 5 + 1)
	if num % 2 == 0:
		roof = int(num / 2 + 1)
	elif num % 3 == 0:
		roof = int(num / 3 + 1)

# Cut down the number of iterations by realizing factors begin repeating after you reach the half way point
	for i in range (1, roof, step): 
		if num % i == 0:
			numFactors += 1
			factors.append(i)
			seed(i)
			numFromRand.append(randint(1, num))
		if numFactors > 4:
			break
		iteration += 1
	if sum(numFromRand) == num:
		print("Fluky Number: " + str(num))
		flukyCount += 1
 		
print("Total Time: " + str(format(process_time(), ".2f")) + " seconds")
print("Total Loops: " + str(format(iteration)))


