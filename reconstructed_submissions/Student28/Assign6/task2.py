# @@@@@@@@@@@
# Assignment 6 Task 2
# CS 1400 14 Week

# Import modules
from random import randint
capsAgain = "YES"

# Set up loop so program runs and can rerun
while capsAgain == "YES":
    onlyOne = 0
    two = 0
    
# Simulate elephants and zookeeper picking pens
    for i in range(1, 100002):
        keeper = randint(1, 6)
        elephant1 = randint(1, 6)
        elephant2 = randint(1, 6)
        if (keeper == elephant1 and keeper != elephant2) or (keeper == elephant2 and keeper != elephant1):
            onlyOne += 1
        if keeper == elephant1 and keeper == elephant2:
            two += 1
            
# Calculating results
        percentOnlyOne = (onlyOne / i) * 100
        percentTwo = (two / i) * 100
        
# Show Results
    print("Results")
    print("Percent of the time there is only one elephant in the chosen pen:")
    print("{:.2f}".format(percentOnlyOne) + "%")
    print("Percent of the time there are two elephants in the chosen pen:")
    print("{:.2f}".format(percentTwo) + "%")
    
# Is zookeeper or custodian correct
    if (percentOnlyOne > 31.3 and percentOnlyOne < 35.33) and (percentTwo > 14.67 and percentTwo < 18.67):
        print("The zookeeper is correct.")
    else:
        print("The custodian is correct.")

# Ask to play again
    again = input("Run the simulation again? (yes or no): ")
    capsAgain = again.upper()
