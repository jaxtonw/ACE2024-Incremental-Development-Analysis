# @@@@@@@@@@@@
# CS1400 - MW1
# Assignment 6

# Import Random
import random

# Create counter variables
totalOccurrences = 0
totalElephants = 0
totalTwoElephants = 0
val = True

# Create while loop to repeat if desired
while val == True:
    # Select the pens for the elephants and the zookeeper's selection
    for i in range(1,100000 + 1):
        elephantA = random.randint(1,6)
        elephantB = random.randint(1,6)
        zookeeperSelection = random.randint(1,6)
        totalOccurrences += 1
        # Determine if there is an elephant in the pen selected
        if zookeeperSelection == elephantA or zookeeperSelection == elephantB:
            totalElephants += 1
            # Determine if both elephants are in the same pen (given that there is at least one)
            if elephantA == elephantB:
                totalTwoElephants += 1
    # Calculate relative frequencies
    probOneElephant = totalElephants / totalOccurrences
    probTwoElephants = totalTwoElephants / totalElephants
    print("\nThe percentage that there is one elephant is:",format(probOneElephant,".2%"))
    print("The percentage that there are two elephants when one is there is:",format(probTwoElephants,".2%"))
    # Determine who is correct
    if abs(probOneElephant - 0.33) > 0.02 and abs(probTwoElephants - 0.17) > 0.02:
        print("The custodian was correct")
    else:
        print("The zookeeper was correct")
    # Ask if they would like to run it again
    response = input("Run again? (yes or no): ")
    response = response.lower()
    if response != "yes":
        val = False
        print("\nHope that was useful! Have a great day!!")
