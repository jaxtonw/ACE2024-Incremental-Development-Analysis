# @@@@@@@@@@@
# CS1400 - 14 Week
# Assignment 12.2

def maxVal(demlist):
    for i in demlist:
        eval(i)

    demlist.sort()
    return demlist[len(demlist) - 1]


def minVal(demlist):
    for i in demlist:
        eval(i)
        
    demlist.sort()
    return min(demlist)


def sum(demlist):
    sum = 0
    for i in demlist:
        sum += eval(i)

    return sum


def avgVal(demlist):
    avg = sum(demlist) // len(demlist)
    
    return avg
    
    
def main():
    numList = []
    done = False
    
    while not done:
        userNum = input("Enter a number: ")
        numList.append(userNum)
        
        if userNum == "":
            numList.remove(userNum)
            done = True
        
    print("The list is", numList)
    print("The max value is", maxVal(numList))
    print("The min value is", minVal(numList))
    print("The sum is", sum(numList))
    print("The average is", avgVal(numList))


main()

