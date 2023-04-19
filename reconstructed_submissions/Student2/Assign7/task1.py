# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#@@@@@_@@@@@@@_Assn7

#Input for number of rows

num = int(input("Enter the number of rows:"))

#Pyramid rows and numbers
for i in range(num):
    msg =(" "*(num-i-1) +(str(1+i)+" ")*(1+i))
    if num ==0:
        print("")
    elif num <=9:
        print(msg)
    elif num >9:
        format(print(msg), )

print()
