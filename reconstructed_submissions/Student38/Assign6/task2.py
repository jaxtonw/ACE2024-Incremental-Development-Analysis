# @@@@@@@@@@@@@
# CS-1400 MW1
# Assignment 6

# import modules
import random

# set up beginning variables to 0
timesCorrect = 0

j = 0
# create outermost loop, so user can keep running simulation if wanted
while j < 100000:
    for i in range(100000): ## run loop 100,000 times to get high sample to make conclusions from
        nightActual = random.randint(0, 7) ## represents actual number of pen where an elephant is
        guess = random.randint(0, 7) ## represents 1/6 chance of zookeeper finding elephant
        if guess == nightActual:
            timesCorrect += 1
            nightTogether = random.randint(0, 7) ## represents actual chance of finding elephants together
            if nightTogether == guess:
                timesCorrect += 1
        else:
            continue
    # print and calculate actual number and percentage of times zookeeper was correct 
    print("Times zookeeper correct: " + str(timesCorrect))
    percentCorrect = (timesCorrect / 100000) * 100
    print("Percent correct: " + format(percentCorrect, "5.2f") + "%")
    # ask user if they want to run simulation again
    answer = input("Do you want to run the simulation again? (yes or no?): ")
    result = answer.upper() ## save user input as all uppercase in order to compare strings
    j += 1
    if str(result) != "YES":
        break
    else: 
        continue
    
        
    

