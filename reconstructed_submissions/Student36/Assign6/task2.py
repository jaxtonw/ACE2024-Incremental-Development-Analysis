# @@@@@@@@@@@@@@@
# CS 1400- 14 week
# Assignment 6

#import statements
from random import randint


cont = "yes"
#simulation
while cont == "yes":
    # variables
    samePen = 0
    checkedPen = 0
    noPen = 0
    for i in range(0, 100001):
        elephant1 = randint(1,6)
        elephant2 = randint(1,6)
        penCheck = randint(1,6)
        #both in same pen that zookeeper checked
        if elephant2 == penCheck and elephant1 == penCheck:
            samePen += 1
        #zookeeper checks a pen with one   
        elif elephant1 == penCheck or elephant2 == penCheck:
            checkedPen += 1
        #zookeeper checks an empty pen
        else:
            noPen += 1
    
    #converting to percents        
    samePenPercent = round(samePen / 100000, 2)
    checkedPenPercent = round(checkedPen / 100000, 2)
    noPenPercent = round(noPen / 100000, 2)
    
    samePenPercent = round(samePenPercent * 100, 2)
    checkedPenPercent = round(checkedPenPercent * 100, 2)
    noPenPercent = round(noPenPercent * 100, 2)
    
    #print statements
    print("The percentage of there being one elephant in the pen the zookeeper checks is: " + str(checkedPenPercent) + "%")
    print("The chance of there being both elephants in the pen the zookeeper checks is: " + str(samePenPercent) + "%")
    
    if samePenPercent == range(14,19) and checkedPenPercent == range(31,36):
        print("The zookeeper was correct")
    else:
        print("The zookeeper was a dirty rotten liar.")
      
    cont = input("Run the simulation again? (Yes or No): ").lower()


