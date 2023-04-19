# @@@@@@@@@@@@@@
# CS1400 - MW2
# Assignment 6

# import the random module
import random

# create a loop so the simulation will run however many times we need it to
# create a variable that will tell the loop when to stop
stop = False
while not stop == True:

    # create variables for the pen that either elephant chooses, and the pen the zookeeper chooses
    elephantOne = random.randint(1, 6)
    elephantTwo = random.randint(1, 6)
    zookeeperPen = random.randint(1, 6)

    # create variable that will store the total number of iterations, the amount of times one elephant was in a pen, and
    # the amount of times both elephants were in the same pen
    onePen = 0
    twoPen = 0
    total = 0

    # Create a for loop statement that will run 100,000 iterations
    for i in range(100000):
        elephantOne = random.randint(1, 6)
        elephantTwo = random.randint(1, 6)
        zookeeperPen = random.randint(1, 6)
        total += 1
        if elephantOne == zookeeperPen or elephantTwo == zookeeperPen \
                or elephantOne == zookeeperPen and elephantTwo == zookeeperPen:
            onePen += 1
        if elephantOne == zookeeperPen or elephantTwo == zookeeperPen and elephantOne == elephantTwo:
            twoPen += 1

    print(onePen)
    print(twoPen)
    print(total)

    # divide the variables and convert to percentages to display in the print statement
    statOne = round((onePen / total) * 100, 2)
    statTwo = round((twoPen / total) * 100, 2)

    if statOne >= 31.33 and statOne <= 35.33 and statTwo >= 14.6666 and statTwo <= 18.6666:
        result = "The Zookeeper was correct this time"
    else:
        result = "The Custodian was correct this time"

    # create a message to print at the end of the program
    msg = "Percentage of times where one elephant was in a pen "
    msg += str(statOne)
    msg += "%"
    msg += "\n"
    msg += "Percentage of times when both elephants were in the same pen "
    msg += str(statTwo)
    msg += "%"
    msg += "\n"
    msg += result
    print(msg)

    # ask the user if they want to restart the simulation
    restart = str(input("Run the simulation again? (yes / no) "))
    # use the upper function so that however the user capitalizes their input, we will have one output to test
    restart = restart.upper()
    # the answer they give will change the variable that the while loop uses
    if restart == "YES":
        stop = False
        print()
    elif restart == "NO":
        stop = True
        print("\n Simulation Ended")
    else:
        print("\n invalid input. Simulation ended")
        stop = True




