# @@@@@@@@@@@
# CS1400 - MW1 XL
# Assignment 6 - Task 2

from random import randint
from random import seed
import math

#use a function to make running simulation again easier.
def zookeeper():
    pen1 = 0
    pen2 = 0
    pen3 = 0
    pen4 = 0
    pen5 = 0
    pen6 = 0
    penCrowd = 0
    trials = 1000000    
    
    
    for i in range(trials):
        elephant1 = randint(1, 6)
        elephant2 = randint(1, 6)
        if elephant1 == 1:
            pen1 += 1
        elif elephant1 == 2:
            pen2 += 1
        elif elephant1 == 3:
            pen3 += 1
        elif elephant1 == 4:
            pen4 += 1
        elif elephant1 == 5:
            pen5 += 1
        else:
            pen6 += 1
    
        if elephant2 == 1:
            pen1 += 1
        elif elephant2 == 2:
            pen2 += 1
        elif elephant2 == 3:
            pen3 += 1
        elif elephant2 == 4:
            pen4 += 1
        elif elephant2 == 5:
            pen5 += 1
        else:
            pen6 += 1
    
        if elephant1 == elephant2:
            penCrowd += 1
            
#If trial results show approximately 33.33% for each pen and 16.67% for both elephants in one pen, 
    # then the zookeeper is correct.     
    print("Pen 1: " + str(pen1) + " = " + "{:.2%}".format(pen1 / trials))
    print("Pen 2: " + str(pen2) + " = " + "{:.2%}".format(pen2 / trials))
    print("Pen 3: " + str(pen3) + " = " + "{:.2%}".format(pen3 / trials))
    print("Pen 4: " + str(pen4) + " = " + "{:.2%}".format(pen4 / trials))
    print("Pen 5: " + str(pen5) + " = " + "{:.2%}".format(pen5 / trials))
    print("Pen 6: " + str(pen6) + " = " + "{:.2%}".format(pen6 / trials))
    print("")
    print("Both elephants in the pen: " + str(penCrowd) + " = " + "{:.2%}".format(penCrowd / trials))
    
zookeeper()
print("Based on the calculations in the simulation, the Zookeeper is correct.\n")

runAgain = input("Run the simulation again? (yes or no): ").lower()
if runAgain == "yes":
    zookeeper()
else:
    print("Thank you and have a good day.")
    


