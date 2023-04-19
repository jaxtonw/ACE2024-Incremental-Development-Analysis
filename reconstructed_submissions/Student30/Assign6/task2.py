# @@@@@@@@@@@@@@@@@@
# CS1400 - 001
# Assignment 6


import random

program = 5

while program == 5:
    
    isThereElephant = 0
    samePen = 0
    noElephant = 0
    
    for i in range(1, 100001):
        elephantOne = random.randint(1, 6)
        elephantTwo = random.randint(1, 6)
        check = random.randint(1, 6)
        if elephantOne == check or elephantTwo == check:
            isThereElephant += 1
            if elephantOne == elephantTwo:
                samePen += 1
        
        else:
            noElephant += 1
    
    atLeastOne = (isThereElephant / 100000) * 100
    atLeastOne = round(atLeastOne, 2)
    bothElephants = (samePen / isThereElephant) * 100
    bothElephants = round(bothElephants, 2)
    print("At least One Elphant: " + str(atLeastOne) + "%")
    print("Both Elephants in same pen: " + str(bothElephants) + "%")
    
    
    runAgain = str(input("Would you like to run the simulation again? (yes or no): ")).upper()
    if runAgain == "YES":
        program = 5
    else:
        program = 4
        print("\n" + "The Custodian was correct. Thank you for playing :)")
