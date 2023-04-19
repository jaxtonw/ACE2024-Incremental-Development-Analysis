# @@@@@@@@@@@@@@
# CS1400 - 14 week
# Assignment 11
import random

from modules.orbian import Orbian
from time import sleep
from random import randint
from random import shuffle # Hint Hint


def main():
    print("WELCOME TO ORBIAN FAMILY")
    print()

    family = []
    input("Hit Enter to Create the First Four Orbians")

    for i in range(0, 4):
        name = input("\tEnter a name for Orbian " + str(i + 1) + ": ")
        # The first four Orbians are created with random values
        headRadius = randint(2, 5)
        bodyRadius = randint(3, 8)
        bodyHeight = randint(5, 15)
        family.append(Orbian(name, headRadius, bodyRadius, bodyHeight))

    print("\tCreating your Orbian Family", end="")
    thinking()

    done = False

    while not done:
        print()
        print("Menu")
        print("\t1) Meet Orbian Family")
        print("\t2) Compare Orbians")
        print("\t3) Orbian Info")
        print("\t4) Create Orbian Baby")
        print("\t5) Send to Pasture")
        print("\t6) Orbian Thanos")
        print("\t7) Quit")
        choice = int(input("Choose an option: "))
        print()

        if choice == 1:
            listFamily(family)
        elif choice == 2:
            compare(family)
        elif choice == 3:
            info(family)
        elif choice == 4:
            createBaby(family)
        elif choice == 5:
            toPasture(family)
        elif choice == 6:
            thanosSnap(family)
        elif choice == 7:
            done = True

    print("Thanks for playing Orbian Family!!!")

def thinking():
    for i in range(5):
        print(".", end="")
        sleep(0.5) # You can comment this out while testing to make things go faster
    print()

def selectOrbian(famList, selected=None):
    count = 1
    for i in famList:
        print("\t" + str(count) + ") " + i.getName(), end="")
        if selected is not None and i is selected:
            print(" (already selected)")
        else:
            print()
        count += 1

    return famList[int(input("Select an Orbian: ")) - 1] # Returns an Orbian object

########### DO NOT MODIFY ANY CODE ABOVE THIS LINE ##############
########### Define/Complete the functions below ###################

def listFamily(famList):
    # <<<<<<<<<<<<<< Write code to list the Orbian family >>>>>>>>>>>>>>>
    print(famList)

def compare(famList):
    #<<<<<<<<<<<<<< Write code to select two orbians to compare >>>>>>>>>>>>>>>
    orb1 = selectOrbian(famList, selected=None)
    orb2 = selectOrbian(famList)
    ########### DO NOT MODIFY THIS FUNCTION BEYOND THIS LINE ############
    if (orb1 == orb2):
        print("\tOrbian " + orb1.getName() + " is equal to Orbian " + orb2.getName())
    elif (orb1 > orb2):
        print("\tOrbian " + orb1.getName() + " is bigger than Orbian " + orb2.getName())
    else:
        print("\tOrbian " + orb1.getName() + " is smaller than Orbian " + orb2.getName())

def createBaby(famList):
    #<<<<<<<<<<<<<< Write code to select two orbians to be parents >>>>>>>>>>>>>>>
    orb1 = selectOrbian(famList)
    orb2 = selectOrbian(famList)

    ########### DO NOT MODIFY THIS FUNCTION BEYOND THIS LINE ############
    famList.append(orb1 + orb2)
    print("\tGreetings Orbian " + famList[len(famList) - 1].getName())

def info(famList):
    ########### DO NOT MODIFY THIS FUNCTION ############
    print("Select an Orbian to view")
    orbian = selectOrbian(famList)

    print("Orbian " + orbian.getName() + " is " + str(orbian.getAge()) + " zungs old") # Age measured in zungs
    print("\tand is " + str(orbian.getVolume()) + " zogs, and " + str(len(orbian)) + " zings") # Volume measured in zogs, Height in zings

def toPasture(famList):
    #<<<<<<<<<<<<<< COMPLETE THIS ENTIRE FUNCTION >>>>>>>>>>>>>
    orb1 = selectOrbian(famList)
    famList.remove(orb1)
    print("\tFarewell " + str(orb1.getName()) + " enjoy retirement!")


def thanosSnap(famList):
    print("Uh oh. Orbian Thanos just snapped his fingers")
    thinking()
    #<<<<<<<<<<<<<< COMPLETE THE REST OF THIS FUNCTION >>>>>>>>>>>>>
    orb1 = shuffle(famList)
    famList.remove(orb1)

main()

