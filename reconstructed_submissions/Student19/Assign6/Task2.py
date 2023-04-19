# @@@@@@@@@@@@
# CS1400 - MW1 (14 week)
# Assignment 6
import random

check = "yes"
while check == "yes":
    stat1 = 0
    stat2 = 0
    stat3 = 0

    for i in range(0, 100000):
        # determins locations of elphants and zookeeper.
        
        ele1 = random.randint(1, 6)
        ele2 = random.randint(1, 6)
        zookeeper = random.randint(1, 6)
        
        # tests locatrions
        if ele1 == zookeeper or ele2 == zookeeper:
            stat1 += 1
            if ele1 == zookeeper and ele2 == zookeeper:
                stat2 += 1
    stat1P = round(stat1 / 1000, 2)
    stat2P = round((stat2 / stat1) * 100, 2)
    print("At least an elephant was in a checked pen: " + str(stat1P) + "% of the time")
    print("Both elephants were in a checked pen: " + str(stat2P)+ "% of the time")
    # test margin of error to chekc if the zookeeper was right.
    if abs(stat1P - 33.33) <= 2 and abs(stat2P - 16.67) <= 2:
        print("The zookeeper is correct")
    else:
        print("the zookeeper was incorrect")
    check = input("would you like to run the simulation again? (type yes to repeat): ").lower()
    
print("Thanks for playing!!!")
