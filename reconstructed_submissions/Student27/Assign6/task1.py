# @@@@@@@@@@@@@
# CS1400 - MW1
# Assignment 6

# import time and random modules
import time
start = time.time()
import random 


#begin loop counter
loops=0
#for loop to check numbers 1 through 10,000
for number in range(1,10001):
    sum = 0
    #loops +=1
    #for loop 
    for i in range(1,number):
        if number%i ==0:
            sum+=i
            loops +=1
    # skip over number=1 because it cannot be a fluky number
    if sum==0:
        continue
    #set seed as sum of factors see if the randint equals the number
    random.seed(sum)
    if random.randint(0, number) == number:
        # print fluky numbers 
        print("Fluky number: " + str(number))
                    
#stop keeping time
end = time.time()
time = end-start
#print time and number of iterations
print("Total time: " + format(time,".2f") + " seconds")
print("Total loops: " + str(loops))
