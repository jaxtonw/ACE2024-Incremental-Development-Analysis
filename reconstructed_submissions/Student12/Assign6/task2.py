# @@@@@@@@@@@@
# CS1400 - 14 Week
# Assignment 6

from random import randint
# variables
count = 0
num = 0
redo = "yes"
# loop
while redo != "no":
    for val in range(100000):
        zookeeper = randint(1, 6)
        elephant1 = randint(1, 6)
        elephant2 = randint(1, 6)
        if zookeeper == elephant1 == elephant2:
            count += 1
        elif zookeeper == elephant1 or zookeeper == elephant2:
            num += 1
    # percentages/probabilities
    # divide by 1000 to get percentage value
    per1 = num / 1000 
    per2 = (count / num) * 100
    # statements
    print("Both elephants in the pen: " + str(round(per1, 2)) + "%")
    print("At least one elephant in the pen: " + str(round(per2, 2)) + "%")
    # zookeeper or custodian?
    if 14 < per1 < 16 and (per2 - 2) <= per2 <= (per2 + 2):
        print("The zookeeper was right.")
    else:
        print("The custodian was right.")
    redo = input("Run the simulation again? (yes or no): ").lower()
    
    
