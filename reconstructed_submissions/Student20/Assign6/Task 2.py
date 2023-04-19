import random

#error adjustments for the percentages given by zoo keeper.
jAdjustmentlow = (1/3) - ((1/3)*.02) 
kAdjustmentlow = (1/18)- ((1/18)*.02) 
jAdjustmentHigh = (1/3) + ((1/3)*.02) 
kAdjustmentHigh = (1/18) + ((1/18)*.02) 
while True:
#counters given for each situation
    atleastOne = 0
    both = 0
    neither = 0
#this loop will determine if elephant and zookeeper are in the same pin
    for i in range (100000):
        firstElephant = random.randint(1,6)
        secondElephant = random.randint(1,6)
        zookeeper = random.randint(1,6)
        if firstElephant == zookeeper or secondElephant == zookeeper :
            atleastOne += 1
        if firstElephant == zookeeper and secondElephant == zookeeper :
            both += 1
        else:
            neither += 1
 #This section gives us the true percentages       
    j = (atleastOne/100000)*100
    k = (both/100000)*100
    print("True percentage of sighting of at least one elephant: %.2f " %(j))
    print("True percentage of sightings of both elephants: %.2f " %(k))
#This section determines who was correct
    if jAdjustmentlow < j and jAdjustmentHigh > j and kAdjustmentlow < k and kAdjustmentHigh > k :
        print("The Zookeeper is correct.")
    else:
        print("The custodian is correct.")
    repeat = input("Would you like to run simulation again? (yes or no): ")
    if repeat == "no" or repeat == "No" or repeat == "nO" or repeat == "No" :
        break
    else: 
        continue    
