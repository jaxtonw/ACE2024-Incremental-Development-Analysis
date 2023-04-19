# @@@@@@@@@@@@
# CS1400 - 006
# Assignment 06

from random import randint
#while condition
goAgain = "yes"

#Loop for simulation
while goAgain == "yes":
    oneElephant = 0
    twoElephant = 0
    for i in range(1,100001):
        oneRan = randint(1, 6)
        twoRan = randint(1, 6)
        zooKeeper = randint(1, 6)
        if zooKeeper == oneRan == twoRan:
            twoElephant += 1
        elif zooKeeper == oneRan or zooKeeper == twoRan:
            oneElephant += 1
        else:
            continue
    
#Percentages for one elephant in pen and two elephants in pen checked by zookeeper
    percentOne = ((oneElephant + twoElephant) / 100000) * 100
    percentTwo = (twoElephant / 100000) * 100

    print("Percent of time at least one elephant in checked pen: " + format(percentOne, ".2f") + "%")
    print("Percent of time there are two elephants in checked pen: " + format(percentTwo, ".2f") + "%")

#Determining who is correct
    if percentOne >= (.98 * (1 / 3) * 100) and percentOne <= (1.02 * (1 / 3) * 100) and percentTwo >= (.98 * ((1 / 3) * (1 / 6)) * 100) and percentTwo <= (1.02 * ((1 / 3) * (1 / 6)) * 100):
        print("Zookeeper is correct\n")
    else:
        print("Custodian is correct\n")
        
#Repeat simulation
    goAgain = input("Run the simulation again? (yes or no): ").lower()
    print("\n")
