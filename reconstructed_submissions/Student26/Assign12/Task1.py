# @@@@@@@@@@@@@
# CS1400 - M01
# Assignment 12


def main():
    baseList = list(range(1, 101))

    list1 = baseList[1:101:2]
    print(list1)

    list2 = baseList[2:50:3]
    print(list2)

    list3 = [x*10 for x in baseList[54:101:5]]
    print(list3)

main()
