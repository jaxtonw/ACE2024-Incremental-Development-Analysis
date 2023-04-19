# @@@@@@@@@@@@@@
# CS1400 - MW1 XL
# Assignment #6
from random import randint

runAgain = "true"

while runAgain:

    samePen = 0
    notSamePen = 0
    zookeeperSawAtLeastOne = 0
    zookeeperSawBoth = 0
    for nightNumber in range(1, 100001):
        elephantOne = randint(1, 6)
        elephantTwo = randint(1, 6)
        zookeeperCheck = randint(1, 6)


# Code for presence of one elephant. In this case, elephant one
        if zookeeperCheck == elephantOne:
            zookeeperSawAtLeastOne += 1
# Code for both elephants, elephant two was in the pen at the same time as elephant one. 
            if zookeeperCheck == elephantTwo:
                zookeeperSawBoth += 1
# Again, code for presence of one elephant. In this case, elephant 2
        elif zookeeperCheck == elephantTwo:
            zookeeperSawAtLeastOne += 1

    percentSawAtLeastOne = (zookeeperSawAtLeastOne / 100000)
    percentSawBoth = (zookeeperSawBoth / zookeeperSawAtLeastOne)
    print("Percentage the Zookeper saw at least one elephant when he checks: " + str(
        (round((percentSawAtLeastOne * 100), 2))))
    if (percentSawAtLeastOne * 100) < 31.33 or (percentSawAtLeastOne * 100) > 35.33:
        print("Zookeeper's guess was not accurate.")
    print("percentage the zookeeper saw both of the elephants when he saw at least one: " + str(
        (round((percentSawBoth * 100), 2))))
    if ((percentSawBoth * 100)/ (zookeeperSawAtLeastOne * 100)) < 14.66 * zookeeperSawAtLeastOne or ((percentSawBoth * 100)/ (zookeeperSawAtLeastOne * 100)) > 18.66 :
        print("Zookeeper's guess was not accurate.")

    runIt = str(input("Do you wanna run it again? (Yes or No):"))

    if runIt.upper() != "YES":
        print("\nThat's all folks! Thanks for playing.")
        break


    
    
    
    
        


        
        
    
    

