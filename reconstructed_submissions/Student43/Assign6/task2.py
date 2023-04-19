# @@@@@@@@@@@@@
# CS1400 - MW1 XL
# Assignment 6

# Import the desired random functions
from random import randint

# Create the while loop 
while True:
    # atLeastOneE = Probability of the keeper seeing at least one elephant
    atLeastOneE = 0
    # bothE = Probability of keeper seeing both based on if he saw at least one
    bothE = 0
    
    # Simulate the 100,000 trials
    for i in range(1, 100001):
        # elephant1 = First elephant, randint(1, 6) because 1/6 chance of any pen
        elephant1 = randint(1, 6)
        # elephant2 = Second elephant
        elephant2 = randint(1, 6)
        # zooKeep = Zookeeper, randint(1, 6) because 1/6 chance of checking any pen
        zooKeep = randint(1, 6)
        
        # Probability of at least 1 = probability of 1 + probability of 2
        if zooKeep == elephant1 or zooKeep == elephant2:
            atLeastOneE += 1
            # Probability of both = Zookeeper seeing both elephants
            if zooKeep == elephant1 and zooKeep == elephant2:
                bothE += 1

    # Percents = numbers * 100, and rounding them to 2 decimal places
    percentAtLeastOneE = round(atLeastOneE / 100000 * 100, 2)
    percentBothE = round(bothE / atLeastOneE * 100, 2)
    
    # Print the statements that the user will see
    print("Probability that there is at least one elephant"
          " when the zookeeper checks is %" + str(percentAtLeastOneE))
    print("Probability that the zookeeper finds both elephants"
          " in the pen %" + str(percentBothE))
    print("Using a two percent margin of error:")
    print("The custodian is correct, as the percentages are not "
          "close enough to 1/3 (%33.33) and 1/6 (%16.67).")

    # Prompt the user to run the test again if they want
    runAgain = input("Run the simulation again? (yes or no): ")
    if runAgain.lower() == "yes":
        continue
    else:
        print("Go tell the zookeeper that he is wrong!")
        break
        
