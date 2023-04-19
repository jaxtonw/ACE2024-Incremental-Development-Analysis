# @@@@@@@@@@@@@@
# CS1400 - 001
# Assignment 6 task 2

import random

# set the times the pens are checked
penChecks = 0

# set the amount of times a single elephant is in a pen
singleElephant = 0

# set the amount of times both elephants are in a pen
doubleElephant = 0

# run code 100000 times
while penChecks < 100000:
    
    # calculate random pen
    elephant1 = random.randint(1, 6)
    elephant2 = random.randint(1, 6)
    
    # calculate random pens that are checked 
    zookeeper = random.randint(1, 6)

    # make a variable that represents when both elephants are together
    twoElephants = elephant1 == elephant2
    
    # add to the count when there is one elephant in a pen that is checked    
    if elephant1 == zookeeper or elephant2 == zookeeper:
        singleElephant += 1
        
    # add to the count when both elephants are in a pen when it is checked 
    elif twoElephants == zookeeper:
        doubleElephant += 1
        
    # add 1 to each night that the zookeeper checks the pens   
    penChecks += 1

# convert the amount of times there was a single elephant to percentage 
singleElephantPercent = (singleElephant / 100000) * 100

# convert the amount of times both elephants to percentage 
doubleElephantPercent = (doubleElephant / 100000) * 100

# print the percentages 
print("The zookeeper finds at least one elephant in a pen " + format(singleElephantPercent, "2.2f") + "% of the time.")
print("The zookeeper finds two elephants in a pen " + format(doubleElephantPercent, "2.2f") + "% of the time.")

# as the user if they would like to run the program again
userAnswer = input("Would you like to run the simulation again? (yes or no): ") 


