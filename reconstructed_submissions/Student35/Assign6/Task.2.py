# @@@@@@@@@@@
# CS1400 - 007
# Assignment 6
import random
val = True
#Write statement that will create a loop 
while val == True:    
    stat1 = 0
    stat2 = 0
    #make the range from 0 to 100000 and make it random to calculate the probability.
    for i in range(100000):
        ele1 = random.randint(1, 6)
        ele2 = random.randint(1, 6)
        keeper = random.randint(1, 6)
        #set the if statements to calculate the possibility of seeing the elephants. 
        if keeper == ele1:
            stat1 += 1
            if keeper == ele2:
                stat2 += 1
        elif keeper == ele2:
            stat1 += 1
            if keeper == ele1:
                stat2 += 1
    #set the final calculation in percent by dividing by 1000.
    newstat1 = stat1 / 1000
    newstat2 = stat2 / 1000
    
    #calculate the upper bound and lower bound of the 2 % error bar.
    
    uBnewstat1 = (1/3) * (1.02)
    lBnewstat1 = (1/3) * (.98)
    uBnewstat2 = (1/6) * (1.02)
    lBnewstat2 = (1/6) * (.98)
    
    #Determine if the zooKeeper is wrong. 
    if newstat1 > uBnewstat1 or newstat1 < lBnewstat1:
        print("Zoo keeper is wrong")
    elif newstat2 > uBnewstat2 or newstat2 < lBnewstat2:
        print("Zoo Keeper is wrong")
    else:
        #print results
        print("Zoo keeper is right.")
    print("The amount of times that the zoo keeper see's at least one elephant: %s %%" % newstat1)
    print("The amount of times that the zoo keeper see's at least two elephant: %s %%" % newstat2)
    #get input from the user to determine 
    user = input("Run the simulation again? (yes or no): ")
    if user == "no":
        #close the loop so function can end
        val = False

