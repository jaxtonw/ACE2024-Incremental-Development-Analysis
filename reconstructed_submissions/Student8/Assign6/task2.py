# @@@@@@@@@@@@@
# CS1400 - MW1
# Assignment 6

# import the random module
import random

# define the switch variable (this variable allows the user to repeat the simulation)
switch = "yes"

# run the program the first time automatically, and then only if the user opts to run it again
while switch == "yes":

    # define tracking variables (variables that will track the number of each occurrence)
    found0 = 0
    atLeast1 = 0
    found2 = 0

    # define simulationCount
    simulationCount = 100000

    # run the simulation simulationCount times
    for i in range(simulationCount):

        # which pen did Elephant 1 choose?
        elephant1 = random.randint(1, 6)
        # which pen did Elephant 2 choose?
        elephant2 = random.randint(1, 6)
        # which pen did the zookeeper choose?
        zookeeper = random.randint(1, 6)
    
        # identify which occurrence will take place
        if zookeeper == elephant1 and zookeeper == elephant2:
            atLeast1 += 1
            found2 += 1
        elif zookeeper == elephant1 or zookeeper == elephant2:
            atLeast1 += 1
        else:
            found0 += 1
        
    # calculate the decimal probabilities
    percentAtLeast1 = atLeast1 / simulationCount

    percentFound2 = found2 / atLeast1

    # convert decimal probabilities to rounded percents
    percentAtLeast1 *= 100
    percentAtLeast1 = round(percentAtLeast1, 2)

    percentFound2 *= 100
    percentFound2 = round(percentFound2, 2)

    # convert the zookeeper's probabilities to percents
    zookeeperAtLeast1 = 1 / 3
    zookeeperAtLeast1 *= 100
    zookeeperAtLeast1 = round(zookeeperAtLeast1, 2)

    zookeeperFound2 = 1 / 6
    zookeeperFound2 *= 100
    zookeeperFound2 = round(zookeeperFound2, 2)

    # was the zookeeper right?

    # find differences between the zookeeper's and the simulation's probabilities both sets
    differenceAtLeast1 = abs(percentAtLeast1 - zookeeperAtLeast1)
    differenceFound2 = abs(percentFound2 - zookeeperFound2)

    # if the difference is greater than or equal to two percent, the custodian was correct
    if differenceAtLeast1 < 2 and differenceFound2 < 2:
        winner = "zookeeper"
    else:
        winner = "custodian"

    # output the results of the simulation

    msg = "The simulation found the following: "
    
    msg += "\n"

    msg += "The zookeeper found at least one elephant in the pen he selected "
    msg += str(percentAtLeast1)
    msg += "% of the time."
    
    msg += "\n"

    msg += "When the zookeeper found an elephant in a pen, there was a second elephant "
    msg += str(percentFound2)
    msg += "% of the time."
    
    msg += "\n"

    msg += "This means that the "
    msg += winner
    msg += " was correct."

    print(msg)
    
    switch = input("Run the simulation again? (yes or no): ")
    switch = switch.lower()
    
    # add line of space
    print()
    
    # run the program again or leave an ending message based on the switch response
    if switch == "no":
        print("Thank you for using this simulator.")
