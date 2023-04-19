# @@@@@@@@@@@  
# CS 1400 - MW1 XL
# Assignment 006

import random

runAgain = "yes"
totalRun = 100000

# the main loop when run again does not = yes the loop breaks
while runAgain == "yes":
    
    # to run the simulations multiple times the numbers are reset to 0
    # zookeeper1 is if the zookeeper saw 1 elephant, zookeeper2 is for 2 elephants

    zooKeeper1 = 0
    zooKeeper2 = 0
    
    # now the simulation is run  according to the total run number (100,000)
    for i in range(0, totalRun):
        
        # the two elephants now have their random pen assigned to them and the one the zookeeper checks
        elephant1 = random.randint(1, 6)
        elephant2 = random.randint(1, 6)
        zooKeeper = random.randint(1, 6)

        # This test sees if the zookeeper sees both elephants
        if elephant1 == elephant2 == zooKeeper:
            zooKeeper2 += 1

            # this test sees if the zookeeper only sees 1 elephant and not the other
        elif elephant1 == zooKeeper or elephant2 == zooKeeper and not elephant1 == elephant2:
            zooKeeper1 += 1
            
    # one elephant determines how many times the zookeeper saw at least 1 elephant
    # I add zookeeper 2 since it is how many times he saw at least 1 of them
    oneElephant = (zooKeeper1 + zooKeeper2)/totalRun * 100
    
    # two elephant determines how many times he saw one elephant he also saw the other
    # I read the assignment and it seemed like 1/6 of the time second elephant was with the first one
    # and not 1/6 of the total times he checks a pen both are there.
    twoElephant = zooKeeper2/zooKeeper1 * 100
    
    msg2 = format(oneElephant, ".2f")
    msg3 = format(twoElephant, ".2f")

    print("Simulation Results")
    print("Percentage there was at least one elephant: " + msg2 + "%")
    print("Percentage the second elephant was with the first elephant: " + msg3 + "%")

    # the first test is if both numbers were right according to the zookeeper
    # I converted 1/3 and 1/6 to percentages and then added the 2% margin to compare to
    if 31.33 < oneElephant < 35.33 and 14.66 < twoElephant < 18.66:
        print("The zooKeeper is right on both accounts")
        
        # the second test is if the zookeeper is right on the first % but wrong on the second
    elif 31.33 < oneElephant < 35 and not 14.66 < twoElephant < 18.66:
        print("The zooKeeper is right with one elephant but not two )
        
        # the third test is if the zookeeper is wrong on the first but right on the second
    elif not 31.33 < oneElephant < 35.33 and 14.66 < twoElephant < 18.66:
        print("The zooKeeper is wrong with seeing one elephant but right with seeing two")
        
        # now the last option is if the custodian is right both times
    else:
        print("The custodian is right on both accounts")

    # here is the prompt to run the simulation again any version of yes works
    runAgain = input("Do you want to run the simulation again? (Yes/No) ")
    runAgain = runAgain.lower()

