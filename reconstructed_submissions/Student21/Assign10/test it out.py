# @@@@@@@@@@@@@@@@
# CECS1400 - MW1
# Assignment ??


print("Welcome to the Wordinator")
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

print(min(word1, word2))
print(str(word1.capitalize() + word2))
print(word1.upper())
print(word2.upper())

print(len(list(word1)))

def reverseWord(word):
    list1 = []
    
    reverseWord1 = ""
    
    for i in word:
        list1.insert(0, i)
    for k in list1:
        reverseWord1 += k
    
    return reverseWord1

x = reverseWord(word1)
y = reverseWord(word2)
z = reverseWord("@@@@@@@")

print(x)
print(y)
print(z)


