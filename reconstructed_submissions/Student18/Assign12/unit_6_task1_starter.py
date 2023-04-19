def main():
    baseList = list(range(1, 101))

    list1 = [x for x in baseList if x % 2 == 0]
    print(list1)

    list2 = [3 * x for x in baseList if x <= 16]
    print(list2)

    list3 = [10 * x for x in baseList if x > 50 and x % 5 == 0]
    print(list3)

main()
