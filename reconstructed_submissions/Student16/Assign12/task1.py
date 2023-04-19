# @@@@@@@@@@@@@@
# CS1400 - MW2
# Assignment 12


def main():
    baseList = list(range(1, 101))
    
    list1 = []
    # iterate though the base list and check for multiples of 2
    for i in baseList:
        if i % 2 == 0:
            list1.append(i)
    print(list1)
    
    list2 = []
    # iterate though the base list and check for multiples of 3 and if the item is less than 50
    for i in baseList:
        if i % 3 == 0 and i < 50:
            list2.append(i)
    print(list2)
    
    list3 = [] 
    # iterate though the base list and check for multiples of 5 and if the value is greater than 50
    for i in baseList:
        if i % 5 == 0 and i > 50:
            # When you append the item, multiply it by 10
            list3.append(i * 10)
    print(list3)
    
main()
