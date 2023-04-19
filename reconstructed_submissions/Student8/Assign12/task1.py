# @@@@@@@@@@@@@
# CS 1400 - MW1
# Assignment 12

def main():
    baseList = list(range(1, 101))

    list1 = [] + baseList[1:100:2]
    print(list1)

    list2 = [] + baseList[2:48:3]
    print(list2)

    list3 = [x * 10 for x in baseList[54:100:5]]
    print(list3)

main()
