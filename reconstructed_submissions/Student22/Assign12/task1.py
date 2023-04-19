# @@@@@@@@@@@  
# CS 1400 - MW1 XL
# Assignment 012
def main():
    baseList = list(range(1, 101))

    list1 = baseList[1: 101 : 2]
    print(list1)

    list2 = baseList[2:50:3]
    print(list2)

    list3 = [i * 10 for i in baseList[54:100:5]]
    print(list3)

main()
