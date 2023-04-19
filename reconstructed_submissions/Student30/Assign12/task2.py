# @@@@@@@@@@@@@@@@@@
# CS1400 - 001
# Assignment 12

isOn = True

list1 = []

while isOn:
    userInput = input("Enter a number: ")
    
    
    if userInput == "":
        isOn = False
        
    else:
        list1.append(eval(userInput))
        isOn = True
print(list1)

def mySearch(usersList):
    for i in range(len(list1) - 1):
        if list1[i] > list1[i + 1]:
            list1[i], list1[i + 1] = list1[i + 1], list1[i]
            
    return list1[len(list1) - 1]



def sumList(usersList):
    listSum = 0    
    for i in range(len(list1)):
        listSum += list1[i]
    
    return listSum
        
def listAverage(usersList):
    return round(sumList(usersList) / len(usersList), 2)


print("Number of values entered: " + str(len(list1)))
print("The maximum value is " + str(mySearch(list1)))
print("The minimum value is " + str(min(list1)))
print("The sum of all values is " + str(sumList(list1)))
print("The average value is " + str(listAverage(list1)))



