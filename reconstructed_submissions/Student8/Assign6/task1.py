# @@@@@@@@@@@@@
# CS1400 - MW1
# Assignment 6 

# import the needed random and time modules
import random
import time

# track runtime
startTime = time.time()

# sets number of Fluke Numbers discovered at 0
flukyNumber = 0

# set the number being tested at 1
theNumber = 1

# define the count variable the will keep track of the number of iterations of the inner loop
count = 0

# define the variable msg
msg = ""

# this while loop will test every integer between 1 and 10000 unless 7 Fluky Numbers are identified first
while flukyNumber != 7 and theNumber != 10001:
    
    # resets the sum variable to 0 for each iteration of the overall while loop
    total = 0
    
    # the for loop tests for factors given the first half of the range of numbers between 1 and theNumber
    for i in range(1, ((theNumber // 2) + 1)):
        
        # when the remainder is 0 and number is a factor and should be added to sum variable
        if i == theNumber:
            count += 1
            continue
        elif (theNumber % i) == 0:
            count += 1
            total += i
    
    # use the seed function to set the seed using the total variable if the seed is greater than 0
    if total > 0:
        random.seed(total)
            
        # test to see if theNumber is equal to the randomly generated number based of the seed based of the sum variable
        if theNumber == random.randint(0, theNumber):
            msg += "Fluky Number: "
            msg += str(theNumber)
            msg += "\n"
        
            # count the number of Fluky Numbers identified
            flukyNumber += 1
        
    # increment theNumber variable by one
    theNumber += 1

# calculate the total time it took to run the program
endTime = time.time()
runtime = endTime - startTime

# round runtime to two decimal places
runtime = round(runtime, 2)

# output the total time
msg += "Total Time: "
msg += str(runtime)
msg += " seconds"

# output the number of iterations of the inner loop
msg += "\n"
msg += "Total Loops: "
msg += str(count)

# print the output
print(msg)
