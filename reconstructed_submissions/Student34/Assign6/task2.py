# @@@@@@@@@@@@
# CS 1400 - 14 Weeks
# Assignment 6

from random import randint

userChoice = "yes"

while userChoice == "yes":
    msg = ""
    totalIterations = 0
    zookeeperSuccessCount = 0
    bothElephantsCount = 0
    zookeeperAnalysis = False
    
    for i in range(0, 100000):
        zookeeperChoice = randint(1, 6)
        firstElephantChoice = randint(1, 6)
        secondElephantChoice = randint(1, 6)
        # Determine whether at least one elephant is present in the pen chosen by the zookeeper
        if zookeeperChoice == firstElephantChoice or zookeeperChoice == secondElephantChoice:
            zookeeperSuccessCount += 1
            # Determine whether both elephants are present in the pen chosen by the zookeeper
            if firstElephantChoice == secondElephantChoice:
                bothElephantsCount += 1
        totalIterations += 1
    
    zookeeperSuccessPercentage = zookeeperSuccessCount / totalIterations
    msg += "At least one elephant is in the pen checked by the zookeeper " + \
           format(zookeeperSuccessPercentage, "<.2%") + " of the time."
    
    bothElephantsPercentage = bothElephantsCount / zookeeperSuccessCount
    msg += "\n"
    msg += "When at least one elephant is in the pen checked by the zookeeper, both elephants are in " \
           "the pen " + format(bothElephantsPercentage, "<.2%") + " of the time."
    msg += "\n"
    
    zookeeperAnalysis = (1 / 3 - 0.02 <= zookeeperSuccessPercentage <= 1 / 3 + 0.02) and \
                        (1 / 6 - 0.02 <= bothElephantsPercentage <= 1 / 6 + 0.02)
    
    if zookeeperAnalysis:
        msg += "The zookeeper is correct."
    else:
        msg += "The custodian is correct."
        
    print(msg)
    
    userChoice = input("Do you want to run the simulation again? (yes or no): ").lower()
    
    print()

print("Thanks for using the simulation.")

