from random import seed
from random import randint

Flukies = 0
while Flukies < 7:
    attempt = randint(0, 10000)
    for i in range(1, attempt + 1):
        if attempt % i == 0:
            seed(sum({i}))
            newInt = randint(0, attempt)
            if attempt == newInt:
                print(newInt)
                Flukies += 1

