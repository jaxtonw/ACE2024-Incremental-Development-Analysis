# @@@@@@@@@@@
# CS1400 - MW1 XL
# Assignment 6


import random

#setting variable to run simulation once in while loop
again = 1


while again == 1:
    #set counting variables as 0 
    oneElephant = 0
    twoElephant = 0
    for i in range (100001):
        #this selects a random number between 1 and 6 for elephant 1, elephant 2, and the zookeeper to check
        elephantOne = random.randint(1,6)
        elephantTwo = random.randint(1,6)
        zooCheck = random.randint(1,6)
        # this counts the number of times that there is at least one of the elephants 
        # in the pen the zookeeper checks
        if elephantOne == zooCheck or elephantTwo == zooCheck:
            oneElephant = oneElephant+1
        # this counts the number of times that when there is one elephant in the pen the zookeeper checks, 
        # that there is both in there
        if elephantOne == zooCheck and elephantTwo == zooCheck:
            twoElephant = twoElephant + 1

    #calculation of at least one elephant in the pen that the zookeeper checks out of the 100,000 times 
    # the simulation is run and rounding to two decimal places
    percentageOne = (oneElephant/100000) * 100
    percentageOne = round(percentageOne, 2)

    #calculation of both elephants being in the pen that the zookeeper checks, out of the times that there
    # is at least one elephant in the pen the zookeeper checks & rounding to 2 decimal places
    percentageBothWhenOne = (twoElephant/oneElephant) * 100
    percentageBothWhenOne = round(percentageBothWhenOne, 2)

    # messages of what the percentages found are
    print("There is at leat least one elephant in the pen the zookeeper checks " +str(percentageOne)+ "% of the time.")
    print("")
    print("When there is an elephant in the pen the zookeeper checks, both elephants are in the pen " + str(percentageBothWhenOne)+"% of the time.")
    print("")
    
    # looking at the percentages within 2% of zookeeper's claimed % for the zookeeper to be correct
    if 14.7 <= percentageBothWhenOne <= 18.7 and 31.3 < percentageOne < 35.3:
        print("The ZooKeeper is correct.")
        
    #all other percentages mean the custodian is correct
    else:
        print("The Custodian is correct.")
    print("")
    
    #ask user if they want to run simulation again and making input be all lowercase letters
    again = input("Run the simulation again? (yes or no): ")
    print("")
    again = again.lower()
    #keeps while loop open to reiterate simulation
    if again == "yes":
        again = 1
    #closes while loop so program stops
    else:
        again = 0
        print("Thanks for running this simulation.")
