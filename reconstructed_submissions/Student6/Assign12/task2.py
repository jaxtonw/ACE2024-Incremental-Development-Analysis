# @@@@@@@@@@@@@
# CS1400 - 001
# Assignment 12

def main():
    numL = []
    
    while True:
        numEnter = input("Enter a number: ")
        if numEnter.isdigit():
            numL.append(int(numEnter))
        else: 
            print("Number of values entered: " + str(len(numL)))
            
            numL.sort()
            print("Maximum value: " + str(numL[len(numL) - 1]))
            
            print("Minimum value: " + str(min(numL)))
            
            sumTotal = 0
            for i in numL:
                sumTotal = sumTotal + i 
            print("Sum of all values: " + str(sumTotal))
            
            print("Average value: " + str(sumTotal / len(numL)))
            
            break
            
    
main()

# Number of values entered
# Maximum value. Write your own code. Do not use a built-in function.
# Minimum value. Use a built-in function
# Sum of all values. Use a loop to calculate.
# Average value. Use your calculated sum to calculate. 
