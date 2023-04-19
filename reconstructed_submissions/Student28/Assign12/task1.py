# @@@@@@@@@@@
# Assignment 12 Task 1
# CS 1400 14 week

def main():
    baseList = list(range(1, 101))

    list1 = baseList[1:102:2]
    print(list1)

    list2 = baseList[2:50:3]
    print(list2)

    list3 = [10 * x for x in baseList if x > 51 and x % 5 == 0]
    print(list3)
    
main()
