# @@@@@@@@@@@@@
# CS1400 - MW1 XL
# Assignment 6

# Import the random module functions
from random import seed
from random import randint 

# Import the time module
import time

# Set up the total time of the program
startTime = time.time()

# iterations = Total number of iterations
iterations = 0
# flukyNumber = How many Fluky Numbers have been found
flukyNumber = 0

# Set up the main loop
for i in range(1, 10001):
    # seedSum = Sum of factors that will become the seed value
    seedSum = 0
    # topRange = The factor will never be more than half of the number
    topRange = (1/2) * i + 1
    for j in range(1, int(topRange)):
        # modulus = Remainder of division
        modulus = i % j
        iterations += 1
        # If the modulus numbers are factors, add them together
        if modulus == 0:
            seedSum += j
            
    # Put the value for seedSum in the seed function if it is greater than 0           
    if seedSum == 0:
        continue
    else:
        seed(seedSum)
    # Print the Fluky Number if the random integer is equal to i
    if randint(0, i) == i:
        print("Fluky Number: " + str(i))
        flukyNumber += 1
        # To reduce iterations, stop searching for Fluky Numbers when 7 are found
        if flukyNumber == 7:
            break
            
# Print the total time and total number of iterations
totalTime = round(time.time() - startTime, 2)
print("Total time: " + str(totalTime) + " seconds")
print("Total loops: " + str(iterations))

