# @@@@@@@@@@@@@@@
# CS1400 - 14 Week
# Assignment 12

def main():
    list = []
    add = True
    while add == True:
        append = input("Add number to list:")
        if append == "":
            add = False
        else:
            list.append(append)
    max = list[0]
    for i in list:
        if i > max:
            max = i
    sum = 0
    for i in range(len(list)):
        sum += int(list[i])
    mean = sum/len(list)
    print(list)
    print("Length of list is: " + str(len(list)))
    print("Maximum value is: "+ max)
    print("Minimum value is: "+ str(min(list)))
    print("Sum of all values is: "+ str(sum))
    print("Average value is: "+ str(mean))
    
main()

