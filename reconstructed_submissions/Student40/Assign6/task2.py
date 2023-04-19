# @@@@@@@@@@
# CS1400 - 14 week
# Assignment 6 - task 2

# import modules
from random import randint

# set values
onePresent = 0
bothPresent = 0
start = True
numberTrials = 100000

# elephant in pen checked
while start:
    for trial in range(numberTrials):
        elephant1 = randint(1, 6)
        elephant2 = randint(1, 6)
        penChecked = randint(1, 6)
        if elephant1 == penChecked or elephant2 == penChecked:
            onePresent += 1
            # both in same pen
            if elephant1 == elephant2:
                bothPresent += 1  
    # calculate percentages
    atLeast1 = onePresent / numberTrials
    both = bothPresent / onePresent
    
    # messages
    print("Percentage of the time there is at least 1 elephant in the pen checked: " + format(atLeast1, ".2%"))
    print("Percentage of the time both are in checked pen, given one is present: " + format(both, ".2%"))
    
    # who is correct
    who = "Zookeeper"
    diff1 = abs(atLeast1 - 1/3)
    diff2 = abs(both - 1/6)
    if diff1 > .02 or diff2 > .02:
        who = "Custodian"
    print("\n" + "The " + who + " is right" + "\n")

    # play again?
    reply = input("Run simulation again?(yes or no): ")
    print()
    start = str.lower(reply) == "yes"
        
print("Thanks for using the elephant simulator!")
        
