# @@@@@@@@@@@@@
# CS1400 - MW1
# Assignment 12

numbers = []
done = False

while not done:
    
    number = input("Enter a number: ")
    if number == "":
        done = True
    else:
        numbers.append(eval(number))
#Max value
def bubbleSort(numbers):
    didSwap = True

    while didSwap:
        didSwap = False
        sortCnt = 1

        for i in range(len(numbers) - sortCnt):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                didSwap = True

        sortCnt += 1

bubbleSort(numbers)]maxValue = numbers[-1]

#Get sum of list
sum = 0
for i in numbers:
        sum +=i
        
#calculate average value
averageValue = sum / len(numbers)


print(numbers)
print("Number of values entered: " + str(len(numbers)))
print("Maximum value: " + str(maxValue))
print("Minimum value: " + str(min(numbers)))
print("The sum of all numbers is: " + str(sum))
print("The average value is: " + str(averageValue))

