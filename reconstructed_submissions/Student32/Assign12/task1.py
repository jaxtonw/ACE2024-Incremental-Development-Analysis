# @@@@@@@@@@@@@@
# CS1400 - 14 week
# Assignment 12 task 1

def main():
    baseList = list(range(1, 101))

    list1 = [num for num in baseList if num % 2 == 0]
    print(list1)

    list2 = [num for num in baseList if num < 50 and num % 3 == 0]
    print(list2)

    list3 = [num *10 for num in baseList if num % 5 == 0 and num > 50]
    print(list3)

main()

