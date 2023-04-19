# @@@@@@@@@@
# CS 1400 - 14 week
# Assignment 6

from random import randint

count = 0

#run again loop
while count == 0:
    atLeastOne = 0
    seesTwo = 0
    
    #simulation loop
    for i in range(1, 100000+1):
        el1 = randint(1, 6)
        el2 = randint(1, 6)
        zookeeper = randint(1, 6)
        #if at least one elephant
        if zookeeper == el1 or zookeeper == el2:
            atLeastOne+= 1
        #if both elephants
        if el1 == el2 and zookeeper == el1:
            seesTwo += 1
    
    #calculate percentages
    oneEl = atLeastOne / 100000
    twoEl = seesTwo / atLeastOne
    
    #who is correct
    if ((1 / 3 - .02) < oneEl and oneEl < (1 / 3 + .02)) and ((1 / 6 - .02) < twoEl and twoEl < (1 / 6 + .02)):
        correct = "Zookeeper"
    else:
        correct = "Custodian"
    
    #display results
    print(format("Elephant Simulation - 100,000 Nights", "^90s") + "\n")
    print("Percent of time there is at least one elephant in the pen checked: " + format(100 * oneEl, ".2f") + "%")
    print("When there is at least one elephant in the pen checked, percent of time both elephants are there: " + format(100 * twoEl, ".2f") + "%")
    print("Who is correct: " + correct + "\n")
    
    #run again?
    again = input("Run the simulation again? (yes or no): ")
    print()
    if again.lower() == "yes":
        count = 0
    else:
        count = 1
        print("Simulation Ended")
