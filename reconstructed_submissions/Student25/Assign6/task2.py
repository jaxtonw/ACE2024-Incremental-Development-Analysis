from random import seed
from random import randint
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
