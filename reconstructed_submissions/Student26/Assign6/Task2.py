# @@@@@@@@@@@@@
# CS1400 - M01
# Assignment 6

import random

# While Statement
while True:
    ele = 0
    count = 0
    ele1 = 0
    while count < 100000:
        pen = random.randint(1, 7)
        elephant1 = random.randint(1, 7)
        elephant2 = random.randint(1, 7)
        
# 1 elephant in the pen
        if elephant1 == pen or elephant2 == pen:
            ele += 1
            
# Both elephants in the pen
        if elephant2 == pen and elephant1 == pen:
            ele1 += 1
        count += 1

# Transfer to percent  
    percent1 = ele / 100000
    percent2 = ele1 / ele
    var1 = format(percent1, "<1.2%")
    var2 = format(percent2, "<1.2%")
        
    print("There is at least one elephant in the pen the zookeeper checks " + var1 + " of the time.")
    print("When there is at least one elephant in the pen the zookeeper checks, there are two elephants " + var2 + " of the time.\n")
    
# Zookeeper or custodian is correct
    if .3133 < percent1 < .3533 and .1467 < percent2 < .1867:
        print("The zookeeper is correct!\n")
    else:
        print("The custodian is correct!\n")
        
# Run the simulation again
    again = input("Run the simulation again? Yes or No: ")
    again1 = again.upper()
    if again1 == "YES":
        continue
    if again1 == "NO":
        break
print("Have a great day!")

