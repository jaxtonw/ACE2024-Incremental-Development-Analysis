# @@@@@@@@@@@@@
# CS1400 - MW1
# Assignment 6

from random import randint



print("Welcome to the Zookeeper/Elephant Pen Simulation!")
input("Press Enter to continue with the simulation.")

while True:  # loop that is necessary to repeat
    oneDumbo = 0
    twoDumbo = 0
    for i in range(0, 10000):  # start tests
        # generate and assign positions
        zPos = randint(1, 6)
        e1Pos = randint(1, 6)
        e2Pos = randint(1, 6)
        # evaluate positions and record if zookeeper ends up with elephants
        if zPos == e1Pos and zPos == e2Pos:
            twoDumbo += 1
        elif zPos == e1Pos or zPos == e2Pos:
            oneDumbo += 1
            
    # create new variables to hold results which will be printed
    oneDumboPercent = round(((oneDumbo + twoDumbo) / 100000) * 100, 2)
    twoDumboPercent = round((twoDumbo / (twoDumbo + oneDumbo)) * 100, 2)
    # determine if the zookeeper was right
    if (31.33 < oneDumboPercent < 35.33) and (14.65 < twoDumboPercent < 18.65):
        zookeeper = True
    else:
        zookeeper = False
    # print results
    print("The zookeeper saw an elephant " + str(oneDumboPercent) + "% of nights")
    print("The zookeeper saw both elephants " + str(twoDumboPercent) + "% of the nights he saw elephants")
    if zookeeper == True:
        print("The Zookeeper was right!")
    else:
        print("The Zookeeper was wrong!\n")
    # ask user if they would like to repeat
    userInput = input("Would you like to run the simulation again? (yes/no): ").lower()
    # continue/end simulation
    if userInput == "yes":
        print("Let's run it again!")
        
    else:
        print("Ok. Goodbye!")
        break
        
    
        
            
        
