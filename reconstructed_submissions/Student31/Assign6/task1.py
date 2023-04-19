# @@@@@@@@@@@
# CS1400 - MW1 XL
# Assignment 6

from random import seed
from random import randint

for i in range(0, 25):
    x = 1
    for j in range(1,i):
        
        factor = i%j
        if factor == 0:
            x =+ j

    seed(x)
    print(randint(0, x))
    
    

print("Seed value of 1")
seed(1)
print(randint(1, 10))
print(randint(1, 10))
print(randint(1, 10))

print("\nSeed value of 2")
seed(2)
print(randint(1, 10))
print(randint(1, 10))
print(randint(1, 10))

print("\nSeed value of 1")
seed(1)
print(randint(1, 10))
print(randint(1, 10))
print(randint(1, 10))

print("\nFactors of 25, not including 25")
factor1 = 1
factor2 = 5
print(factor1, factor2)

sum = factor1 + factor2
seed(sum)
print("\nFirst random number 0-25")
print(randint(0, 25))
