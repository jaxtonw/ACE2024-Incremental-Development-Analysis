running = True
list = []
while running: 
    numberInput = input("Enter a number: ")
    if numberInput == "":
        running = False
    else:
        list.append(eval(numberInput))
    
print("The number of values is " + str(len(list)))
for maxVal in range(len(list) - 1):
    if list[maxVal] > list[maxVal + 1]:
        list[maxVal], list[maxVal + 1] = list[maxVal + 1], list[maxVal]
print("The highest value of the list is " + str(list[len(list) - 1]))      
print("The smallest value of the list is " + str(min(list)))
sum = 0
for sumVal in range(len(list)):
    sum += list[sumVal]
print("The sum of all values in the list is " + str(sum))
averageVal = sum / len(list)
print("The average value of the list is " + str(averageVal))

