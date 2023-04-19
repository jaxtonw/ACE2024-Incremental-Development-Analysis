# @@@@@@@@@@@@@
# CS1400 - 00?
# Assignment ??
word1 = "DonaldDuck"
word2 = "bum"
List = [word1, word2]
newWord1 = List[0].lower()
newWord2 = List[1].lower()
newList = [newWord1, newWord2]
newList = sorted(newList)
if newList[0] == newWord1:
    print(List[0])
else:
    print(List[1])

