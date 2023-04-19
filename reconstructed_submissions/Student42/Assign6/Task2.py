# @@@@@@@@@@@@@
# CS1400 - 14 week
# Assignment 6
userValue = True
while userValue:
    from random import randint
    seesElephant = 0
    sees2Elephant = 0
    count = 1
    while count <= 100000:
        elephant1 = randint(1, 6)
        elephant2 = randint(1, 6)
        zookeeper = randint(1, 6)

        if zookeeper == elephant1 == elephant2:
            sees2Elephant += 1
        elif zookeeper == elephant1:
            seesElephant += 1
        elif zookeeper == elephant2:
            seesElephant += 1
        count += 1
    seesElephant /= 100000
    sees2Elephant /= 100000
    seesElephant *= 100
    sees2Elephant *= 100
    msg = "This program determines the percentage of times the zookeeper sees the two elephants \n"
    msg += "Percent of time zookeeper saw one elephant: " + str(round(seesElephant, 2)) + "%\n"
    msg += "Percent of time zookeeper saw both elephants: " + str(round(sees2Elephant, 2)) + "%\n"

    if seesElephant + 2 or - 2 == 33 and sees2Elephant + 2 or -2 == 16:
        msg += "zookeeper is correct"
    userValue = False
    print(msg)
    userInput = input("Run the simulation again? (yes or no): ").upper()
    if userInput == "YES":
        userValue = True

