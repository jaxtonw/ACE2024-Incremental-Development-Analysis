# @@@@@@@@@@@@@@
# CS 1400 - 14 week
# Assignment 6

# Import random module
import random
playAgain = True

# create for loop to run simulation 100,000 times
while playAgain == True:
    count = 0
    oneAnimalPercentage = 0
    twoAnimalPercentage = 0
    
    while count < 100000:
        
# generate and save random number from 1-6 for
pen
 pen loc
oorf
elepha of nts nd     2    elephant1 = random.andint(1, 6)
        elephant2 = random.randint(1, 6)
    
# generate and save random number from 1-6 fore
pe pen n of 
k
ofke# 
       keeper = random.randint(1, 6)or
    
#          rn simul    
    aton 100, 000 times# pha n
function
run
zok# u             if keeper == elephant1 or keeper == elephant2:
            oneAnimalPercentage += 1
            if keeper == elephant1 and keeper == elephant2:
                twoAnimalPercentage += 1 
        count += 1
    
# on 
d       s
f seei ng one or seeing two el        ephants     
    # print(oneAnimalPercentage, twoAnimalPercentage)
    twoAnimalPercentage = float((twoAnimalPercentage / oneAnimalPercentage) * 100)
    oneAnimalPercentage = float(oneAnimalPercentage / 1000)
    oneAnimalPercentage = format(oneAnimalPercentage, ".2f")
    twoAnimalPercentage = format(twoAnimalPercentage, ".2f")

# determine who is r@@@@ based on percentages    
    winner1 = "x"
    winner2 = "y" 
    for i in range(31,36):
        if i == round(float(oneAnimalPercentage)):
            winner1 = "zookeeper"
    for i in range(14, 19):
        if i == round(float(twoAnimalPercentage)):
            winner2 = "zookeeper"
    if winner1 == winner2:
        r@@@@Person = "zookeeper"
    else:
        r@@@@Person = "custodian"
        
    
# print final statements
    print()
    print("Percentage of the time there's at least one elephant in the pen the zookeeper checks: " + str(oneAnimalPercentage) + "%")
    print("When there is an elephant in the pen the zookeeper checks, percentage of time both elephants are in the same pen: " + str(twoAnimalPercentage) + "%")
    print("Based on these results, the " + r@@@@Person + " is correct!" + "\n")
    playAgain = str(input("Would you like to run the simulation again? (y/n) "))
    if playAgain == "y":
        playAgain = True
    else:
        print("Okay, have a good day! ")
        playAgain = False
        
  
