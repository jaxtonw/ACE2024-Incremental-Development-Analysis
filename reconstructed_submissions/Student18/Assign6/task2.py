# @@@@@@@@@@@
# CS 1400 - A01 XL
# Assignment 6

from random import randint

countOfElephant1 = 0
countOfElephant2 = 0 
repeat = True

while repeat: 
    for i in range(1,100001):
        elephant1 = randint(1,6)
        elephant2 = randint(1,6)
        zookeeper = randint(1,6)
        if zookeeper == elephant1 or zookeeper == elephant2: 
            countOfElephant1 += 1
        if zookeeper == elephant1 and zookeeper == elephant2: 
            countOfElephant2 += 1

    percentFor1Elephant = round(countOfElephant1 / 100000 * 100, 2)
    percentFor2Elephant = round(countOfElephant2 / 100000 * 100, 2)
    print(countOfElephant1)
    print(countOfElephant2)
    print("The percentage of time that there is one elephant in the pen: " + str(percentFor1Elephant))
    print("The percentage of time that there are both elephants in the pen: " + str(percentFor2Elephant))
    userInput = str(input("Run this simulation again? yes or no:  ")) 
    
    if userInput == "no": 
        break
    


