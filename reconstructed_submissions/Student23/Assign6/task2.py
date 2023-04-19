# @@@@@@@@@@@@@@
# CS1400 - 001
# Assignment 6

import random


while True:
    # Define variables and values
    found1 = 0
    found2 = 0
    
    # Define variables and assign chosen pen 
    for days in range(1, 100000 + 1):
        elephantOne = random.randint(1, 6)
        elephantTwo = random.randint(1, 6)
        Zookeeper = random.randint(1, 6)
        if Zookeeper == elephantOne or Zookeeper == elephantTwo:
            found1 += 1
            if Zookeeper == elephantOne and Zookeeper == elephantTwo:
                found2 += 1
            
    print("There is at least one elephant in the pen when the zookeeper checks " + format(found1 / days, ".2%") + " of the time.")
    print("When there is an elephant in the pen the zookeeper checks both elephants are present " + format(found2 / found1, ".2%") + " of the time.")
    
    # Print if zookeeper or custodian is correct
    if .31333 <= (found1 / days) and .35333 >= (found1 / days) and .14666 <= (found2 / found1) and .18666 >= (found2 / found1):
        print("The Zookeeper is correct. His percentages are accurate" + "\n")
    else:
        print("The custodian is correct. The Zookeeper's percentages are incorrect" + "\n")
    
    # User input of to run again or not
    answer = input("Run the simulation again? (yes or no): ")
    if str(answer.upper()) == "YES":
        continue
    elif str(answer.upper()) == "NO":
        print("Thank you")
        break
    else:
        print("Invalid response. Exiting simulation")
        break
    

