# @@@@@@@@@@@@@
# CS1400 - MW1
# Assignment 12

def main():
    baseList = list(range(1, 101))

    list1 = [i for i in baseList if i % 2 ==0]
    print(list1)

    list2 = [i for i in baseList[0:50] if i % 3 ==0]
    print(list2)

    list3 = [(10 * i) for i in baseList[51:100] if i % 5 ==0]
    print(list3)

main()
