# @@@@@@@@@@@@
# CS1400 - 012
# Assignment 12

def main():
    baseList = list(range(1, 101))

    list1 = baseList[1:101:2]
    print(list1)

    list2 = baseList[2:50:3]
    print(list2)

    list3 = [i * 10 for i in baseList if i % 5 == 0 and i > 50]
    print(list3)

main()
