# @@@@@@@@@@@@@
# CS1400 - 14 week
# Assignment 12
def main():
    baseList = list(range(1, 101))
    list1 = baseList
    print(list1)
    list2 = [i for i in baseList if i % 3 == 0 if i < 50]
    print(list2)
    list3 = [i * 10 for i in baseList if i % 5 == 0 if i > 50]
    print(list3)
    
    
main()

