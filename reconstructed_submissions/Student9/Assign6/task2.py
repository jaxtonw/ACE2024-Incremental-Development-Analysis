# @@@@@@@@@@@@@@@
# CS1400 - 14 Week
# Assignment 6

import random
from random import randint

#identify the variables
n = 0
s = 0
b = 0
t = 1

#make big while loop that controls the whole thing
while True:
    #while loop that calculates the percentages
    while True:
        n += 1
            
        e1 = randint(1,6)
        e2 = randint(1,6)
        z = randint(1,6)
            
        if z == e1 or z == e2:
            s +=1
        elif e1 == e2:
            b += 1
    
        if n > 100000: #stop after 100000 times
            break
    p = (s/n)*100
    p2 = (b/n)*100  #turn all of them into 2 decimal points
    p = '{:.2f}'.format(p)
    p2 = '{:.2f}'.format(p2)
        
    if p == range(31,35):   #check if zookeeper is correct
        w = "zookeeper"
    else:
        w = "custodian"
        
    print("The chance that there will be at least one elephant in the pen the zookeeper check is " + p + "%")
    print("The chance that the elephants are in the same pen is " + p2 + "%")       #print outcomes
    print("The "+ w + " is correct!")
    
    again=str(input("Would you like to play again?"))
    again2 = again.lower()          #check if they want to play again
    if again2 == 'yes':
        continue
    else:
        print("Thank you for playing!")
        break
        
        

