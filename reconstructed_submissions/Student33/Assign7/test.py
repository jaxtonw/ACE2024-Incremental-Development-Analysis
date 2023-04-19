# @@@@@@@@@@@@
# CS1400 - 001
# Assignment ??
import random

def luckyNum():
    num = random.randint(1, 5)

    if num != 2:
        return num
    else:
        return

def main():
    val = luckyNum()
    if val == None:
        print("You don't have a lucky number")
    else:
        print("Your lucky number is " + str(val))

main()
