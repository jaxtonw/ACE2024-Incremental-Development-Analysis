# @@@@@@@@@@@
# CS1400 - MW1
# Assignment 6

# import modules
from random import randint
playAgain = "yes"

# set up variables
while playAgain == "yes":
    oneElephant = 0
    bothElephants = 0
    total = 0
    for i in range(1, 100001): # loop random stalls
        elephant1 = randint(1, 6)
        elephant2 = randint(1, 6)
        zookeeper = randint(1, 6)
        if zookeeper == elephant2 or zookeeper == elephant1:
            oneElephant += 1
        if zookeeper == elephant2 and zookeeper == elephant1:
            bothElephants += 1
        total += 1
    onePercentage = round((oneElephant / total * 100), 2) # calculate percentage answers
    bothPercentage = round((bothElephants / total), 2)
    if onePercentage in range(31, 36):
        if bothPercentage in range(14, 19):
            part3 = "zookeeper"
    else:
        part3 = "custodian" # next print statements
    print("There is at least one elephant in the pen " + str(onePercentage) + "% of the time the zookeeper checks.")
    print("Of the times when there is an elephant when the zookeeper checks, both elephants are in the pen " + str(bothPercentage) + "% of the time.")
    print("The " + str(part3) + " is correct.")
    playAgain = input("Run the simulation again? (yes or no): ").lower
    if playAgain == "no":
        print("Simulation ended")
        break
        
