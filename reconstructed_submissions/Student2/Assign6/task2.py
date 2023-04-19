#@@@@@_@@@@@@@_Assn6


# Step1
import random

from random import seed
from random import randint

#Step2


seed(1)
randint(1, 6)
randint(1, 6)
randint(1, 6)

seed(2)
randint(1,6)
randint(1,6)
randint(1,6)

results =(seed(1)+seed(2)/6)

#Step3
if results == (1/3):
    print("Zookeper won the bet")
elif results == (1/6):
    print("Zookeper won the bet")
else:
    print("Custodian won the bet")


#Step4
