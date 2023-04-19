# @@@@@@@@@@@@@@@@
# CECS1400 - MW1
# Assignment 6-Task 2

# import random module
import random

# set condition for while loop
playOn = True

# run zookeeper and elephant simulation
while playOn:
    # set counters to 0 for all scenarios and select random pens for both elephants and zookeeper
    countNightlySelection = 0
    countZookeeperFoundOne = 0
    countZookeeperFoundBoth = 0
    countZookeeperFoundNone = 0
    for nightlyPenChoice in range(100000):
        elephant1 = random.randint(1, 6)
        elephant2 = random.randint(1, 6)
        zookeeper = random.randint(1, 6)
        # add 1 to the nightly count for each iteration
        countNightlySelection += 1
        # check to see if selection of elephants and zookeeper match and add 1 to the appropriate counter
        if zookeeper == elephant1 and zookeeper == elephant2:
            countZookeeperFoundBoth += 1    
        elif zookeeper == elephant1 or zookeeper == elephant2:
            countZookeeperFoundOne += 1    
        else:
            countZookeeperFoundNone += 1
    # calculate percents for each possibility
    zookeeperFoundAtLeastOne = countZookeeperFoundOne + countZookeeperFoundBoth
    percentZookeeperFoundOne = round(((countZookeeperFoundOne / countNightlySelection) * 100), 2)
    percentZookeeperFoundBoth = round(((countZookeeperFoundBoth / countNightlySelection) * 100), 2)
    percentZookeeperFoundAtLeastOne = round(((zookeeperFoundAtLeastOne / countNightlySelection) * 100), 2)
    
    # display the results of the analysis
    msg1 = "Over the course of " + str(countNightlySelection) + " nights, the Zookeeper found at least "
    msg1 += "1 Elephant in the pen he checked " + str(zookeeperFoundAtLeastOne) + " times."
    print(msg1)
    msg2 = "That is " + str(round(((zookeeperFoundAtLeastOne / countNightlySelection) * 100), 2))
    msg2 += "% of the nights."
    print(msg2)
    msg3 = "Of the " + str(zookeeperFoundAtLeastOne) + " nights the Zookeeper found at least 1 Elephant "
    msg3 += "he found both Elephants " + str(round(((countZookeeperFoundBoth / zookeeperFoundAtLeastOne) * 100), 2)) + "% "
    msg3 += "of the time.\n"
    print(msg3)
    
    # compare results to determine if zookeeper or custodian is correct and offer to run analysis again
    if percentZookeeperFoundAtLeastOne + 2 >= ((1 / 3) * 100) and percentZookeeperFoundBoth + 2 >= ((1 / 18) * 100):
        print("The Zookeeper is correct.\n")
    else:
        print("The Custodian is correct.\n")
    runAgain = input("Do You want to run analysis again? ")
    if runAgain.lower() == "yes":
        playOn = True
    else:
        playOn = False
print("Thanks for checking.")        
