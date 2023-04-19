# @@@@@@@@@@@@@@
# CS1400 - 001
# Assignment 12

userList = []
    
while True:
    number = input("Input a number (Hit enter when done): ")
    if number == "":
        break
    userList.append(int(number))
    
    
# Number of numbers in the list
length = len(userList) 
print("The length of the list is: " + str(length))

# Maximum value in the list
high = userList[0]
for i in userList:
    if i >= high:
        high = i
print("The maximum value in the list is: " + str(high))


# Minimum value in the list
minimum = min(userList)
print("The minimum value in the list is: " + str(minimum))

# Sum of all values in the list
total = 0
for i in userList:
    total += i
print("The sum of all the values in the list is: " + str(total))

# Average value
average = total / length
print("The average value of the list is: " + str(average))

