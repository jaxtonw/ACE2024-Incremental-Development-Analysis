# @@@@@@@@@
# CS1400 - MW1
# Assignment 6 - task 2

from random import randint

def simulation():
    count = 0
    yesOne = 0
    yesBoth = 0
    
    while count < 100000:
        pen1 = randint(1, 6) #create random number 1
        pen2 = randint(1, 6)    #create random number 2
        check = randint(1, 6)   #create check random number
        
        if check == pen1 and check == pen2: 
            yesBoth += 1
        elif check == pen1 or check == pen2:
            yesOne += 1
        
        count += 1
    
    oneStat = yesOne / 1000 #percent of the time there was one 
    bothStat = yesBoth / yesOne * 100
    
    oneStatFormat = format(oneStat, "5.2f")
    bothStatFormat = format(bothStat, "5.2f")
    
    print("% chance one is found = " + oneStatFormat + "%")
    print("% chance both are found = " + bothStatFormat + "%")
            
    # check if the statistics are within 2% of the zookeeper's claims
    
    if oneStat - .02 < 33333.33 < oneStat + .02 and bothStat - .02 < 16666.66 < bothStat + .02:
        print("\nThe Zookeeper's claim was correct!")
    else:
        print("\nThe Custodian is correct!")
    
    again()
        

def again(): #asks if they want to run the simulation again
    restart = input("\nRun the simulation again? (yes or no): ")
    
    if restart.lower() == "yes":
        simulation()
    else:
        print("\nThank you for running the simulation!\n")
    
    
simulation()
    

