# @@@@@@@@@@@@
# CS1400 - MW1
# Assignment 12

def main():
    list = []
    val = False
    # Get values from user
    num = input("Enter a number: ")
    while not val:
        num = input("Enter another number (blank to stop): ")
        # Stop adding numbers when it is blank
        if num == "":
            val = True
        # Add it to a list (as a float) if it is a number
        else:
            num = num.removeprefix(" ")
            num = num.removesuffix(" ")
            list.append(eval(num))
    # Create the message to display
    msg = ""
    # Find the number of values, add it to message to display
    msg += "Number of values entered: " + str(len(list))
    # Set the maximum value to be the first element so it the max will be an element from the list (the first element if
    # that is max and a different if that is larger)
    maxVal = list[0]
    # Determine if each element is larger than the current max val
    for i in list:
        if i > maxVal:
            maxVal = i
    # Add it to the message
    msg += "\nThe maximum value is: " + str(maxVal)
    # Find minimum
    minVal = min(list)
    msg += "\nThe minimum value is: " + str(minVal)
    # Find sum
    sum = 0
    for i in list:
        sum += i
    msg += "\nThe sum is: " + str(sum)
    # Find average
    avg = sum / len(list)
    msg += "\nThe average is: " + str(avg)
    print(msg)
    
main()
