# @@@@@@@@@@@@
# CS1400 - MW 1
# Assignment ?


def main():
    print("Concatenation (+): ", end="")
    print("First String" + "Second String")
    print()

    print("Repetition (*): ", end="")
    print("One String" * 6)
    print()

    print("Index ([index]): ", end="")
    str1 = "This is a string"
    print(str1[12])
    print()

    print("First Item Index ([index]): ", end="")
    str1 = "This is a string"
    print(str1[0])
    print()

    print("Last Item Index ([index]): ", end="")
    str1 = "This is a string"
    print(str1[len(str1) - 1])
    print()

    print("Slice ([start:end]): ", end="")
    str1 = "Slice this string"
    print(str1[3:12])
    print()

    print("Slice ([start:end:step]): ", end="")
    str1 = "Slice this string"
    print(str1[3:12:2])
    print()

    print("Slice negative step ([start:end:step]): ", end="")
    str1 = "Slice this string"
    print(str1[12:3:-2])
    print()

    print("in: ", end="")
    str1 = "Look in this string"
    print("ook" in str1, end=" ")
    print("zzz" in str1)
    print()


    print(str(13 // 2))
main()
