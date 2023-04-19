# @@@@@@@@@@@@@
# CS1400 - MW1
# Assignment 6

#import random 
import random 
#start counters of one and both elephants in the room
one = 0
both = 0
count = 0
#for loop of simulations
for count in range(100000):
    # assign rooms to elephants and zookeeper
    elephant1 = (random.randint(1, 6))
    elephant2 = (random.randint(1, 6))
    zookeeper = (random.randint(1, 6))
    #add to counters based off of results of each simulation
    if zookeeper == elephant1 == elephant2:
        both += 1
    if zookeeper == elephant1 or zookeeper == elephant2:
        one += 1
        

  
#print("One: " + str(one))
#print("Both: " + str(both))

#results of at least one elephant in the room he checks
atleastone = one + both
probAtLeastOne = atleastone /1000
print("Percent of time there is at least one elephant: " + format(probAtLeastOne,".2f") + "%")

#results of both elephants in a room checked where there is an elephant
oneBoth = both / atleastone
probOneBoth = oneBoth * 100 
print("Percent of time when there is an elephant that there are both elephants: " + format(probOneBoth,".2f") + "%")

#print conclusion
if atleastone >= 31333 and atleastone <= 35333 \
        and oneBoth >= 14666 and oneBoth <= 18666:
    print("Zookeeper is correct (within 2% margin of error)")
else:
    print("The custodian is correct")
    
#play again    
if(input("Would you like to play again?")) == int(yes) or int(YES) \
        or int(Yes) or int(YEs) or int(yEs) or int(yES) or int(yeS)\
        or int(YeS):
    count = 0
else:
    print("The simulation is over")
