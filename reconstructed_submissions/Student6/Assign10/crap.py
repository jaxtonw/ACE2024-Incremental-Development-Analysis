# @@@@@@@@@@@@@
# CS1400 - 001
# Assignment 10

import math


class Wordinator:

    def __init__(self, word1):
        self.word1 = word1

    def __lt__(self, other):
        if self.word1 < other.word1:
            return self.word1
        else:
            return other.word1

    def __add__(self, other):
        return self.word1 + other.word1

    def __mul__(self, factor):
        return self.word1 * factor + "\n" + self.word2 * factor

    def mixWords(self):
        s = ""
        i = 0
        for i in range(min(len(self.word1), len(self.word2))):
            s += self.word1[i] + self.word2[i]
        if len(self.word2) > len(self.word1):
            s += self.word2[i + 1:]
        else:
            s += self.word1[i + 1:]
        return s

    def middleWords(self):
        s = ""
        middle = len(self.word1) // 2 - 1
        for i in range(middle, len(self.word1)):
            if len(self.word1) - i == middle:
                break
            else:
                s += self.word1[i]
        s += "\n"
        middle = len(self.word2) // 2 - 1
        for i in range(middle, len(self.word2)):
            if len(self.word2) - i == middle:
                break
            else:
                s += self.word2[i]
        return s

    def __sub__(self, other):
        s1 = ""
        s2 = ""
        for i in self.word1:
            if i.isupper():
                s1 += i.lower()
            else:
                s1 += i.upper()
        for i in other.word1:
            if i.isupper():
                s2 += i.lower()
            else:
                s2 += i.upper()
        return s1, s2

    def backWordSlice(self):
        return self.word1[::-1]

    def backWordManual(self):
        s = ""
        for i in range(len(self.word1) - 1, -1, -1):
            s += self.word1
        return s 

