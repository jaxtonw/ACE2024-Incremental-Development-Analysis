# @@@@@@@@@@@@@
# CS1400 - MW1
# Assignment 12


def main():
    userlist = []
    flag = True
    
    print("Welcome to the List Analyzer!\n")
    
    while flag:
        userinput = input("Please enter a number to put in the list: ")
        if userinput == "":
            flag = False
        else:
            userlist.append(eval(userinput))
            
    print("\nResults: \n\nNumber of values in list: " + str(len(userlist)))
    print("Maximum value in list: " + str(maxval(userlist)))
    print("Minimum value in list: " + str(min(userlist)))
    print("Sum of all items in list: " + str(sumall(userlist)))
    print("Average of all items in list: " + str(average(userlist)))


def maxval(inputlist):
    output = inputlist[0]
    for i in inputlist:
        if i > output:
            output = i
    return output


def sumall(inputlist):
    output = 0
    for i in inputlist:
        output += i
    return output


def average(inputlist):
    return sumall(inputlist) / len(inputlist)
    
    
main() 

