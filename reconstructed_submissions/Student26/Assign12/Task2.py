# @@@@@@@@@@@@@
# CS1400 - M01
# Assignment 12


def main():
    list1 = []
    while True:
        number = (input("Enter a number: "))
        if number == "":
            break
        list1.append(int(number))
    print("\nThe number of values is " + str(numberOfValues(list1)))
    print("The maximum value is " + str(maxValue(list1)))
    print("The minimum value is " + str(minValue(list1)))
    print("The sum of values is " + str(sumOfValues(list1)))
    print("The average value is " + str(averageValue(list1)))
     
def numberOfValues(list1):
    return len(list1)
def maxValue(list1):
    didChange = True
    while didChange:
        didChange = False
        sortCnt = 1
        for i in range(len(list1) - sortCnt):
            if list1[i] > list1[i + 1]:
                list1[i], list1[i+1] = list1 [i+1], list1[i]
                didChange = True
        sortCnt += True
        return list1[len(list1)-1]
def minValue(list1):
    didChange = True
    while didChange:
        didChange = False
        sortCnt = 1
        for i in range(len(list1) - sortCnt):
            if list1[i] > list1[i + 1]:
                list1[i], list1[i + 1] = list1[i + 1], list1[i]
                didChange = True
        sortCnt += True
    return list1[0]
def sumOfValues(list1):
    sum = 0
    for i in range(len(list1)):
        sum += (list1[i])
    return sum
def averageValue(list1):
    return sumOfValues(list1)/len(list1)   

main()
