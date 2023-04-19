# @@@@@@@@@@@@@@@
# CS1400 - 14 Week
# Assignment 11

from modules.orbian import Orbian
from time import sleep
from random import randint
from random import shuffle # Hint hint
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
        sleep(0.5) # You can comment this out while testing to make things go 
#faster
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
    for i in range(len(famList)):
        print("I am Orbian "+ famList[i].getName())
def compare(famList):
    orb1 = selectOrbian(famList)
    orb2 = selectOrbian(famList,selected=orb1)
    ########### DO NOT MODIFY THIS FUNCTION BEYOND THIS LINE ############
    if (orb1 == orb2):
        print("\tOrbian " + orb1.getName() + " is equal to Orbian " + orb2.getName())
    elif (orb1 > orb2):
        print("\tOrbian " + orb1.getName() + " is bigger than Orbian " + orb2.getName())
    else:
        print("\tOrbian " + orb1.getName() + " is smaller than Orbian " + orb2.getName())
def createBaby(famList):
    pick1 = selectOrbian(famList)
    pick2 = selectOrbian(famList,selected=pick1)
    first = str(pick1.getName())
    second = str(pick2.getName())
    firstt = list(first)
    secondd = list(second)
    shuffle(firstt)
    shuffle(secondd)
    length1 = len(first)
    length2 = len(second)
    length = (length1 + length2) // 4
    name1 = ""
    for i in range(length):
        name1 += firstt[i]
        name1 += secondd[i]
    outname = list(name1)
    shuffle(outname)
    name = str(outname)
    head1 = pick1.getHeadRadius()
    head2 = pick2.getHeadRadius()
    headRadius = int((head1 + head2) * .25)
    body1 = pick1.getBodyRadius()
    body2 = pick2.getBodyRadius()
    bodyRadius = int((body1 + body2) * .25)
    bheight1 = pick1.getBodyHeight()
    bheight2 = pick2.getBodyHeight()
    bodyHeight = int((bheight1 + bheight2) * .125)
    new = Orbian(name,headRadius,bodyRadius,bodyHeight)
    ########### DO NOT MODIFY THIS FUNCTION BEYOND THIS LINE ############
    famList.append(new)
    print("\tGreetings Orbian " + name)                            #I couldn't figure out how to do this part the right way
def info(famList):
    ########### DO NOT MODIFY THIS FUNCTION ############
    print("Select an Orbian to view")
    orbian = selectOrbian(famList)
    print("Orbian " + orbian.getName() + " is " + str(orbian.getAge()) + " zungs old") 
    # Age measured in zungs
    print("\tand is " + str(orbian.getVolume()) + " zogs, and " + str(orbian.getHeight()) + " zings")
    # Volume measured in zogs, Height in zings
def toPasture(famList):
    orbian = selectOrbian(famList)
    count = famList.index(orbian)
    famList.pop(count)
def thanosSnap(famList):
    print("Uh oh. Orbian Thanos just snapped his fingers")
    thinking()
    for i in range(len(famList)//2):
        count = randint(0, len(famList))
        famList.pop(count)
    
    #<<<<<<<<<<<<<< COMPLETE THE REST OF THIS FUNCTION >>>>>>>>>>>>>
main()

