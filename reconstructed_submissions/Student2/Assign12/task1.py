#@@@@@@@@@@@@@ Assn12
#CS1400

def main():
    baseList = list(range(1, 101))
    list1 = [n for n in baseList if n % 2 == 0]
    print(list1)
    list2 = [n for n in baseList if n % 3 ==0]
    print(list2)
    list3 = [n*10 for n in baseList if n % 5 >= 50]
    print(list3)
main()
