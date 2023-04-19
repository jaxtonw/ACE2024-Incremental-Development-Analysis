# @@@@@@@@@@
# CS 1400 - 14 week
# Assignment 12

def main():
    #user created list
    list = []
    done = False
    while not done:
        val = input("Enter a number: ")
        if val == "":
            done = True
        else:
            list.append(eval(val))
    
    # get max value
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            list[i], list[i + 1] = list[i + 1], list[i]
    maxVal = list[len(list) - 1]
    
    #get sum of all values
    sum = 0
    for i in list:
        sum += i
    
    #get average of all values
    avg = sum / len(list)
    
    #results
    print("Number of values entered: " + str(len(list)))    
    print("Maximum value: " + str(maxVal))
    print("Minimum value: " + str(min(list)))
    print("Sum of all values: " + str(sum))
    print("Average value: " + str(avg))
                   
main()
