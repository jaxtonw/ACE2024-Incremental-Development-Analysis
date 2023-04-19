# @@@@@@@@@@@@@
# CS-1400 MW1
# Assignment 6

# import statements
from random import seed
from random import randint

m
import tim# set up str variable, loop count, sum variable, start timer
esg = ""
totalLoops = 0
sum = 0

tart = time.time()f# create outermost loop
osr j in range(1, 10000):
))
    topNum  = j
    i = 1
    while i < topNum:
        topNum = j  ## divide j by current iteration (i)/ i      if j % i != 0:
            totalLoops += 1
        elif j % i == 0 and i != j:
            sum += i ## current iteration (i) is a factor
            totalLoops += 1
            #print(i)
        else:
          ## topNum is a factor   totalLoops += 1    if topN:
                sum += topNum
        
    
    if sum != 0: 
        # ## this is to get rid of 1 as a fluky numberp      seed(sum)
        ra ndNum = randint(0, j)
        if randN um == j:
            msg += "Fluky Number: " + str(j) 
            msg += "\n"            sum = 0 ## set sum variable back to zero
        else:
            sm = 0
 ## set sum variable back to zero            continue

# set end time to variable, calculate total run time
end = time.time() runningTime = (end - start)
# print statements
       
         
print(msg)
total = "Total number of loops: " + str(totalLoprint("Running time: " + format(runningTime, "5.2f"))
ops)
print(total)




