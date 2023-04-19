# @@@@@@@@@@@@
# CS1400 - 001
# Assignment 12

numList = []
done = False
j = 0
while not done:
    num = input("Enter a number: ")
    if num != "":   
        numList.append(num)
        j += 1
    if str(num) == "":
        done = True

    currentMax = 0
    for number in numList:
        number = int(number)
        if number > currentMax:
            currentMax = number  
            
    currentMin = min(numList)

    sum = 0
    for number in numList:
        sum += int(number)

    average = 0
    for number in numList:
        average = sum / len(numList)

print("Number of values entered")      
print(len(numList))# works
print()
print("Maximum value:")
print(currentMax)# works
print()
print("Minimum value:")# works
print(currentMin)
print()
print("Sum of all values:")# works
print(sum)
print()
print("Average value:")# works
print(average)
            
