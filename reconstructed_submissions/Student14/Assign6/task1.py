# @@@@@@@@@@@@
# CS 1400 - MW 1
# Assignment 6 Task 1

#Import
import random
import time

#variables
iterations = 0
sevenFluky = 0

#get the start time
startTime = time.time()

#this for loop starts at 1 and goes to 10000
for num_fluky in range(1,10000):
    #This variable is used to check to see if the number is a fluky and resets on each iteration
    numSum = 0
    #This for loop is used to get the seed and to check to see if a fluky number
    for check_for_facotrs in range(1, num_fluky):
        #This checks to is if the num fluky when divided by check for facotrs is equal to 0
        if num_fluky % check_for_facotrs == 0:
            random.seed(check_for_facotrs)
            numSum += random.randint(1, num_fluky)
    #This checks to see if the number is a fluky then shows the results
    if num_fluky == numSum:
        print("Fluky number: " + str(num_fluky))
        #track the number of fluky numbers
        sevenFluky += 1
        #checks to see if the program has found the 7 fluky numbers then breaks out of the loop
        if sevenFluky == 7:
            break
        #This is used to keep track of the number of iterations in the inner loop of the program goes through   
        iterations += check_for_facotrs

# get the end time
endTime = time.time()
#This displays the time from the start to the end
print("Total Time: %.2f second" % (endTime - startTime))
#This displays the number of iterations
print("Total Loops:", iterations)

