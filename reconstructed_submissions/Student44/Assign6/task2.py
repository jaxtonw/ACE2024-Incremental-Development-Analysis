# @@@@@@@@@@@@
# CS1400 - MW 1
# Assignment 6

import random

continueLoop = 'YES'

while continueLoop == 'YES':
    oneElephant = 0
    twoElephants = 0
    
    for i in range(1, 100001):
       
        # generate random number for elephant 1, 2, and zookeeper

        elephant1 = random.randint(1, 6)
        
        elephant2 = random.randint(1, 6)
        
        zookeeper = random.randint(1, 6)
        
        # adding a number to elephant count for 1 elephant
        
        if zookeeper == elephant1 or zookeeper == elephant2:
           
            oneElephant += 1
            
        # adding a number to elephant count for 2 elephants
        
        if zookeeper == elephant2 and zookeeper == elephant1:
            
            twoElephants += 1
            
    
    onePresentpercent = (oneElephant / 100000) * 100
    twoPresentpercent = ((twoElephants / 100000) / onePresentpercent) * 100
    


    
    print(round(onePresentpercent, 2))
    print(round(twoPresentpercent, 2))
    
    # print conditionals to display who is correct
   
    if 35.33 > onePresentpercent > 31.33:
        print("The zookeeper is correct about one elephant being in the pen percentage")
    else:
        print("The custodian is correct the percentage is off")
    if 14.66 < twoPresentpercent < 18.66:
        print("The zookeeper is corect about the percent of times the pen he checks has both elephants")
    else:
        print("The custodian is correct the percentage is off")
        
    # Ask user if they want to run simulation again

    continueLoopanswer = input("Run the simulation again? (yes or no): ")
    continueLoop = continueLoopanswer.upper()
print("Simulation complete!")

